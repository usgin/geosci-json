# gsmBorehole

GeoSciML 4.1 building block `gsmBorehole`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `Borehole`.

Contains 3 feature types, 3 data types, 4 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `Borehole` | «FeatureType» | JSON-FG Feature |
| `BoreholeDetails` | «DataType» | plain JSON object |
| `BoreholeDrillingMethodCode` | «CodeList» | URI codelist (`format: uri`) |
| `BoreholeInclinationCode` | «CodeList» | URI codelist (`format: uri`) |
| `BoreholeInterval` | «FeatureType» | JSON-FG Feature |
| `BoreholePurposeCode` | «CodeList» | URI codelist (`format: uri`) |
| `BoreholeStartPointCode` | «CodeList» | URI codelist (`format: uri`) |
| `DrillingDetails` | «DataType» | plain JSON object |
| `OriginPosition` | «FeatureType» | JSON-FG Feature |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `Borehole`

A Borehole is the generalized term for any narrow shaft drilled in the ground, either vertically, horizontally, or inclined.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `logElement` | (oneOf - see schema) | 0..1 | The property logElement is an association between a Borehole and a BoreholeInterval instance to describe measured dow… |
| `downholeDrillingDetails` | (oneOf - see schema) | 0..1 | The property downholeDrillingDetails:DrillingDetails specifies the drilling method and borehole diameter for interval… |
| `referenceLocation` | (oneOf - see schema) | 0..1 | The property referenceLocation is an association between a Borehole and an OriginPosition corresponding to the start … |
| `indexData` | (oneOf - see schema) | 0..1 | The property indexData:BoreholeDetails describes metadata about a borehole, such as the operator, the custodian, date… |

### `BoreholeDetails`

BoreholeDetails describes borehole-specific index data, often termed “header information”. It contains metadata about the parties involved in the drilling, the storage of drilled material and other information relevant to the borehole as a whole. Properties that may vary along the borehole path are managed in DrillingDetails

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `operator` | (oneOf - see schema) | 0..1 | The operator property is an association between a BoreholeDetails and a CIT:CI_ResponsibleParty describing the organi… |
| `driller` | (oneOf - see schema) | 0..1 | The driller property is an association between a BoreholeDetails and a CIT:CI_ResponsibleParty describing of the orga… |
| `dateOfDrilling` | (oneOf - see schema) | 0..1 | The property dateOfDrilling:TM_Period describes the time period during which drilling of the borehole occurred. |
| `startPoint` | (oneOf - see schema) | 0..1 | The property startPoint:BoreholeStartPointCode provides a term from a controlled vocabulary indicating the named posi… |
| `inclinationType` | (oneOf - see schema) | 0..1 | The property inclinationType:BoreholeInclinationCode contains a term from a controlled vocabulary indicating the incl… |
| `boreholeMaterialCustodian` | (oneOf - see schema) | 0..1 | The property boreholeMaterialCustodian is an association between BoreholeDetails and a CIT:CI_ResponsibleParty descri… |
| `purpose` | (oneOf - see schema) | 0..1 | The property purpose:BoreholePurposeCode contains a term from a controlled vocabulary describing the purpose for whic… |
| `dataCustodian` | (oneOf - see schema) | 0..1 | The dataCustodian is an association between a BoreholeDetails and a CIT:CI_ResponsibleParty describing the custodian … |
| `boreholeLength` | (oneOf - see schema) | 0..1 | The property boreholeLength (SWE::Quantity) contains a measurement (a value and a unit of measurement) corresponding … |

### `BoreholeInterval`

A BoreholeInterval is similar to a MappedFeature whose shape is 1-D interval and uses the SRS of the containing borehole. The "mappedIntervalBegin" and "mappedIntervalEnd" properties are alternative to the 1D geometry to overcome problems with the delivery and ease of queryability of 1D GML shapes.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `observationMethod` | (oneOf - see schema) | 0..1 | The observationMethod property (SWE::Category) contains a term from a controlled vocabulary that describes the method… |
| `specification` | (oneOf - see schema) | 0..1 | The specification property is an association between a BoreholeInterval and a GFI_Feature, a domain feature that is s… |
| `mappedIntervalBegin` | (oneOf - see schema) | 0..1 | The property mappedIntervalBegin (SWE::Quantity) is a measurement (a value and a unit of measurement) corresponding t… |
| `mappedIntervalEnd` | (oneOf - see schema) | 0..1 | The mappedIntervalEnd property (SWE::Quantity) is a measurement (a value and a unit of measure) corresponding to the … |
| `collectionIdentifier` | (oneOf - see schema) | 0..1 | The collectionIdentifier:ScopedName is a string unique within a scope that identifies a collection which forms a set … |
| `shape` | (oneOf - see schema) | 0..1 | The property shape:GM_Object is a 1-D interval (e.g., a "from" and "to", or "top" and "base" measurement) covering th… |
| `parentBorehole` | (oneOf - see schema) | 0..1 | The property parentBorehole is an association between a BoreholeInterval and a Borehole to which the interval belongs. |

### `DrillingDetails`

DrillingDetails is a class that captures the description of drilling methods and hole diameters down the drilling path. Properties that apply to the Borehole as a whole are managed in BoreholeDetails.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `drillingMethod` | (oneOf - see schema) | 0..1 | The drillingMethod:BoreholeDrillingMethodCode property contains a term from a controlled vocabulary indicating the dr… |
| `boreholeDiameter` | (oneOf - see schema) | 0..1 | The boreholeDiameter property (SWE::Quantity) contains a measurement (a value and a unit of measure) corresponding to… |
| `intervalBegin` | (oneOf - see schema) | 0..1 | The intervalBegin property (SWE::Quantity) contains a measurement (a value and a unit of measurement) that correspond… |
| `intervalEnd` | (oneOf - see schema) | 0..1 | The property intervalEnd (SWE::Quantity) contains a measurement (a value and a unit of measurement) of the measured d… |

### `OriginPosition`

A borehole OriginPosition is a feature corresponding to the start point of a borehole log. This may correspond to the borehole collar location (e.g., kelly bush).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `location` | (oneOf - see schema) | 0..1 | The property location contains a geometry corresponding to the location of the borehole collar. |
| `elevation` | (oneOf - see schema) | 0..1 | The elevation:DirectPosition property is a compromise approach to supply elevation explicitly for location; this is t… |
| `relatedBorehole` | (oneOf - see schema) | 0..1 | The hole that has this collar for its start point |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `BoreholeDrillingMethodCode` | `_(treat as open - no `codeList` annotation)_` |
| `BoreholeInclinationCode` | `_(treat as open - no `codeList` annotation)_` |
| `BoreholePurposeCode` | `_(treat as open - no `codeList` annotation)_` |
| `BoreholeStartPointCode` | `_(treat as open - no `codeList` annotation)_` |

## External dependencies

- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.json`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.json`
- `https://geojson.org/schema/Geometry.json`
- `https://geojson.org/schema/Point.json`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [borehole_complex.json](examples/borehole_complex.json)
- [borehole_simple.json](examples/borehole_simple.json)
- [examplegsmBoreholeMinimal.json](examples/examplegsmBoreholeMinimal.json)
- [origin_position_simple.json](examples/origin_position_simple.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `Borehole`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
