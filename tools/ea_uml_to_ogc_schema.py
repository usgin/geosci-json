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
        target_package: str,
        swe_mappings: dict,
        category_codelists: dict,
    ):
        self.loader = loader
        self.target_package = target_package
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

        # 5. ISO 19103 composite (ScopedName, etc.) - placeholder
        if t in ISO_19103_COMPOSITES:
            ns = ISO_19103_COMPOSITES[t]
            return ResolvedType(
                "external_iso",
                {"$ref": f"{ns}:{t}", "$comment": "External type — needs concrete schema URL"},
            )

        # 6. ISO prefix-based imports (CI_*, TM_*, SC_*, ...)
        for pat, ns in ISO_PREFIX_MAP:
            if pat.match(t):
                return ResolvedType(
                    "external_iso",
                    {"$ref": f"{ns}:{t}", "$comment": "External type — needs concrete schema URL"},
                )

        # 7. A class defined somewhere in the XMI: local or cross-BB.
        #    Apply UML tag inlineOrByReference for non-CodeList class types.
        #    CodeList types always use the URI codelist encoding (overrides tag).
        if t in self.loader.name_to_id:
            cls = self.loader.classes[self.loader.name_to_id[t]]
            same_pkg = bool(cls.package_path and cls.package_path[-1] == self.target_package)
            target_stereo = (cls.stereotype or "").lower()

            # CodeList target: $ref to the local codelist class definition.
            # No codeList annotation per OGC team's convention.
            if target_stereo == "codelist":
                ref = {"$ref": f"#{t}"} if same_pkg else {
                    "$ref": f"../geosciml_{cls.package_path[-1]}/schema.json#{t}",
                    "$comment": f"cross-BB reference to {t}",
                }
                return ResolvedType("category", ref, target_class_name=t)

            inline_ref = {"$ref": f"#{t}"} if same_pkg else {
                "$ref": f"../geosciml_{cls.package_path[-1]}/schema.json#{t}",
                "$comment": f"cross-BB inline reference to {t}",
            }
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
                    "local" if same_pkg else "cross_bb",
                    inline_ref, target_class_name=t,
                )

            iob = (attr.inline_or_byref or "").strip()
            if iob == "inline":
                return ResolvedType(
                    "local" if same_pkg else "cross_bb",
                    inline_ref, target_class_name=t,
                )
            if iob == "byReference":
                return ResolvedType("cross_bb", link_obj, target_class_name=t)
            # default (and explicit inlineOrByReference) -> oneOf [SCLinkObject, $ref Class]
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
        # OGC 24-017r1 req/codelists-basic/codelist-tag: emit the `codeList`
        # annotation ONLY when the source UML's «CodeList» class carries a
        # non-blank `codeList` tagged value. Otherwise produce a plain
        # {type: string, format: uri} (matches OGC team's geoscimlBasic/Lite
        # default — they ship without the annotation).
        d: dict = OrderedDict()
        d["$anchor"] = cls.name
        desc = self._class_description(cls)
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
        same_pkg = sup.package_path and sup.package_path[-1] == self.r.target_package
        if same_pkg:
            return {"$ref": f"#{sup.name}"}
        # Cross-BB: $ref by path; the user will resolve the eventual filename.
        pkg = sup.package_path[-1] if sup.package_path else "unknown"
        return {
            "$ref": f"../geosciml_{pkg}/schema.json#{sup.name}",
            "$comment": f"cross-BB reference to {sup.name} in package {pkg}",
        }



# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def collect_package_classes(loader: EaXmiLoader, package_name: str) -> list[UmlClass]:
    out: list[UmlClass] = []
    for cls in loader.classes.values():
        if cls.package_path and cls.package_path[-1] == package_name:
            out.append(cls)
    out.sort(key=lambda c: c.name)
    return out


def build_schema(
    loader: EaXmiLoader,
    package_name: str,
    swe_mappings: dict,
    category_codelists: dict,
    bb_id: str,
) -> dict:
    resolver = Resolver(loader, package_name, swe_mappings, category_codelists)
    emitter = Emitter(resolver, loader)
    classes = collect_package_classes(loader, package_name)
    defs: dict = OrderedDict()
    for cls in classes:
        defs[cls.name] = emitter.emit_class(cls)
    # Add the local SCLinkObject definition so each BB is self-contained for
    # by-reference encoding. Matches OGC team's geoscimlBasic/Lite convention.
    defs["SCLinkObject"] = SCLINK_OBJECT_DEF
    schema: dict = OrderedDict()
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["$id"] = f"https://schemas.usgin.org/geosci-json/{bb_id}/schema.json"
    schema["description"] = f"GeoSciML {package_name} building block (generated)."
    schema["$defs"] = defs
    return schema


def build_bblock_metadata(bb_id: str, package_name: str) -> dict:
    return OrderedDict({
        "itemIdentifier": f"usgin.bbr.geosci.{bb_id}",
        "name": package_name,
        "abstract": f"GeoSciML 4.1 {package_name} encoded as JSON Schema per OGC 24-017r1.",
        "status": "under-development",
        "dateTimeAddition": "2026-05-11",
        "sources": [{"title": "GeoSciML 4.1 XMI"}],
        "schema": "schema.json",
    })


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1] if __doc__ else "")
    p.add_argument("--xmi", required=True, type=Path)
    p.add_argument("--package", required=True)
    p.add_argument("--bb-name", default=None)
    p.add_argument("--out-dir", type=Path, default=Path("_sources"))
    p.add_argument("--swe-mappings", type=Path, default=Path("swe-mappings.yaml"))
    p.add_argument("--category-codelists", type=Path,
                   default=Path("cgi-vocab-reference.yaml"))
    args = p.parse_args()

    bb_name = args.bb_name or f"geosciml_{args.package}"
    out_dir = args.out_dir / bb_name
    out_dir.mkdir(parents=True, exist_ok=True)

    loader = EaXmiLoader(args.xmi)
    swe = yaml.safe_load(args.swe_mappings.read_text(encoding="utf-8"))
    cats = yaml.safe_load(args.category_codelists.read_text(encoding="utf-8"))

    schema = build_schema(loader, args.package, swe, cats, bb_name)
    (out_dir / "schema.json").write_text(
        json.dumps(schema, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (out_dir / "bblock.json").write_text(
        json.dumps(build_bblock_metadata(bb_name, args.package), indent=2) + "\n",
        encoding="utf-8",
    )
    # Tiny report
    classes = collect_package_classes(loader, args.package)
    print(f"Wrote {out_dir / 'schema.json'}")
    print(f"  classes ({len(classes)}):")
    for c in classes:
        print(f"    - {c.name:35s} stereotype={c.stereotype:12s} abstract={c.abstract} supertypes={c.supertypes}")


if __name__ == "__main__":
    main()
