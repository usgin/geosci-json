# Agents guide: geosci-json

This file orients a future Claude Code (or similar agent) session in the **geosci-json** repository. Read this before making changes.

## What this repo is

JSON Schema building blocks for **GeoSciML 4.1**, generated from a UML model (`geosciml4.1.xmi`) using a config-driven generator. Output follows **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*), is JSON-FG-compliant for `«FeatureType»` classes, and conforms to the [bblocks-template](https://github.com/opengeospatial/bblocks-template) per-BB layout (with CDIF-style flattened examples, `<bb>Schema.json` JSON output, and `resolvedSchema.json`).

The workflow is **generator-driven**, not hand-authored. The XMI plus `bb-grouping.yaml` are the source of truth:

- `geosciml4.1.xmi` - classes, attributes, stereotypes, tagged values, associations from the UML.
- `bb-grouping.yaml` - which UML packages map to which BB, and per-BB `dispatch:` config (with `wrapAsFeature` and extension constraints).
- `swe-mappings.yaml` - SWE 2.0 → SWE 3.0 substitution table.
- `cgi-vocab-reference.yaml` - reference documentation only; not consumed by the generator.

Everything under `_sources/` is **generator output**. Do not hand-edit it.

## What this repo is NOT

- **Not the CDIF metadataBuildingBlocks workflow.** That sibling repo hand-authors per-class BBs with `cdi:` JSON-LD context, `@graph` wrappers, and a different generator. None of that applies here. If you see CDIF-style conventions creeping in (`@context`, `@graph`, `@type` const checks, `cdi:`), back them out.
- **Not a place to redefine SWE Common 2.0 types.** SWE 2.0 references in the UML map to external SWE 3.0 schemas. `SWECommon2.0.xmi` is reference material.
- **Not a place to hand-edit `_sources/*/*.json`.** Those get regenerated. Edit the generator, `bb-grouping.yaml`, or mapping files instead.

## Repo layout

```
geosci-json/
├── geosciml4.1.xmi               # source UML (EA UML 1.3 / XMI 1.1)
├── SWECommon2.0.xmi              # reference only
├── bb-grouping.yaml              # BB definitions, package mapping, per-BB dispatch config
├── swe-mappings.yaml             # SWE 2.0 → SWE 3.0 substitution
├── cgi-vocab-reference.yaml      # CGI vocab URLs (reference only)
├── swe-types-used.md             # decision record
├── tools/
│   ├── ea_uml_to_ogc_schema.py   # generator
│   ├── resolve_geosci_schema.py  # cross-BB ref inliner -> resolvedSchema.json
│   ├── build_bb_docs.py          # description.md + examples.yaml manifests
│   ├── validate_all.py           # batch validator with .schema_cache/
│   ├── augment_register.py       # adds resolvedSchema URLs to register.json
│   └── generate_custom_report.py # SHACL severity-coloured HTML report
├── _sources/                     # generated; one dir per BB:
│   └── gsm<Name>/
│       ├── schema.yaml           # canonical (YAML)
│       ├── <bb>Schema.json       # JSON with $id
│       ├── resolvedSchema.json   # standalone, no cross-BB refs
│       ├── bblock.json           # OGC bblock metadata
│       ├── description.md
│       ├── context.jsonld        # stub
│       ├── rules.shacl           # stub
│       ├── examples.yaml         # bblocks-template wrapper format
│       ├── examples/*.json       # instances
│       └── tests.yaml            # stub `[]`
├── .github/workflows/
│   ├── process-bblocks.yml       # bblocks-postprocess on push to main
│   └── deploy-viewer.yml         # cascades on process-bblocks success
├── bblocks-config.yaml           # identifier-prefix: usgin.bbr.geosci.
├── build.sh, view.sh             # local pipeline runners
└── README.md, agents.md, USAGE.md, LICENSE
```

## BB inventory (10 BBs, 147 class defs, 61 examples)

| BB | UML packages | Dispatcher | Note |
| --- | --- | --- | --- |
| `gsmBasicGeology` | GeoSciMLBasic, Collection, GSML_DataTypes, GeologicEvent, GeologicStructure, GeologyBasic, Geomorphology | 9 FTs | Foundation; other BBs `$ref` here. |
| `gsmscimlLite` | GeoSciMLLite | 7 FTs | Flat Lite views |
| `gsmSpecimen` | LaboratoryAnalysis-Specimen + 3 sub-packages | 2 FTs (SF_Specimen, ReferenceSpecimen) | `SF_Specimen` hand-curated (ISO 19156 §8.6). The other 7 LabAnalysis classes stay in `$defs` as `$ref` targets but aren't dispatched. |
| `gsmEarthMaterial` | EarthMaterialDetails | 4 FTs via `wrapAsFeature` | Merged from former gsmEarthMaterialExtension + gsmEarthMaterialCollection. Mineral / OrganicMaterial / RockMaterial / CompoundMaterial are «Type» (not «FeatureType»); profile injects the JSON-FG envelope. |
| `gsmGeologicStructureExtension` | GeologicStructureDetails | 6 FTs | DisplacementEvent, FoldSystem, Joint, Layering, Lineation, NonDirectionalStructure |
| `gsmGeologicUnitExtension` | GeologicUnitDetails | - | DataType library (GeologicUnitDescription, BeddingDescription) |
| `gsmGeologicRelationExtension` | GeologicRelation | - | DataType library (typed binary relations) |
| `gsmBorehole` | Borehole | 3 FTs | Borehole, BoreholeInterval, OriginPosition |
| `gsmGeologicTime` | GeologicTime, GSSP, TemporalReferenceSystem, TimeScale, GeologicAgeDetails | 6 FTs | `GeochronologicEra` + `GeochronologicBoundary` hand-curated, Cox & Richard 2015 / OWL-Time aligned. |
| `gsmExtendedGeologyCollection` | (FC profile, no packages) | 9 FTs | All 9 gsmBasicGeology FTs with applicable extension description-slot constraints. |

## Generator config: `bb-grouping.yaml`

Two top-level keys:

```yaml
bbs:
  gsmBasicGeology:
    description: |
      ...
    packages:
      - GeoSciMLBasic
      - Collection
      # ...
    dispatch:                              # OPTIONAL - overrides auto-discovery
      - name: Mineral                      # featureType discriminator value
        ref: "#Mineral"                    # local anchor (or cross-BB ref)
        wrapAsFeature: true                # inject JSON-FG envelope (for «Type» classes)
        extensionConstraintsArray:         # OR extensionConstraints (scalar)
          gbEarthMaterialDescription: "#RockMaterialDescription"

profiles:
  gsmExtendedGeologyCollection:
    description: |
      ...
    featureTypes:                          # FC profile dispatch entries
      - name: GeologicUnit
        ref: ../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicUnit
        extensionConstraintsArray:
          gbUnitDescription: ../gsmGeologicUnitExtension/gsmGeologicUnitExtensionSchema.json#GeologicUnitDescription
```

The `dispatch:` block and the `profiles[].featureTypes:` block use the same entry shape (`name`, `ref`, optional `wrapAsFeature` / `extensionConstraints` / `extensionConstraintsArray`). Both flow through `_build_profile_branch()` in the generator.

## Generator precedence for dispatch list (per BB)

When deciding what featureType values to accept:

1. **`bb-grouping.yaml` `dispatch:` block** (preferred - rich entries)
2. **`DISPATCHER_OVERRIDES_PER_BB`** (Python constant in the generator - simple name list, used for narrow overrides like `gsmSpecimen: ["SF_Specimen", "ReferenceSpecimen"]`)
3. **`dispatchable_fts(loader, pkgs)`** - auto-discovery from XMI («FeatureType»-stereotyped, non-abstract, not an FC-container)

## Encoding rules

| Topic | Decision |
| --- | --- |
| Base format | JSON-FG for «FeatureType»; plain JSON for «DataType»/«Type»; `{type: string, format: uri}` for «CodeList» |
| «CodeList» with inline enum members | `{type: string, enum: [...]}` (only `DescriptionPurpose` in GeoSciML 4.1) |
| «Union» encoding | `oneOf` over value types (only `GSMLitem`) |
| FeatureType envelope | `allOf [<parent ref>, <properties.properties.<own>>, <required featureType+id on root>]` |
| Merged Feature/FC schema per BB | root `if/then/else` on `type`: FeatureCollection branch wraps json-fg/featurecollection with items dispatched via `_FeatureDispatch`; else-branch routes single Feature via same helper |
| Optional values | `oneOf [{type:null}, <inner>]` (allows explicit null) |
| By-reference encoding | local `$defs.SCLinkObject` (the [OGC API Link Object](https://schemas.opengis.net/ogcapi/common/part1/1.0/openapi/schemas/link.json) shape per RFC 8288, ShapeChange-conventional name). Type-with-identity targets get `oneOf [SCLinkObject, $ref Class]`. UML `byReference` tag is overridden: emit oneOf (inline + ref) regardless - matches OGC code-sprint convention. |
| Cross-BB refs | `../<bb>/<bb>Schema.json#<ClassName>` |
| External ISO types | resolved via `EXTERNAL_TYPE_RESOLUTION` table in the generator. See "External types" below. |
| SWE 2.0 substitution | SWE 3.0 URLs from `swe-mappings.yaml` |
| SWE::Category | `$ref` to SWE 3.0 `Category.json` |
| `entityType` discriminator | NOT used - `featureType` alone is the discriminator |
| OCL constraints | embedded in `description`, prefixed `Constraint:` |

## External type resolution (`EXTERNAL_TYPE_RESOLUTION`)

ISO 19103/19107/19108/19115/19156 types in the UML default to `SCLinkObject` (by-reference). Three categories carry richer alignments:

**OWL-Time-aligned** (W3C [OWL-Time](https://www.w3.org/TR/owl-time/)):

| External type | Encoding |
| --- | --- |
| `iso19108:TM_Instant` ≡ `time:Instant` | oneOf [SCLinkObject, OWL-Time `inXSDDateTime`/`inXSDDate`/etc., bare ISO 8601 string] |
| `iso19108:TM_Period` ≡ `time:ProperInterval` | oneOf [SCLinkObject, `{hasBeginning, hasEnd}` Instant refs, `{hasBeginningDateTime, hasEndDateTime}` shortcut, compact `[startDate, endDate]` tuple] |

The compact tuple is documented as a convenience alias; the OWL-Time object form is canonical.

**CDIF metadata cross-references**:

| External type | Encoding |
| --- | --- |
| `iso19115:CI_Responsibility` | `anyOf [SCLinkObject, CDIF agentInRole]` |
| `iso19103:ScopedName` | `anyOf [SCLinkObject, CDIF definedTerm, CDIF skosConcept]` |
| `iso19103:NamedValue` | `anyOf [SCLinkObject, CDIF variableMeasured]` |

**Everything else** (CI_Citation, OM_Observation, GFI_Feature, SF_SamplingFeature, etc.): plain `$ref SCLinkObject` - by-reference only.

## Hand-curated classes (`EXTRA_DEFS_PER_BB`)

Some classes consumers want aren't in the GeoSciML XMI (they live in external standards). Hand-author the `$def` and inject it into the BB's `$defs` via `EXTRA_DEFS_PER_BB[bb_name]`:

| Class | BB | Source | Reason |
| --- | --- | --- | --- |
| `SF_Specimen` | `gsmSpecimen` | ISO 19156:2011 §8.6 | Sampling-feature specimen; inlines SF_SamplingFeature parent's properties (sampledFeature, relatedObservation, relatedSamplingFeature, lineage) since the parent isn't separately schematised. |
| `GeochronologicEra` | `gsmGeologicTime` | Cox & Richard 2015, OWL-Time | ≡ `time:ProperInterval`; properties `start` / `end` ↔ `time:hasBeginning` / `time:hasEnd`; `member[]` ↔ `time:intervalContains` |
| `GeochronologicBoundary` | `gsmGeologicTime` | Cox & Richard 2015, OWL-Time | ≡ `time:Instant`; `stratotype` → existing XMI StratigraphicPoint anchor |

Mechanism: the constants `SF_SPECIMEN_DEF`, `GEOCHRONOLOGIC_ERA_DEF`, etc., live near the top of `tools/ea_uml_to_ogc_schema.py`. `build_schema()` merges them into the BB's `$defs` after the XMI-derived classes. Then `bb-grouping.yaml`'s `dispatch:` block on the receiving BB adds the new featureType to the dispatcher.

## How the generator works

`tools/ea_uml_to_ogc_schema.py` is a single-file Python script. Three phases:

1. **`EaXmiLoader`** - regex-based reader for EA's UML 1.3 / XMI 1.1 (cp1252). Builds `UmlClass` objects, pre-passes harvest OCL constraints and `<UML:Association>` navigable ends.
2. **`Resolver`** - classifies each attribute's type into primitive / geometry / SWE / Category / local / cross_bb / external_iso / unknown. Cross-BB refs use `../<bb>/<bb>Schema.json#X`.
3. **`Emitter`** - applies OGC code-sprint conventions per stereotype:
   - `«FeatureType»` → `allOf [<parent ref>, <properties.properties.<own>>, <required featureType+id on root FT>]`
   - `«Type»` / `«DataType»` / unstereotyped → plain object with optional `allOf [<parent ref>, ...]`
   - `«CodeList»` → `{type: string, format: uri}` (or `{type: string, enum: [...]}` if UML has inline enum members)
   - `«Union»` → `oneOf` over value types
   - Always adds local `$defs.SCLinkObject` to every emitted schema.

After per-class emission, `build_merged_schema()` wraps the library `$defs` with a root `if/then/else` on `type` and an internal `_FeatureDispatch` helper, producing the single merged `<bb>Schema.json` per FT-bearing BB.

For FC profile BBs (no UML packages, hand-authored in `bb-grouping.yaml profiles:`), `build_profile_schema()` produces the FC-only schema with `features.items` dispatching via the same `_build_profile_branch()` helper.

CLI:

```bash
python tools/ea_uml_to_ogc_schema.py --xmi geosciml4.1.xmi
python tools/ea_uml_to_ogc_schema.py --xmi geosciml4.1.xmi --bb gsmBasicGeology
```

## Property nesting in the schema

`properties.properties.properties.<x>` is **three different roles**, not redundancy:

```
properties:             # [A] JSON Schema keyword: "names allowed in the outer Feature object"
  properties:           # [B] one of those names, literally "properties" (GeoJSON envelope key)
    type: object
    properties:         # [C] JSON Schema keyword: "names allowed in the inner envelope object"
      <className>: ...  #     the actual domain attributes
```

[A] and [C] are JSON-Schema syntax; [B] is the GeoJSON convention that Feature.properties carries the domain payload. The depth is fixed by GeoJSON/JSON-FG, not by our generator.

## CI / build

Two workflows:

- **`process-bblocks.yml`** - runs the OGC bblocks-postprocess action on push to `main`. Validates schemas + examples, builds `register.json`, commits build artifacts back. `fail_on_error: false` is set as a first-deploy bootstrap (cross-BB `$ref`s target gh-pages URLs that don't exist until the initial deploy publishes them - flip back to `true` once stable).
- **`deploy-viewer.yml`** - cascades on process-bblocks success. Runs `augment_register.py` (adds `resolvedSchema` URLs to register entries; reads identifier-prefix from `bblocks-config.yaml` so it works in any repo with the OGC layout) and `generate_custom_report.py` (SHACL severity-coloured validation report). Deploys [smrgeoinfo/bblocks-viewer](https://github.com/smrgeoinfo/bblocks-viewer) - a fork of the OGC viewer with `resolvedSchema` links and orange/yellow SHACL severity flags.

CDIF-specific workflows (`update-validation-schemas.yml`, `generate-jsonforms.yml`) have been removed - they pushed to a separate CDIF validation repo and walked CDIF's `_sources/profiles/` layout, neither of which applies here.

## Adding things

### A new dispatchable featureType to an existing BB

If the class is already in the BB's `$defs` (i.e., came from the XMI): add a `dispatch:` entry in `bb-grouping.yaml`:

```yaml
gsmSpecimen:
  packages: [...]
  dispatch:
    - name: SF_Specimen
      ref: "#SF_Specimen"
    - name: ReferenceSpecimen
      ref: "#ReferenceSpecimen"
```

If the class isn't in the XMI: hand-curate the `$def` (see `SF_SPECIMEN_DEF`, `GEOCHRONOLOGIC_ERA_DEF` for patterns), add it to `EXTRA_DEFS_PER_BB[bb_name]`, then add the dispatch entry.

### A new external-type mapping

Edit `EXTERNAL_TYPE_RESOLUTION` in the generator. Pattern: one entry per `"iso19xxx:TypeName"` key with the schema fragment to emit. CDIF cross-refs use `https://cross-domain-interoperability-framework.github.io/.../<bb>/schema.json`.

### A new SWE substitution

Edit `swe-mappings.yaml` under `external_types:`.

### A new FC profile

Add an entry under `profiles:` in `bb-grouping.yaml`:

```yaml
profiles:
  gsmMyProfile:
    description: |
      ...
    featureTypes:
      - name: FooFeature
        ref: ../gsmBasicGeology/gsmBasicGeologySchema.json#FooFeature
        # optional extensionConstraints / extensionConstraintsArray / wrapAsFeature
```

The generator emits `_sources/gsmMyProfile/gsmMyProfileSchema.json` + the standard layout.

## Validation

`tools/validate_all.py` batch-validates every example file at `_sources/*/examples/*.json` against its BB's schema (always `<bb>Schema.json` after the Feature/FC merge). Remote schemas (json-fg, SWE 3.0, CDIF property BBs) are fetched once and cached in `.schema_cache/` (gitignored).

Pre-fill the cache by running validate_all once; subsequent runs go from minutes to seconds.

Current status: **61 / 61 examples validate clean**.

## Process notes for agents

- **Trust the XMI + `bb-grouping.yaml`.** When in doubt about a class, attribute, or BB grouping, those are authoritative.
- **Don't edit `_sources/*` by hand.** Every commit there will be wiped on the next regen.
- **Surface tradeoffs before coding** (per repo's [CLAUDE.md](CLAUDE.md) - "Think Before Coding").
- **Match the existing generator style.** Single file, regex-based, single-pass per concern. Resist the urge to introduce a class hierarchy or a "framework."
- **Iterate on one BB first** before regenerating everything. `python tools/ea_uml_to_ogc_schema.py --bb gsmBasicGeology` is fast.

## Related skills and resources

- **`/ogc-uml2json`** - user-global Claude skill: decision workflow for OGC 24-017r1, with bundled mapping tables.
- **OGC 24-017r1 PDF**: `C:\Users\smrTu\OneDrive\Documents\Workspace\DataModel\OGC\UML2JSON-24-017r1.pdf`
- **OWL-Time spec**: https://www.w3.org/TR/owl-time/
- **Cox & Richard 2015**: "A formal model for the geologic timescale and GSSP" (geologic time concepts on top of OWL-Time)
- **CGI vocabulary catalog**: https://www.geosciml.org/resource/vocabulary/cgi/current/
- **SWE Common 3.0 JSON schemas**: https://schemas.opengis.net/sweCommon/3.0/json/
- **JSON-FG Feature schema**: https://schemas.opengis.net/json-fg/feature.json
- **OGC API Link Object schema**: https://schemas.opengis.net/ogcapi/common/part1/1.0/openapi/schemas/link.json
