#!/usr/bin/env python3
"""
Generate description.md and a minimal example per BB from its schema.json.

For each `_sources/geosciml_<Package>/` directory:
  - Write `description.md` summarising classes, properties, encoding, deps.
  - Write `examples/example<Bb>Minimal.json` — a bare valid instance.

Does NOT touch existing examples/example*Complete.json files.

Run from repo root:
    python tools/build_bb_docs.py            # all BBs
    python tools/build_bb_docs.py geosciml_Borehole  # one BB
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from collections import OrderedDict

# Pull the XMI loader from the sibling generator so we can read stereotype
# info authoritatively (the emitted schemas no longer carry x-stereotype).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ea_uml_to_ogc_schema import EaXmiLoader  # type: ignore[import-not-found]


SCHEMA_DIR = Path("_sources")
DEFAULT_XMI = Path("geosciml4.1.xmi")

# Lazy-loaded class → stereotype map keyed by XMI class name.
_STEREO_BY_CLASS: dict[str, str] = {}

def load_stereotypes(xmi_path: Path) -> None:
    global _STEREO_BY_CLASS
    if _STEREO_BY_CLASS or not xmi_path.exists():
        return
    loader = EaXmiLoader(xmi_path)
    for cls in loader.classes.values():
        _STEREO_BY_CLASS[cls.name] = cls.stereotype or ""


# ---------------------------------------------------------------------------

def discover_bbs(filter_name: str | None) -> list[Path]:
    out: list[Path] = []
    for d in sorted(SCHEMA_DIR.glob("geosciml_*")):
        if filter_name and d.name != filter_name:
            continue
        if (d / "schema.json").exists():
            out.append(d)
    return out


def classify_class(name: str, defs: dict) -> str:
    """Return one of: featuretype | datatype | codelist | union | unknown.
    Looks up the stereotype from the XMI (loaded once); falls back to
    structural heuristics for classes not in the XMI (e.g., SCLinkObject)."""
    stereo = _STEREO_BY_CLASS.get(name, "").lower()
    if stereo == "featuretype":
        return "featuretype"
    if stereo in ("datatype", "type"):
        return "datatype"
    if stereo == "codelist":
        return "codelist"
    if stereo == "union":
        return "union"
    # Fallback heuristics for classes that have no XMI entry
    body = defs.get(name, {})
    if body.get("type") == "string" and body.get("format") == "uri":
        return "codelist"
    if "oneOf" in body:
        return "union"
    if "allOf" in body:
        first = body["allOf"][0]
        ref = first.get("$ref", "") if isinstance(first, dict) else ""
        if "json-fg" in ref or "Feature.json" in ref:
            return "featuretype"
        return "datatype"
    if body.get("type") == "object":
        return "datatype"
    return "unknown"


def get_description(body: dict) -> str:
    d = body.get("description")
    if d:
        return d
    # Drill into allOf[1].properties or first allOf element
    if "allOf" in body:
        for sub in body["allOf"]:
            if isinstance(sub, dict) and "description" in sub:
                return sub["description"]
    return ""


def get_own_properties(body: dict) -> dict:
    """Return the own-structure properties dict (after allOf parent peel).
    For FeatureType classes the properties live one level deeper, under
    `properties.properties` (the JSON-FG envelope)."""
    # FeatureType: allOf [parent_ref, {type:object, properties:{properties:{...own...}}}]
    if "allOf" in body:
        for sub in body["allOf"]:
            if not isinstance(sub, dict):
                continue
            envelope = sub.get("properties", {}).get("properties")
            if isinstance(envelope, dict) and "properties" in envelope:
                return envelope["properties"]
        # DataType subtype: allOf [parent_ref, {type:object, properties:{...own...}}]
        for sub in reversed(body["allOf"]):
            if isinstance(sub, dict) and "properties" in sub and "properties" not in sub["properties"]:
                return sub["properties"]
    if "properties" in body:
        # plain DataType
        if "properties" in body["properties"]:
            # could be FeatureType structure at top level (rare)
            return body["properties"]["properties"].get("properties", body["properties"])
        return body["properties"]
    return {}


def get_required(body: dict) -> list[str]:
    if "required" in body:
        return body["required"]
    if "allOf" in body:
        for sub in reversed(body["allOf"]):
            if isinstance(sub, dict) and "required" in sub:
                return sub["required"]
    return []


def parent_ref(body: dict) -> str:
    """Find a parent class $ref (local or cross-BB) from allOf[0]."""
    if "allOf" not in body:
        return ""
    first = body["allOf"][0]
    if isinstance(first, dict):
        return first.get("$ref", "")
    return ""


def collect_external_refs(schema: dict) -> set[str]:
    out: set[str] = set()
    def walk(node):
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and ref.startswith(("http://", "https://", "../")):
                out.add(ref)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(schema)
    return out


# ---------------------------------------------------------------------------

def property_row(name: str, schema: dict, required: list[str]) -> str:
    """Render one property as a table row."""
    is_array = schema.get("type") == "array"
    items = schema.get("items", {}) if is_array else schema
    # Multiplicity hint
    lo = "1" if name in required else "0"
    if is_array:
        upper = schema.get("maxItems", "*")
        mult = f"{schema.get('minItems', lo)}..{upper}"
    else:
        mult = f"{lo}..1"
    # Type summary
    if "$ref" in items:
        ref = items["$ref"]
        if ref.startswith("#"):
            type_str = f"`{ref[1:]}`"
        elif "sweCommon" in ref:
            sname = ref.rsplit("/", 1)[-1].replace(".json", "")
            type_str = f"SWE 3.0 `{sname}`"
        elif "json-fg" in ref:
            type_str = "JSON-FG Feature"
        elif "geojson.org" in ref:
            type_str = f"GeoJSON `{ref.rsplit('/', 1)[-1].replace('.json','')}`"
        elif "LinkObject" in ref:
            type_str = "OGC LinkObject"
        elif ref.startswith("iso19"):
            type_str = f"`{ref}` (external)"
        else:
            type_str = f"`{ref}`"
    elif "oneOf" in items:
        type_str = "(oneOf — see schema)"
    elif items.get("codeList"):
        type_str = f"URI codelist · `{items['codeList']}`"
    elif items.get("type") == "string" and items.get("format"):
        type_str = f"`string({items['format']})`"
    elif items.get("type"):
        type_str = f"`{items['type']}`"
    else:
        type_str = "—"
    desc = schema.get("description", "")
    # Strip embedded Constraint: text from description for table compactness
    desc = re.sub(r"\s*Constraint:.*$", "", desc).strip()
    if len(desc) > 120:
        desc = desc[:117] + "…"
    return f"| `{name}` | {type_str} | {mult} | {desc} |"


def render_description(bb_name: str, schema: dict) -> str:
    pkg = bb_name.replace("geosciml_", "")
    defs = schema.get("$defs", {})
    # Hide the local SCLinkObject helper from docs — it's not a UML class.
    class_names = sorted(c for c in defs.keys() if c != "SCLinkObject")

    # Classify each class
    classifications = {c: classify_class(c, defs) for c in class_names}
    n_feat = sum(1 for v in classifications.values() if v == "featuretype")
    n_data = sum(1 for v in classifications.values() if v == "datatype")
    n_cl = sum(1 for v in classifications.values() if v == "codelist")
    n_u = sum(1 for v in classifications.values() if v == "union")

    if not class_names:
        # Umbrella package with no own classes
        return f"""# GeoSciML {pkg}

Empty umbrella package — no classes are defined here. Other Leaf BBs nested under this Application Schema in the source UML carry the substantive content.

This BB exists so the OGC bblocks register has a placeholder entry for the application schema name; downstream consumers reference the sibling Leaf BBs directly.
"""

    out: list[str] = []
    out.append(f"# GeoSciML {pkg}")
    out.append("")
    out.append(f"JSON Schema building block for the `{pkg}` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).")
    out.append("")
    summary_bits = []
    if n_feat: summary_bits.append(f"{n_feat} feature type{'s' if n_feat != 1 else ''}")
    if n_data: summary_bits.append(f"{n_data} data type{'s' if n_data != 1 else ''}")
    if n_cl: summary_bits.append(f"{n_cl} code list{'s' if n_cl != 1 else ''}")
    if n_u: summary_bits.append(f"{n_u} union{'s' if n_u != 1 else ''}")
    if summary_bits:
        out.append(f"Contains {', '.join(summary_bits)}.")
        out.append("")

    # Classes table
    out.append("## Classes in this BB")
    out.append("")
    out.append("| Class | Stereotype | Encoding |")
    out.append("| --- | --- | --- |")
    enc_map = {
        "featuretype": "JSON-FG Feature",
        "datatype":    "plain JSON object",
        "codelist":    "URI codelist (`format: uri`)",
        "union":       "type discriminator (`oneOf`)",
        "abstract":    "plain JSON object (abstract)",
        "unknown":     "(unclassified)",
    }
    stereo_map = {
        "featuretype": "«FeatureType»",
        "datatype":    "«DataType»",
        "codelist":    "«CodeList»",
        "union":       "«Union»",
        "abstract":    "«DataType» (abstract)",
        "unknown":     "—",
    }
    for c in class_names:
        kind = classifications[c]
        out.append(f"| `{c}` | {stereo_map[kind]} | {enc_map[kind]} |")
    out.append("")

    # Per-class detail (only for FeatureType and DataType — skip CodeList table since they are atomic)
    detail_classes = [c for c in class_names if classifications[c] in ("featuretype", "datatype")]
    if detail_classes:
        out.append("## Class details")
        out.append("")
        for c in detail_classes:
            body = defs[c]
            desc = get_description(body)
            out.append(f"### `{c}`")
            out.append("")
            if desc:
                out.append(desc)
                out.append("")
            parent = parent_ref(body)
            if parent and "json-fg" not in parent:
                if parent.startswith("#"):
                    out.append(f"**Supertype**: [`{parent[1:]}`](#{parent[1:]}) (this BB).")
                else:
                    target = parent.rsplit("#", 1)[-1] if "#" in parent else parent
                    out.append(f"**Supertype**: `{target}` (cross-BB).")
                out.append("")
            props = get_own_properties(body)
            required = get_required(body)
            if props:
                out.append("Properties (own; inherited properties listed in supertype's BB):")
                out.append("")
                out.append("| Name | Type | Mult | Notes |")
                out.append("| --- | --- | --- | --- |")
                for pname, pschema in props.items():
                    out.append(property_row(pname, pschema, required))
                out.append("")

    # CodeLists list (short)
    cls_codelists = [c for c in class_names if classifications[c] == "codelist"]
    if cls_codelists:
        out.append("## Code lists")
        out.append("")
        out.append("| Class | `codeList` vocab |")
        out.append("| --- | --- |")
        for c in cls_codelists:
            body = defs[c]
            cl = body.get("codeList", "_(treat as open — no `codeList` annotation)_")
            out.append(f"| `{c}` | `{cl}` |")
        out.append("")

    # Union list
    cls_unions = [c for c in class_names if classifications[c] == "union"]
    if cls_unions:
        out.append("## Unions")
        out.append("")
        for c in cls_unions:
            body = defs[c]
            out.append(f"### `{c}`")
            out.append("")
            if get_description(body):
                out.append(get_description(body))
                out.append("")
            out.append("Branches (`oneOf`):")
            for i, branch in enumerate(body.get("oneOf", [])):
                if isinstance(branch, dict):
                    ref = branch.get("$ref", "")
                    if ref:
                        target = ref.rsplit("/", 1)[-1].replace(".json", "") if "://" in ref else ref.lstrip("#")
                        comment = branch.get("$comment", "")
                        suffix = f" — {comment}" if comment else ""
                        out.append(f"- `{target}`{suffix}")
                    else:
                        out.append(f"- (branch {i})")
            out.append("")

    # Dependencies
    refs = collect_external_refs(schema)
    if refs:
        out.append("## External dependencies")
        out.append("")
        for r in sorted(refs):
            label = r
            if r.startswith("../"):
                label = "cross-BB · " + r
            out.append(f"- `{r}`")
        out.append("")

    # Examples and source
    out.append("## Examples")
    out.append("")
    out.append(f"- [Minimal](examples/example{pkg}Minimal.json) — bare valid instance.")
    complete_path = Path(f"_sources/{bb_name}/examples/example{pkg}Complete.json")
    if complete_path.exists():
        out.append(f"- [Complete](examples/example{pkg}Complete.json) — fully-populated example.")
    out.append("")
    out.append("## Source")
    out.append("")
    out.append(f"- UML: `geosciml4.1.xmi`, package `{pkg}`.")
    out.append(f"- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).")
    out.append(f"- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).")
    out.append("")

    return "\n".join(out)


def render_minimal_example(bb_name: str, schema: dict) -> dict | None:
    """Pick the most-derived FeatureType (or first concrete class) and emit a
    bare valid instance."""
    pkg = bb_name.replace("geosciml_", "")
    defs = schema.get("$defs", {})
    if not defs:
        return None

    # Prefer a FeatureType class
    featuretype = None
    datatype = None
    codelist = None
    for c, body in defs.items():
        kind = classify_class(c, defs)
        if kind == "featuretype" and not featuretype:
            featuretype = c
        elif kind == "datatype" and not datatype:
            datatype = c
        elif kind == "codelist" and not codelist:
            codelist = c

    if featuretype:
        return OrderedDict([
            ("type", "Feature"),
            ("id", f"{featuretype.lower()}.minimal.1"),
            ("featureType", featuretype),
            ("geometry", None),
            ("properties", OrderedDict()),
        ])
    if datatype:
        return OrderedDict([("$comment", f"Minimal {datatype} instance — no required properties")])
    if codelist:
        # The minimal example for a codelist-only BB is just a URI value
        body = defs[codelist]
        cl = body.get("codeList", "")
        return OrderedDict([
            ("$comment", f"Minimal example of a {codelist} code value"),
            ("value", cl + "/example-term" if cl else f"http://example.org/{pkg}/example-term"),
        ])
    return None


# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("bb", nargs="?", help="Single BB directory name (e.g. geosciml_Borehole)")
    ap.add_argument("--xmi", type=Path, default=DEFAULT_XMI,
                    help="EA XMI source (used to read stereotype info)")
    args = ap.parse_args()

    load_stereotypes(args.xmi)

    bbs = discover_bbs(args.bb)
    for d in bbs:
        bb_name = d.name
        pkg = bb_name.replace("geosciml_", "")
        schema = json.loads((d / "schema.json").read_text(encoding="utf-8"))

        desc_md = render_description(bb_name, schema)
        (d / "description.md").write_text(desc_md, encoding="utf-8")

        min_ex = render_minimal_example(bb_name, schema)
        if min_ex is not None:
            ex_dir = d / "examples"
            ex_dir.mkdir(exist_ok=True)
            out = ex_dir / f"example{pkg}Minimal.json"
            out.write_text(json.dumps(min_ex, indent=2) + "\n", encoding="utf-8")

        print(f"  {bb_name}: description.md ({len(desc_md)} chars), minimal example {'written' if min_ex else 'skipped (empty BB)'}")


if __name__ == "__main__":
    main()
