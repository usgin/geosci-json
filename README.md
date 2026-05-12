# geosci-json

JSON Schema building blocks for geoscience metadata, generated from the **GeoSciML 4.1** UML model using the [OGC Building Blocks](https://github.com/opengeospatial/bblocks-postprocess) pipeline and the encoding rules in **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*). Output conventions follow the [OGC code-sprint draft](https://github.com/opengeospatial/geosciml-json-code-sprint) (single-file profiles `geoscimlBasic.json` / `geoscimlLite.json`).

## Status

Under development. 23 building blocks generated from `geosciml4.1.xmi`, covering 147 GeoSciML classes. See [generation-summary.md](generation-summary.md) for per-BB statistics and known gaps.

## Repository contents

| Path | What it is |
| --- | --- |
| [geosciml4.1.xmi](geosciml4.1.xmi) | Source UML model (EA UML 1.3 / XMI 1.1 export). Authoritative. |
| [SWECommon2.0.xmi](SWECommon2.0.xmi) | Imported SWE Common 2.0 UML; not converted (we substitute SWE 3.0 — see decisions below). |
| [tools/ea_uml_to_ogc_schema.py](tools/ea_uml_to_ogc_schema.py) | The generator: EA XMI → JSON Schema. |
| [tools/resolve_geosci_schema.py](tools/resolve_geosci_schema.py) | Inlines cross-BB `$refs` to produce a `resolvedSchema.json` per BB. |
| [tools/build_bb_docs.py](tools/build_bb_docs.py) | Templates `description.md` and a minimal example per BB from the schema. |
| [swe-mappings.yaml](swe-mappings.yaml) | External-type mapping consumed by the generator: SWE 2.0 type names → SWE 3.0 `$ref` URLs. |
| [cgi-vocab-reference.yaml](cgi-vocab-reference.yaml) | CGI vocabulary URL reference. **Documentation only** — not consumed by the generator; useful as a starting point for future UML tag enrichment or external vocabulary binding. |
| [swe-types-used.md](swe-types-used.md) | Decision record: which SWE types GeoSciML references, 2.0 → 3.0 member diffs, encoding policies. |
| [generation-summary.md](generation-summary.md) | Per-BB stats, conventions confirmed working, known gaps, full UML:Association inventory. |
| `_sources/geosciml_<Package>/` | Generated BB directories (`schema.json` + `resolvedSchema.json` + `bblock.json` + `description.md` + `examples/*.json`). |
| `tools/` | Inherited helper scripts from `metadataBuildingBlocks` (schema resolver, validators, etc.). |
| `.github/workflows/` | OGC `bblocks-postprocess` CI workflows (inherited). |

## Generating the schemas

```bash
# Single package
python tools/ea_uml_to_ogc_schema.py --xmi geosciml4.1.xmi --package GeologicEvent

# All Leaf + ApplicationSchema packages (loop in a script if regenerating)
# Resolved-schema regeneration after a schema change:
python tools/resolve_geosci_schema.py --all

# Description + minimal-example regeneration (reads stereotypes from XMI):
python tools/build_bb_docs.py --xmi geosciml4.1.xmi
```

The generator reads `swe-mappings.yaml` from the repo root by default and writes to `_sources/geosciml_<Package>/`.

## Encoding decisions

Conventions match the OGC code-sprint draft (`geoscimlBasic.json` / `geoscimlLite.json`). Full rationale in [swe-types-used.md](swe-types-used.md) and [agents.md](agents.md).

- **Base format**: JSON-FG-compliant for `«FeatureType»` classes; plain JSON object schemas for `«DataType»`/`«Type»`; `{type: string, format: uri}` for `«CodeList»`.
- **FeatureType envelope**: root FeatureType (`GeologicFeature`) supplies the JSON-FG `Feature` ref and a 3rd `allOf` element requiring `featureType` and `id`. Subclasses inherit via parent `$ref`. Class-specific fields live under the JSON-FG `properties` envelope (schema declares `properties.properties.<x>`).
- **SWE Common 2.0 → 3.0 substitution**: `Quantity`, `QuantityRange`, `DataRecord` referenced via `$ref` to `https://schemas.opengis.net/sweCommon/3.0/json/*`. `SWECommon2.0.xmi` is not converted.
- **`SWE::Category` attributes**: `$ref` to SWE 3.0 `Category.json`. Instances carry vocab URLs in the `codeSpace`/`definition`/`value` members of each Category object.
- **`«CodeList»` classes**: emitted as `{type: string, format: uri}`; `codeList` annotation is added only when the source UML class has a non-blank `codeList` tagged value (none currently in GeoSciML 4.1).
- **Optional values**: wrapped as `oneOf [{type:null}, <inner>]` allowing explicit null.
- **By-reference encoding**: each schema includes a local `#/$defs/SCLinkObject` definition. Type-with-identity targets (`«FeatureType»` / `«Type»`) get `oneOf [SCLinkObject, $ref Class]`; DataType and CodeList targets are inline `$ref`.
- **Union encoding**: type discriminator (`oneOf` of value type refs). Only one Union in the model (`GSMLitem`).
- **No `entityType`**: `featureType` alone is the discriminator on FeatureType instances (matches OGC code-sprint convention).
- **`chemicalAnalysis`**: generic SWE 3.0 `DataRecord`. Field set deliberately unspecified.
- **One BB per package**: each `«Leaf»` (or `«leaf»`) package and each `«Application Schema»` package becomes one BB.

## CI / build (inherited from `metadataBuildingBlocks`)

```bash
./build.sh    # Run the OGC bblocks-postprocess Docker image locally
./view.sh     # Serve the local register on http://localhost:9090
```

`bblocks-config.yaml` is configured with `identifier-prefix: usgin.bbr.geosci.`.

## Authoring guidance

For Claude Code / agent sessions: [agents.md](agents.md). The generator is the source of truth — **do not hand-edit `_sources/geosciml_*/schema.json`**; edits get clobbered on the next regeneration.

## Related

- Skill: **`/ogc-uml2json`** (user-global Claude skill) — decision workflow for UML → JSON Schema per OGC 24-017r1.
- Sibling CDIF repo: [`metadataBuildingBlocks`](https://github.com/cdif-dt/metadataBuildingBlocks) — different workflow (hand-authored CDIF BBs), shares CI infrastructure and tooling.

## License

MIT. See [LICENSE](LICENSE).
