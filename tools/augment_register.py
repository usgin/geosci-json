"""Add resolvedSchema URLs to register.json for all building blocks."""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTER = REPO_ROOT / "build" / "register.json"
SOURCES = REPO_ROOT / "_sources"
CONFIG = REPO_ROOT / "bblocks-config.yaml"


def _read_identifier_prefix() -> str:
    """Read `identifier-prefix:` from bblocks-config.yaml so this script
    works for any repo (CDIF uses cdif.bbr.metadata., geosci-json uses
    usgin.bbr.geosci., etc.)."""
    if not CONFIG.exists():
        return ""
    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*identifier-prefix\s*:\s*(\S+)", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return ""


def main():
    id_prefix = _read_identifier_prefix()
    if not id_prefix:
        print("WARNING: identifier-prefix not found in bblocks-config.yaml; no BBs will be augmented.")
        return

    with open(REGISTER) as f:
        register = json.load(f)

    base_url = register.get("baseURL", "").rstrip("/")
    count = 0

    for bblock in register.get("bblocks", []):
        item_id = bblock.get("itemIdentifier", "")
        if not item_id.startswith(id_prefix):
            continue

        # Convert dotted suffix to path: e.g. usgin.bbr.geosci.gsmscimlBasic ->
        # gsmscimlBasic; cdif.bbr.metadata.adaProperties.details ->
        # adaProperties/details.
        rel = item_id[len(id_prefix):].replace(".", "/")
        resolved_path = SOURCES / rel / "resolvedSchema.json"

        if resolved_path.exists():
            url = f"{base_url}/_sources/{rel}/resolvedSchema.json"
            bblock["resolvedSchema"] = url
            count += 1

    with open(REGISTER, "w") as f:
        json.dump(register, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added resolvedSchema to {count} building blocks.")


if __name__ == "__main__":
    main()
