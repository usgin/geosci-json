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
    "description": "definition of a link object",
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
# alternative — these are emitted as `anyOf [SCLinkObject, <CDIF $ref> ...]`,
# letting instances provide either a link or a fully-typed metadata object.
_CDIF_BASE = (
    "https://cross-domain-interoperability-framework.github.io/"
    "metadataBuildingBlocks/build/annotated/bbr/metadata"
)
EXTERNAL_TYPE_RESOLUTION: dict[str, dict] = {
    # ISO 19115 metadata — CI_Responsibility has a CDIF agent-in-role mapping;
    # CI_Citation stays SCLinkObject only.
    "iso19115:CI_Responsibility": {
        "anyOf": [
            {"$ref": LINK_OBJECT_REF},
            {"$ref": f"{_CDIF_BASE}/schemaorgProperties/agentInRole/schema.json"},
        ],
        "$comment": "External ISO 19115 CI_Responsibility — by-reference link or inline CDIF agentInRole",
    },
    "iso19115:CI_Citation": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19115 CI_Citation — by-reference link only",
    },
    # ISO 19103 composites with CDIF mappings.
    "iso19103:ScopedName": {
        "anyOf": [
            {"$ref": LINK_OBJECT_REF},
            {"$ref": f"{_CDIF_BASE}/schemaorgProperties/definedTerm/schema.json"},
            {"$ref": f"{_CDIF_BASE}/skosProperties/skosConcept/schema.json"},
        ],
        "$comment": "External ISO 19103 ScopedName — link, CDIF definedTerm, or SKOS concept",
    },
    "iso19103:NamedValue": {
        "anyOf": [
            {"$ref": LINK_OBJECT_REF},
            {"$ref": f"{_CDIF_BASE}/schemaorgProperties/variableMeasured/schema.json"},
        ],
        "$comment": "External ISO 19103 NamedValue — link or inline CDIF variableMeasured (schema:PropertyValue)",
    },
    # ISO 19108 time, 19107 geometry composites, 19156 sampling/observation —
    # no published JSON Schemas; emit SCLinkObject so instances must provide
    # a link to an external resource.
    "iso19108:TM_Instant": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19108 TM_Instant — by-reference link",
    },
    "iso19108:TM_Period": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19108 TM_Period — by-reference link",
    },
    "iso19107:DirectPosition": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19107 DirectPosition — by-reference link",
    },
    "iso19156:GFI_Feature": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 GFI_Feature — by-reference link",
    },
    "iso19156:SF_SamplingFeature": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 SF_SamplingFeature — by-reference link",
    },
    "iso19156:SF_SamplingFeatureCollection": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 SF_SamplingFeatureCollection — by-reference link",
    },
    "iso19156:OM_Observation": {
        "$ref": LINK_OBJECT_REF,
        "$comment": "External ISO 19156 OM_Observation — by-reference link",
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
        "ISO 19156:2011 §8.6 SF_Specimen — a sampling feature representing a "
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
                            "oneOf": [
                                {"type": "null"},
                                {
                                    "type": "array",
                                    "items": {"$ref": LINK_OBJECT_REF},
                                    "minItems": 1,
                                    "uniqueItems": True,
                                },
                            ],
                            "description": (
                                "Feature(s) being sampled (1..*, by-reference "
                                "to ISO 19156 GFI_Feature). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        "relatedObservation": {
                            "oneOf": [
                                {"type": "null"},
                                {
                                    "type": "array",
                                    "items": {"$ref": LINK_OBJECT_REF},
                                    "uniqueItems": True,
                                },
                            ],
                            "description": (
                                "Observations whose featureOfInterest is this "
                                "specimen (0..*, by-reference to ISO 19156 "
                                "OM_Observation). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        "relatedSamplingFeature": {
                            "oneOf": [
                                {"type": "null"},
                                {
                                    "type": "array",
                                    "items": {"$ref": LINK_OBJECT_REF},
                                    "uniqueItems": True,
                                },
                            ],
                            "description": (
                                "Self-association: relations to other "
                                "SF_SamplingFeature instances (0..*, "
                                "by-reference). Inherited from "
                                "SF_SamplingFeature."
                            ),
                        },
                        "lineage": {
                            "oneOf": [
                                {"type": "null"},
                                {"$ref": LINK_OBJECT_REF},
                            ],
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
                                {"type": "null"},
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
                            "oneOf": [
                                {"type": "null"},
                                {"$ref": _GEOJSON_GEOMETRY_REF},
                            ],
                            "description": (
                                "Location where the specimen was sampled "
                                "(0..1, GeoJSON Geometry). Distinct from the "
                                "top-level Feature geometry, which may carry "
                                "the specimen's current footprint."
                            ),
                        },
                        "processingDetails": {
                            "oneOf": [
                                {"type": "null"},
                                {
                                    "type": "array",
                                    "items": {"$ref": "#GeologicSpecimenPreparation"},
                                    "uniqueItems": True,
                                },
                            ],
                            "description": (
                                "Processing / preparation steps applied to "
                                "the specimen (0..*). ISO 19156 types as "
                                "SpecimenProcessing; here items are the "
                                "GeoSciML GeologicSpecimenPreparation "
                                "DataType."
                            ),
                        },
                        "size": {
                            "oneOf": [
                                {"type": "null"},
                                {"$ref": _SWE_QUANTITY_REF},
                            ],
                            "description": (
                                "Specimen size as a SWE Quantity (0..1). ISO "
                                "19156 types as Measure."
                            ),
                        },
                        "currentLocation": {
                            "oneOf": [
                                {"type": "null"},
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
                            "oneOf": [
                                {"type": "null"},
                                {"$ref": _SWE_CATEGORY_REF},
                            ],
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

# Map of BB name -> additional $defs to merge into the library.
EXTRA_DEFS_PER_BB: dict[str, dict] = {
    "gsmSpecimen": {
        "SF_Specimen": SF_SPECIMEN_DEF,
    },
}

# Map of BB name -> override list of dispatchable featureTypes. When set,
# replaces the FT list auto-discovered from the XMI (dispatchable_fts()).
DISPATCHER_OVERRIDES_PER_BB: dict[str, list[str]] = {
    "gsmSpecimen": ["SF_Specimen", "ReferenceSpecimen"],
}


def _resolve_external_type(key: str) -> dict:
    """Return the schema fragment for an external ISO type identifier
    (e.g. 'iso19156:GFI_Feature'). Falls back to SCLinkObject when no
    specific mapping is configured."""
    if key in EXTERNAL_TYPE_RESOLUTION:
        # Deep-copy to avoid downstream mutation
        return json.loads(json.dumps(EXTERNAL_TYPE_RESOLUTION[key]))
    return {
        "$ref": LINK_OBJECT_REF,
        "$comment": f"External type {key} — by-reference link (no specific mapping configured)",
    }

# Names from ISO 19103 that aren't primitives (composite types) — placeholder them.
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
                owner.attributes.append(Attribute(
                    name=end["name"],
                    type_name=prop_type,
                    lower=lo,
                    upper=up,
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
        t = attr.type_name

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
# Emitter — applies OGC 24-017r1 to produce a class's JSON Schema definition.
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
        if s == "featuretype":
            return self._emit_feature_type(cls)
        if s == "union":
            return self._emit_union(cls)
        # DataType / Type / unstereotyped class
        return self._emit_object_type(cls)

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
        # Two paths:
        #   (a) «CodeList» with inline UML enumeration members (attributes with
        #       empty/missing type names): emit as a closed JSON enum per OGC
        #       24-017r1 Table 6 «enumeration» encoding. Values are the bare
        #       attribute names.
        #   (b) «CodeList» with no inline members: emit {type: string, format: uri}
        #       per req/codelists-basic. Add `codeList` annotation only when the
        #       source UML class carries a non-blank `codeList` tagged value
        #       (matches OGC team's geoscimlBasic/Lite convention).
        d: dict = OrderedDict()
        d["$anchor"] = cls.name
        desc = self._class_description(cls)
        if desc:
            d["description"] = desc

        # An attribute with an empty type_name is the EA pattern for an
        # enumeration literal. Treat the codelist as closed when *all* its
        # attributes are untyped literals.
        enum_members = [a.name for a in cls.attributes if not a.type_name]
        if cls.attributes and len(enum_members) == len(cls.attributes):
            d["type"] = "string"
            d["enum"] = enum_members
            return d

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
        else:
            d["allOf"] = [
                {"$ref": JSON_FG_FEATURE_REF},
                own_props_envelope,
                {
                    "required": ["featureType", "id"],
                    "properties": {"id": {"type": "string"}},
                },
            ]
        return d

    def _build_feature_type_own_envelope(self, cls: UmlClass) -> dict:
        """Build the {type: object, properties: { properties: { ... } } }
        envelope for a FeatureType — class-specific fields live inside the
        JSON-FG `properties` member."""
        inner_props: dict = OrderedDict()
        for a in cls.attributes:
            inner_props[a.name] = self._build_attribute_schema(cls.name, a)
        envelope: dict = OrderedDict()
        envelope["type"] = "object"
        envelope["properties"] = {
            "properties": {
                "type": "object",
                "properties": inner_props,
            }
        }
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
        """Per OGC team convention: optional values are wrapped as
        oneOf [{type: null}, <inner>]; required values use the inner schema
        directly. Array-valued attributes wrap the value type in a 'type:array'
        envelope before applying optionality."""
        rt = self.r.resolve(owning_class, a)
        desc = self._attribute_description(owning_class, a)
        optional = (a.lower == 0)

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

        if optional:
            wrapped: dict = OrderedDict()
            wrapped["oneOf"] = [{"type": "null"}, inner]
            if desc:
                wrapped["description"] = desc
            return wrapped

        out: dict = OrderedDict(inner) if isinstance(inner, dict) else dict(inner)
        if desc and "description" not in out:
            out["description"] = desc
        return out

    # ----- supertype resolution --------------------------------------------

    def _feature_supertype_ref(self, cls: UmlClass) -> Optional[dict]:
        """If cls has a supertype that's a FeatureType, $ref it instead of JSON-FG."""
        for sup_name in cls.supertypes:
            sup_id = self.loader.name_to_id.get(sup_name)
            if not sup_id:
                continue
            sup = self.loader.classes[sup_id]
            if (sup.stereotype or "").lower() != "featuretype":
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
    ft_names: list[str],
) -> dict:
    """Combine the library `$defs` and the Feature / FeatureCollection
    dispatchers into a single schema. The root discriminates on `type`:
      - `type == "FeatureCollection"`: validate as json-fg FeatureCollection
        with `features.items` dispatched by featureType via the internal
        `_FeatureDispatch` helper def.
      - otherwise: treat as a single Feature and validate via the same
        `_FeatureDispatch` helper.
    All class anchors live in `$defs` (alongside `_FeatureDispatch` and the
    local `SCLinkObject`), so the if/then branches can use local `#FT`
    anchor refs."""
    # Build the if/then dispatcher chain. Refs are local anchors (same doc).
    branches: list[dict] = []
    for ft in ft_names:
        branches.append({
            "if": {
                "required": ["featureType"],
                "properties": {"featureType": {"const": ft}},
            },
            "then": {"$ref": f"#{ft}"},
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
    """Build <bbName>FeatureSchema.json — an if/then chain on `featureType`
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
    """Build <bbName>FeatureCollectionSchema.json — composes the JSON-FG
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

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"https://schemas.usgin.org/geosci-json/{profile_name}/{profile_name}Schema.json"),
        ("description", info["description"].strip()),
        ("allOf", [
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
        ]),
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
                "title": "GeoSciML 4.1 — FC profile composed across building blocks",
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

        # For BBs with concrete FeatureType classes, merge the library and the
        # Feature / FeatureCollection dispatchers into a single schema that
        # accepts either form. Pure DataType BBs emit the library as-is.
        # DISPATCHER_OVERRIDES_PER_BB lets a BB narrow (or otherwise replace)
        # the auto-discovered dispatcher list, e.g. gsmSpecimen exposes only
        # SF_Specimen while keeping the other classes available in $defs.
        ft_names = DISPATCHER_OVERRIDES_PER_BB.get(bb_name,
                                                   dispatchable_fts(loader, pkgs))
        if ft_names:
            final_schema = build_merged_schema(bb_name, library_schema, ft_names)
            total_dispatchers += 1
            dispatcher_note = f", merged Feature+FC dispatch ({len(ft_names)} branches)"
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

        print(f"Wrote _sources/{bb_name}/{bb_name}Schema.json — "
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
        print(f"Wrote _sources/{prof_name}/{prof_name}Schema.json — FC profile, {nft} featureType branches")

    print(f"\nTotal: {len(targets)} BB(s), {total_classes} class defs, "
          f"{total_dispatchers} BB(s) with dispatchers, "
          f"{len(target_profiles)} FC profile BB(s)")


if __name__ == "__main__":
    main()
