# geosci-json

JSON Schema building blocks for geoscience metadata, generated from the **GeoSciML 4.1** UML model via a config-driven generator and published with the [OGC Building Blocks](https://github.com/opengeospatial/bblocks-postprocess) pipeline. Encoding follows **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*) with JSON-FG-compliant FeatureTypes. Repo layout matches the [bblocks-template](https://github.com/opengeospatial/bblocks-template) plus extensions from the sibling CDIF [metadataBuildingBlocks](https://github.com/cdif-dt/metadataBuildingBlocks) repo.

## Status

**10 building blocks** (consolidated from the XMI's 19 UML packages plus 1 hand-curated FC profile), **147 class definitions** preserved 1:1 from the source UML, **61 example instances** validating clean. Cross-BB `$ref` resolution and FC dispatch are exercised end-to-end.

| BB | Role | Dispatchable featureTypes |
| --- | --- | --- |
| `gsmBasicGeology` | Basic library + merged Feature/FC dispatcher | 9 (GeologicUnit, MappedFeature, Contact, Fold, Foliation, ShearDisplacementStructure, GeologicEvent, AnthropogenicGeomorphologicFeature, NaturalGeomorphologicFeature) |
| `gsmscimlLite` | Lite views | 7 |
| `gsmSpecimen` | Specimen | 2 (SF_Specimen [ISO 19156 §8.6, hand-curated], ReferenceSpecimen) |
| `gsmEarthMaterial` | EarthMaterial library + merged dispatch via `wrapAsFeature` | 4 (Mineral, OrganicMaterial, RockMaterial, CompoundMaterial) |
| `gsmGeologicStructureExtension` | Structure Extension | 6 (DisplacementEvent, FoldSystem, Joint, Layering, Lineation, NonDirectionalStructure) |
| `gsmGeologicUnitExtension` | GeologicUnit DataType library | — |
| `gsmGeologicRelationExtension` | GeologicRelation DataType library | — |
| `gsmBorehole` | Borehole | 3 (Borehole, BoreholeInterval, OriginPosition) |
| `gsmGeologicTime` | Geologic time, OWL-Time aligned | 6 (GeochronologicEra [Cox & Richard 2015 ≡ time:ProperInterval], GeochronologicBoundary [≡ time:Instant], plus 4 stratotype FTs) |
| `gsmExtendedGeologyCollection` | FC profile — all 9 Basic FTs with Extension description-slot constraints | 9 |

## Per-BB layout (bblocks-template + CDIF extensions)

Each BB directory contains:

| File | Role |
| --- | --- |
| `schema.yaml` | Canonical schema (YAML) |
| `<bb>Schema.json` | JSON serialization with `$id` (CDIF extension) |
| `resolvedSchema.json` | Standalone — all cross-BB `$refs` inlined into local `$defs` (CDIF extension) |
| `bblock.json` | OGC bblock metadata (`itemClass`, `register`, `version`, etc.) |
| `description.md` | Narrative (auto-generated, includes class table + per-class detail) |
| `context.jsonld` | JSON-LD context (stub — for future semantic uplift) |
| `rules.shacl` | SHACL rules (stub) |
| `examples.yaml` | Manifest pointing to `examples/<file>.json` (bblocks-template wrapper format) |
| `examples/*.json` | Instance examples (Features and FeatureCollections) |
| `tests.yaml` | Negative-test manifest (stub — empty list `[]`) |

## Repository contents

| Path | What it is |
| --- | --- |
| [geosciml4.1.xmi](geosciml4.1.xmi) | Source UML model (EA UML 1.3 / XMI 1.1 export). Authoritative. |
| [SWECommon2.0.xmi](SWECommon2.0.xmi) | Imported SWE Common 2.0 UML; reference only (we substitute SWE 3.0). |
| [bb-grouping.yaml](bb-grouping.yaml) | **The generator config.** Defines BBs (UML package grouping), per-BB `dispatch:` lists (rich entries with `wrapAsFeature` / extension constraints), and FC profile BBs. |
| [swe-mappings.yaml](swe-mappings.yaml) | SWE 2.0 type names → SWE 3.0 `$ref` URLs |
| [cgi-vocab-reference.yaml](cgi-vocab-reference.yaml) | CGI vocabulary URL reference (documentation only) |
| [swe-types-used.md](swe-types-used.md) | Decision record for SWE encoding |
| [tools/ea_uml_to_ogc_schema.py](tools/ea_uml_to_ogc_schema.py) | Main generator: EA XMI + bb-grouping.yaml → BB schemas |
| [tools/resolve_geosci_schema.py](tools/resolve_geosci_schema.py) | Inlines cross-BB `$refs` to produce `resolvedSchema.json` per BB |
| [tools/build_bb_docs.py](tools/build_bb_docs.py) | Generates `description.md` + `examples.yaml` manifests + template stubs |
| [tools/validate_all.py](tools/validate_all.py) | Batch validator with `.schema_cache/` for remote schemas (json-fg, SWE 3.0) |
| [tools/augment_register.py](tools/augment_register.py) | Adds `resolvedSchema` URLs to `register.json` for the viewer |
| `_sources/gsm<Name>/` | Generated BB directories (see layout above) |
| `.github/workflows/` | CI: `process-bblocks.yml` + `deploy-viewer.yml` |

## Generating the schemas

```bash
# Regenerate every BB (defaults to bb-grouping.yaml + geosciml4.1.xmi)
python tools/ea_uml_to_ogc_schema.py --xmi geosciml4.1.xmi

# Single BB (e.g. while iterating)
python tools/ea_uml_to_ogc_schema.py --xmi geosciml4.1.xmi --bb gsmBasicGeology

# Standalone resolved schemas (per BB, cross-BB refs inlined):
python tools/resolve_geosci_schema.py --all

# Description.md + examples.yaml manifests + stub artifacts:
python tools/build_bb_docs.py

# Batch validate every example file (caches remote schemas in .schema_cache/):
python tools/validate_all.py
```

The generator reads `bb-grouping.yaml` for the BB→package mapping AND per-BB dispatcher config (`dispatch:` block with rich entries). The legacy `--package` CLI flag is gone — generation is config-driven.

## Encoding decisions

Full rationale in [swe-types-used.md](swe-types-used.md) and [agents.md](agents.md).

- **Base format**: JSON-FG for `«FeatureType»`; plain JSON object schemas for `«DataType»`/`«Type»`; `{type: string, format: uri}` for `«CodeList»` (or `{type: string, enum: [...]}` if the UML CodeList has inline enumeration members — currently only `DescriptionPurpose`).
- **JSON-FG envelope**: FeatureType own properties live under `properties.properties.<x>` (the double-`properties` nesting is JSON-Schema syntax + GeoJSON envelope key, not redundancy — see agents.md).
- **Merged Feature/FC schema per BB**: each FT-bearing BB ships ONE `<bb>Schema.json` with a root `if/then/else` on `type` — `type=FeatureCollection` validates as JSON-FG FC with `features.items` dispatched via `_FeatureDispatch`, otherwise dispatched as a single Feature.
- **SWE Common 2.0 → 3.0 substitution**: `Quantity`, `QuantityRange`, `DataRecord` → SWE 3.0 URLs via `swe-mappings.yaml`. SWE::Category → SWE 3.0 `Category.json`.
- **By-reference encoding**: each schema has a local `$defs.SCLinkObject` (the ShapeChange-conventional implementation of [OGC API Link Object](https://schemas.opengis.net/ogcapi/common/part1/1.0/openapi/schemas/link.json) per RFC 8288). Type-with-identity targets get `oneOf [SCLinkObject, $ref Class]` — accepting either inline content or a link reference.
- **Hand-curated extensions** (added because the source XMI didn't include them): `SF_Specimen` (ISO 19156 §8.6), `GeochronologicEra` / `GeochronologicBoundary` (Cox & Richard 2015 — aligns to W3C OWL-Time `time:ProperInterval` / `time:Instant`). See `EXTRA_DEFS_PER_BB` in the generator.
- **OWL-Time alignment for `iso19108:TM_Period` / `TM_Instant`**: accept SCLinkObject, OWL-Time object form (`hasBeginning`/`hasEnd` or `hasBeginningDateTime`/`hasEndDateTime`), or compact tuple `[start, end]`. Canonical encoding is the OWL-Time object form.
- **CDIF cross-references for ISO 19115 metadata**: `CI_Responsibility` → `anyOf [SCLinkObject, CDIF agentInRole]`; `ScopedName` → `anyOf [SCLinkObject, CDIF definedTerm, CDIF skosConcept]`; `NamedValue` → `anyOf [SCLinkObject, CDIF variableMeasured]`.

## CI / build

```bash
./build.sh    # Run the OGC bblocks-postprocess Docker image locally
./view.sh     # Serve the local register on http://localhost:9090
```

Two workflows in `.github/workflows/`:

- **`process-bblocks.yml`** — on push to `main`, runs the OGC bblocks-postprocess action over `_sources/`, produces `build/register.json`, validates schemas + examples, and commits the build artifacts back to `main`.
- **`deploy-viewer.yml`** — cascades from process-bblocks success. Augments `register.json` with `resolvedSchema` URLs (`augment_register.py`), generates a custom validation report, and deploys the [smrgeoinfo/bblocks-viewer](https://github.com/smrgeoinfo/bblocks-viewer) (a fork of the OGC viewer with a `resolvedSchema` link on each BB page and orange/yellow SHACL severity flags).

CDIF-specific workflows (`update-validation-schemas.yml`, `generate-jsonforms.yml`) are NOT used here — those generate CDIF-Discovery-Profile artifacts and push to a separate validation repo, neither of which applies to geosci-json.

`bblocks-config.yaml`: `identifier-prefix: usgin.bbr.geosci.` → each BB has `usgin.bbr.geosci.<bbName>` as its `itemIdentifier`.

## Authoring guidance

For Claude Code / agent sessions: [agents.md](agents.md). The generator is the source of truth — **do not hand-edit `_sources/`**. Add classes via `EXTRA_DEFS_PER_BB`, extend dispatchers via `bb-grouping.yaml`'s `dispatch:` block, change cross-cutting policy in the resolver (`EXTERNAL_TYPE_RESOLUTION`).

## Related

- Skill: **`/ogc-uml2json`** (user-global) — decision workflow for OGC 24-017r1 with bundled mapping tables.
- Sibling: [CDIF metadataBuildingBlocks](https://github.com/cdif-dt/metadataBuildingBlocks) — different workflow (hand-authored CDIF BBs in JSON-LD); shares CI infrastructure and the bblocks-postprocess pipeline.
- Viewer fork: [smrgeoinfo/bblocks-viewer](https://github.com/smrgeoinfo/bblocks-viewer) — adds the `resolvedSchema` link and SHACL severity colouring used by both this repo and CDIF.

## License

MIT. See [LICENSE](LICENSE).
