#!/usr/bin/env python3
"""
Resolve a geosci-json BB schema into a self-contained resolvedSchema.json.

OGC 24-017r1 definitions-schemas use $defs at the root. The CDIF
tools/resolve_schema.py expects a root schema with anyOf/properties and
doesn't preserve $defs. This script does the OGC-style resolution: copies
the source schema as-is, then inlines every cross-BB $ref pointing to a
sibling BB's schema (`../geosciml_<X>/schema.json#<Class>`) by pulling that
class's definition into the local $defs.

External public $refs (SWE 3.0, JSON-FG, GeoJSON, OGC LinkObject) are left
untouched — they are stable URLs.

ISO placeholder $refs (`iso19xxx:TypeName`) are left untouched — they have
no real schema to inline.

Usage:
    python tools/resolve_geosci_schema.py path/to/schema.json -o resolvedSchema.json
    python tools/resolve_geosci_schema.py --all       # walks every _sources/geosciml_*/
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path


CROSS_BB_REF = re.compile(r'^\.\./(geosciml_[^/]+)/schema\.json#(.+)$')


def collect_refs(node, found: set[tuple[str, str]]) -> None:
    """Walk a JSON Schema and collect every (bb, class) tuple referenced via
    a `../geosciml_*/schema.json#X` $ref."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                m = CROSS_BB_REF.match(v)
                if m:
                    found.add((m.group(1), m.group(2)))
            else:
                collect_refs(v, found)
    elif isinstance(node, list):
        for item in node:
            collect_refs(item, found)


def rewrite_refs(node, mapping: dict[tuple[str, str], str]) -> None:
    """Rewrite cross-BB $refs in-place: `../geosciml_X/schema.json#Cls` → `#Cls`."""
    if isinstance(node, dict):
        ref_v = node.get("$ref")
        if isinstance(ref_v, str):
            m = CROSS_BB_REF.match(ref_v)
            if m:
                new_target = mapping.get((m.group(1), m.group(2)))
                if new_target:
                    node["$ref"] = f"#{new_target}"
                    c = node.get("$comment", "")
                    if "cross-BB" in c:
                        node.pop("$comment", None)
        for v in list(node.values()):
            rewrite_refs(v, mapping)
    elif isinstance(node, list):
        for item in node:
            rewrite_refs(item, mapping)


def resolve_one(schema_path: Path) -> dict:
    src = json.loads(schema_path.read_text(encoding="utf-8"))
    resolved = copy.deepcopy(src)
    repo_sources = schema_path.parent.parent

    # BFS: keep collecting until no new refs appear
    seen: set[tuple[str, str]] = set()
    pending: set[tuple[str, str]] = set()
    collect_refs(resolved, pending)
    pending -= seen

    while pending:
        bb, cls = pending.pop()
        seen.add((bb, cls))
        ext_path = repo_sources / bb / "schema.json"
        if not ext_path.exists():
            continue
        ext_schema = json.loads(ext_path.read_text(encoding="utf-8"))
        ext_def = ext_schema.get("$defs", {}).get(cls)
        if not ext_def:
            continue
        # Prefix to avoid local collisions
        local_key = cls if cls not in resolved.get("$defs", {}) else f"{bb}_{cls}"
        resolved.setdefault("$defs", {})[local_key] = copy.deepcopy(ext_def)
        # Walk newly added subtree for further cross-BB refs
        more: set[tuple[str, str]] = set()
        collect_refs(ext_def, more)
        for ref in more:
            if ref not in seen:
                pending.add(ref)

    # Build mapping (bb, cls) -> local def key, then rewrite refs
    mapping: dict[tuple[str, str], str] = {}
    for bb, cls in seen:
        local_key = cls if cls in resolved.get("$defs", {}) else None
        if local_key is None:
            # Search for the prefixed alias
            for k in resolved.get("$defs", {}):
                if k == f"{bb}_{cls}":
                    local_key = k
                    break
        if local_key:
            mapping[(bb, cls)] = local_key
    rewrite_refs(resolved, mapping)

    return resolved


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("schema", nargs="?", type=Path, help="Path to a BB schema.json")
    p.add_argument("-o", "--output", type=Path,
                   help="Output path (default: <schema_dir>/resolvedSchema.json)")
    p.add_argument("--all", action="store_true",
                   help="Resolve every BB under _sources/geosciml_*/")
    args = p.parse_args()

    if args.all:
        roots = sorted(Path("_sources").glob("geosciml_*/schema.json"))
        for sp in roots:
            out = sp.parent / "resolvedSchema.json"
            resolved = resolve_one(sp)
            out.write_text(json.dumps(resolved, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
            print(f"wrote {out}")
        return

    if not args.schema:
        p.error("provide a schema path or --all")
    out = args.output or args.schema.parent / "resolvedSchema.json"
    resolved = resolve_one(args.schema)
    out.write_text(json.dumps(resolved, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
