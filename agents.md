# Agents guide: geosci-json

This file orients a future Claude Code (or similar agent) session in the **geosci-json** repository. Read this before making changes.

## What this repo is

JSON Schema building blocks for **GeoSciML 4.1**, generated from a UML model (`geosciml4.1.xmi`) using the OGC bblocks-postprocess pattern and the encoding rules from **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*). Output conventions match the OGC code-sprint draft (`geosciml-json-code-sprint`).

The workflow is **generator-driven**, not hand-authored. The XMI is the source of truth: classes, attributes, stereotypes, tagged values (`inlineOrByReference`, `codeList`, etc.), and associations all come from the UML. `swe-mappings.yaml` is the only configuration file the generator currently consumes (for the SWE 2.0 → SWE 3.0 substitution). `cgi-vocab-reference.yaml` is **reference documentation only** — kept for human reference of CGI vocabulary URLs but not consumed by the generator. Everything in `_sources/` is produced output.

## What this repo is NOT

- **Not the CDIF metadataBuildingBlocks workflow.** That sibling repo hand-authors per-class BBs in JSON-LD with the `cdi:` namespace, `@graph` wrappers, etc. None of that applies here. If you see CDIF-style conventions creeping in (`@context`, `@graph`, `@type` const checks, `cdi:`), back them out.
- **Not a place to redefine SWE Common 2.0 types.** SWE 2.0 references in the UML map to SWE 3.0 JSON Schemas externally. `SWECommon2.0.xmi` is reference material, not input to the generator.
- **Not a place to hand-edit `_sources/*/schema.json` files.** Those get regenerated. Edit the generator or the YAML mapping files instead.

## Repo layout

```
geosci-json/
├── geosciml4.1.xmi              # source UML (EA UML 1.3 / XMI 1.1)
├── SWECommon2.0.xmi             # reference only — not converted
├── tools/
│   ├── ea_uml_to_ogc_schema.py  # the generator
│   └── (other inherited helpers — schema_resolver, validators, etc.)
├── swe-mappings.yaml            # SWE 2.0 type → SWE 3.0 $ref URL (consumed by generator)
├── cgi-vocab-reference.yaml      # CGI vocabulary URL reference (documentation only — not consumed)
├── swe-types-used.md            # decision record (SWE diffs, encoding policy)
├── generation-summary.md        # per-BB stats, conventions, full association inventory
├── bblocks-config.yaml          # OGC bblocks-postprocess config (identifier-prefix: usgin.bbr.geosci.)
├── _sources/                    # generated output (one dir per BB)
│   └── geosciml_<Package>/
│       ├── schema.json
│       └── bblock.json
├── .github/workflows/           # CI (inherited from metadataBuildingBlocks)
├── build.sh, view.sh            # local pipeline runners
└── README.md, agents.md, USAGE.md, LICENSE
```

## Encoding rule (settled decisions, 2026-05-11)

Recorded in [swe-types-used.md](swe-types-used.md). Summary:

| Topic | Decision |
| --- | --- |
| Base format | JSON-FG-compliant for `«FeatureType»`; plain JSON object schemas for `«DataType»`/`«Type»`; `{type: string, format: uri}` for `«CodeList»` |
| `«union»` encoding | type discriminator (`oneOf` of value types) |
| `entityType` discriminator | **not used** — `featureType` alone (OGC code-sprint convention) |
| FeatureType `featureType`/`id` requirement | required via 3rd `allOf` element on the root FeatureType (`GeologicFeature`); inherited by subtypes |
| FeatureType property nesting | class-specific fields live under JSON-FG `properties` envelope (schema declares `properties.properties.<x>`) |
| Optional values | wrapped as `oneOf [{type:null}, …]` (allows explicit null) |
| By-reference encoding | local `#/$defs/SCLinkObject` definition; type-with-identity targets get `oneOf [SCLinkObject, $ref Class]`; DataType targets always inline |
| BB granularity | one BB per `«Leaf»`/`«leaf»` or `«Application Schema»` package |
| External package links | by-reference (per user policy) |
| SWE 2.0 substitution | `Quantity`, `QuantityRange`, `DataRecord` → SWE 3.0 URLs from `swe-mappings.yaml` |
| `SWE::Category` attributes | `$ref` to SWE 3.0 `Category.json` (instances are `{type:"Category", definition, label, codeSpace, value}` objects) |
| `«CodeList»`-typed properties | `$ref` to the local CodeList class definition (which is `{type:string, format:uri}`) |
| `codeList` annotation on CodeList classes | emitted only when the source UML class carries a non-blank `codeList` tagged value (none in GeoSciML 4.1) |
| `chemicalAnalysis` (one attribute) | generic SWE 3.0 `DataRecord` |
| ISO 19103/19107/19115 imports | placeholder `$ref` as `"iso19xxx:TypeName"` (will be resolved later) |
| OCL constraints (20) | embedded into `description` of the constrained class/attribute, prefixed `Constraint:` |
| `voidable` attribute stereotype | ignored (not relevant for JSON's open-world model) |
| Stereotype case | normalised at load — `featureType` ≡ `FeatureType`, etc. |
| JSON-FG URL | `https://schemas.opengis.net/json-fg/feature.json` (non-beta) |

Use the **`/ogc-uml2json`** skill (user-global) for the underlying OGC 24-017r1 decision workflow.

## How the generator works

`tools/ea_uml_to_ogc_schema.py` is a single-file Python script (~900 lines). Three phases:

1. **`EaXmiLoader`** — regex-based reader for EA's UML 1.3 / XMI 1.1 (cp1252 encoding). Builds `UmlClass` objects with attributes, supertypes, package path. Pre-passes harvest:
   - OCL `<UML:Constraint>` elements → attributed to enclosing class/attribute by document position.
   - `<UML:Association>` elements → navigable ends merged as synthetic `Attribute`s on the opposite class (dedupes against existing `UML:Attribute`s).
2. **`Resolver`** — classifies each attribute's type into one of: `primitive`, `geometry`, `swe`, `category` (`SWE::Category` → SWE 3.0 `Category.json` ref), `local`, `cross_bb`, `external_iso`, `unknown`. Honors the `inlineOrByReference` UML tagged value for FeatureType/Type targets.
3. **`Emitter`** — applies OGC code-sprint conventions per class stereotype:
   - `«FeatureType»` → `allOf [<parent or JSON-FG Feature>, <{type:object, properties.properties.<own>}>, <required featureType/id on root>]`
   - `«DataType»` / `«Type»` / unstereotyped → `{type: object, properties: {<own>}}` (plus `allOf [<parent>, ...]` if subtype)
   - `«CodeList»` → `{type: string, format: uri}` plus `codeList: <URL>` iff the UML class carries a `codeList` tagged value
   - `«Union»` → `{oneOf: [<value types>]}`
   - Adds `SCLinkObject` definition to every emitted schema's `$defs` for by-reference encoding

CLI:

```bash
python tools/ea_uml_to_ogc_schema.py \
  --xmi geosciml4.1.xmi \
  --package <PackageName> \
  [--bb-name geosciml_<PackageName>] \
  [--out-dir _sources] \
  [--swe-mappings swe-mappings.yaml]
```

(The legacy `--category-codelists` flag still exists for forward compatibility but the YAML it points at is no longer consumed for schema emission.)

To regenerate everything, loop over every package whose stereotype list contains `Leaf`, `leaf`, or `Application Schema` (skipping the root `GeoSciML 4.1` and `GeoSciML4.1` umbrella packages). See `generation-summary.md` for the canonical 23-package list.

## Adding or correcting a mapping

### CodeList class → vocab URL annotation

Add a `codeList` UML tagged value on the `«CodeList»` class in the EA model. Re-export the XMI and re-run the generator. The annotation will be emitted on the generated codelist class definition.

The conditional emission means that for GeoSciML 4.1 today (which carries zero such tags) every codelist class is just `{type: string, format: uri}`. To add an annotation, edit the source UML — not a YAML.

### Category attribute → SWE 3.0 Category vocabulary

Category-typed attributes resolve uniformly to `$ref` SWE 3.0 `Category.json`. Instances carry the vocabulary URL in the `codeSpace` and `definition` members of each Category object — no schema-level binding to a specific vocabulary is needed. If you do need to constrain a specific Category attribute to a fixed vocab, that requires a domain-specific extension of the schema (out of scope for the current encoder).

### New SWE type substitution

Edit `swe-mappings.yaml` under `external_types:`. Add a new key matching the UML type name, with `ref` and `rationale`.

### New ISO type substitution

Currently emitted as `"iso19xxx:TypeName"` placeholders. To replace with real URLs, you'll need to extend the resolver (add an `iso-imports.yaml` mirror of `swe-mappings.yaml` and wire it in).

### Reference: CGI vocabulary URLs

`cgi-vocab-reference.yaml` lists the CGI vocabulary URLs we inferred for the 35 Category-typed attributes and 47 CodeList classes during initial analysis. It is **documentation only** — the schema generator does not read it. Useful as a starting point if you decide to add `codeList` tags to the UML or build a vocabulary-binding profile externally.

## Known gaps (do not silently work around)

See [generation-summary.md](generation-summary.md) for the live list. Highlights:

1. **`lax` wildcard type** (7 occurrences in GeoSciMLLite) — XSD-style open-content slot. Currently emits `{$comment: "Unresolved type: lax", type: object}`. To fix, add a `lax` special-case in the resolver that emits `{type: object, additionalProperties: true}`.
2. **21 ISO placeholder `$refs`** — `iso19115:CI_Citation`, `iso19108:TM_Instant`, etc. Intentional placeholders pending an `iso-imports.yaml` mapping file. Validators will fail to resolve these.
3. **26 unmatched CodeList classes** — no CGI vocab exists for them; emitted as `format: uri` with no `codeList` annotation. Per `treat as open` policy. Re-examine if GeoSciML publishes new vocabularies.
4. **`GSMLitem` Union** — encoded as `oneOf` over 4 LinkObject `$ref`s + 2 typed alternatives. A validator handed an arbitrary LinkObject cannot pick a branch; this is a known OGC 24-017r1 warning for type-discriminator unions over by-reference types. Workaround if it bites: switch to property-choice encoding.
5. **Cross-BB `$ref` paths** use `../geosciml_<Package>/schema.json#<Class>` — resolves on disk after generating all packages. The OGC bblocks-postprocess workflow rewrites these to absolute URLs at publish time.

## CI / build

Inherited from `metadataBuildingBlocks`:

- `.github/workflows/process-bblocks.yml` — runs OGC bblocks-postprocess on push to `main`, produces `register.json`, `bblocks.jsonld`, `bblocks.ttl`, etc.
- `.github/workflows/deploy-viewer.yml`, `generate-jsonforms.yml`, `update-validation-schemas.yml`.
- `build.sh` — local Docker run of bblocks-postprocess.
- `view.sh` — local Docker run of bblocks-viewer on `localhost:9090`.

`bblocks-config.yaml` sets `identifier-prefix: usgin.bbr.geosci.` so every BB gets a `usgin.bbr.geosci.geosciml_<Package>` identifier.

## Process notes for agents

- **Trust the XMI.** When in doubt about a class, attribute, or relationship, the answer is in `geosciml4.1.xmi`. The generator regex-parses it; you can do the same.
- **Don't edit `_sources/*` by hand.** Every commit there will be wiped on the next regen.
- **Surface tradeoffs before coding** (per repo's [CLAUDE.md](CLAUDE.md) — "Think Before Coding").
- **Match the existing style in the generator.** It's a single file, regex-based, single-pass per concern. Resist the urge to introduce a class hierarchy or a "framework."
- **Test with one package first** before running the full 23-package sweep — `GeologicEvent` is a good first target (FeatureType + cross-BB inheritance + SWE refs + Category attribute, all in one small package).

## Related skills and resources

- **`/ogc-uml2json`** — user-global Claude skill: decision workflow for OGC 24-017r1 encoding rules, with bundled mapping tables (ISO 19103 primitives, ISO 19107 geometry, etc.).
- **OGC 24-017r1 PDF**: `C:\Users\smrTu\OneDrive\Documents\Workspace\DataModel\OGC\UML2JSON-24-017r1.pdf`.
- **CGI vocabulary catalog**: `https://www.geosciml.org/resource/vocabulary/cgi/current/`.
- **SWE Common 3.0 JSON schemas**: `https://schemas.opengis.net/sweCommon/3.0/json/`.
- **JSON-FG Feature schema**: `https://beta.schemas.opengis.net/json-fg/feature.json`.
- **OGC LinkObject schema**: `https://bp.schemas.opengis.net/24-017r1/uml2json/1.0/schema_definitions.json#/$defs/LinkObject`.
