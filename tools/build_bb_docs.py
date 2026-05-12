#!/usr/bin/env python3
"""
Generate description.md and a minimal example per BB from its <bb>.json.

For each `_sources/gsm*/` directory:
  - Write `description.md` summarising classes, properties, encoding, deps.
  - Write `examples/example<Bb>Minimal.json` — a bare valid instance
    (only when one does not already exist).

Does NOT touch existing examples/*.json files.

Run from repo root:
    python tools/build_bb_docs.py            # all BBs
    python tools/build_bb_docs.py gsmBorehole   # one BB
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
    for d in sorted(SCHEMA_DIR.glob("gsm*")):
        if not d.is_dir():
            continue
        if filter_name and d.name != filter_name:
            continue
        if (d / f"{d.name}Schema.json").exists():
            out.append(d)
    return out


def _list_example_files(bb_dir: Path) -> list[Path]:
    """Examples sit in the bblocks-template-style `examples/` subdir. Any
    *.json there is treated as an example instance."""
    ex_dir = bb_dir / "examples"
    if not ex_dir.exists():
        return []
    return sorted(ex_dir.glob("*.json"))


def write_examples_yaml(bb_dir: Path) -> int:
    """Write the OGC bblocks-template-style examples.yaml manifest listing
    every example file at the BB root. Returns the count of examples.

    Format follows bblocks-template's `prefixes:` + `examples:` wrapper
    (https://github.com/opengeospatial/bblocks-template/blob/master/_sources/myFeature/examples.yaml).
    Example file `ref` values are relative paths from the BB directory; we
    keep CDIF's flattened-to-BB-root convention so refs are bare filenames."""
    examples = _list_example_files(bb_dir)
    if not examples:
        return 0
    lines: list[str] = []
    lines.append("# Examples manifest for this building block.")
    lines.append("# Each entry lists a title, descriptive content (Markdown),")
    lines.append("# and one or more snippets pointing to example files.")
    lines.append("")
    lines.append("examples:")
    for ex in examples:
        try:
            doc = json.loads(ex.read_text(encoding="utf-8-sig"))
            comment = doc.get("$comment") if isinstance(doc, dict) else None
        except Exception:
            comment = None
        title = ex.stem.replace("_", " ").replace("-", " ")
        content = (comment.strip().splitlines()[0] if comment else
                   f"Example instance: {ex.stem}")
        content_escaped = content.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f"  - title: {title}")
        lines.append(f"    content: \"{content_escaped}\"")
        lines.append(f"    snippets:")
        lines.append(f"      - language: json")
        lines.append(f"        ref: examples/{ex.name}")
    (bb_dir / "examples.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(examples)


def write_stub_artifacts(bb_dir: Path, bb_name: str) -> list[str]:
    """Write template-aligned stubs for context.jsonld, rules.shacl, tests.yaml.
    Only writes if the file doesn't already exist (don't clobber hand edits)."""
    written: list[str] = []

    ctx_path = bb_dir / "context.jsonld"
    if not ctx_path.exists():
        ctx_path.write_text(
            json.dumps({"@context": {"@version": 1.1}}, indent=2) + "\n",
            encoding="utf-8",
        )
        written.append("context.jsonld")

    shacl_path = bb_dir / "rules.shacl"
    if not shacl_path.exists():
        shacl_path.write_text(
            f"# SHACL rules for {bb_name}.\n"
            f"# Placeholder — populate with shape constraints as the model is profiled.\n"
            f"\n"
            f"@prefix sh: <http://www.w3.org/ns/shacl#> .\n",
            encoding="utf-8",
        )
        written.append("rules.shacl")

    tests_yaml = bb_dir / "tests.yaml"
    if not tests_yaml.exists():
        # bblocks-postprocess expects a list at the root (CDIF convention).
        # Negative tests can be added later; empty list means none.
        tests_yaml.write_text("[]\n", encoding="utf-8")
        written.append("tests.yaml")

    return written


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


def render_description(bb_name: str, schema: dict, packages: list[str] | None = None) -> str:
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
        # Profile BB or empty umbrella — fall back to schema description
        return f"""# {bb_name}

{schema.get("description", "GeoSciML 4.1 building block.")}
"""

    out: list[str] = []
    out.append(f"# {bb_name}")
    out.append("")
    out.append(f"GeoSciML 4.1 building block `{bb_name}`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).")
    out.append("")
    if packages:
        out.append(f"Source UML packages: {', '.join('`' + p + '`' for p in packages)}.")
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

    # Examples (CDIF style: example files sit at BB root; examples.yaml lists them)
    out.append("## Examples")
    out.append("")
    bb_dir = Path(f"_sources/{bb_name}")
    example_files = _list_example_files(bb_dir)
    if example_files:
        for f in example_files:
            out.append(f"- [{f.name}](examples/{f.name})")
        out.append("")
        out.append("See [examples.yaml](examples.yaml) for the full manifest.")
    else:
        out.append("_No examples yet._")
    out.append("")
    out.append("## Source")
    out.append("")
    pkgs_str = ", ".join('`' + p + '`' for p in packages) if packages else "(see bb-grouping.yaml)"
    out.append(f"- UML: `geosciml4.1.xmi`, package(s) {pkgs_str}.")
    out.append(f"- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).")
    out.append(f"- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).")
    out.append("")

    return "\n".join(out)


def render_minimal_example(bb_name: str, schema: dict) -> dict | None:
    """Pick the most-derived FeatureType (or first concrete class) and emit a
    bare valid instance."""
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
        body = defs[codelist]
        cl = body.get("codeList", "")
        return OrderedDict([
            ("$comment", f"Minimal example of a {codelist} code value"),
            ("value", cl + "/example-term" if cl else f"http://example.org/{bb_name}/example-term"),
        ])
    return None


# ---------------------------------------------------------------------------

def load_bb_packages() -> dict[str, list[str]]:
    """Return {bb_name: [package_names]} from bb-grouping.yaml, for description
    headers and source attribution."""
    try:
        import yaml
    except ImportError:
        return {}
    p = Path("bb-grouping.yaml")
    if not p.exists():
        return {}
    raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    out: dict[str, list[str]] = {}
    for bb, info in (raw.get("bbs", {}) or {}).items():
        if isinstance(info, dict) and "packages" in info:
            out[bb] = list(info["packages"])
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("bb", nargs="?", help="Single BB directory name (e.g. gsmBorehole)")
    ap.add_argument("--xmi", type=Path, default=DEFAULT_XMI,
                    help="EA XMI source (used to read stereotype info)")
    args = ap.parse_args()

    load_stereotypes(args.xmi)
    bb_pkgs = load_bb_packages()

    bbs = discover_bbs(args.bb)
    for d in bbs:
        bb_name = d.name
        schema = json.loads((d / f"{bb_name}Schema.json").read_text(encoding="utf-8"))
        packages = bb_pkgs.get(bb_name)

        desc_md = render_description(bb_name, schema, packages)
        (d / "description.md").write_text(desc_md, encoding="utf-8")

        # Auto-write a minimal example at the BB root only if no example files
        # already exist (don't clobber curated/copied ones).
        existing = _list_example_files(d)
        wrote_example = False
        if not existing:
            min_ex = render_minimal_example(bb_name, schema)
            if min_ex is not None:
                ex_dir = d / "examples"
                ex_dir.mkdir(exist_ok=True)
                out_path = ex_dir / f"example{bb_name}Minimal.json"
                out_path.write_text(json.dumps(min_ex, indent=2) + "\n", encoding="utf-8")
                wrote_example = True

        # Emit the bblocks-template-style examples.yaml manifest after any
        # auto-writes, plus stub artifacts that match the template + CDIF layout.
        n_examples = write_examples_yaml(d)
        stubs = write_stub_artifacts(d, bb_name)

        stub_note = (f", stubs={'+'.join(stubs)}" if stubs else "")
        print(f"  {bb_name}: description.md ({len(desc_md)} chars), "
              f"minimal example {'written' if wrote_example else 'skipped'}, "
              f"examples.yaml lists {n_examples}{stub_note}")


if __name__ == "__main__":
    main()
