#!/usr/bin/env python3
"""
Resolve a geosci-json BB schema into a self-contained resolvedSchema.json.

OGC 24-017r1 definitions-schemas use $defs at the root. This script does the
OGC-style resolution: copies the source schema as-is, then inlines every
cross-BB $ref pointing to a sibling BB's schema (`../<bb>/<bb>.json#<Class>`)
by pulling that class's definition into the local $defs.

External public $refs (SWE 3.0, JSON-FG, GeoJSON, CDIF property BBs) are left
untouched - they are stable URLs.

Usage:
    python tools/resolve_geosci_schema.py path/to/<bb>.json -o resolvedSchema.json
    python tools/resolve_geosci_schema.py --all       # walks every _sources/gsm*/
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path


CROSS_BB_REF = re.compile(r'^\.\./([A-Za-z][A-Za-z0-9_]*)/([A-Za-z][A-Za-z0-9_]*)\.json#(.+)$')


def collect_refs(node, found: set[tuple[str, str, str]]) -> None:
    """Walk a JSON Schema and collect every (bb_dir, file_base, class) tuple
    referenced via a `../<bb>/<file>.json#X` $ref."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                m = CROSS_BB_REF.match(v)
                if m:
                    found.add((m.group(1), m.group(2), m.group(3)))
            else:
                collect_refs(v, found)
    elif isinstance(node, list):
        for item in node:
            collect_refs(item, found)


def rewrite_refs(node, mapping: dict[tuple[str, str, str], str]) -> None:
    """Rewrite cross-BB $refs in-place: `../<bb>/<file>.json#Cls` → `#<local>`."""
    if isinstance(node, dict):
        ref_v = node.get("$ref")
        if isinstance(ref_v, str):
            m = CROSS_BB_REF.match(ref_v)
            if m:
                new_target = mapping.get((m.group(1), m.group(2), m.group(3)))
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

    seen: set[tuple[str, str, str]] = set()
    pending: set[tuple[str, str, str]] = set()
    collect_refs(resolved, pending)

    while pending:
        ref = pending.pop()
        if ref in seen:
            continue
        seen.add(ref)
        bb_dir, file_base, cls = ref
        ext_path = repo_sources / bb_dir / f"{file_base}.json"
        if not ext_path.exists():
            continue
        ext_schema = json.loads(ext_path.read_text(encoding="utf-8"))
        ext_def = ext_schema.get("$defs", {}).get(cls)
        if not ext_def:
            continue
        # Prefix to avoid local collisions
        local_key = cls if cls not in resolved.get("$defs", {}) else f"{bb_dir}_{cls}"
        resolved.setdefault("$defs", {})[local_key] = copy.deepcopy(ext_def)
        more: set[tuple[str, str, str]] = set()
        collect_refs(ext_def, more)
        for r in more:
            if r not in seen:
                pending.add(r)

    # Build mapping (bb, file, cls) -> local def key, then rewrite refs.
    mapping: dict[tuple[str, str, str], str] = {}
    for bb_dir, file_base, cls in seen:
        if cls in resolved.get("$defs", {}):
            # Check it's actually the ref we resolved (not a same-name local def
            # we accidentally aliased): the prefixed key wins when there was
            # a collision.
            prefixed = f"{bb_dir}_{cls}"
            mapping[(bb_dir, file_base, cls)] = prefixed if prefixed in resolved["$defs"] else cls
    rewrite_refs(resolved, mapping)

    return resolved


def _find_library_schema(bb_dir: Path) -> Path | None:
    """Locate the BB's library schema: <bb_dir.name>Schema.json (skip
    *FeatureSchema.json / *FeatureCollectionSchema.json dispatchers)."""
    candidate = bb_dir / f"{bb_dir.name}Schema.json"
    return candidate if candidate.exists() else None


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("schema", nargs="?", type=Path, help="Path to a BB <bb>.json")
    p.add_argument("-o", "--output", type=Path,
                   help="Output path (default: <schema_dir>/resolvedSchema.json)")
    p.add_argument("--all", action="store_true",
                   help="Resolve every BB under _sources/gsm*/")
    args = p.parse_args()

    if args.all:
        for bb_dir in sorted(Path("_sources").glob("gsm*")):
            if not bb_dir.is_dir():
                continue
            sp = _find_library_schema(bb_dir)
            if not sp:
                continue
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
