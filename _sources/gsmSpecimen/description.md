# gsmSpecimen

GeoSciML 4.1 building block `gsmSpecimen`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `LaboratoryAnalysis-Specimen`, `Geochronology`, `GeologicSpecimen`, `LaboratoryAnalysis`.

Contains 7 feature types, 2 data types, 7 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AnalyticalInstrument` | «FeatureType» | JSON-FG Feature |
| `AnalyticalMethod` | «DataType» | plain JSON object |
| `AnalyticalMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `AnalyticalProcess` | «FeatureType» | JSON-FG Feature |
| `AnalyticalSession` | «FeatureType» | JSON-FG Feature |
| `GeochronologicInterpretation` | «FeatureType» | JSON-FG Feature |
| `GeologicSamplingMethod` | «FeatureType» | JSON-FG Feature |
| `GeologicSamplingMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicSpecimenPreparation` | «DataType» | plain JSON object |
| `GeologicSpecimenPreparationTerm` | «CodeList» | URI codelist (`format: uri`) |
| `Image` | «FeatureType» | JSON-FG Feature |
| `InstrumentTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `IsotopicEventType` | «CodeList» | URI codelist (`format: uri`) |
| `IsotopicSystemName` | «CodeList» | URI codelist (`format: uri`) |
| `ReferenceSpecimen` | «FeatureType» | JSON-FG Feature |
| `StatisticalMethodTerm` | «CodeList» | URI codelist (`format: uri`) |

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

### `GeochronologicInterpretation`

A GeochronologicInterpretation is an interpretation made by a geologist of the age of a specimen made by statistical analysis of a collection of observations. A geologic specimen may have multiple geochronological interpretations made on it, each related to a different observation/result collection.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `interpretedAge` | (oneOf — see schema) | 0..1 | The interpretedAge property is an association between a GeochronologicInterpretation and a GeologicEvent that describ… |
| `isotopicEvent` | (oneOf — see schema) | 0..1 | The isotopicEvent:IsotopicEventType contains a term from a controlled vocabulary that describes any isotopic events t… |
| `isotopicSystem` | (oneOf — see schema) | 0..1 | The property isotopicSystem:IsotopicSystemName contains a term from a controlled vocabulary that describes the isotop… |
| `statisticalMethod` | (oneOf — see schema) | 0..1 | The property statisticalMethod:StatisticalMethodTerm contains a term from a controlled vocabulary that describes the … |
| `interpretedBy` | (oneOf — see schema) | 0..1 | The property interpretedBy is an association between a GeochronologicInterpretation and a CIT:CI_Responsability descr… |
| `citation` | (oneOf — see schema) | 0..1 | The citation property is an association between a GeochronologicInterpretation and a CIT:CI_Citation that describes a… |
| `preferredInterpretation` | (oneOf — see schema) | 0..1 | The property preferredInterpretation:Primitive::Boolean indicates whether this interpretation is the preferred interp… |
| `sourceCollection` | (oneOf — see schema) | 0..1 | The property sourceCollection is an association between a GeochronologicInterpretation and an OM::SF_SamplingFeatureC… |

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

### `Image`

The Image feature type is used to describe images of sampling features, for example, photographs of ion microprobe grain mounts.

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
| `AnalyticalMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicSamplingMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicSpecimenPreparationTerm` | `_(treat as open — no `codeList` annotation)_` |
| `InstrumentTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `IsotopicEventType` | `_(treat as open — no `codeList` annotation)_` |
| `IsotopicSystemName` | `_(treat as open — no `codeList` annotation)_` |
| `StatisticalMethodTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../gsmscimlBasic/gsmscimlBasicSchema.json#GeologicEvent`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json`
- `https://schemas.opengis.net/json-fg/feature.json`

## Examples

- [examplegsmSpecimenMinimal.json](examplegsmSpecimenMinimal.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `LaboratoryAnalysis-Specimen`, `Geochronology`, `GeologicSpecimen`, `LaboratoryAnalysis`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
