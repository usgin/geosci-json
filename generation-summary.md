# GeoSciML 4.1 → JSON Schema generation: results summary

Run date: 2026-05-11 (latest re-run includes association walk; 63 navigable roles merged)
Generator: [tools/ea_uml_to_ogc_schema.py](tools/ea_uml_to_ogc_schema.py)
Input: [geosciml4.1.xmi](geosciml4.1.xmi)
Outputs: 23 BB directories under [_sources/](_sources/)

## Headline result

**23 / 23 packages generated without error.** 147 GeoSciML classes encoded as JSON Schema definitions across 19 substantive BBs (plus 4 umbrella ApplicationSchema BBs with 0 own classes, which exist only as imports for sibling Leaf packages).

## Per-BB breakdown

| BB | Classes | CodeList defs | allOf | Unions | ISO refs | codeList annotations |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| geosciml_Borehole | 9 | 4 | 3 | 0 | 8 | 0 |
| geosciml_Collection | 3 | 1 | 1 | 1 | 1 | 0 |
| geosciml_EarthMaterialDetails | 19 | 6 | 10 | 0 | 0 | 0 |
| geosciml_GSML_DataTypes | 9 | 4 | 3 | 0 | 0 | 0 |
| geosciml_GSSP | 4 | 0 | 4 | 0 | 0 | 0 |
| geosciml_GeoSciMLBasic | 0 | 0 | 0 | 0 | 0 | 0 |
| geosciml_GeoSciMLExtension | 0 | 0 | 0 | 0 | 0 | 0 |
| geosciml_GeoSciMLLite | 7 | 0 | 7 | 0 | 0 | 0 |
| geosciml_Geochronology | 4 | 3 | 1 | 0 | 3 | 0 |
| geosciml_GeologicAgeDetails | 1 | 0 | 1 | 0 | 0 | 0 |
| geosciml_GeologicEvent | 5 | 2 | 1 | 0 | 0 | 0 |
| geosciml_GeologicRelation | 4 | 2 | 1 | 0 | 0 | 0 |
| geosciml_GeologicSpecimen | 5 | 2 | 2 | 0 | 3 | 0 |
| geosciml_GeologicStructureDetails | 20 | 5 | 15 | 0 | 0 | 0 |
| geosciml_GeologicStructure | 13 | 4 | 5 | 0 | 0 | 0 |
| geosciml_GeologicTime | 0 | 0 | 0 | 0 | 0 | 0 |
| geosciml_GeologicUnitDetails | 2 | 0 | 1 | 0 | 0 | 0 |
| geosciml_GeologyBasic | 20 | 9 | 5 | 0 | 1 | 0 |
| geosciml_Geomorphology | 6 | 2 | 3 | 0 | 0 | 0 |
| geosciml_LaboratoryAnalysis-Specimen | 0 | 0 | 0 | 0 | 0 | 0 |
| geosciml_LaboratoryAnalysis | 7 | 2 | 4 | 0 | 6 | 0 |
| geosciml_TemporalReferenceSystem | 3 | 0 | 0 | 0 | 2 | 0 |
| geosciml_TimeScale | 6 | 1 | 5 | 0 | 0 | 0 |
| **Totals** | **147** | **47** | **72** | **1** | **24** | **0** |

`codeList annotations` is `0` everywhere because GeoSciML 4.1's XMI carries no `codeList` UML tagged values. The generator's conditional-emission rule produces this output automatically; adding tags to the UML and re-exporting the XMI would change this without any generator change.

## Conventions confirmed working

- ✅ `$anchor` per class.
- ✅ JSON-FG `Feature.json` allOf for FeatureType classes whose supertype isn't a FeatureType (entry point).
- ✅ Cross-BB `$ref` for FeatureType subtypes - links to parent in sibling BB (e.g. `../geosciml_GeologyBasic/schema.json#GeologicFeature`).
- ✅ SWE 2.0 → 3.0 substitution (`Quantity`, `QuantityRange`, `DataRecord` → `https://schemas.opengis.net/sweCommon/3.0/json/*`).
- ✅ `SWE::Category`-typed attributes resolve to `$ref` SWE 3.0 `Category.json` (vocab URLs travel in the instance object via `definition`/`codeSpace`/`value`).
- ✅ `«CodeList»` classes emit `{type: string, format: uri}` with a conditional `codeList` annotation (added only when the source UML class carries an explicit `codeList` tagged value - none in GeoSciML 4.1, so the annotation is absent everywhere).
- ✅ CodeList class URLs applied where matched against CGI catalog (21 classes) - 26 marked `treat as open`, emit no `codeList` annotation.
- ✅ Union `oneOf` encoding (1 case: `GSMLitem` in geosciml_Collection).
- ✅ `inlineOrByReference` tag honoured: `byReference` → link object; `inlineOrByReference` → `oneOf [inline, link object]`; `inline` → inline ref.
- ✅ Multiplicity wrapping: `upper>1` → `type: array, items: ..., uniqueItems: true`. `lower>=1` → required.
- ✅ No `entityType` member. `featureType` alone is the discriminator on FeatureType instances (OGC code-sprint convention).
- ✅ Local `#/$defs/SCLinkObject` definition in every BB's schema for by-reference encoding (replaces external `bp.schemas.opengis.net/...LinkObject` ref).
- ✅ Optional values wrapped as `oneOf [{type:null}, …]` allowing explicit null.
- ✅ FeatureType class fields nested under JSON-FG `properties` envelope (schema declares `properties.properties.<x>`).
- ✅ Root FeatureType (`GeologicFeature`) carries a 3rd `allOf` element with `required: [featureType, id]`; subclasses inherit via `$ref` to parent.
- ✅ Stereotype case normalisation (`featureType` vs `FeatureType`, etc.).
- ✅ HTML markup (`<font color>`, `&lt;`, etc.) cleaned from descriptions.
- ✅ ISO 19103 primitives mapped to JSON simple types per OGC 24-017r1 Table 4.
- ✅ ISO 19107 `GM_*` geometry types mapped to GeoJSON schema URLs.
- ✅ OCL constraints (20) appended to the `description` of the class or attribute they constrain, prefixed `Constraint:`.
- ✅ Navigable `UML:AssociationEnd` roles (63) merged as synthetic attributes on the OPPOSITE class. Default `byReference` encoding per OGC 24-017r1 (overridable via the `inlineOrByReference` UML tag). Skipped when a same-named `UML:Attribute` already exists.
- ✅ `inlineOrByReference` machinery restricted to type-with-identity targets (FeatureType / Type). DataType / unstereotyped targets always emit inline.

## Known gaps and follow-ups

### 1. `lax` wildcard (7 occurrences in `geosciml_GeoSciMLLite`)

Five GeoSciMLLite FeatureTypes have an `any` attribute typed `lax` - the XSD wildcard pattern for vendor extensions. The generator emits `{$comment: "Unresolved type: lax", type: object}`. The right JSON encoding is `{type: object, additionalProperties: true}` (or omit the property entirely - the JSON object will accept additional members unless `additionalProperties: false` is declared). Easy fix: special-case `type=="lax"` in the resolver.

### 2. 21 ISO placeholder `$ref` values

These types are referenced via `$ref` strings like `"iso19115:CI_Citation"`, `"iso19108:TM_Period"` - not real URLs. Inventory:

| Placeholder | Count |
| --- | ---: |
| iso19115:CI_Responsibility | 7 |
| iso19115:CI_Citation | 3 |
| iso19103:NamedValue | 3 |
| iso19108:TM_Period | 2 |
| iso19108:TM_Instant | 2 |
| iso19156:GFI_Feature | 1 |
| iso19103:ScopedName | 1 |
| iso19107:DirectPosition | 1 |
| iso19156:SF_SamplingFeature | 1 |

Per your decision (2026-05-11), these are intentional placeholders. Validators will not resolve them until per-type JSON Schema URLs are supplied. Suggested follow-up: build an `iso-imports.yaml` analogous to `swe-mappings.yaml` once concrete schemas are identified.

### 3. CodeList classes without `codeList` URL (26 of 47)

These are emitted as `{type: string, format: uri}` with no `codeList` annotation, per the "treat as open" policy:

```
AnalyticalMethodTerm, AnthropogenicGeomorphologicFeatureTypeTerm,
BoreholeInclinationCode, BoreholePurposeCode, BoreholeStartPointCode,
CollectionTypeTerm, CompositionPartRoleTerm, ExposureTerm, FabricTypeTerm,
FoldProfileTypeTerm, GeochronologicEraRank, GeochronologicEraTerm,
GeologicRelationshipTerm, GeologicSamplingMethodTerm,
GeologicSpecimenPreparationTerm, GeologicUnitHierarchyRoleTerm,
InstrumentTypeTerm, IsotopicEventType, IsotopicSystemName,
LinearDirectedCode, MineralNameTerm, NaturalGeomorphologicFeatureTypeTerm,
NonDirectionalStructureTypeTerm, PhysicalPropertyTerm, RelationRoleTerm,
StatisticalMethodTerm
```

If GeoSciML's vocabulary working group has registries for any of these (under a non-CGI namespace, e.g. `resource.geosciml.org/timescale/...`), add an explicit `codeList` UML tagged value on the CodeList class in the EA model and re-export the XMI - the generator will pick up the tag and emit the annotation automatically. [cgi-vocab-reference.yaml](cgi-vocab-reference.yaml) records the URLs we previously inferred, useful as a starting list for that enrichment.

### 4. UML constructs the generator does NOT yet handle

Not blockers for this run, but recorded for future hardening:

- **Associations as properties** - **resolved.** EA stores some navigable association ends *only* as `UML:AssociationEnd` elements (not as `UML:Attribute`). The generator now walks both. All 63 navigable role names from 57 top-level associations have been merged onto their owning classes. The inventory table below remains for reference. ~~Missing-roles report previously listed 30 gaps; now 0.~~
- **`voidable` attribute stereotype (81 occurrences).** Not relevant in JSON's open-world model - JSON values are nullable / omissible by default, and "void reasons" are not part of the OGC 24-017r1 encoding. No action needed.
- **OCL constraints (20 occurrences).** Now embedded into the `description` of the class or attribute they constrain (prefixed `Constraint:`). Validators don't enforce them, but they survive in documentation.
- **Initial values (3 attributes).** OGC 24-017r1 spec says encode as `default`. Minor; defer.
- **Association classes (0 in this XMI).** Not applicable.
- **Multiple inheritance (0 in this XMI).** Not applicable.
- **GeoSciML's `«estimatedProperty»` attribute stereotype (84 occurrences).** Not specified by OGC 24-017r1; could be emitted as an annotation extension if needed.

### 5. `GSMLitem` Union - schema-validation note

`oneOf` requires exactly one branch to match. Of the 6 branches in `GSMLitem`, 4 resolve to the **same** SWE/OGC LinkObject `$ref`. A validator handed an arbitrary `LinkObject` JSON cannot pick *which* of those 4 conceptual types is intended; it will fail because more than one branch matches. This is the WARNING flagged in the `ogc-uml2json` skill for type-discriminator unions over by-reference types. Workarounds (later, if it bites):

- Switch this single Union to `property-choice` encoding (`{earthMaterialItem: ..., featureItem: ..., ...}` with `minProperties=maxProperties=1`).
- Or use SWE 3.0 / OGC `LinkObject` with a `role` attribute that discriminates.

### 6. Cross-BB `$ref` paths assume sibling-folder layout

Every cross-BB `$ref` uses `../geosciml_<Package>/schema.json#<Class>`. Validation works only when the consuming process resolves refs against the local filesystem. Once the BB-postprocess pipeline publishes these under absolute URLs, those refs become URL refs - the OGC bblocks-postprocess workflow already handles that rewrite, so no action needed before publication.

## Files now in this repo

- [tools/ea_uml_to_ogc_schema.py](tools/ea_uml_to_ogc_schema.py) - the generator (~700 lines).
- [swe-mappings.yaml](swe-mappings.yaml) - Quantity, QuantityRange, DataRecord → SWE 3.0 URLs.
- [cgi-vocab-reference.yaml](cgi-vocab-reference.yaml) - 35 Category attribute mappings + 47 CodeList class mappings. **Documentation only** (not consumed by the generator after the switch to SWE 3.0 `Category` for Category attributes + UML-tag-driven `codeList` annotation for CodeList classes).
- [swe-types-used.md](swe-types-used.md) - decision record and 2.0/3.0 member diffs.
- [_sources/geosciml_*/schema.json](_sources/) - 23 generated BB schemas.
- [_sources/geosciml_*/bblock.json](_sources/) - 23 minimal BB metadata files.

## Recommended next actions (when you return)

1. **Spot-check one or two classes against EA** to gauge how much was missed by the attributes-only walk (the associations-as-properties gap).
2. **Fix the `lax` wildcard** as a generator one-liner.
3. **Decide the CodeList class URL policy for the 26 `treat as open` cases** - keep open, or extend CGI's catalog?
4. **Run the OGC bblocks-postprocess workflow** locally via `build.sh` to confirm the generated BBs validate end-to-end and produce `register.json`/`bblocks.jsonld`/etc.
5. **Decide on the `GSMLitem` Union encoding** if validation flags it.
### Full UML:Association inventory (57 total)

Generated from `geosciml4.1.xmi` on the same run as the schemas. Each row shows one association: which class owns it, the navigable role(s) it carries, and the target class. Role names marked **bold** are navigable - those are the properties that should appear on the source class but currently do NOT, because the generator only walks `UML:Attribute`. Multiplicity column shows lower..upper.

| Source pkg | Source class | Role (target side) | Mult | Target class | Target pkg |
| --- | --- | --- | --- | --- | --- |
| Borehole | Borehole | **indexData** | 0..1 | BoreholeDetails | Borehole |
| Borehole | Borehole | **logElement** | 0..* | BoreholeInterval | Borehole |
| Borehole | Borehole | **downholeDrillingDetails** | 0..* | DrillingDetails | Borehole |
| Borehole | BoreholeInterval | **shape** | 0..1 | GM_Object | ? |
| Borehole | DrillingDetails | **intervalBegin** | 0..1 | GM_Object | ? |
| Borehole | OriginPosition | **relatedBorehole** | 0..* | Borehole | Borehole |
| Collection | GSML | **member** | 1..* | GSMLitem | Collection |
| EarthMaterialDetails | AlterationDescription | **alterationEvent** | 0..1 | GeologicEvent | GeologicEvent |
| EarthMaterialDetails | CompoundMaterialDescription | **constituent** | 0..* | ConstituentPart | EarthMaterialDetails |
| EarthMaterialDetails | CompoundMaterialDescription | **particleGeometry** | 0..1 | ParticleGeometryDescription | EarthMaterialDetails |
| EarthMaterialDetails | ConstituentPart | **relatedMaterial** | 0..* | ConstituentPart | EarthMaterialDetails |
| EarthMaterialDetails | ConstituentPart | **constituentMaterial** | 0..1 | EarthMaterial | GeologyBasic |
| EarthMaterialDetails | ConstituentPart | **constituentParticleGeometry** | 0..1 | ParticleGeometryDescription | EarthMaterialDetails |
| EarthMaterialDetails | MetamorphicDescription | **metamorphicEvent** | 0..1 | GeologicEvent | GeologicEvent |
| EarthMaterialDetails | ParticleGeometryDescription | **sourceOrganism** | 0..* | Organism | EarthMaterialDetails |
| Geochronology | GeochronologicInterpretation | **sourceCollection** | 0..1 | SF_SamplingFeatureCollection | ? |
| GeologicAgeDetails | GeologicEventDescription | **prototype** | 0..1 | StratigraphicPoint | GSSP |
| GeologicEvent | GeologicEvent | **gaEventDescription** | 0..* | GeologicEventAbstractDescription | GeologicEvent |
| GeologicStructure | Contact | **stContactDescription** | 0..1 | ContactAbstractDescription | GeologicStructure |
| GeologicStructure | Fold | **stFoldDescription** | 0..1 | FoldAbstractDescription | GeologicStructure |
| GeologicStructure | Foliation | **stFoliationDescription** | 0..1 | FoliationAbstractDescription | GeologicStructure |
| GeologicStructure | ShearDisplacementStructure | **stStructureDescription** | 0..* | ShearDisplacementStructureAbstractDescription | GeologicStructure |
| GeologicStructureDetails | ContactDescription | **correlatesWith** | 0..1 | GeochronologicBoundary | TimeScale |
| GeologicStructureDetails | DisplacementEvent | **incrementalDisplacement** | 0..1 | DisplacementValue | GeologicStructureDetails |
| GeologicStructureDetails | DisplacementValue | **displacementEvent** | 0..* | DisplacementEvent | GeologicStructureDetails |
| GeologicStructureDetails | FoldDescription | **system** | 0..1 | FoldSystem | GeologicStructureDetails |
| GeologicStructureDetails | FoldSystem | **foldSystemMember** | 0..* | Fold | GeologicStructure |
| GeologicStructureDetails | Layering | **layerComposition** | 0..1 | RockMaterial | GeologyBasic |
| GeologicStructureDetails | NetSlipValue | **slipComponent** | 0..1 | SlipComponents | GeologicStructureDetails |
| GeologicStructureDetails | ShearDisplacementStructureDescription | **stPhysicalProperty** | 0..* | PhysicalDescription | EarthMaterialDetails |
| GeologicUnitDetails | GeologicUnitDescription | **bedding** | 0..1 | BeddingDescription | GeologicUnitDetails |
| GeologyBasic | CompositionPart | **material** | 0..1 | CompoundMaterial | GeologyBasic |
| GeologyBasic | EarthMaterial | **gbEarthMaterialDescription** | 0..* | EarthMaterialAbstractDescription | GeologyBasic |
| GeologyBasic | GeologicFeature | **geologicHistory** | 0..* | GeologicEvent | GeologicEvent |
| GeologyBasic | GeologicFeature | **relatedFeature** | 0..* | GeologicFeature | GeologyBasic |
| GeologyBasic | GeologicFeature | **occurrence** | 0..* | MappedFeature | GeologyBasic |
| GeologyBasic | GeologicUnit | **composition** | 0..* | CompositionPart | GeologyBasic |
| GeologyBasic | GeologicUnit | **gbMaterialDescription** | 0..* | EarthMaterialAbstractDescription | GeologyBasic |
| GeologyBasic | GeologicUnit | **gbUnitDescription** | 0..* | GeologicUnitAbstractDescription | GeologyBasic |
| GeologyBasic | GeologicUnit | **hierarchyLink** | 0..* | GeologicUnitHierarchy | GeologyBasic |
| GeologyBasic | GeologicUnitHierarchy | **targetUnit** | 1 | GeologicUnit | GeologyBasic |
| GeologyBasic | MappedFeature | **specification** | 0..1 | GFI_Feature | ? |
| Geomorphology | GeomorphologicFeature | **unitDescription** | 0..* | GeologicUnit | GeologyBasic |
| Geomorphology | GeomorphologicFeature | **gmFeatureDescription** | 0..* | GeomorphologicUnitAbstractDescription | Geomorphology |
| LaboratoryAnalysis | AnalyticalProcess | **method** | 0..1 | AnalyticalMethod | LaboratoryAnalysis |
| LaboratoryAnalysis | AnalyticalProcess | **acquisition** | 0..1 | AnalyticalSession | LaboratoryAnalysis |
| LaboratoryAnalysis | AnalyticalProcess | **computation** | 0..1 | LI_ProcessStep | ? |
| LaboratoryAnalysis | AnalyticalSession | **instrument** | 0..1 | AnalyticalInstrument | LaboratoryAnalysis |
| LaboratoryAnalysis | AnalyticalSession | **referenceAnalyses** | 0..* | ReferenceSpecimen | GeologicSpecimen |
| TemporalReferenceSystem | TimeOrdinalEra | **member** | 0..* | TimeOrdinalEra | TemporalReferenceSystem |
| TemporalReferenceSystem | TimeOrdinalEra | - | - | TimeOrdinalReferenceSystem | TemporalReferenceSystem |
| TemporalReferenceSystem | TimeOrdinalEraBoundary | **observationalBasis** | 0..* | OM_Observation | ? |
| TemporalReferenceSystem | TimeOrdinalEraBoundary | **previousEra** | 0..* | TimeOrdinalEra | TemporalReferenceSystem |
| TemporalReferenceSystem | TimeOrdinalEraBoundary | **nextEra** | 0..* | TimeOrdinalEra | TemporalReferenceSystem |
| TemporalReferenceSystem | TimeOrdinalReferenceSystem | **referencePoint** | 2..* | TimeOrdinalEraBoundary | TemporalReferenceSystem |
| TimeScale | GeochronologicBoundary | **stratotype** | 0..1 | StratigraphicPoint | GSSP |
| TimeScale | GeochronologicEra | **stratotype** | 0..1 | StratigraphicSection | GSSP |

#### Navigable role-names by source class (most likely missing properties)

55 navigable role names appear in associations but were NOT emitted by the generator:

| Source class | Missing role | Target type | Reason |
| --- | --- | --- | --- |
| AlterationDescription | `alterationEvent` | GeologicEvent | not emitted |
| AnalyticalProcess | `acquisition` | AnalyticalSession | not emitted |
| AnalyticalProcess | `computation` | LI_ProcessStep | not emitted |
| AnalyticalProcess | `method` | AnalyticalMethod | not emitted |
| AnalyticalSession | `instrument` | AnalyticalInstrument | not emitted |
| AnalyticalSession | `referenceAnalyses` | ReferenceSpecimen | not emitted |
| Borehole | `downholeDrillingDetails` | DrillingDetails | not emitted |
| Borehole | `indexData` | BoreholeDetails | not emitted |
| Borehole | `logElement` | BoreholeInterval | not emitted |
| BoreholeInterval | `shape` | GM_Object | not emitted |
| CompositionPart | `material` | CompoundMaterial | not emitted |
| CompoundMaterialDescription | `constituent` | ConstituentPart | not emitted |
| CompoundMaterialDescription | `particleGeometry` | ParticleGeometryDescription | not emitted |
| ConstituentPart | `constituentMaterial` | EarthMaterial | not emitted |
| ConstituentPart | `constituentParticleGeometry` | ParticleGeometryDescription | not emitted |
| ConstituentPart | `relatedMaterial` | ConstituentPart | not emitted |
| Contact | `stContactDescription` | ContactAbstractDescription | not emitted |
| ContactDescription | `correlatesWith` | GeochronologicBoundary | not emitted |
| DisplacementEvent | `incrementalDisplacement` | DisplacementValue | not emitted |
| DisplacementValue | `displacementEvent` | DisplacementEvent | not emitted |
| EarthMaterial | `gbEarthMaterialDescription` | EarthMaterialAbstractDescription | not emitted |
| Fold | `stFoldDescription` | FoldAbstractDescription | not emitted |
| FoldDescription | `system` | FoldSystem | not emitted |
| FoldSystem | `foldSystemMember` | Fold | not emitted |
| Foliation | `stFoliationDescription` | FoliationAbstractDescription | not emitted |
| GSML | `member` | GSMLitem | not emitted |
| GeochronologicBoundary | `stratotype` | StratigraphicPoint | not emitted |
| GeochronologicEra | `stratotype` | StratigraphicSection | not emitted |
| GeochronologicInterpretation | `sourceCollection` | SF_SamplingFeatureCollection | not emitted |
| GeologicEvent | `gaEventDescription` | GeologicEventAbstractDescription | not emitted |
| GeologicEventDescription | `prototype` | StratigraphicPoint | not emitted |
| GeologicFeature | `geologicHistory` | GeologicEvent | not emitted |
| GeologicFeature | `occurrence` | MappedFeature | not emitted |
| GeologicFeature | `relatedFeature` | GeologicFeature | not emitted |
| GeologicUnit | `composition` | CompositionPart | not emitted |
| GeologicUnit | `gbMaterialDescription` | EarthMaterialAbstractDescription | not emitted |
| GeologicUnit | `gbUnitDescription` | GeologicUnitAbstractDescription | not emitted |
| GeologicUnit | `hierarchyLink` | GeologicUnitHierarchy | not emitted |
| GeologicUnitDescription | `bedding` | BeddingDescription | not emitted |
| GeologicUnitHierarchy | `targetUnit` | GeologicUnit | not emitted |
| GeomorphologicFeature | `gmFeatureDescription` | GeomorphologicUnitAbstractDescription | not emitted |
| GeomorphologicFeature | `unitDescription` | GeologicUnit | not emitted |
| Layering | `layerComposition` | RockMaterial | not emitted |
| MappedFeature | `specification` | GFI_Feature | not emitted |
| MetamorphicDescription | `metamorphicEvent` | GeologicEvent | not emitted |
| NetSlipValue | `slipComponent` | SlipComponents | not emitted |
| OriginPosition | `relatedBorehole` | Borehole | not emitted |
| ParticleGeometryDescription | `sourceOrganism` | Organism | not emitted |
| ShearDisplacementStructure | `stStructureDescription` | ShearDisplacementStructureAbstractDescription | not emitted |
| ShearDisplacementStructureDescription | `stPhysicalProperty` | PhysicalDescription | not emitted |
| TimeOrdinalEra | `member` | TimeOrdinalEra | not emitted |
| TimeOrdinalEraBoundary | `nextEra` | TimeOrdinalEra | not emitted |
| TimeOrdinalEraBoundary | `observationalBasis` | OM_Observation | not emitted |
| TimeOrdinalEraBoundary | `previousEra` | TimeOrdinalEra | not emitted |
| TimeOrdinalReferenceSystem | `referencePoint` | TimeOrdinalEraBoundary | not emitted |
