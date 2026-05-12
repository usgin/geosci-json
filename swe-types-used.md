# SWE Common types referenced by GeoSciML 4.1

## Scope

This document inventories the **SWE Common 2.0** types referenced by the GeoSciML 4.1 application schema, and maps them to the **SWE Common 3.0 JSON** schemas published at `https://schemas.opengis.net/sweCommon/3.0/json/`. It is the input to a decision about whether `geosci-json` can substitute SWE 3.0 JSON Schema definitions for SWE 2.0 UML types when generating the GeoSciML JSON encoding.

Sources analyzed:

- `geosciml4.1.xmi` (29,670 lines, EA export of GeoSciML v4.1)
- `SWECommon2.0.xmi` (the package GeoSciML imports — referenced but not deeply analyzed here)
- `https://schemas.opengis.net/sweCommon/3.0/json/` (directory listing fetched 2026-05-11)

## SWE Common 2.0 types referenced by GeoSciML 4.1

Four distinct SWE Common 2.0 types are used as attribute value types across 64 attributes in the GeoSciML model:

| SWE 2.0 type | # attrs | Conceptual role |
| --- | ---: | --- |
| `Category` | 35 | Term from a controlled vocabulary |
| `Quantity` | 14 | Single numeric measurement with units |
| `QuantityRange` | 14 | Numeric range (lower, upper) with units |
| `DataRecord` | 1 | Heterogeneous structured record |

Two attributes are typed `Boolean`, but their descriptions reference `Primitive::Boolean` — they are **ISO 19103 Boolean primitives**, not SWE Common Boolean components. They should map to JSON `boolean` per OGC 24-017r1 Table 4 and are excluded from the SWE substitution discussion.

### Full attribute inventory

| GeoSciML class | Attribute | SWE 2.0 type |
| --- | --- | --- |
| AlterationDescription | alterationDegree | Category |
| AlterationDescription | alterationDistribution | Category |
| BeddingDescription | beddingPattern | Category |
| BeddingDescription | beddingStyle | Category |
| BeddingDescription | beddingThickness | Category |
| BoreholeDetails | boreholeLength | Quantity |
| BoreholeInterval | mappedIntervalBegin | Quantity |
| BoreholeInterval | mappedIntervalEnd | Quantity |
| BoreholeInterval | observationMethod | Category |
| ChemicalComposition | chemicalAnalysis | DataRecord |
| CompositionPart | proportion | QuantityRange |
| CompoundMaterialDescription | compositionCategory | Category |
| CompoundMaterialDescription | geneticCategory | Category |
| ConstituentPart | proportion | QuantityRange |
| ContactDescription | contactCharacter | Category |
| DrillingDetails | boreholeDiameter | Quantity |
| DrillingDetails | intervalBegin | Quantity |
| DrillingDetails | intervalEnd | Quantity |
| EarthMaterial | color | Category |
| FoldDescription | amplitude | QuantityRange |
| FoldDescription | geneticModel | Category |
| FoldDescription | hingeLineCurvature | Category |
| FoldDescription | hingeShape | Category |
| FoldDescription | interLimbAngle | Category |
| FoldDescription | limbShape | Category |
| FoldDescription | span | QuantityRange |
| FoldDescription | symmetry | Category |
| FoldSystem | wavelength | QuantityRange |
| FoliationDescription | continuity | Category |
| FoliationDescription | definingElement | Category |
| FoliationDescription | intensity | Category |
| FoliationDescription | spacing | QuantityRange |
| GSML_LinearOrientation | plunge | QuantityRange |
| GSML_LinearOrientation | trend | QuantityRange |
| GSML_PlanarOrientation | azimuth | QuantityRange |
| GSML_PlanarOrientation | dip | QuantityRange |
| GSML_Vector | magnitude | QuantityRange |
| GeologicEvent | eventEnvironment | Category |
| GeologicFeature | classifier | Category |
| GeologicFeature | observationMethod | Category |
| GeologicUnitDescription | bodyMorphology | Category |
| GeologicUnitDescription | outcropCharacter | Category |
| GeologicUnitDescription | unitComposition | Category |
| GeologicUnitDescription | unitThickness | QuantityRange |
| GeologicUnitHierarchy | proportion | QuantityRange |
| Lineation | definingElement | Category |
| Lineation | intensity | Category |
| MappedFeature | observationMethod | Category |
| MappedFeature | positionalAccuracy | Quantity |
| MetamorphicDescription | metamorphicFacies | Category |
| MetamorphicDescription | metamorphicGrade | Category |
| MetamorphicDescription | peakPressureValue | Quantity |
| MetamorphicDescription | peakTemperatureValue | Quantity |
| NaturalGeomorphologicFeature | activity | Category |
| NumericAgeRange | olderBoundDate | Quantity |
| NumericAgeRange | reportingDate | Quantity |
| NumericAgeRange | youngerBoundDate | Quantity |
| ParticleGeometryDescription | aspectRatio | Category |
| ParticleGeometryDescription | shape | Category |
| ParticleGeometryDescription | size | QuantityRange |
| ParticleGeometryDescription | sorting | Category |
| PhysicalDescription | propertyMeasure | Quantity |
| RockMaterialDescription | consolidationDegree | Category |
| TimeOrdinalEraBoundary | positionalUncertainty | Quantity |

## SWE Common 3.0 JSON schemas published

Twenty-three JSON Schema files are published at `https://schemas.opengis.net/sweCommon/3.0/json/`:

| Filename | Component type |
| --- | --- |
| AbstractDataComponent.json | Base class for data components |
| AbstractSimpleComponent.json | Base class for simple components |
| AbstractSweIdentifiable.json | Base class for identifiable SWE objects |
| Boolean.json | Boolean SWE component |
| Category.json | Categorical value |
| CategoryRange.json | Range of categorical values |
| Count.json | Integer count |
| CountRange.json | Range of count values |
| DataArray.json | Array-structured data |
| DataChoice.json | Choice among multiple data options |
| DataRecord.json | Structured record of mixed data types |
| DataStream.json | Streaming data |
| Geometry.json | Geometric data |
| Matrix.json | Matrix data |
| Quantity.json | Numerical quantity with units |
| QuantityRange.json | Range of quantity values |
| Text.json | Text string |
| Time.json | Temporal data |
| TimeRange.json | Range of time values |
| Vector.json | Vector data |
| basicTypes.json | Foundational type definitions |
| encodings.json | Data encoding specifications |
| sweCommon.json | Aggregate file |

## Encoding decisions

| SWE 2.0 type | # attrs | Encoding policy |
| --- | ---: | --- |
| Category | 35 | **OGC codelist encoding** (not SWE 3.0 Category). See [Category encoding policy](#category-encoding-policy) below. |
| Quantity | 14 | `$ref` to `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json` |
| QuantityRange | 14 | `$ref` to `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json` |
| DataRecord | 1 | `$ref` to `https://schemas.opengis.net/sweCommon/3.0/json/DataRecord.json` — generic SWE 3.0 DataRecord (decided 2026-05-11) |

## SWE 2.0 → 3.0 member diffs

The SWE 2.0 class hierarchy (extracted from `SWECommon2.0.xmi`):

```
AbstractSWE
  extension : Any [0..*]
└── AbstractSWEIdentifiable
      identifier  : ScopedName       [0..1]
      label       : CharacterString  [0..1]
      description : CharacterString  [0..1]
    └── AbstractDataComponent
          definition : ScopedName [0..1]
          optional   : Boolean    [0..1]
          updatable  : Boolean    [0..1]
        ├── AbstractSimpleComponent
        │     referenceFrame : SC_CRS         [0..1]
        │     axisID         : CharacterString [0..1]
        │     quality        : Quality         [0..*]
        │     nilValues      : NilValues       [0..1]
        │   ├── Category, Quantity, QuantityRange, ...
        └── DataRecord
              field : AbstractDataComponent [1..*]
```

Cross-cutting changes 2.0 → 3.0 (verified against `AbstractSweIdentifiable.json`, `AbstractDataComponent.json`, `AbstractSimpleComponent.json`, and `basicTypes.json`):

- **`type` discriminator added.** Every concrete component now has a required `type` string with a `const` equal to the class name (e.g., `"type": "Quantity"`). This was implicit (via XML element name) in SWE 2.0 XML; in JSON it must be explicit.
- **`definition` and `label` are optional in inheritance but required on concrete schemas.** Both `AbstractSweIdentifiable.label` and `AbstractDataComponent.definition` are declared optional. Each concrete component (Category, Quantity, QuantityRange, ...) re-declares them in its own `required` array. Net effect at the JSON surface: producers must supply them.
- **`uom` reference type renamed**: 2.0 `UnitOfMeasure` → 3.0 `UnitReference`. The 3.0 `UnitReference` accepts either a UCUM code or a URI, with optional label and symbol.
- **`nilValues` specialized by data domain.** 2.0 had a generic `NilValues` aggregate; 3.0 splits into `NilValuesText`, `NilValuesNumber`, `NilValuesInteger`, `NilValuesTime`, chosen per simple-component type. Each `NilValues*` is an array of `{value, reason: uri}` entries.
- **Three members dropped between 2.0 and 3.0:**
  - `extension : Any [0..*]` from `AbstractSWE` — gone.
  - `identifier : ScopedName [0..1]` from `AbstractSWEIdentifiable` — gone. (The 3.0 `AbstractSWE.id` is a JSON-pointer-style fragment identifier, not a real-world identifier.)
  - `quality : Quality [0..*]` from `AbstractSimpleComponent` — gone.
  None of the three are referenced by GeoSciML attributes; acceptable loss for this project.
- **`optional` and `updatable` retained** on `AbstractDataComponent` (both boolean, default `false`).

### Category — 2.0 vs 3.0

| Member | SWE 2.0 | SWE 3.0 | Notes |
| --- | --- | --- | --- |
| `type` | (implicit element name) | **required**, `const: "Category"` | Added in 3.0 |
| `definition` | inherited, optional | **required** | Tightened |
| `label` | inherited, optional | **required** | Tightened |
| `codeSpace` | `Dictionary` [0..1] | `string` `format: uri` [0..1] | Type narrowed to URI string |
| `constraint` | `AllowedTokens` [0..1] | `AllowedTokens` [0..1] | Unchanged |
| `nilValues` | inherited `NilValues` [0..1] | `NilValuesText` [0..1] | Specialized for text |
| `value` | `CharacterString` [0..1] | `string` [0..1] | Unchanged at JSON level |
| `identifier` | inherited [0..1] | **dropped** | Removed from 3.0 |
| `description` | inherited [0..1] | inherited, optional, minLength 1 | Unchanged |

**Not used.** Per the policy above, GeoSciML Category attributes are not encoded as SWE 3.0 Category. This diff is retained for completeness.

### Quantity — 2.0 vs 3.0

| Member | SWE 2.0 | SWE 3.0 | Notes |
| --- | --- | --- | --- |
| `type` | (implicit) | **required**, `const: "Quantity"` | Added |
| `definition` | inherited, optional | **required** | Tightened |
| `label` | inherited, optional | **required** | Tightened |
| `uom` | `UnitOfMeasure` [1..1] | `UnitReference` [1..1] | Reference type renamed |
| `constraint` | `AllowedValues` [0..1] | `AllowedValues` [0..1] | Unchanged |
| `nilValues` | inherited `NilValues` [0..1] | `NilValuesNumber` [0..1] | Specialized for numeric |
| `value` | `Real` [0..1] | `NumberOrSpecial` [0..1] | Widened to allow nil-token literals alongside numbers |
| `referenceFrame` | inherited [0..1] | inherited, `format: uri-reference`, optional | Unchanged |
| `axisID` | inherited [0..1] | inherited, optional | Unchanged |
| `quality` | inherited [0..*] | **dropped** | Removed from 3.0 |

**Impact on GeoSciML 14 Quantity attributes**: producers must populate `type`, `definition`, `label`, and `uom`. In SWE 2.0 publishers could omit `definition` and `label`; in SWE 3.0 they cannot. If GeoSciML 2.0-era data lacks `definition` / `label` for Quantity-valued properties, those values must be supplied during transformation (e.g., `definition` from a vocabulary URL, `label` from the attribute name).

### QuantityRange — 2.0 vs 3.0

| Member | SWE 2.0 | SWE 3.0 | Notes |
| --- | --- | --- | --- |
| `type` | (implicit) | **required**, `const: "QuantityRange"` | Added |
| `definition` | inherited, optional | **required** | Tightened |
| `label` | inherited, optional | **required** | Tightened |
| `uom` | `UnitOfMeasure` [1..1] | `UnitReference` [1..1] | Renamed |
| `constraint` | `AllowedValues` [0..1] | `AllowedValues` [0..1] | Unchanged |
| `nilValues` | inherited `NilValues` [0..1] | `NilValuesNumber` [0..1] | Specialized |
| `value` | `RealPair` [0..1] (object) | `array` [0..1] of `NumberOrSpecial`, `minItems: 2, maxItems: 2` | **Structure change**: pair object → 2-element array |

**Impact on GeoSciML 14 QuantityRange attributes** (e.g., `FoldDescription.amplitude`, `GSML_PlanarOrientation.dip`): the value goes from `{lowerValue, upperValue}` (or similar 2.0 pair members) to `[low, high]` as a JSON array. Range-rendering UI and instance generators must be adjusted.

### DataRecord — 2.0 vs 3.0

| Member | SWE 2.0 | SWE 3.0 | Notes |
| --- | --- | --- | --- |
| `type` | (implicit) | **required**, `const: "DataRecord"` | Added |
| `field` → `fields` | `field : AbstractDataComponent [1..*]` | `fields : array [minItems: 1]` of `(SoftNamedProperty + AnyComponent)` items | **Member rename** plus item structure change |
| `definition` | inherited [0..1] | inherited, `format: uri`, optional | Unchanged |
| `optional` | inherited [0..1] | inherited, default `false` | Unchanged |
| `updatable` | inherited [0..1] | inherited, default `false` | Unchanged |

**Impact on GeoSciML `ChemicalComposition.chemicalAnalysis`**: any consumer expecting `field` must read `fields`; each field item is a name-component pair rather than just an `AbstractDataComponent`.

### Inheritance chain verified

The four abstract / shared schemas were fetched and inspected on 2026-05-11:

```
basicTypes.json#/$defs/AbstractSWE
  id : string (optional, minLength 1) — JSON-pointer-style fragment identifier only
└── AbstractSweIdentifiable.json  (allOf AbstractSWE)
      label       : string  optional, minLength 1
      description : string  optional, minLength 1
    └── AbstractDataComponent.json  (allOf AbstractSweIdentifiable)
          type       : string  optional at this level (each concrete schema adds a `const` and requires it)
          updatable  : boolean optional, default false
          optional   : boolean optional, default false
          definition : string  optional, format uri
        ├── AbstractSimpleComponent.json  (allOf AbstractDataComponent)
        │     referenceFrame : string optional, format uri-reference
        │     axisID         : string optional, minLength 1
        │     nilValues      : (typed per concrete: NilValuesText / NilValuesNumber / ...)
        │     constraint     : (typed per concrete: AllowedTokens / AllowedValues / ...)
        │     value          : (typed per concrete)
        │   └── Category / Quantity / QuantityRange / Boolean / Count / Text / Time / ...
        └── DataRecord  (allOf AbstractDataComponent)
              fields : array minItems:1 of (SoftNamedProperty + AnyComponent)
```

`basicTypes.json` definitions used by the four GeoSciML-relevant concrete schemas:

- `UnitReference` — either a UCUM `code` or a `href` URI; optional `label` and `symbol`.
- `AllowedTokens` — enumeration of strings or regex `pattern`.
- `AllowedValues` — enumeration of numbers, inclusive ranges, or significant-figure spec.
- `NumberOrSpecial` — number, or one of `"NaN"`, `"Infinity"`, `"+Infinity"`, `"-Infinity"`.
- `NilValuesText` / `NilValuesNumber` — array of `{value, reason: uri}`.
- `SoftNamedProperty` — object with required `name` matching `^[A-Za-z][A-Za-z0-9_\-]*$`.
- `AssociationAttributeGroup` — object with required `href` URI-reference and optional `role`, `arcrole`, `title`.

## Category encoding policy

**Final decision (revised 2026-05-12):** the 35 GeoSciML `SWE::Category`-typed attributes are encoded as `$ref` to **SWE 3.0 `Category.json`**, matching the OGC code-sprint draft (`geoscimlBasic.json` / `geoscimlLite.json`).

JSON Schema shape (for a Category property on a class):

```json
"eventEnvironment": {
  "oneOf": [
    {"type": "null"},
    {
      "type": "array",
      "items": {"$ref": "https://schemas.opengis.net/sweCommon/3.0/json/Category.json"},
      "uniqueItems": true
    }
  ]
}
```

JSON instance shape — each value is a SWE 3.0 Category object:

```json
"eventEnvironment": [
  {
    "type": "Category",
    "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
    "label": "deep crustal",
    "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
    "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/deep-crustal"
  }
]
```

The vocabulary URL travels in the instance via `definition`/`codeSpace`; there is no schema-level binding. This is more flexible than the original codelist-URI encoding (any vocabulary can be used per instance) and matches the OGC code-sprint convention.

**Historical record:** an earlier draft of this repo used the OGC 24-017r1 codelist-URI encoding (`{type: string, format: uri, codeList: <vocab URL>}`) for Category attributes. That was superseded after the OGC code sprint published its draft, which uses SWE 3.0 Category. We followed.

### CodeList classes — `codeList` annotation

For `«CodeList»` classes (e.g. `EventProcessTerm`, `LithologyTerm`), the OGC 24-017r1 spec says emit `codeList: <vocab URL>` on the class definition **when the UML class carries an explicit `codeList` tagged value**. GeoSciML 4.1's XMI carries **zero** such tags — verified by scan of all class-level tagged values. So our generator emits plain `{type: string, format: uri}` for every CodeList class, matching the OGC code-sprint draft's default behavior.

If the source UML is later enriched with `codeList` tags, the generator will emit the annotation automatically (mechanism is implemented, dormant for now).

### `cgi-vocab-reference.yaml`

The companion `cgi-vocab-reference.yaml` records inferred CGI vocabulary URLs for the 35 Category attributes and 47 CodeList classes. It is **documentation only** — the schema generator does not read it. Useful as a starting point if you want to add `codeList` UML tags later, or build a vocabulary-binding profile externally.

## Open items and caveats

1. **`uom` policy.** GeoSciML 2.0-era data used UCUM unit codes via `UnitOfMeasure`. SWE 3.0 `UnitReference` accepts either a UCUM `code` or a URI `href`; producers should default to UCUM. None of the Quantity/QuantityRange attributes carry a `unit` tag in the UML — units are supplied per instance, not fixed per attribute.
2. **`chemicalAnalysis` content** — resolved 2026-05-11: use the generic SWE 3.0 `DataRecord` `$ref`. Field set left to publisher convention. Revisit if a community profile emerges.
3. **Boolean disambiguation.** `FoldSystem.periodic` and `GeochronologicInterpretation.preferredInterpretation` are ISO 19103 `Primitive::Boolean`, not SWE Boolean. They map to JSON `boolean`. No SWE substitution applies.
4. **`SWECommon2.0.xmi` not processed.** Under the substitution approach, the 2.0 XMI is not converted to JSON Schema — only the four type names above are recognized as external types by the generator.
5. **Category attributes → SWE 3.0 `Category.json`** — vocabulary URIs travel in the instance, not the schema. `cgi-vocab-reference.yaml` is reference-only.
6. **Three SWE 2.0 members dropped in 3.0** (`extension`, `identifier`, `quality`) — accepted, none referenced by GeoSciML attributes.

## Recommended next steps

1. ~~Pick the Category codelist sub-option~~ — done: URI encoding.
2. ~~Verify SWE 3.0 abstract supertypes~~ — done: see [Inheritance chain verified](#inheritance-chain-verified).
3. ~~Decide `chemicalAnalysis` encoding~~ — done: generic SWE 3.0 DataRecord ref.
4. ~~Build `cgi-vocab-reference.yaml`~~ — built, now repurposed as documentation only.
5. ~~Build `swe-mappings.yaml`~~ — built; consumed by the generator for the 3 SWE substitutions.
6. ~~Configure / extend the JSON Schema generator~~ — done. Generator emits SWE 3.0 `Category.json` refs for `SWE::Category` attributes; plain `{type: string, format: uri}` for `«CodeList»` classes (with conditional `codeList` annotation when the UML carries the tag).
7. Validate sample instances against the SWE 3.0 schemas — see translated examples under `_sources/geosciml_*/examples/`.
