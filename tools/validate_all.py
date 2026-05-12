#!/usr/bin/env python3
"""
Batch-validate every example file under _sources/<bb>/examples/ against the
appropriate schema for its BB.

Schema choice per file:
  - profile BBs (gsmBasicGeologyCollection, gsmExtendedGeologyCollection,
    gsmEarthMaterialCollection): validate against <bb>.json at the BB root.
  - BBs with dispatchers: pick <bb>FeatureCollection.json if the instance is a
    FeatureCollection, otherwise <bb>Feature.json.
  - BBs without dispatchers: validate against the library <bb>.json.

Remote schemas (json-fg/feature.json, json-fg/featurecollection.json, SWE 3.0,
CDIF property BBs) are fetched once and cached under .schema_cache/. Subsequent
runs read from cache, cutting per-example validation from minutes to seconds.

Usage:
    python tools/validate_all.py                # validate every BB's examples
    python tools/validate_all.py gsmscimlBasic  # validate one BB's examples only
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import urllib.error
from collections import Counter
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    import referencing
    from referencing import Registry, Resource
except ImportError:
    print("Install jsonschema + referencing: pip install jsonschema referencing",
          file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "_sources"
CACHE_DIR = ROOT / ".schema_cache"
BASE = "https://schemas.usgin.org/geosci-json"

PROFILE_BBS = {
    "gsmBasicGeologyCollection",
    "gsmExtendedGeologyCollection",
    "gsmEarthMaterialCollection",
}


# ---------------------------------------------------------------------------
# Registry: local schemas + cached remote retrieval

def _load_local_schemas() -> list[tuple[str, Resource]]:
    out: list[tuple[str, Resource]] = []
    for bb_dir in sorted(SOURCES.iterdir()):
        if not bb_dir.is_dir():
            continue
        for p in bb_dir.glob("*.json"):
            if p.name in ("bblock.json", "resolvedSchema.json"):
                continue
            try:
                data = json.loads(p.read_text(encoding="utf-8-sig"))
            except Exception:
                continue
            sid = data.get("$id") if isinstance(data, dict) else None
            if sid:
                out.append((sid, Resource.from_contents(data)))
    return out


def _cache_path(uri: str) -> Path:
    safe = uri.replace("://", "_").replace("/", "_").replace("?", "_")
    return CACHE_DIR / safe


def _retrieve(uri: str) -> Resource:
    cp = _cache_path(uri)
    if cp.exists():
        return Resource.from_contents(json.loads(cp.read_text(encoding="utf-8")))
    try:
        with urllib.request.urlopen(uri, timeout=20) as r:
            contents = json.loads(r.read())
    except (urllib.error.URLError, json.JSONDecodeError) as exc:
        raise referencing.exceptions.NoSuchResource(ref=uri) from exc
    CACHE_DIR.mkdir(exist_ok=True)
    cp.write_text(json.dumps(contents), encoding="utf-8")
    return Resource.from_contents(contents)


def build_registry() -> Registry:
    return Registry(retrieve=_retrieve).with_resources(_load_local_schemas())


# ---------------------------------------------------------------------------
# Validation per example

def pick_schema_url(bb: str, bb_dir: Path, inst: dict) -> str:
    """The unified <bb>Schema.json handles both Feature and FeatureCollection
    via a root if/then/else on `type`. Same URL for any shape."""
    return f"{BASE}/{bb}/{bb}Schema.json"


def validate_example(reg: Registry, sid: str, inst: dict) -> list:
    v = Draft202012Validator({"$ref": sid}, registry=reg)
    try:
        return sorted(v.iter_errors(inst), key=lambda e: str(e.absolute_path))
    except referencing.exceptions.Unresolvable as ex:
        # Surface as a single synthetic error so the report still shows the file.
        return [type("E", (), {"absolute_path": [], "message": f"[unresolvable] {ex}"})()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("bb", nargs="?", help="Optional: only validate this BB's examples")
    args = ap.parse_args()

    reg = build_registry()

    bbs = sorted(p for p in SOURCES.iterdir() if p.is_dir())
    if args.bb:
        bbs = [p for p in bbs if p.name == args.bb]
        if not bbs:
            print(f"BB {args.bb!r} not found under {SOURCES}", file=sys.stderr)
            return 2

    rows: list[tuple[str, str, int]] = []
    pattern_counter: Counter[str] = Counter()
    pass_count = fail_count = 0

    # Example files live in the bblocks-template-style `examples/` subdir
    # under each BB.
    for bb_dir in bbs:
        bb = bb_dir.name
        ex_dir = bb_dir / "examples"
        if not ex_dir.exists():
            continue
        for f in sorted(ex_dir.glob("*.json")):
            try:
                inst = json.loads(f.read_text(encoding="utf-8-sig"))
            except Exception as exc:
                rows.append((bb, f.name, -1))
                print(f"  {bb}/{f.name}: JSON parse error: {exc}")
                fail_count += 1
                continue
            sid = pick_schema_url(bb, bb_dir, inst)
            errs = validate_example(reg, sid, inst)
            rows.append((bb, f.name, len(errs)))
            if errs:
                fail_count += 1
                for e in errs:
                    path = "/".join(str(x) for x in (getattr(e, "absolute_path", []) or []))
                    import re
                    pattern_counter[re.sub(r"/\d+", "/*", path)] += 1
            else:
                pass_count += 1

    # Report
    print(f"{'BB':35s} {'Example':55s} {'Errs':>4s}")
    print("-" * 100)
    for bb, name, n in rows:
        flag = "OK" if n == 0 else (f"{n}" if n > 0 else "PARSE")
        print(f"  {bb:33s} {name:55s} {flag:>4s}")
    print(f"\n{pass_count} pass, {fail_count} fail (of {pass_count + fail_count})")

    if pattern_counter:
        print("\nError patterns (top 20):")
        for path, n in pattern_counter.most_common(20):
            print(f"  {n:>3d}x  {path or '(root)'}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
