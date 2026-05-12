# GeoSciML GeologicSpecimen

JSON Schema building block for the `GeologicSpecimen` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 2 feature types, 1 data type, 2 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeologicSamplingMethod` | «FeatureType» | JSON-FG Feature |
| `GeologicSamplingMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicSpecimenPreparation` | «DataType» | plain JSON object |
| `GeologicSpecimenPreparationTerm` | «CodeList» | URI codelist (`format: uri`) |
| `ReferenceSpecimen` | «FeatureType» | JSON-FG Feature |

## Class details

### `GeologicSamplingMethod`

GeologicSamplingMethod is an implementation of OM::SF_Process to describe the method used to obtain a geologic specimen. Examples include: &#x9;diamond drilling &#x9;percussion drilling &#x9;piston core drilling &#x9;vibro core drilling &#x9;channel sampling &#x9;sea floor dredging &#x9;outcrop sampling  Constraint: Only for use with SF_Specimen/samplingMethod

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `method` | (oneOf — see schema) | 0..1 | The property method:GeologicSamplingMethodTerm is a term from a controlled vocabulary that describes the process used… |
| `parameter` | (oneOf — see schema) | 0..1 | The property parameter (OM::NamedValue) contains a name/value pair to describe arbitrary parameters used in the sampl… |

### `GeologicSpecimenPreparation`

GeologicSpecimenPreparation is an extension of ISO Specimen::preparationStep to allow details of preparation steps to be delivered (e.g., filtration and mesh size, chemical additives, crushing methods, drying parameters, etc.).  Constraint: Only for use with SF_Specimen/processingDetails

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `preparationMethod` | (oneOf — see schema) | 0..1 | The preparationMethod:GeologicSpecimenPreparationTerm contains a term from a controlled vocabulary that describes the… |
| `parameter` | (oneOf — see schema) | 0..1 | The property parameter (OM::NamedValue) contains name/value pair to describe arbitrary parameters used in this prepar… |

### `ReferenceSpecimen`

A reference specimen is a specimen with known or accepted values of some property. The citation property describes the location of a published description of these values. Reference specimens include analytical blanks. ReferenceSpecimens are used in quality control procedures to assess method reproducibility. Analytical results from a reference specimen analysed during an AnalyticalSession are delivered in the same way as the results of other specimens analysed in that session.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `referenceDescription` | (oneOf — see schema) | 0..1 | The property referenceDescription is an association between a ReferenceSpecimen and a CIT:CI_Citation that references… |
| `usedIn` | (oneOf — see schema) | 0..1 | The property usedIn is an association between a ReferenceSpecimen and an AnalyticalSession in which the reference spe… |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `GeologicSamplingMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicSpecimenPreparationTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `https://schemas.opengis.net/json-fg/feature.json`

## Examples

- [Minimal](examples/exampleGeologicSpecimenMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeologicSpecimenComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GeologicSpecimen`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
