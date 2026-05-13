#!/usr/bin/env python3
"""
Generate an OGC 24-017r1-compliant JSON Schema building block from an
Enterprise Architect UML 1.3 / XMI 1.1 export.

First-cut target: GeoSciML 4.1 Leaf packages. One BB per package.

Inputs:
  --xmi PATH                EA XMI 1.1 file (e.g. geosciml4.1.xmi)
  --package NAME            target Leaf/ApplicationSchema package name
  --bb-name NAME            output BB directory name (default: geosciml_<package>)
  --out-dir DIR             parent of the BB directory (default: _sources)
  --swe-mappings PATH       YAML mapping of SWE 2.0 type names -> SWE 3.0 $ref
  --category-codelists PATH YAML mapping of <Class>.<attr> -> CGI vocabulary URL

Conventions (per ogc-uml2json skill + recorded decisions):
  - FeatureType classes -> JSON-FG-compliant encoding (allOf JSON-FG Feature ref
    OR a $ref to the supertype if it already provides Feature in its allOf chain).
  - DataType/Type classes -> plain JSON object schemas.
  - CodeList classes -> { type: string, format: uri, codeList: <URL> }
    (URI codelist encoding per OGC 24-017r1 req/codelists-uri).
  - Abstract classes encoded same as concrete; subtypes use allOf.
  - Generalizations: allOf [ {$ref to parent}, {own properties} ].
  - $anchor = ClassName for every class.
  - entityType: required string member on every concrete FeatureType / DataType
    / Type (skip for CodeList; skip if a supertype already declared it).
  - Class-typed properties (types-with-identity) -> by-reference encoding using
    SWE 3.0 / OGC LinkObject ($ref to bp.schemas.opengis.net LinkObject).
  - SWE 2.0 Quantity / QuantityRange / DataRecord -> $ref to SWE 3.0 URL
    (consult swe-mappings.yaml).
  - Category attributes -> URI codelist encoding; codeList annotation from
    cgi-vocab-reference.yaml. Unmapped/"treat as open" entries omit codeList.
  - ISO 19103 primitives (CharacterString, Real, Boolean, ...) -> simple JSON
    Schema type per OGC 24-017r1 Table 4.
  - ISO 19107 geometry (GM_*) -> GeoJSON schema URL.
  - Other ISO imports (CI_Citation, ScopedName, TM_Instant, ...) -> placeholder
    $ref of the form "<isoXXXX>:<TypeName>"; resolved later.
  - Multiplicity: upper>1 -> array; lower>=1 -> required (or minItems).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# Teach PyYAML to dump OrderedDict like a plain mapping. Python 3.7+ preserves
# insertion order on dict, but we use OrderedDict throughout to make intent
# explicit; without this registration, safe_dump raises RepresenterError.
yaml.SafeDumper.add_representer(
    OrderedDict,
    lambda d, data: d.represent_mapping("tag:yaml.org,2002:map", data.items()),
)


# ---------------------------------------------------------------------------
# Constants from OGC 24-017r1 and the ogc-uml2json skill
# ---------------------------------------------------------------------------

JSON_FG_FEATURE_REF = "https://schemas.opengis.net/json-fg/feature.json"
LINK_OBJECT_REF = "#/$defs/SCLinkObject"   # local definition, added to every schema's $defs
SWE3_MEASURE_REF = (
    "https://bp.schemas.opengis.net/24-017r1/uml2json/1.0/"
    "schema_definitions.json#/$defs/Measure"
)

# Inline SCLinkObject definition emitted into every BB's $defs so the schema
# is self-contained. Matches the OGC geoscimlBasic/Lite schemas.
SCLINK_OBJECT_DEF = {
    "title": "link object",
    "description": (
        "SCLinkObject originates from ShapeChange implementation of "
        "https://schemas.opengis.net/ogcapi/common/part1/1.0/openapi/"
        "schemas/link.json, based on RFC 8288 web linking."
    ),
    "type": "object",
    "required": ["href"],
    "properties": {
        "href":     {"type": "string",  "description": "Supplies the URI to a remote resource (or resource fragment)."},
        "rel":      {"type": "string",  "description": "The type or semantics of the relation."},
        "type":     {"type": "string",  "description": "A hint indicating what the media type of the result of dereferencing the link should be."},
        "hreflang": {"type": "string",  "description": "A hint indicating what the language of the result of dereferencing the link should be."},
        "title":    {"type": "string",  "description": "Used to label the destination of a link such that it can be used as a human-readable identifier."},
        "length":   {"type": "integer"},
    },
}

ISO_19103_PRIMITIVE_MAP: dict[str, tuple[str, Optional[str]]] = {
    "Boolean":         ("boolean", None),
    "CharacterString": ("string",  None),
    "Date":            ("string",  "date"),
    "DateTime":        ("string",  "date-time"),
    "Decimal":         ("number",  None),
    "Integer":         ("integer", None),
    "Number":          ("number",  None),
    "Real":            ("number",  None),
    "Time":            ("string",  "time"),
    "URI":             ("string",  "uri"),
}

ISO_19107_GEOMETRY_MAP: dict[str, str] = {
    "GM_Point":       "https://geojson.org/schema/Point.json",
    "GM_Curve":       "https://geojson.org/schema/LineString.json",
    "GM_Surface":     "https://geojson.org/schema/Polygon.json",
    "GM_MultiPoint":  "https://geojson.org/schema/MultiPoint.json",
    "GM_MultiCurve":  "https://geojson.org/schema/MultiLineString.json",
    "GM_MultiSurface":"https://geojson.org/schema/MultiPolygon.json",
    "GM_Aggregate":   "https://geojson.org/schema/GeometryCollection.json",
    "GM_Object":      "https://geojson.org/schema/Geometry.json",
}

# ISO type-name prefix detection. Maps recognised prefixes to a namespace tag.
ISO_PREFIX_MAP: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^CI_"), "iso19115"),
    (re.compile(r"^MD_"), "iso19115"),
    (re.compile(r"^SC_"), "iso19111"),
    (re.compile(r"^SF_"), "iso19156"),
    (re.compile(r"^GFI_"),"iso19156"),
    (re.compile(r"^TM_"), "iso19108"),
    (re.compile(r"^OM_"), "iso19156"),
]

# Mapping from external ISO type keys (form: "iso<doc>:<TypeName>") to JSON
# Schema fragments. Most external types have no canonical JSON Schema, so we
# encode them as by-reference link objects (SCLinkObject). A few metadata
# types have published CDIF building blocks that can be inlined as a richer
# alternative - these are emitted as `anyOf [SCLinkObject, <CDIF $ref> ...]`,
# letting instances provide either a link or a fully-typed metadata object.
_CDIF_BASE = (
    "https://cross-domain-interoperability-framework.github.io/"
    "metadataBuildingBlocks/build/annotated/bbr/metadata"
)
EXTERNAL_TYPE_RESOLUTION: dict[str, dict] = {
    # ISO 19115 metadata - CI_Responsibility has a CDIF agent-in-role mapping;
    # CI_Citation stays SCLinkObject only.
    "iso19115:CI_Responsibility": {
        "anyOf": [
            {"$ref": LINK_OBJECT_REF},
            {"$ref": f"{_CDIF_BASE}/schemaorgProperties/agentInRole/schema.json"},
        ],
        "$comment": "External ISO 19115 CI_Responsibility - by-reference link or inline CDIF agentInRole",
    },
    "iso19115:CI_Citation": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19115 CI_Citation - by-reference link only",
    },
    # ISO 19103 composites with CDIF mappings.
    "iso19103:ScopedName": {
        "anyOf": [
            {"$ref": LINK_OBJECT_REF},
            {"$ref": f"{_CDIF_BASE}/schemaorgProperties/definedTerm/schema.json"},
            {"$ref": f"{_CDIF_BASE}/skosProperties/skosConcept/schema.json"},
        ],
        "$comment": "External ISO 19103 ScopedName - link, CDIF definedTerm, or SKOS concept",
    },
    "iso19103:NamedValue": {
        "anyOf": [
            {"$ref": LINK_OBJECT_REF},
            {"$ref": f"{_CDIF_BASE}/schemaorgProperties/variableMeasured/schema.json"},
        ],
        "$comment": "External ISO 19103 NamedValue - link or inline CDIF variableMeasured (schema:PropertyValue)",
    },
    # ISO 19108 time, 19107 geometry composites, 19156 sampling/observation -
    # no published JSON Schemas; emit SCLinkObject so instances must provide
    # a link to an external resource.
    "iso19108:TM_Instant": {
        "oneOf": [
            {"$ref": LINK_OBJECT_REF},
            # OWL-Time object form - Instant carrying an xsd:dateTime via inXSDDateTime
            # (or inXSDDate / inXSDgYear / etc. for the various OWL-Time positional shortcuts).
            {
                "type": "object",
                "properties": {
                    "inXSDDateTime":     {"type": "string", "format": "date-time"},
                    "inXSDDate":         {"type": "string", "format": "date"},
                    "inXSDgYearMonth":   {"type": "string", "pattern": r"^-?\d{4}-\d{2}$"},
                    "inXSDgYear":        {"type": "string", "pattern": r"^-?\d{4}$"},
                },
                "anyOf": [
                    {"required": ["inXSDDateTime"]},
                    {"required": ["inXSDDate"]},
                    {"required": ["inXSDgYearMonth"]},
                    {"required": ["inXSDgYear"]},
                ],
            },
            # OWL-Time shortcut: just an ISO 8601 datetime / date string
            {"type": "string", "format": "date-time"},
            {"type": "string", "format": "date"},
        ],
        "$comment": (
            "ISO 19108 TM_Instant aligned to W3C OWL-Time time:Instant "
            "(https://www.w3.org/TR/owl-time/#time:Instant). Accepts a "
            "SCLinkObject by-reference, an OWL-Time Instant object with one "
            "of `inXSDDateTime` / `inXSDDate` / `inXSDgYearMonth` / "
            "`inXSDgYear`, or a bare ISO 8601 string as a convenience alias."
        ),
    },
    "iso19108:TM_Period": {
        "oneOf": [
            {"$ref": LINK_OBJECT_REF},
            # OWL-Time object form: time:ProperInterval with time:hasBeginning / time:hasEnd
            # pointing at Instants.
            {
                "type": "object",
                "properties": {
                    "hasBeginning": {"type": "object"},
                    "hasEnd":       {"type": "object"},
                },
                "required": ["hasBeginning", "hasEnd"],
            },
            # OWL-Time shortcut form: time:hasBeginningDateTime / time:hasEndDateTime
            # carrying ISO 8601 strings inline.
            {
                "type": "object",
                "properties": {
                    "hasBeginningDateTime": {"type": "string"},
                    "hasEndDateTime":       {"type": "string"},
                },
                "required": ["hasBeginningDateTime", "hasEndDateTime"],
            },
            # Compact [startDate, endDate] tuple. NOT OWL-Time-canonical;
            # semantically equivalent to the hasBeginningDateTime / hasEndDateTime
            # shortcut form. Accepted for compatibility with the OGC code-sprint
            # convention; consumers preferring OWL-Time should use the object form.
            {
                "type": "array",
                "minItems": 2, "maxItems": 2,
                "items": {"type": "string"},
            },
        ],
        "$comment": (
            "ISO 19108 TM_Period aligned to W3C OWL-Time time:ProperInterval "
            "(https://www.w3.org/TR/owl-time/#time:ProperInterval). Canonical "
            "encoding is the OWL-Time object with `hasBeginning`/`hasEnd` (or "
            "the shortcut `hasBeginningDateTime`/`hasEndDateTime`). A "
            "two-element [startDate, endDate] array is accepted as a "
            "convenience alias (OGC code-sprint convention) but is not "
            "OWL-Time-canonical; consumers should prefer the object form."
        ),
    },
    "iso19107:DirectPosition": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19107 DirectPosition - by-reference link",
    },
    "iso19156:GFI_Feature": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 GFI_Feature - by-reference link",
    },
    "iso19156:SF_SamplingFeature": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 SF_SamplingFeature - by-reference link",
    },
    "iso19156:SF_SamplingFeatureCollection": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 SF_SamplingFeatureCollection - by-reference link",
    },
    "iso19156:OM_Observation": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 OM_Observation - by-reference link",
    },
}


# ---------------------------------------------------------------------------
# Hand-curated extension definitions.
#
# Some classes that callers want to validate aren't in the GeoSciML 4.1 XMI
# (they live in External packages / imported standards). Rather than try to
# auto-import ISO 19156 / 19115 / etc. we hand-author the needed shapes and
# inject them into the appropriate BB's $defs via EXTRA_DEFS_PER_BB.
#
# DISPATCHER_OVERRIDES_PER_BB lets a BB ship a different dispatcher
# featureType list than what dispatchable_fts() would discover from the XMI.
# Useful when the BB's "wrapper" intent is narrower than its $defs library
# (e.g. gsmSpecimen exposes only SF_Specimen as a featureType, but the
# library also holds AnalyticalInstrument, ReferenceSpecimen, etc. as DataType
# defs that other features may $ref).
# ---------------------------------------------------------------------------

_GEOJSON_GEOMETRY_REF = "https://geojson.org/schema/Geometry.json"
_SWE_CATEGORY_REF = "https://schemas.opengis.net/sweCommon/3.0/json/Category.json"
_SWE_QUANTITY_REF = "https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json"

# ISO 19156:2011 §8.6 SF_Specimen, encoded as a JSON-FG FeatureType. Includes
# SF_SamplingFeature's inherited properties (sampledFeature, relatedObservation,
# relatedSamplingFeature, lineage) plus SF_Specimen's own properties.
SF_SPECIMEN_DEF = {
    "$anchor": "SF_Specimen",
    "description": (
        "ISO 19156:2011 §8.6 SF_Specimen - a sampling feature representing a "
        "physical specimen collected from a sampled feature. Implementation "
        "inlines the SF_SamplingFeature parent's properties (sampledFeature, "
        "relatedObservation, relatedSamplingFeature, lineage) since the parent "
        "is not separately schematised here. External ISO types referenced "
        "from properties (OM_Process, OM_Observation, GFI_Feature, "
        "TM_Object, LI_Lineage, SF_SamplingFeature) are by-reference only via "
        "SCLinkObject."
    ),
    "allOf": [
        {"$ref": JSON_FG_FEATURE_REF},
        {
            "type": "object",
            "properties": {
                "properties": {
                    "type": "object",
                    "properties": {
                        # ----- SF_SamplingFeature inherited properties -----
                        "sampledFeature": {
                            "type": "array",
                            "items": {"$ref": LINK_OBJECT_REF},
                            "minItems": 1,
                            "uniqueItems": True,
                            "description": (
                                "Feature(s) being sampled (1..*, by-reference "
                                "to ISO 19156 GFI_Feature). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        "relatedObservation": {
                            "type": "array",
                            "items": {"$ref": LINK_OBJECT_REF},
                            "uniqueItems": True,
                            "description": (
                                "Observations whose featureOfInterest is this "
                                "specimen (0..*, by-reference to ISO 19156 "
                                "OM_Observation). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        "relatedSamplingFeature": {
                            "type": "array",
                            "items": {"$ref": LINK_OBJECT_REF},
                            "uniqueItems": True,
                            "description": (
                                "Self-association: relations to other "
                                "SF_SamplingFeature instances (0..*, "
                                "by-reference). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        "lineage": {
                            "$ref": LINK_OBJECT_REF,
                            "description": (
                                "Provenance metadata (by-reference to ISO "
                                "19115 LI_Lineage). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        # ----- SF_Specimen own properties -----
                        "materialClass": {
                            "$ref": _SWE_CATEGORY_REF,
                            "description": (
                                "Material class of the specimen (1..1). ISO "
                                "19156 types this as ScopedName; encoded here "
                                "as a SWE Category to carry the vocabulary "
                                "URI."
                            ),
                        },
                        "samplingTime": {
                            "$ref": LINK_OBJECT_REF,
                            "description": (
                                "Time of sampling (1..1, by-reference to ISO "
                                "19108 TM_Object)."
                            ),
                        },
                        "samplingMethod": {
                            "oneOf": [
                                {"$ref": LINK_OBJECT_REF},
                                {"$ref": "#GeologicSamplingMethod"},
                            ],
                            "description": (
                                "Sampling method (0..1). ISO 19156 types as "
                                "OM_Process; here implemented as the GeoSciML "
                                "GeologicSamplingMethod FeatureType, either "
                                "by-reference (SCLinkObject) or inline."
                            ),
                        },
                        "samplingLocation": {
                            "$ref": _GEOJSON_GEOMETRY_REF,
                            "description": (
                                "Location where the specimen was sampled "
                                "(0..1, GeoJSON Geometry). Distinct from the "
                                "top-level Feature geometry, which may carry "
                                "the specimen's current footprint."
                            ),
                        },
                        "processingDetails": {
                            "type": "array",
                            "items": {"$ref": "#GeologicSpecimenPreparation"},
                            "uniqueItems": True,
                            "description": (
                                "Processing / preparation steps applied to "
                                "the specimen (0..*). ISO 19156 types as "
                                "SpecimenProcessing; here items are the "
                                "GeoSciML GeologicSpecimenPreparation "
                                "DataType."
                            ),
                        },
                        "size": {
                            "$ref": _SWE_QUANTITY_REF,
                            "description": (
                                "Specimen size as a SWE Quantity (0..1). ISO "
                                "19156 types as Measure."
                            ),
                        },
                        "currentLocation": {
                            "oneOf": [
                                {"type": "string"},
                                {"$ref": LINK_OBJECT_REF},
                            ],
                            "description": (
                                "Current physical location of the specimen "
                                "(0..1). Free text address, URI, or link "
                                "object to a repository record."
                            ),
                        },
                        "specimenType": {
                            "$ref": _SWE_CATEGORY_REF,
                            "description": (
                                "Specimen type classifier (0..1). ISO 19156 "
                                "types as ScopedName; encoded here as a SWE "
                                "Category."
                            ),
                        },
                    },
                    "required": ["sampledFeature", "materialClass", "samplingTime"],
                },
            },
        },
        {
            "required": ["featureType", "id"],
            "properties": {"id": {"type": "string"}},
        },
    ],
}

# ISO 19156 + OWL-Time + Cox/Richard geologic timescale hand-curated classes.
# Both Geochronologic classes align to W3C OWL-Time (https://www.w3.org/TR/owl-time/)
# per the Cox & Richard 2015 formal model for the geologic timescale and GSSP:
#   GeochronologicEra      ≡ time:ProperInterval
#   GeochronologicBoundary ≡ time:Instant
#   start                  ↔ time:hasBeginning
#   end                    ↔ time:hasEnd
#   member                 ↔ time:intervalContains (Allen relation)
# stratotype anchors the abstract time concepts to rock-record evidence.

GEOCHRONOLOGIC_BOUNDARY_DEF = {
    "$anchor": "GeochronologicBoundary",
    "description": (
        "A point in geologic time defined by a stratotype. Aligns to "
        "time:Instant from W3C OWL-Time (https://www.w3.org/TR/owl-time/). "
        "Cox & Richard 2015, 'A formal model for the geologic timescale and "
        "GSSP': the boundary's instant is anchored to the rock record via "
        "the `stratotype` property, which references a StratigraphicPoint "
        "(typically a GSSP if ratified by ICS)."
    ),
    "allOf": [
        {"$ref": JSON_FG_FEATURE_REF},
        {
            "type": "object",
            "properties": {
                "properties": {
                    "type": "object",
                    "properties": {
                        "stratotype": {
                            "description": (
                                "The StratigraphicPoint that defines this "
                                "boundary in the rock record. Inline Feature "
                                "or by-reference SCLinkObject."
                            ),
                            "oneOf": [
                                {"$ref": LINK_OBJECT_REF},
                                {"$ref": "#StratigraphicPoint"},
                            ],
                        },
                    },
                    "required": ["stratotype"],
                },
            },
        },
        {
            "required": ["featureType", "id"],
            "properties": {"id": {"type": "string"}},
        },
    ],
}

GEOCHRONOLOGIC_ERA_DEF = {
    "$anchor": "GeochronologicEra",
    "description": (
        "A named interval of geologic time (Eon, Era, Period, Epoch, Age, "
        "biozone, etc.). Aligns to time:ProperInterval from W3C OWL-Time "
        "(https://www.w3.org/TR/owl-time/). Cox & Richard 2015, 'A formal "
        "model for the geologic timescale and GSSP': `start` / `end` map to "
        "time:hasBeginning / time:hasEnd (both linking to "
        "GeochronologicBoundary ≡ time:Instant); `member[]` expresses "
        "sub-era containment (Allen time:intervalContains). The optional "
        "`stratotype` anchors the era to a defining rock section."
    ),
    "allOf": [
        {"$ref": JSON_FG_FEATURE_REF},
        {
            "type": "object",
            "properties": {
                "properties": {
                    "type": "object",
                    "properties": {
                        "rank": {
                            "type": "string",
                            "format": "uri",
                            "description": (
                                "Chronostratigraphic / geochronologic rank "
                                "(URI from the ICS chart vocabulary or "
                                "equivalent: Eon, Era, Period, Epoch, Age, "
                                "biozone, etc.)."
                            ),
                        },
                        "start": {
                            "description": (
                                "Lower boundary of this era (time:hasBeginning). "
                                "Inline GeochronologicBoundary Feature or "
                                "by-reference SCLinkObject."
                            ),
                            "oneOf": [
                                {"$ref": LINK_OBJECT_REF},
                                {"$ref": "#GeochronologicBoundary"},
                            ],
                        },
                        "end": {
                            "description": (
                                "Upper boundary of this era (time:hasEnd). "
                                "Inline GeochronologicBoundary Feature or "
                                "by-reference SCLinkObject."
                            ),
                            "oneOf": [
                                {"$ref": LINK_OBJECT_REF},
                                {"$ref": "#GeochronologicBoundary"},
                            ],
                        },
                        "member": {
                            "description": (
                                "Sub-eras contained within this era "
                                "(time:intervalContains). Array of "
                                "by-reference links or inline "
                                "GeochronologicEra Features."
                            ),
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {"$ref": LINK_OBJECT_REF},
                                    {"$ref": "#GeochronologicEra"},
                                ],
                            },
                            "uniqueItems": True,
                        },
                        "stratotype": {
                            "description": (
                                "Defining stratigraphic section for this "
                                "era (the rock-record anchor). Inline "
                                "StratigraphicSection Feature or "
                                "by-reference SCLinkObject."
                            ),
                            "oneOf": [
                                {"$ref": LINK_OBJECT_REF},
                                {"$ref": "#StratigraphicSection"},
                            ],
                        },
                    },
                    "required": ["rank", "start", "end"],
                },
            },
        },
        {
            "required": ["featureType", "id"],
            "properties": {"id": {"type": "string"}},
        },
    ],
}

# Map of BB name -> additional $defs to merge into the library.
EXTRA_DEFS_PER_BB: dict[str, dict] = {
    "gsmSpecimen": {
        "SF_Specimen": SF_SPECIMEN_DEF,
    },
    "gsmGeologicTime": {
        "GeochronologicBoundary": GEOCHRONOLOGIC_BOUNDARY_DEF,
        "GeochronologicEra": GEOCHRONOLOGIC_ERA_DEF,
    },
}

# Map of BB name -> override list of dispatchable featureTypes. When set,
# replaces the FT list auto-discovered from the XMI (dispatchable_fts()).
DISPATCHER_OVERRIDES_PER_BB: dict[str, list[str]] = {
    "gsmSpecimen": ["SF_Specimen", "ReferenceSpecimen"],
}

# UML classes excluded from JSON Schema emission entirely (no $def, no
# dispatch). Mirrors OGC's ShapeChange config tagged value
#   <TaggedValue name="jsonEncodingRule" value="notEncoded"
#                modelElementName="^(GSML|GSMLitem)$"/>
# which treats the GSML collection container and the GSMLitem member-type
# union as XSD-only constructs that have no JSON encoding. The corresponding
# JSON-FG concepts are FeatureCollection (for GSML) and a featureType-
# discriminated dispatch chain (for GSMLitem).
NOT_ENCODED_CLASSES: set[str] = {"GSML", "GSMLitem"}

# Map of (owning class, attribute name) -> overridden UML type name.
# Reserved for cases the loader can't auto-detect (none currently — the
# canonical GeologicFeature.relatedFeature -> AbstractFeatureRelation case is
# now handled by the AssociationClassMapper logic in _merge_associations,
# which mirrors the ShapeChange transformer of the same name).
ATTRIBUTE_TYPE_OVERRIDES: dict[tuple[str, str], str] = {}


def _resolve_external_type(key: str) -> dict:
    """Return the schema fragment for an external ISO type identifier
    (e.g. 'iso19156:GFI_Feature'). Falls back to SCLinkObject when no
    specific mapping is configured."""
    if key in EXTERNAL_TYPE_RESOLUTION:
        # Deep-copy to avoid downstream mutation
        return json.loads(json.dumps(EXTERNAL_TYPE_RESOLUTION[key]))
    return {
        "$ref": LINK_OBJECT_REF,
        "$comment": f"External type {key} - by-reference link (no specific mapping configured)",
    }

# Names from ISO 19103 that aren't primitives (composite types) - placeholder them.
ISO_19103_COMPOSITES = {
    "ScopedName": "iso19103",
    "GenericName": "iso19103",
    "LocalName": "iso19103",
    "TypeName": "iso19103",
    "NamedValue": "iso19103",
    "DirectPosition": "iso19107",
    "Logical": "iso19103",
    "Component": "iso19103",
    "Invariant": "iso19103",
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Attribute:
    name: str
    type_name: str            # raw type string from UML tagged-value
    lower: int
    upper: int                # -1 for unbounded *
    doc: str = ""
    stereotype: str = ""      # e.g. voidable
    is_id: bool = False
    inline_or_byref: str = "" # UML tag 'inlineOrByReference': inline|byReference|inlineOrByReference|""


@dataclass
class UmlClass:
    xmi_id: str
    name: str
    stereotype: str           # FeatureType / DataType / Type / CodeList / Union / ""
    abstract: bool
    package_path: list[str]   # e.g. ['GeoSciML 4.1','GeoSciML4.1','GeoSciMLBasic','GeologicEvent']
    attributes: list[Attribute] = field(default_factory=list)
    supertypes: list[str] = field(default_factory=list)  # class names
    doc: str = ""
    tagged_values: dict[str, str] = field(default_factory=dict)  # class-level UML tagged values


# Canonicalise EA's case-inconsistent stereotype names.
STEREOTYPE_CANON = {
    "featuretype": "FeatureType",
    "datatype":    "DataType",
    "type":        "Type",
    "codelist":    "CodeList",
    "union":       "Union",
}


def canon_stereotype(s: str) -> str:
    if not s:
        return ""
    return STEREOTYPE_CANON.get(s.strip().lower(), s.strip())


# ---------------------------------------------------------------------------
# XMI loader (EA UML 1.3 / XMI 1.1)
# ---------------------------------------------------------------------------

class EaXmiLoader:
    """Regex-based reader for Enterprise Architect's UML 1.3 / XMI 1.1 export."""

    def __init__(self, path: Path):
        self.path = path
        self.text = path.read_text(encoding="cp1252", errors="replace")
        # Normalize Unicode em-dash (U+2014) and en-dash (U+2013) to ASCII
        # hyphen-minus so generated schema/example strings stay in pure ASCII.
        self.text = self.text.replace("\u2014", "-").replace("\u2013", "-")
        # xmi_id -> UmlClass
        self.classes: dict[str, UmlClass] = {}
        # class name -> xmi_id  (first hit wins; collisions warned)
        self.name_to_id: dict[str, str] = {}
        # xmi_id -> class name (faster lookups)
        self.id_to_name: dict[str, str] = {}
        # subtype_id -> [supertype_id, ...]
        self.generalizations: dict[str, list[str]] = {}
        self._load()

    # ----- low-level helpers -------------------------------------------------

    @staticmethod
    def _clean_html(s: str) -> str:
        if not s:
            return ""
        # Decode XML entities first so encoded markup becomes real markup,
        # then strip all HTML tags. Decode &amp; last (and iteratively) so
        # double-encoded sequences like &amp;amp; resolve fully.
        s = (s.replace("&lt;", "<").replace("&gt;", ">")
               .replace("&quot;", "\"").replace("&apos;", "'").replace("&#xA;", " "))
        prev = None
        while prev != s:
            prev = s
            s = s.replace("&amp;", "&")
        s = re.sub(r"<[^>]+>", "", s)
        s = re.sub(r"\s+", " ", s).strip()
        return s

    def _package_stack_at(self, pos: int) -> list[str]:
        """Return the open-package stack at character offset `pos`."""
        before = self.text[:pos]
        events = []
        for m in re.finditer(r'<UML:Package\s+name="([^"]+)"', before):
            events.append((m.start(), "open", m.group(1)))
        for m in re.finditer(r"</UML:Package>", before):
            events.append((m.start(), "close", None))
        events.sort()
        stack: list[str] = []
        for _, kind, name in events:
            if kind == "open":
                stack.append(name)  # type: ignore[arg-type]
            elif stack:
                stack.pop()
        return stack

    # ----- loading ----------------------------------------------------------

    def _load(self) -> None:
        # Pre-pass: harvest constraints. EA nests <UML:Constraint> inside the
        # constrained <UML:Class> or <UML:Attribute>. The constraint's `name`
        # attribute holds the OCL/invariant text. We attribute each constraint
        # to its nearest enclosing Class (and optional Attribute) by position.
        self.constraints_by_class: dict[str, list[str]] = {}
        self.constraints_by_class_attr: dict[tuple[str, str], list[str]] = {}
        self._harvest_constraints()

        # Pass 1: collect every UML:Class with its enclosing package stack.
        # Match the whole opening tag, then parse attribute key="value" pairs
        # individually so order-of-attributes does not matter.
        class_re = re.compile(r'<UML:Class\b([^>]*)>')
        attr_kv = re.compile(r'(\w[\w.\-]*)="([^"]*)"')
        for cm in class_re.finditer(self.text):
            attrs = dict(attr_kv.findall(cm.group(1)))
            cls_name = attrs.get("name")
            cls_id = attrs.get("xmi.id")
            if not cls_name or not cls_id:
                continue
            abstract = (attrs.get("isAbstract") == "true")
            pkg_stack = self._package_stack_at(cm.start())

            # Find end of this class block (balanced)
            end = self._find_class_end(cm.end())
            body = self.text[cm.end():end]

            stereotype = self._extract_stereotype(body)
            doc = self._extract_doc(body)
            tagged = self._extract_class_tagged_values(body)
            attrs = self._extract_attributes(body)

            uc = UmlClass(
                xmi_id=cls_id, name=cls_name, stereotype=canon_stereotype(stereotype),
                abstract=abstract, package_path=pkg_stack,
                attributes=attrs, doc=doc, tagged_values=tagged,
            )
            self.classes[cls_id] = uc
            self.id_to_name[cls_id] = cls_name
            self.name_to_id.setdefault(cls_name, cls_id)

        # Pass 1.5: walk UML:Association elements and turn each navigable end
        # into a synthetic Attribute on the OPPOSITE class. EA stores some
        # properties only as association ends, not as UML:Attribute, so this
        # is required to capture the full property set.
        self._merge_associations()

        # Pass 2: collect generalizations (subtype -> [supertype, ...])
        gen_re = re.compile(
            r'<UML:Generalization\b[^>]*subtype="([^"]+)"[^>]*supertype="([^"]+)"'
        )
        for gm in gen_re.finditer(self.text):
            sub, sup = gm.group(1), gm.group(2)
            self.generalizations.setdefault(sub, []).append(sup)

        # Pass 2.5: pull class-name lookups from sibling XMI files in the same
        # directory so cross-XMI generalizations resolve. The canonical case is
        # GSML_QuantityRange extends swe:QuantityRange, where the parent lives
        # in SWECommon2.0.xmi, not the main GeoSciML XMI. Without this we'd
        # store "__unresolved_<eaid>__" and lose the chance to emit a $ref to
        # the external mapped JSON schema (sweCommon/3.0/json/QuantityRange.json).
        ext_class_re = re.compile(
            r'<UML:Class\s+name="([^"]+)"\s+xmi\.id="([^"]+)"'
        )
        for sibling in self.path.parent.glob("*.xmi"):
            if sibling.resolve() == self.path.resolve():
                continue
            try:
                sib_text = sibling.read_text(encoding="cp1252", errors="replace")
            except Exception:
                continue
            for em in ext_class_re.finditer(sib_text):
                ext_name, ext_id = em.group(1), em.group(2)
                self.id_to_name.setdefault(ext_id, ext_name)

        # Stitch supertype class names onto each UmlClass
        for cls_id, uc in self.classes.items():
            for sup_id in self.generalizations.get(cls_id, []):
                sup_name = self.id_to_name.get(sup_id)
                if sup_name:
                    uc.supertypes.append(sup_name)
                else:
                    uc.supertypes.append(f"__unresolved_{sup_id[:12]}__")

    @staticmethod
    def _find_class_end(after_open: int) -> int:
        # Find the matching </UML:Class> at depth 0. EA never nests classes,
        # so the first close is the right one.
        end = re.search(r'</UML:Class>', "", )
        # Cheap version: find next </UML:Class>
        m = re.compile(r'</UML:Class>').search
        # 'after_open' is offset; we need to search the file text from this loader.
        raise NotImplementedError  # patched below at runtime

    # The static method above is replaced below to access self.text.

    def _extract_stereotype(self, body: str) -> str:
        # Try <UML:ModelElement.stereotype><UML:Stereotype name="X"/> first
        m = re.search(
            r'<UML:ModelElement\.stereotype>\s*<UML:Stereotype\s+name="([^"]+)"',
            body, re.DOTALL,
        )
        if m:
            return m.group(1)
        # Fall back to tagged-value stereotype
        m = re.search(r'<UML:TaggedValue tag="stereotype" value="([^"]+)"', body)
        return m.group(1) if m else ""

    def _extract_doc(self, body: str) -> str:
        m = re.search(r'<UML:TaggedValue tag="documentation" value="([^"]*)"', body)
        return self._clean_html(m.group(1)) if m else ""

    def _extract_class_tagged_values(self, body: str) -> dict[str, str]:
        """Return class-level tagged values only. Scoped to the body region
        before <UML:Classifier.feature>, so attribute-level tags are excluded."""
        feature_start = body.find("<UML:Classifier.feature>")
        scope = body if feature_start == -1 else body[:feature_start]
        out: dict[str, str] = {}
        for m in re.finditer(r'<UML:TaggedValue tag="([^"]+)" value="([^"]*)"', scope):
            out.setdefault(m.group(1), m.group(2))
        return out

    def _extract_attributes(self, body: str) -> list[Attribute]:
        attrs: list[Attribute] = []
        for am in re.finditer(r'<UML:Attribute\s+name="([^"]+)"', body):
            a_start = am.start()
            a_end = body.find("</UML:Attribute>", a_start)
            if a_end == -1:
                continue
            seg = body[a_start:a_end]
            type_m = re.search(r'<UML:TaggedValue tag="type" value="([^"]+)"', seg)
            lo_m = re.search(r'<UML:TaggedValue tag="lowerBound" value="([^"]+)"', seg)
            up_m = re.search(r'<UML:TaggedValue tag="upperBound" value="([^"]+)"', seg)
            desc_m = re.search(r'<UML:TaggedValue tag="description" value="([^"]*)"', seg)
            st_m = re.search(r'<UML:Stereotype\s+name="([^"]+)"', seg)
            type_name = type_m.group(1) if type_m else ""
            lo = self._parse_bound(lo_m.group(1) if lo_m else "1")
            up = self._parse_bound(up_m.group(1) if up_m else "1")
            iob_m = re.search(r'<UML:TaggedValue tag="inlineOrByReference" value="([^"]+)"', seg)
            attrs.append(Attribute(
                name=am.group(1),
                type_name=type_name,
                lower=lo,
                upper=up,
                doc=self._clean_html(desc_m.group(1)) if desc_m else "",
                stereotype=st_m.group(1) if st_m else "",
                inline_or_byref=iob_m.group(1) if iob_m else "",
            ))
        return attrs

    def _merge_associations(self) -> None:
        """Walk every <UML:Association> and merge each navigable end as a
        synthetic Attribute on the OPPOSITE class. Uses ea_sourceName/
        ea_targetName to identify endpoint classes (more robust than xmi.idref
        resolution in EA's XMI 1.1 export)."""
        assoc_re = re.compile(
            r'<UML:Association\b(?!Class)[^>]*xmi\.id="[^"]+"[^>]*>(.*?)</UML:Association>',
            re.DOTALL,
        )
        end_re = re.compile(
            r'<UML:AssociationEnd\b([^>]*)>(.*?)</UML:AssociationEnd>', re.DOTALL,
        )
        attr_kv = re.compile(r'(\w[\w.\-]*)="([^"]*)"')

        for am in assoc_re.finditer(self.text):
            body = am.group(1)
            src_m = re.search(r'<UML:TaggedValue tag="ea_sourceName" value="([^"]+)"', body)
            tgt_m = re.search(r'<UML:TaggedValue tag="ea_targetName" value="([^"]+)"', body)
            if not src_m or not tgt_m:
                continue
            src_name, tgt_name = src_m.group(1), tgt_m.group(1)
            # association-level inlineOrByReference (rare)
            assoc_iob = re.search(
                r'<UML:TaggedValue tag="inlineOrByReference" value="([^"]+)"', body)
            assoc_iob_val = assoc_iob.group(1) if assoc_iob else ""
            # ShapeChange's AssociationClassMapper equivalent: if this Association
            # carries an `associationclass` tagged value (EA XMI 1.1 marker),
            # synthetic Attributes generated from navigable ends are re-typed to
            # the association class itself, not the partner class. Mirrors OGC's
            # geoscimlBasic.json shape where GeologicFeature.relatedFeature[].items
            # references #AbstractFeatureRelation (the AC), not #GeologicFeature.
            ac_m = re.search(
                r'<UML:TaggedValue tag="associationclass" value="([^"]+)"', body)
            ac_name = self.id_to_name.get(ac_m.group(1)) if ac_m else None

            ends: list[dict] = []
            for em in end_re.finditer(body):
                end_attrs = dict(attr_kv.findall(em.group(1)))
                end_body = em.group(2)
                ea_end_m = re.search(
                    r'<UML:TaggedValue tag="ea_end" value="([^"]+)"', end_body)
                desc_m = re.search(
                    r'<UML:TaggedValue tag="description" value="([^"]*)"', end_body)
                iob_m = re.search(
                    r'<UML:TaggedValue tag="inlineOrByReference" value="([^"]+)"', end_body)
                ends.append({
                    "side": ea_end_m.group(1) if ea_end_m else "?",
                    "name": end_attrs.get("name", ""),
                    "multiplicity": end_attrs.get("multiplicity", ""),
                    "navigable": end_attrs.get("isNavigable", "false") == "true",
                    "doc": self._clean_html(desc_m.group(1)) if desc_m else "",
                    "iob": iob_m.group(1) if iob_m else "",
                })

            # Map sides to class names
            side_to_class = {"source": src_name, "target": tgt_name}
            for end in ends:
                if not (end["navigable"] and end["name"]):
                    continue
                # Owner = opposite side; property type = same side's class
                opposite = "target" if end["side"] == "source" else "source"
                owner_class_name = side_to_class.get(opposite)
                prop_type = side_to_class.get(end["side"])
                if not owner_class_name or not prop_type:
                    continue
                owner_id = self.name_to_id.get(owner_class_name)
                if not owner_id:
                    continue
                owner = self.classes[owner_id]
                # Dedupe: skip if a UML:Attribute with this name already exists
                if any(a.name == end["name"] for a in owner.attributes):
                    continue
                lo, up = self._parse_multiplicity(end["multiplicity"])
                # Default for association role per OGC 24-017r1 = byReference,
                # unless overridden by an explicit tag on the end or association.
                iob_val = end["iob"] or assoc_iob_val or "byReference"
                # AssociationClassMapper: when the Association carries an
                # `associationclass` tag, the property's type is the AC itself,
                # not the partner class. (`prop_type` is replaced; owner-class
                # ends with a property typed by the relation class that mediates
                # the link.)
                effective_type = ac_name if ac_name else prop_type
                owner.attributes.append(Attribute(
                    name=end["name"],
                    type_name=effective_type,
                    lower=lo,
                    upper=up,
                    doc=end["doc"],
                    stereotype="associationRole",
                    inline_or_byref=iob_val,
                ))
                # AssociationClassMapper second direction: emit the back-
                # pointing property on the AC itself. Mirrors OGC's
                # geoscimlBasic.json, where AbstractFeatureRelation carries a
                # `relatedFeature` slot (singular, required) referencing the
                # partner class via `oneOf [SCLinkObject, GeologicFeature]`.
                # From the relation's perspective the target is exactly one
                # partner-class instance, so lower=upper=1.
                if ac_name:
                    ac_id = self.name_to_id.get(ac_name)
                    if ac_id is not None:
                        ac_class = self.classes[ac_id]
                        # Don't double-add if a UML:Attribute or earlier
                        # association pass already created this slot.
                        if not any(a.name == end["name"] for a in ac_class.attributes):
                            ac_class.attributes.append(Attribute(
                                name=end["name"],
                                type_name=prop_type,
                                lower=1,
                                upper=1,
                                doc=end["doc"],
                                stereotype="associationRole",
                                inline_or_byref=iob_val,
                            ))

    @staticmethod
    def _parse_multiplicity(s: str) -> tuple[int, int]:
        """Parse a UML multiplicity string ('0..1', '1..*', '0..*', '1', '*')."""
        s = (s or "").strip()
        if not s:
            return (1, 1)
        if ".." in s:
            lo_s, up_s = s.split("..", 1)
        else:
            lo_s, up_s = s, s
        def _b(x: str) -> int:
            x = x.strip()
            if x in ("*", "-1", "unbounded"):
                return -1
            try:
                return int(x)
            except ValueError:
                return 1
        return (_b(lo_s), _b(up_s))

    def _harvest_constraints(self) -> None:
        """Walk every <UML:Constraint> and attribute it to the enclosing
        <UML:Class> (and optionally <UML:Attribute>) based on document position.
        """
        # First, index Class open/close positions and Attribute open/close.
        class_spans: list[tuple[int, int, str]] = []  # (start, end, name)
        for cm in re.finditer(r'<UML:Class\b([^>]*)>', self.text):
            name_m = re.search(r'name="([^"]+)"', cm.group(1))
            if not name_m:
                continue
            end = self.text.find('</UML:Class>', cm.end())
            if end == -1:
                continue
            class_spans.append((cm.start(), end, name_m.group(1)))

        attr_spans: list[tuple[int, int, str]] = []
        for am in re.finditer(r'<UML:Attribute\b([^>]*)>', self.text):
            name_m = re.search(r'name="([^"]+)"', am.group(1))
            if not name_m:
                continue
            end = self.text.find('</UML:Attribute>', am.end())
            if end == -1:
                continue
            attr_spans.append((am.start(), end, name_m.group(1)))

        for cm in re.finditer(
            r'<UML:Constraint\b[^>]*name="([^"]+)"', self.text,
        ):
            text = self._clean_html(cm.group(1))
            pos = cm.start()
            # Find enclosing class
            owner_class = None
            for cstart, cend, cname in class_spans:
                if cstart <= pos <= cend:
                    owner_class = cname
                    # ok to keep the innermost (classes don't nest in EA)
            if not owner_class:
                continue
            # Find enclosing attribute (if any) - narrower than the class span
            owner_attr = None
            for astart, aend, aname in attr_spans:
                if astart <= pos <= aend:
                    owner_attr = aname
                    break
            if owner_attr:
                self.constraints_by_class_attr.setdefault(
                    (owner_class, owner_attr), []).append(text)
            else:
                self.constraints_by_class.setdefault(owner_class, []).append(text)

    @staticmethod
    def _parse_bound(s: str) -> int:
        s = s.strip()
        if s in ("*", "-1", "unbounded"):
            return -1
        try:
            return int(s)
        except ValueError:
            return 1


# Patch class-end finder onto the loader (needs access to self.text).
def _find_class_end(self: EaXmiLoader, after_open: int) -> int:
    m = re.compile(r'</UML:Class>').search(self.text, after_open)
    return m.end() if m else after_open
EaXmiLoader._find_class_end = _find_class_end  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Type resolver
# ---------------------------------------------------------------------------

@dataclass
class ResolvedType:
    """Describes how to encode a single attribute's value type in JSON Schema."""
    kind: str   # 'primitive' | 'geometry' | 'swe' | 'category' | 'local' | 'cross_bb' | 'external_iso' | 'unknown'
    schema: dict
    code_list_url: Optional[str] = None  # for kind='category' with a vocab
    target_class_name: Optional[str] = None  # for cross_bb / local


class Resolver:
    def __init__(
        self,
        loader: EaXmiLoader,
        target_packages: set[str],
        package_to_bb: dict[str, str],
        swe_mappings: dict,
        category_codelists: dict,
    ):
        self.loader = loader
        # Packages whose classes belong in the BB currently being generated.
        # Classes inside any of these are emitted into the BB's local $defs and
        # referenced as "#ClassName"; classes in other packages get a cross-BB
        # $ref via package_to_bb.
        self.target_packages = set(target_packages)
        self.package_to_bb = package_to_bb
        self.swe = swe_mappings.get("external_types", {})
        # index category codelists by (class, attribute)
        self.codelists: dict[tuple[str, str], dict] = {}
        for entry in category_codelists.get("attributes", []):
            key = (entry["class"], entry["attribute"])
            self.codelists[key] = entry
        # CodeList class → vocabulary URL (or "treat as open" sentinel)
        self.codelist_class_urls: dict[str, str] = category_codelists.get("codelist_classes", {}) or {}

    @staticmethod
    def _normalise(s: str) -> str:
        return (s or "").strip().lower().replace(",", " ")

    def category_for(self, class_name: str, attr_name: str) -> Optional[dict]:
        return self.codelists.get((class_name, attr_name))

    def resolve(self, owning_class: str, attr: Attribute) -> ResolvedType:
        # Honor any per-attribute type override before consulting the UML type.
        # See ATTRIBUTE_TYPE_OVERRIDES for rationale.
        t = ATTRIBUTE_TYPE_OVERRIDES.get((owning_class, attr.name), attr.type_name)

        # 1. ISO 19103 primitive
        if t in ISO_19103_PRIMITIVE_MAP:
            json_t, fmt = ISO_19103_PRIMITIVE_MAP[t]
            schema = {"type": json_t}
            if fmt:
                schema["format"] = fmt
            return ResolvedType("primitive", schema)

        # 2. ISO 19107 geometry
        if t in ISO_19107_GEOMETRY_MAP:
            return ResolvedType("geometry", {"$ref": ISO_19107_GEOMETRY_MAP[t]})

        # 3. SWE 2.0 -> SWE 3.0 substitution
        if t in self.swe:
            return ResolvedType("swe", {"$ref": self.swe[t]["ref"]})

        # 4. Category -> SWE 3.0 Category $ref (per OGC team's convention).
        # The OGC team uses SWE Category objects for SWE::Category-typed
        # attributes, not plain URI strings. Drop the `codeList` annotation.
        if t == "Category":
            return ResolvedType(
                "category",
                {"$ref": "https://schemas.opengis.net/sweCommon/3.0/json/Category.json"},
            )

        # 5. ISO 19103 composite (ScopedName, NamedValue, etc.)
        if t in ISO_19103_COMPOSITES:
            ns = ISO_19103_COMPOSITES[t]
            return ResolvedType("external_iso", _resolve_external_type(f"{ns}:{t}"))

        # 6. ISO prefix-based imports (CI_*, TM_*, SC_*, ...)
        for pat, ns in ISO_PREFIX_MAP:
            if pat.match(t):
                return ResolvedType("external_iso", _resolve_external_type(f"{ns}:{t}"))

        # 7. A class defined somewhere in the XMI: local or cross-BB.
        #    Apply UML tag inlineOrByReference for non-CodeList class types.
        #    CodeList types always use the URI codelist encoding (overrides tag).
        if t in self.loader.name_to_id:
            cls = self.loader.classes[self.loader.name_to_id[t]]
            target_pkg = cls.package_path[-1] if cls.package_path else None
            same_bb = bool(target_pkg and target_pkg in self.target_packages)
            target_stereo = (cls.stereotype or "").lower()

            def _cross_bb_ref(suffix: str) -> dict:
                bb = self.package_to_bb.get(target_pkg) if target_pkg else None
                if not bb:
                    return {
                        "$ref": f"unresolved:{t}",
                        "$comment": f"unmapped package {target_pkg!r} for class {t}",
                    }
                return {
                    "$ref": f"../{bb}/{bb}Schema.json#{t}",
                    "$comment": f"cross-BB {suffix} to {t} in BB {bb}",
                }

            # CodeList target: $ref to the local codelist class definition.
            # No codeList annotation per OGC team's convention.
            if target_stereo == "codelist":
                ref = {"$ref": f"#{t}"} if same_bb else _cross_bb_ref("reference")
                return ResolvedType("category", ref, target_class_name=t)

            inline_ref = {"$ref": f"#{t}"} if same_bb else _cross_bb_ref("inline reference")
            link_obj = {
                "$ref": LINK_OBJECT_REF,
                "$comment": f"by-reference link to {t}",
            }

            # OGC team convention: DataType and unstereotyped object targets
            # are always inline. Types-with-identity (FeatureType / Type) get
            # oneOf [SCLinkObject, $ref Class] by default; explicit
            # inlineOrByReference tag values override.
            is_with_identity = target_stereo in ("featuretype", "type")
            if not is_with_identity:
                return ResolvedType(
                    "local" if same_bb else "cross_bb",
                    inline_ref, target_class_name=t,
                )

            iob = (attr.inline_or_byref or "").strip()
            if iob == "inline":
                return ResolvedType(
                    "local" if same_bb else "cross_bb",
                    inline_ref, target_class_name=t,
                )
            # Default (and `byReference` and explicit `inlineOrByReference`): allow
            # either a link object or a fully-inlined class instance. The OGC team's
            # geoscimlBasic.json uses this same oneOf pattern. We override the UML
            # `byReference` tag intent here so that rich example instances (with
            # nested feature content) remain valid alongside terse link refs.
            return ResolvedType(
                "cross_bb",
                {"oneOf": [link_obj, inline_ref]},
                target_class_name=t,
            )

        # 8. Unknown
        return ResolvedType(
            "unknown",
            {
                "$comment": f"Unresolved type: {t}",
                "type": "object",
            },
        )


# ---------------------------------------------------------------------------
# Emitter - applies OGC 24-017r1 to produce a class's JSON Schema definition.
# ---------------------------------------------------------------------------

class Emitter:
    def __init__(self, resolver: Resolver, loader: EaXmiLoader):
        self.r = resolver
        self.loader = loader

    # ----- public ----------------------------------------------------------

    def emit_class(self, cls: UmlClass) -> dict:
        s = (cls.stereotype or "").lower()
        if s == "codelist":
            return self._emit_codelist(cls)
        if s == "union":
            return self._emit_union(cls)
        # A class is Feature-shaped if it carries «FeatureType», has an OCL
        # constraint pinning its hierarchyLevel to feature, or transitively
        # inherits from such a class. OGC's geoscimlBasic.json applies this
        # to EarthMaterial/CompoundMaterial/RockMaterial (UML stereotype is
        # `type`, but constraint `self.metadata.hierarchyLevel=feature`
        # marks them as Features). Without this transitive check, nested
        # `composition[].material` instances cannot be valid Features.
        if self._is_feature_like(cls):
            return self._emit_feature_type(cls)
        # DataType / Type / unstereotyped class
        return self._emit_object_type(cls)

    def _is_feature_like(self, cls: UmlClass) -> bool:
        """True if cls should be emitted as a JSON-FG Feature.

        Mirrors OGC's ShapeChange config (geoscimlBasic_jsonfg.xml) which sets
        `baseJsonSchemaDefinitionForObjectTypes = feature.json` and applies it
        to both FeatureType and Type stereotypes. So any UML class with
        identity (FeatureType, Type) becomes a Feature; only DataType / Union /
        CodeList classes stay flat. Also honored: legacy «type» classes that
        carry an explicit `self.metadata.hierarchyLevel=feature` OCL constraint,
        and transitive inheritance from any Feature-like class."""
        s = (cls.stereotype or "").lower()
        if s in ("featuretype", "type"):
            return True
        for c in self.loader.constraints_by_class.get(cls.name, []):
            lc = c.lower()
            if "hierarchylevel" in lc and "feature" in lc:
                return True
        for sup_name in cls.supertypes:
            sup_id = self.loader.name_to_id.get(sup_name)
            if not sup_id:
                continue
            sup = self.loader.classes[sup_id]
            if self._is_feature_like(sup):
                return True
        return False

    def _class_description(self, cls: UmlClass) -> str:
        """Class doc with any class-level OCL constraints appended."""
        parts: list[str] = []
        if cls.doc:
            parts.append(cls.doc)
        for c in self.loader.constraints_by_class.get(cls.name, []):
            parts.append(f"Constraint: {c}")
        return "  ".join(parts)

    def _attribute_description(self, cls_name: str, attr: Attribute) -> str:
        parts: list[str] = []
        if attr.doc:
            parts.append(attr.doc)
        for c in self.loader.constraints_by_class_attr.get((cls_name, attr.name), []):
            parts.append(f"Constraint: {c}")
        return "  ".join(parts)

    # ----- per stereotype --------------------------------------------------

    def _emit_codelist(self, cls: UmlClass) -> dict:
        # All «CodeList» classes - including those with inline UML enumeration
        # members like DescriptionPurpose - emit as {type: string, format: uri}
        # per OGC 24-017r1 req/codelists-basic. Inline enum-member names (when
        # present in the source UML) are surfaced via the class description so
        # consumers can map labels to vocabulary URIs externally, but the
        # JSON-Schema-side constraint stays URI-shaped to match the OGC
        # code-sprint convention and the OGC sprint example instances
        # (which encode `purpose: "http://inspire.../DescriptionPurpose/instance"`
        # - full URI form - not bare names).
        d: dict = OrderedDict()
        d["$anchor"] = cls.name
        desc = self._class_description(cls)
        # If the UML carries inline enumeration members, surface them in the
        # description so the allowed labels are documented even though the
        # constraint is just `format: uri`.
        enum_members = [a.name for a in cls.attributes if not a.type_name]
        if enum_members:
            label_note = f"Allowed labels: {', '.join(enum_members)}."
            desc = (desc + "  " + label_note).strip() if desc else label_note
        if desc:
            d["description"] = desc
        d["type"] = "string"
        d["format"] = "uri"
        cl_tag = (cls.tagged_values.get("codeList") or "").strip()
        if cl_tag:
            d["codeList"] = cl_tag
        return d

    def _emit_union(self, cls: UmlClass) -> dict:
        # OGC 24-017r1 req/union-type-discriminator: encode as a choice between
        # the value types of the union's properties.
        d: dict = OrderedDict()
        d["$anchor"] = cls.name
        desc = self._class_description(cls)
        if desc:
            d["description"] = desc
        one_of: list[dict] = []
        for a in cls.attributes:
            rt = self.r.resolve(cls.name, a)
            one_of.append(rt.schema)
        d["oneOf"] = one_of
        return d

    def _emit_feature_type(self, cls: UmlClass) -> dict:
        # OGC team convention (geoscimlBasic.json): FeatureType is encoded as
        #   allOf [
        #     { $ref: parent or JSON-FG Feature },
        #     { type: object, properties: { properties: { type: object, properties: { ...own fields... } } } },
        #     { required: [featureType, id], properties: { id: {type:string} } }    ← only on root FeatureType
        #   ]
        # The nested `properties.properties` matches JSON-FG's `properties`
        # envelope. The required constraint lives on the root FeatureType
        # (one without a FeatureType supertype) and is inherited by subtypes.
        own_props_envelope = self._build_feature_type_own_envelope(cls)
        d: dict = OrderedDict()
        d["$anchor"] = cls.name
        desc = self._class_description(cls)
        if desc:
            d["description"] = desc

        parent_ref = self._feature_supertype_ref(cls)
        if parent_ref is not None:
            d["allOf"] = [parent_ref, own_props_envelope]
            return d

        # No Feature-like UML supertype. Before falling back to JSON-FG
        # Feature as the base, check whether the class has a supertype that
        # resolves to an external mapped schema (e.g. SWE QuantityRange in
        # swe-mappings.yaml, or an ISO 19103/19107 mapped type). If so, use
        # that external schema as the parent and omit the JSON-FG
        # featureType/id requirement (those don't apply to non-Feature
        # parents like swe:QuantityRange). Mirrors ShapeChange's
        # rule-json-cls-virtualGeneralization behaviour against MapEntries.
        ext_ref = self._external_mapped_supertype_ref(cls)
        if ext_ref is not None:
            d["allOf"] = [ext_ref, own_props_envelope]
            return d

        d["allOf"] = [
            {"$ref": JSON_FG_FEATURE_REF},
            own_props_envelope,
            {
                "required": ["featureType", "id"],
                "properties": {"id": {"type": "string"}},
            },
        ]
        return d

    def _external_mapped_supertype_ref(self, cls: UmlClass) -> Optional[dict]:
        """If cls has a UML supertype that resolves to an external mapped
        schema (SWE, ISO 19103/107 composite/geometry), return a $ref to that
        external schema. Used by _emit_feature_type when a class with a
        non-local parent (e.g. GSML_QuantityRange extends swe:QuantityRange)
        should hang off the external schema instead of being wrapped in
        json-fg/feature.json."""
        for sup_name in cls.supertypes:
            if not sup_name or sup_name.startswith("__unresolved_"):
                continue
            # Local UML class -> handled by _feature_supertype_ref already
            if sup_name in self.loader.name_to_id:
                continue
            # SWE 2.0 -> 3.0 substitution (swe-mappings.yaml)
            if sup_name in self.r.swe:
                return {"$ref": self.r.swe[sup_name]["ref"]}
            # ISO 19107 geometry types
            if sup_name in ISO_19107_GEOMETRY_MAP:
                return {"$ref": ISO_19107_GEOMETRY_MAP[sup_name]}
            # ISO 19103 composites (ScopedName, NamedValue, etc.)
            if sup_name in ISO_19103_COMPOSITES:
                ns = ISO_19103_COMPOSITES[sup_name]
                return _resolve_external_type(f"{ns}:{sup_name}")
        return None

    def _build_feature_type_own_envelope(self, cls: UmlClass) -> dict:
        """Build the {type: object, properties: { properties: { ... } } }
        envelope for a FeatureType - class-specific fields live inside the
        JSON-FG `properties` member. Inner properties whose UML multiplicity
        is lower>=1 are listed in `required` (matches OGC's emission, e.g.
        AbstractFeatureRelation.required = [relatedFeature]).

        UML attribute names that ShapeChange maps to JSON-FG root members
        (`identifier` -> `id`, `entityType` -> `featureType`, `shape` ->
        `geometry`/`place`) are excluded from the inner required list -
        OGC's rule-json-cls-restrictExternalIdentifierMember /
        rule-json-cls-restrictExternalEntityTypeMember do the equivalent.
        We still emit them as inner properties (a partial divergence from
        ShapeChange, which strips them entirely) but don't enforce them as
        required since they're satisfied by the JSON-FG root slots."""
        inner_props: dict = OrderedDict()
        required: list[str] = []
        # JSON-FG-reserved name equivalents. UML lower>=1 on these slots is
        # satisfied by the JSON-FG root member, not by an inner property.
        FG_RESERVED_NAMES = {"identifier", "entityType", "shape"}
        for a in cls.attributes:
            inner_props[a.name] = self._build_attribute_schema(cls.name, a)
            if a.lower >= 1 and a.name not in FG_RESERVED_NAMES:
                required.append(a.name)
        inner_obj: dict = OrderedDict()
        inner_obj["type"] = "object"
        inner_obj["properties"] = inner_props
        if required:
            inner_obj["required"] = required
        envelope: dict = OrderedDict()
        envelope["type"] = "object"
        envelope["properties"] = {"properties": inner_obj}
        # If any inner property is required, the outer `properties` envelope
        # itself must exist on the instance. OGC's emission applies this
        # consistently (e.g. AbstractFeatureRelation.required = ["properties"];
        # GSML_QuantityRange.required = ["properties"]).
        if required:
            envelope["required"] = ["properties"]
        return envelope

    def _emit_object_type(self, cls: UmlClass) -> dict:
        # DataType / Type / unstereotyped: simple {type: object, properties:{...}}
        # No JSON-FG envelope, no entityType, no required slots beyond what's
        # explicitly multiplicity-1 on each attribute.
        own: dict = OrderedDict()
        own["type"] = "object"
        own_props: dict = OrderedDict()
        required: list[str] = []
        for a in cls.attributes:
            own_props[a.name] = self._build_attribute_schema(cls.name, a)
            if a.lower >= 1:
                required.append(a.name)
        if own_props:
            own["properties"] = own_props
        if required:
            own["required"] = required

        d: dict = OrderedDict()
        d["$anchor"] = cls.name
        desc = self._class_description(cls)
        if desc:
            d["description"] = desc
        parent_ref = self._object_supertype_ref(cls)
        if parent_ref is not None:
            d["allOf"] = [parent_ref, own]
            return d
        d.update(own)
        return d

    # ----- attribute schema builder ----------------------------------------

    def _build_attribute_schema(self, owning_class: str, a: Attribute) -> dict:
        """Per OGC team convention (geoscimlBasic.json): optional attributes
        are not present in the instance at all when there's no value (omit-key,
        not explicit null). The schema therefore emits the value's inner shape
        directly without an `oneOf [{type: null}, ...]` wrap. Optionality is
        conveyed by absence from the enclosing `required` array. Array-valued
        attributes still get the `type: array` envelope before this rule."""
        rt = self.r.resolve(owning_class, a)
        desc = self._attribute_description(owning_class, a)

        if a.upper > 1 or a.upper == -1:
            # array-valued
            inner: dict = OrderedDict()
            inner["type"] = "array"
            if a.lower >= 1:
                inner["minItems"] = a.lower
            if a.upper > 1:
                inner["maxItems"] = a.upper
            inner["items"] = rt.schema
            inner["uniqueItems"] = True
        else:
            inner = rt.schema

        out: dict = OrderedDict(inner) if isinstance(inner, dict) else dict(inner)
        if desc and "description" not in out:
            out["description"] = desc
        return out

    # ----- supertype resolution --------------------------------------------

    def _feature_supertype_ref(self, cls: UmlClass) -> Optional[dict]:
        """If cls has a Feature-like supertype, $ref it instead of JSON-FG."""
        for sup_name in cls.supertypes:
            sup_id = self.loader.name_to_id.get(sup_name)
            if not sup_id:
                continue
            sup = self.loader.classes[sup_id]
            if not self._is_feature_like(sup):
                continue
            return self._supertype_ref_for(sup)
        return None

    def _object_supertype_ref(self, cls: UmlClass) -> Optional[dict]:
        """For non-FeatureType: $ref any supertype, local or cross-BB."""
        for sup_name in cls.supertypes:
            sup_id = self.loader.name_to_id.get(sup_name)
            if not sup_id:
                continue
            sup = self.loader.classes[sup_id]
            return self._supertype_ref_for(sup)
        return None

    def _supertype_ref_for(self, sup: UmlClass) -> dict:
        pkg = sup.package_path[-1] if sup.package_path else None
        if pkg and pkg in self.r.target_packages:
            return {"$ref": f"#{sup.name}"}
        bb = self.r.package_to_bb.get(pkg) if pkg else None
        if not bb:
            return {
                "$ref": f"unresolved:{sup.name}",
                "$comment": f"unmapped package {pkg!r} for supertype {sup.name}",
            }
        return {
            "$ref": f"../{bb}/{bb}Schema.json#{sup.name}",
            "$comment": f"cross-BB supertype reference to {sup.name} in BB {bb}",
        }



# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def collect_group_classes(loader: EaXmiLoader, packages: set[str]) -> list[UmlClass]:
    out: list[UmlClass] = []
    for cls in loader.classes.values():
        if cls.name in NOT_ENCODED_CLASSES:
            continue
        if cls.package_path and cls.package_path[-1] in packages:
            out.append(cls)
    out.sort(key=lambda c: c.name)
    return out


# ---------------------------------------------------------------------------
# Phase 2: per-BB Feature and FeatureCollection dispatcher schemas
# ---------------------------------------------------------------------------

_FC_MEMBER_ATTR_NAMES = {"member", "members", "features"}


def _is_fc_container(cls: UmlClass) -> bool:
    """Heuristic: a «FeatureType» class with a *..* member-like attribute is a
    FeatureCollection container (e.g. GSML), not a dispatchable Feature. It
    becomes the seed for the FC dispatcher schema rather than a regular FT def.
    """
    if (cls.stereotype or "").lower() != "featuretype":
        return False
    for a in cls.attributes:
        if a.name.lower() in _FC_MEMBER_ATTR_NAMES and (a.upper > 1 or a.upper == -1):
            return True
    return False


def dispatchable_fts(loader: EaXmiLoader, packages: set[str]) -> list[str]:
    """Concrete «FeatureType» classes in the BB that are dispatchable via the
    `featureType` discriminator: non-abstract, not an FC-container."""
    out: list[str] = []
    for cls in loader.classes.values():
        if not (cls.package_path and cls.package_path[-1] in packages):
            continue
        if (cls.stereotype or "").lower() != "featuretype":
            continue
        if cls.abstract:
            continue
        if _is_fc_container(cls):
            continue
        out.append(cls.name)
    return sorted(out)


def build_merged_schema(
    bb_name: str,
    library_schema: dict,
    dispatch_entries: list[dict],
) -> dict:
    """Combine the library `$defs` and the Feature / FeatureCollection
    dispatchers into a single schema. The root discriminates on `type`:
      - `type == "FeatureCollection"`: validate as json-fg FeatureCollection
        with `features.items` dispatched by featureType via the internal
        `_FeatureDispatch` helper def.
      - otherwise: treat as a single Feature and validate via the same
        `_FeatureDispatch` helper.

    `dispatch_entries` is a list of dicts, each with:
      - name (str)           the featureType discriminator value
      - ref (str)            JSON Pointer / $ref to the target schema. Local
                             anchors look like "#ClassName"; cross-BB look
                             like "../<bb>/<bb>Schema.json#ClassName".
      - wrapAsFeature (bool, optional)  inject JSON-FG envelope (use for
                                        «Type» classes that aren't already
                                        FeatureType-stereotyped)
      - extensionConstraints (dict, optional)       slot -> $ref (scalar)
      - extensionConstraintsArray (dict, optional)  slot -> $ref (array)

    Entries reuse _build_profile_branch() for the `then`-schema, so all
    wrap / constrain semantics are shared with FC-profile BBs."""
    branches: list[dict] = []
    ft_names = [e["name"] for e in dispatch_entries]
    for entry in dispatch_entries:
        branches.append({
            "if": {
                "required": ["featureType"],
                "properties": {"featureType": {"const": entry["name"]}},
            },
            "then": _build_profile_branch(entry),
        })
    branches.append({
        "if": {
            "not": {
                "required": ["featureType"],
                "properties": {"featureType": {"enum": list(ft_names)}},
            }
        },
        "then": False,
    })
    feature_dispatch = {"allOf": branches}

    # Compose new $defs: dispatcher helper first, then all library defs.
    merged_defs: dict = OrderedDict()
    merged_defs["_FeatureDispatch"] = feature_dispatch
    for name, d in library_schema.get("$defs", {}).items():
        merged_defs[name] = d

    desc = library_schema.get("description", "").rstrip()
    desc += (
        "\n\nValidates either a single Feature (dispatched by `featureType` "
        f"to one of: {', '.join(ft_names)}) or a FeatureCollection whose "
        "`features[]` items are dispatched the same way."
    )

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", library_schema["$id"]),  # keep same canonical URL
        ("description", desc),
        ("if", {
            "type": "object",
            "required": ["type"],
            "properties": {"type": {"const": "FeatureCollection"}},
        }),
        ("then", {
            "allOf": [
                {"$ref": "https://schemas.opengis.net/json-fg/featurecollection.json"},
                {
                    "type": "object",
                    "properties": {
                        "features": {
                            "type": "array",
                            "items": {"$ref": "#/$defs/_FeatureDispatch"},
                        }
                    },
                },
            ],
        }),
        ("else", {"$ref": "#/$defs/_FeatureDispatch"}),
        ("$defs", merged_defs),
    ])


def build_feature_dispatcher(bb_name: str, ft_names: list[str]) -> dict:
    """Build <bbName>FeatureSchema.json - an if/then chain on `featureType`
    routing each recognised value to the corresponding $anchor in the BB's
    library schema. An unrecognised featureType fails (else-false clause)."""
    branches: list[dict] = []
    for ft in ft_names:
        branches.append({
            "if": {
                "required": ["featureType"],
                "properties": {"featureType": {"const": ft}},
            },
            "then": {"$ref": f"{bb_name}Schema.json#{ft}"},
        })
    branches.append({
        "if": {
            "not": {
                "required": ["featureType"],
                "properties": {"featureType": {"enum": list(ft_names)}},
            }
        },
        "then": False,
    })
    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"https://schemas.usgin.org/geosci-json/{bb_name}/{bb_name}FeatureSchema.json"),
        ("description",
         f"Single-Feature dispatcher for the {bb_name} BB. Routes by the "
         f"instance's `featureType` value to the matching $anchor in "
         f"{bb_name}Schema.json. Recognised featureType values: "
         f"{', '.join(ft_names)}."),
        ("allOf", branches),
    ])


def build_fc_dispatcher(bb_name: str, ft_names: list[str]) -> dict:
    """Build <bbName>FeatureCollectionSchema.json - composes the JSON-FG
    FeatureCollection schema with `features.items` validated through the
    Feature dispatcher. DRY composition: dispatch logic lives in
    <bbName>FeatureSchema.json."""
    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"https://schemas.usgin.org/geosci-json/{bb_name}/{bb_name}FeatureCollectionSchema.json"),
        ("description",
         f"FeatureCollection wrapper for the {bb_name} BB. Combines "
         f"json-fg/featurecollection.json with per-item dispatch via "
         f"{bb_name}FeatureSchema.json. Recognised featureType values for items: "
         f"{', '.join(ft_names)}."),
        ("allOf", [
            {"$ref": "https://schemas.opengis.net/json-fg/featurecollection.json"},
            {
                "type": "object",
                "properties": {
                    "features": {
                        "type": "array",
                        "items": {"$ref": f"{bb_name}FeatureSchema.json"},
                    }
                },
            },
        ]),
    ])


def build_schema(
    loader: EaXmiLoader,
    bb_name: str,
    packages: set[str],
    package_to_bb: dict[str, str],
    swe_mappings: dict,
    category_codelists: dict,
    bb_description: str,
) -> dict:
    resolver = Resolver(loader, packages, package_to_bb, swe_mappings, category_codelists)
    emitter = Emitter(resolver, loader)
    classes = collect_group_classes(loader, packages)
    defs: dict = OrderedDict()
    for cls in classes:
        defs[cls.name] = emitter.emit_class(cls)
    # Add the local SCLinkObject definition so each BB is self-contained for
    # by-reference encoding. Matches OGC team's geoscimlBasic/Lite convention.
    defs["SCLinkObject"] = SCLINK_OBJECT_DEF
    # Merge any hand-curated extra defs for this BB (e.g. SF_Specimen for
    # gsmSpecimen, since ISO 19156 isn't in the GeoSciML XMI).
    for name, d in EXTRA_DEFS_PER_BB.get(bb_name, {}).items():
        defs[name] = d
    schema: dict = OrderedDict()
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["$id"] = f"https://schemas.usgin.org/geosci-json/{bb_name}/{bb_name}Schema.json"
    schema["description"] = bb_description.strip() or f"GeoSciML 4.1 {bb_name} building block."
    schema["$defs"] = defs
    return schema


def build_bblock_metadata(bb_name: str, bb_description: str, packages: list[str]) -> dict:
    abstract = bb_description.strip().splitlines()[0] if bb_description else \
        f"GeoSciML 4.1 {bb_name} encoded as JSON Schema per OGC 24-017r1."
    return OrderedDict({
        "$schema": "metaschema.yaml",
        "itemIdentifier": f"usgin.bbr.geosci.{bb_name}",
        "name": bb_name,
        "abstract": abstract,
        "status": "under-development",
        "dateTimeAddition": "2026-05-12T00:00:00Z",
        "itemClass": "schema",
        "register": "usgin-geosci-bblocks-register",
        "version": "0.1",
        "link": "https://github.com/usgin/geosci-json",
        "sources": [
            {
                "title": "GeoSciML 4.1 UML model (Enterprise Architect XMI export)",
                "link": "https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi"
            }
        ],
        "tags": ["geoscience", "geosciml", "uml-derived"],
        "umlPackages": packages,
    })


def load_grouping(config_path: Path) -> tuple[dict[str, dict], dict[str, str], dict[str, dict]]:
    """Returns (bbs, package_to_bb, profiles).

    bbs maps bb_name -> {description, packages} for UML-driven BBs.
    profiles maps profile_bb_name -> {description, featureTypes} for hand-
    authored FC profile BBs (not driven by UML packages).
    """
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    bbs_raw = (raw or {}).get("bbs", {}) or {}
    profiles_raw = (raw or {}).get("profiles", {}) or {}
    bbs: dict[str, dict] = {}
    package_to_bb: dict[str, str] = {}
    for bb_name, entry in bbs_raw.items():
        if not entry or "packages" not in entry:
            continue
        pkgs = list(entry["packages"])
        bbs[bb_name] = {
            "description": entry.get("description", "") or "",
            "packages": pkgs,
            # Optional explicit dispatch config (list of dicts: name, ref,
            # wrapAsFeature, extensionConstraints, extensionConstraintsArray).
            # When present, replaces the auto-discovered FT list AND any
            # Python-side DISPATCHER_OVERRIDES_PER_BB entry.
            "dispatch": list(entry["dispatch"]) if entry.get("dispatch") else None,
        }
        for p in pkgs:
            if p in package_to_bb:
                raise ValueError(
                    f"Package {p!r} assigned to both {package_to_bb[p]!r} and {bb_name!r}"
                )
            package_to_bb[p] = bb_name
    profiles: dict[str, dict] = {}
    for prof_name, entry in profiles_raw.items():
        if not entry or "featureTypes" not in entry:
            continue
        profiles[prof_name] = {
            "description": entry.get("description", "") or "",
            "featureTypes": list(entry["featureTypes"]),
            "featuresConstraintsArrayAnyOf": entry.get("featuresConstraintsArrayAnyOf") or {},
        }
    return bbs, package_to_bb, profiles


def _build_constraint_block(scalar_constraints: dict, array_constraints: dict) -> Optional[dict]:
    """Build the {properties: {properties: {properties: {<slot>: ...}}}} block
    that constrains specific slots inside the JSON-FG `properties` envelope.
    Returns None if no constraints."""
    inner_props: dict = OrderedDict()
    for slot, ext_ref in (scalar_constraints or {}).items():
        inner_props[slot] = {"$ref": ext_ref}
    for slot, ext_ref in (array_constraints or {}).items():
        inner_props[slot] = {"type": "array", "items": {"$ref": ext_ref}}
    if not inner_props:
        return None
    return {
        "type": "object",
        "properties": {
            "properties": {
                "type": "object",
                "properties": inner_props,
            }
        },
    }


def _build_profile_branch(entry: dict) -> dict:
    """Produce the `then` schema for one featureType branch.

    Two modes:
      (a) entry.wrapAsFeature is false/missing: the source class is already
          a «FeatureType», so its $anchor includes the JSON-FG envelope.
          Compose allOf [ref, scalar+array constraints].
      (b) entry.wrapAsFeature is true: the source class is «Type». Wrap
          the schema with the JSON-FG Feature envelope and put the class
          schema under properties.properties.allOf, where extra constraints
          on inner slots can be added.
    """
    ref = entry["ref"]
    scalar = entry.get("extensionConstraints", {}) or {}
    array  = entry.get("extensionConstraintsArray", {}) or {}

    if not entry.get("wrapAsFeature"):
        # Mode (a): the anchor is already a FeatureType.
        chain: list[dict] = [{"$ref": ref}]
        block = _build_constraint_block(scalar, array)
        if block is not None:
            chain.append(block)
        return chain[0] if len(chain) == 1 else {"allOf": chain}

    # Mode (b): «Type» source class -> inject JSON-FG envelope.
    inner: list[dict] = [{"$ref": ref}]
    if scalar or array:
        inner_constraint: dict = OrderedDict()
        slot_props: dict = OrderedDict()
        for slot, ext_ref in scalar.items():
            slot_props[slot] = {"$ref": ext_ref}
        for slot, ext_ref in array.items():
            slot_props[slot] = {"type": "array", "items": {"$ref": ext_ref}}
        inner_constraint["type"] = "object"
        inner_constraint["properties"] = slot_props
        inner.append(inner_constraint)
    inner_schema = inner[0] if len(inner) == 1 else {"allOf": inner}

    return {
        "allOf": [
            {"$ref": "https://schemas.opengis.net/json-fg/feature.json"},
            {
                "type": "object",
                "required": ["featureType", "id"],
                "properties": {"id": {"type": "string"}},
            },
            {
                "type": "object",
                "properties": {
                    "properties": inner_schema,
                },
            },
        ],
    }


def build_profile_schema(profile_name: str, info: dict) -> dict:
    """Build an FC-profile schema: json-fg/featurecollection with `features`
    items dispatched by featureType to cross-BB anchors. Per-entry options:
      ref:                        $ref to the source class anchor (required)
      wrapAsFeature:              when true, inject the JSON-FG envelope
                                  (allOf [feature.json, required featureType/id,
                                  properties.properties: <ref> + constraints]).
                                  Use this when the source class is «Type»,
                                  not «FeatureType», and lacks the FT envelope.
      extensionConstraints:       scalar slot -> $ref (applied to
                                  properties.properties.<slot>)
      extensionConstraintsArray:  array slot -> $ref (constrains items)

    Profile-level options (apply to every dispatched feature regardless of
    featureType):
      featuresConstraintsArrayAnyOf: dict of slot -> list[$ref]. Emits a new
        top-level allOf clause requiring every feature's
        properties.<slot>.items to validate against `anyOf [{$ref: each}]`.
        Use to narrow an abstract slot (e.g. relatedFeature whose Basic items
        type is AbstractFeatureRelation) to a fixed set of concrete subtypes
        in the profile.
    """
    ft_entries = info["featureTypes"]
    ft_names = [e["name"] for e in ft_entries]

    branches: list[dict] = []
    for entry in ft_entries:
        branches.append({
            "if": {
                "required": ["featureType"],
                "properties": {"featureType": {"const": entry["name"]}},
            },
            "then": _build_profile_branch(entry),
        })
    # else-false: featureType not in the recognised list -> fail
    branches.append({
        "if": {
            "not": {
                "required": ["featureType"],
                "properties": {"featureType": {"enum": list(ft_names)}},
            }
        },
        "then": False,
    })

    allof_items: list[dict] = [
        {"$ref": "https://schemas.opengis.net/json-fg/featurecollection.json"},
        {
            "type": "object",
            "properties": {
                "features": {
                    "type": "array",
                    "items": {"allOf": branches},
                }
            },
        },
    ]

    # Optional profile-level slot narrowing applied to every feature.
    extra = info.get("featuresConstraintsArrayAnyOf") or {}
    if extra:
        slot_props: dict = OrderedDict()
        for slot, refs in extra.items():
            slot_props[slot] = {
                "type": "array",
                "items": {"anyOf": [{"$ref": r} for r in refs]},
            }
        allof_items.append({
            "type": "object",
            "properties": {
                "features": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "object",
                                "properties": slot_props,
                            }
                        },
                    },
                }
            },
        })

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"https://schemas.usgin.org/geosci-json/{profile_name}/{profile_name}Schema.json"),
        ("description", info["description"].strip()),
        ("allOf", allof_items),
    ])


def build_profile_metadata(profile_name: str, info: dict) -> dict:
    abstract = info["description"].strip().splitlines()[0] if info["description"] else \
        f"GeoSciML 4.1 FC profile {profile_name}."
    ft_names = [e["name"] for e in info["featureTypes"]]
    return OrderedDict({
        "$schema": "metaschema.yaml",
        "itemIdentifier": f"usgin.bbr.geosci.{profile_name}",
        "name": profile_name,
        "abstract": abstract,
        "status": "under-development",
        "dateTimeAddition": "2026-05-12T00:00:00Z",
        "itemClass": "schema",
        "register": "usgin-geosci-bblocks-register",
        "version": "0.1",
        "link": "https://github.com/usgin/geosci-json",
        "sources": [
            {
                "title": "GeoSciML 4.1 - FC profile composed across building blocks",
                "link": "https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml"
            }
        ],
        "tags": ["geoscience", "geosciml", "profile", "featurecollection"],
        "profileOf": "FeatureCollection",
        "featureTypes": ft_names,
    })


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1] if __doc__ else "")
    p.add_argument("--xmi", required=True, type=Path)
    p.add_argument("--config", type=Path, default=Path("bb-grouping.yaml"),
                   help="BB grouping YAML (default: bb-grouping.yaml)")
    p.add_argument("--bb", default=None,
                   help="Optional: regenerate only this BB by name")
    p.add_argument("--out-dir", type=Path, default=Path("_sources"))
    p.add_argument("--swe-mappings", type=Path, default=Path("swe-mappings.yaml"))
    p.add_argument("--category-codelists", type=Path,
                   default=Path("cgi-vocab-reference.yaml"))
    args = p.parse_args()

    loader = EaXmiLoader(args.xmi)
    swe = yaml.safe_load(args.swe_mappings.read_text(encoding="utf-8"))
    cats = yaml.safe_load(args.category_codelists.read_text(encoding="utf-8"))

    bbs, package_to_bb, profiles = load_grouping(args.config)
    if args.bb:
        if args.bb in bbs:
            targets = {args.bb: bbs[args.bb]}
            target_profiles = {}
        elif args.bb in profiles:
            targets = {}
            target_profiles = {args.bb: profiles[args.bb]}
        else:
            print(f"ERROR: BB {args.bb!r} not in {args.config} (neither bbs nor profiles)", file=sys.stderr)
            sys.exit(2)
    else:
        targets = bbs
        target_profiles = profiles

    total_classes = 0
    total_dispatchers = 0
    for bb_name, info in targets.items():
        pkgs = set(info["packages"])
        out_dir = args.out_dir / bb_name
        out_dir.mkdir(parents=True, exist_ok=True)

        library_schema = build_schema(loader, bb_name, pkgs, package_to_bb,
                                      swe, cats, info["description"])
        classes = collect_group_classes(loader, pkgs)
        total_classes += len(classes)

        # Resolve the dispatcher's featureType list in precedence order:
        #   1. The BB entry's `dispatch:` block in bb-grouping.yaml (rich
        #      entries with wrapAsFeature / extension constraints).
        #   2. DISPATCHER_OVERRIDES_PER_BB (Python constants - simple name list).
        #   3. dispatchable_fts(loader, pkgs) - auto-discovered «FeatureType»
        #      classes from the XMI.
        # Cases 2 and 3 produce a list of bare class-name strings; we wrap
        # them as {"name": s, "ref": f"#{s}"} dicts so build_merged_schema can
        # treat all sources uniformly.
        dispatch_entries: list[dict] = []
        rich_dispatch = info.get("dispatch")
        if rich_dispatch:
            dispatch_entries = rich_dispatch
        else:
            simple_names = DISPATCHER_OVERRIDES_PER_BB.get(
                bb_name, dispatchable_fts(loader, pkgs))
            dispatch_entries = [{"name": n, "ref": f"#{n}"} for n in simple_names]

        if dispatch_entries:
            final_schema = build_merged_schema(bb_name, library_schema, dispatch_entries)
            total_dispatchers += 1
            dispatcher_note = (
                f", merged Feature+FC dispatch ({len(dispatch_entries)} branches)")
        else:
            final_schema = library_schema
            dispatcher_note = ", no FTs (library only)"

        (out_dir / f"{bb_name}Schema.json").write_text(
            json.dumps(final_schema, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (out_dir / "schema.yaml").write_text(
            yaml.safe_dump(final_schema, sort_keys=False, allow_unicode=True, width=120),
            encoding="utf-8",
        )
        (out_dir / "bblock.json").write_text(
            json.dumps(build_bblock_metadata(bb_name, info["description"], info["packages"]),
                       indent=2) + "\n",
            encoding="utf-8",
        )

        print(f"Wrote _sources/{bb_name}/{bb_name}Schema.json - "
              f"{len(classes)} classes from {len(pkgs)} package(s){dispatcher_note}")

    # Profile BBs: hand-configured FC profiles composed across multiple BBs.
    for prof_name, prof_info in target_profiles.items():
        out_dir = args.out_dir / prof_name
        out_dir.mkdir(parents=True, exist_ok=True)
        prof_schema = build_profile_schema(prof_name, prof_info)
        (out_dir / f"{prof_name}Schema.json").write_text(
            json.dumps(prof_schema, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (out_dir / "schema.yaml").write_text(
            yaml.safe_dump(prof_schema, sort_keys=False, allow_unicode=True, width=120),
            encoding="utf-8",
        )
        (out_dir / "bblock.json").write_text(
            json.dumps(build_profile_metadata(prof_name, prof_info), indent=2) + "\n",
            encoding="utf-8",
        )
        nft = len(prof_info["featureTypes"])
        print(f"Wrote _sources/{prof_name}/{prof_name}Schema.json - FC profile, {nft} featureType branches")

    print(f"\nTotal: {len(targets)} BB(s), {total_classes} class defs, "
          f"{total_dispatchers} BB(s) with dispatchers, "
          f"{len(target_profiles)} FC profile BB(s)")


if __name__ == "__main__":
    main()
