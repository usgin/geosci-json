# GeoSciML LaboratoryAnalysis

JSON Schema building block for the `LaboratoryAnalysis` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 4 feature types, 1 data type, 2 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AnalyticalInstrument` | «FeatureType» | JSON-FG Feature |
| `AnalyticalMethod` | «DataType» | plain JSON object |
| `AnalyticalMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `AnalyticalProcess` | «FeatureType» | JSON-FG Feature |
| `AnalyticalSession` | «FeatureType» | JSON-FG Feature |
| `Image` | «FeatureType» | JSON-FG Feature |
| `InstrumentTypeTerm` | «CodeList» | URI codelist (`format: uri`) |

## Class details

### `AnalyticalInstrument`

The analytical instrument is the category of instrument used to perform an analytical measurement or observation.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `type` | (oneOf — see schema) | 0..1 | The property type:InstrumentTypeTerm reports a term from a controlled vocabulary that describes the category of instr… |
| `model` | (oneOf — see schema) | 0..1 | The property mode:Primitive::CharacterString contains a string identifying the model of instrument used. (e.g., instr… |
| `serialNumber` | (oneOf — see schema) | 0..1 | The property serialNumber:Primitive::CharacterString contains a string that contains the serial number of the machine… |
| `commissionDate` | (oneOf — see schema) | 0..1 | The property commissionDate is an association between an AnalyticalInstrument and a TM_Instant corresponding to the d… |
| `location` | (oneOf — see schema) | 0..1 | The property location is an association between an AnalyticalInstrument and a CIT:Responsibility describing the owner… |
| `usedIn` | (oneOf — see schema) | 0..1 | The property usedIn is an association between an AnalyticalInstrument and an AnalyticalSession identifying an analyti… |

### `AnalyticalMethod`

The AnalyticalMethod provides the name, and published citation, of the analytical method used in an analytical session.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `methodName` | (oneOf — see schema) | 0..1 | The property methodName:AnalyticalMethodTerm contains a term from a controlled vocabulary that describes an analytica… |
| `citation` | (oneOf — see schema) | 0..1 | The citation property is an association between an AnalyticalMethod and a CIT:CI_Citation describing a published desc… |

### `AnalyticalProcess`

An analytical process is a concrete implementation of OM::OM_Process and describes the steps and methods used in an analytical session. It links to an analytical session (data acquisition) or a computational process which produce analytical results.  Constraint: Only for use with OM_Observation/procedure

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `method` | (oneOf — see schema) | 0..1 | The property method is an association that links an AnalyticalProcess to an AnalyticalMethod that describes the type … |
| `computation` | (oneOf — see schema) | 0..1 | The computation property is an association between an AnalyticalProcess and a CIT:ProcessStep that describes the comp… |
| `acquisition` | (oneOf — see schema) | 0..1 | The property acquisition is an association that links an AnalyticalProcess to an AnalyticalSession that describes the… |

### `AnalyticalSession`

This feature type describes the time and operator of a particular laboratory analytical session. AnalyticalSession also has associated links to the type of instrument and analytical method used, processing steps applied to data collected during a session, and instrument parameters unique to that session.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `time` | (oneOf — see schema) | 0..1 | The property time is an association between an AnalyticalSession and a TM_Period describing the time period during wh… |
| `operator` | (oneOf — see schema) | 0..1 | The property operator is an association between an AnalyticalSession and a CIT:CI_Responsability describing the opera… |
| `parameter` | (oneOf — see schema) | 0..1 | The property parameter (OM::NamedValue) contains a name/value pair to describe arbitrary environmental or instrument … |
| `instrument` | (oneOf — see schema) | 0..1 | The property instrument is an association between an AnalyticalSession and an AnalyticalInstrument that describes the… |
| `referenceAnalyses` | (oneOf — see schema) | 0..1 | The property referenceAnalysis is an association between an AnalyticalSession and a ReferenceSpecimen that describes … |

### `Image`

The Image feature type is used to describe images of sampling features, for example, photographs of ion microprobe grain mounts.

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `AnalyticalMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `InstrumentTypeTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `https://schemas.opengis.net/json-fg/feature.json`

## Examples

- [Minimal](examples/exampleLaboratoryAnalysisMinimal.json) — bare valid instance.
- [Complete](examples/exampleLaboratoryAnalysisComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `LaboratoryAnalysis`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
