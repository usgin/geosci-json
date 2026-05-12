# gsmGeologicTime

GeoSciML 4.1 building block `gsmGeologicTime`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeologicTime`, `GSSP`, `TemporalReferenceSystem`, `TimeScale`, `GeologicAgeDetails`.

Contains 4 feature types, 10 data types, 1 code list.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeochronologicBoundary` | «DataType» | plain JSON object |
| `GeochronologicEra` | «DataType» | plain JSON object |
| `GeochronologicEraRank` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicEventDescription` | «DataType» | plain JSON object |
| `GeologicTimescale` | «DataType» | plain JSON object |
| `GlobalStratotypePoint` | «FeatureType» | JSON-FG Feature |
| `GlobalStratotypeSection` | «FeatureType» | JSON-FG Feature |
| `NumericEraBoundary` | «DataType» | plain JSON object |
| `StandardGlobalNumericalAge` | «DataType» | plain JSON object |
| `StratigraphicPoint` | «FeatureType» | JSON-FG Feature |
| `StratigraphicSection` | «FeatureType» | JSON-FG Feature |
| `TimeOrdinalEra` | «DataType» | plain JSON object |
| `TimeOrdinalEraBoundary` | «DataType» | plain JSON object |
| `TimeOrdinalReferenceSystem` | «DataType» | plain JSON object |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `GeochronologicBoundary`

A GeochronologicBoundary is a boundary between two geochronologic time periods.

**Supertype**: [`TimeOrdinalEraBoundary`](#TimeOrdinalEraBoundary) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `stratotype` | (oneOf — see schema) | 0..1 | The property stratotype is an association between a GeochronologicBoundary and a StratigraphicPoint that are associat… |

### `GeochronologicEra`

A GeochronologicEra is a period of time between two GeochronologicBoundaries. The association of a GeochronologicEra with a stratotype is optional. In the GSSP approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes are not used. Rather, the association of an era with geologic units and sections is indirect, via the association of an era with boundaries, which are in turn tied to stratotype points, which occur within host stratotype sections.

**Supertype**: [`TimeOrdinalEra`](#TimeOrdinalEra) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `rank` | (oneOf — see schema) | 0..1 | The property rank:GeochronologicEraRank contains a term from a vocabulary describing the rank of the time period (e.g… |
| `stratotype` | (oneOf — see schema) | 0..1 | The property stratotype is an association between a GeochronologicEra and StratigraphicSection that describes a type … |

### `GeologicEventDescription`

GeologicEventDescription provides extended description of geologic events through links to GeochronologicEras in the GeologicTimescale schema.

**Supertype**: `GeologicEventAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `olderGeochronologicEra` | (oneOf — see schema) | 0..1 | Link to description of the GeochronologicEra that corresponds to the older estimated age of a geologic feature. |
| `youngerGeochronologicEra` | (oneOf — see schema) | 0..1 | Link to description of the GeochronologicEra that corresponds to the younger estimated age of a geologic feature. |
| `prototype` | (oneOf — see schema) | 0..1 | Reference stratigraphic point for stratigraphic events |

### `GeologicTimescale`

The classic "Geologic Timescale" (http://www.stratigraphy.org/index.php/ics-chart-timescale) comprising an ordered, hierarchical set of named "eras" is an example of an Ordinal Temporal Reference System. It may be calibrated with reference to a numeric Temporal Coordinate System, but is, in principle, defined independently.  Constraint: Structure association is with GeochronologicEra

**Supertype**: [`TimeOrdinalReferenceSystem`](#TimeOrdinalReferenceSystem) (this BB).

### `GlobalStratotypePoint`

A type of stratigraphic point used to define a globally agreed point in geologic time. This class does not have any properties beyond those inherited from StratigraphicPoint.  Constraint: value(status)=="GSSP"

**Supertype**: [`StratigraphicPoint`](#StratigraphicPoint) (this BB).

### `GlobalStratotypeSection`

A type of stratigraphic section used to define a globally agreed standard period of geologic time  Constraint: value(status)=="GSSP"

**Supertype**: [`StratigraphicSection`](#StratigraphicSection) (this BB).

### `NumericEraBoundary`

NumericEraBoundary is used for pre-Ediacaran and Pleistocene / Holocene boundaries in the standard timescale where boundaries are not defined by a material reference but as numerical values.

**Supertype**: [`TimeOrdinalEraBoundary`](#TimeOrdinalEraBoundary) (this BB).

### `StandardGlobalNumericalAge`

A standard numeric age point (a numeric analogue to a 'golden spike') is applicable to the formal subdivision of the Precambrian, and perhaps the Pleistocene/Holocene boundary ( http://www.stratigraphy.org/index.php/ics-chart-timescale). The boundary is not defined from a physical stratotype, although it can be influence by some, but placed at a convenient numerical value.  Constraint: value(status)=="GSSA"

**Supertype**: [`NumericEraBoundary`](#NumericEraBoundary) (this BB).

### `StratigraphicPoint`

A point in the stratigraphic record used to define a geochronologic boundary or point in geologic time.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `primaryGuidingCriterion` | (oneOf — see schema) | 0..1 | The property primaryGuidingCriterion:Primitive::CharacterString contains a description of the primary criterion used … |
| `additionalCorrelationProperty` | (oneOf — see schema) | 0..1 | The property additionnalCorrelationProperty:Primitive::CharacterString contains any additional criteria used to estab… |
| `status` | (oneOf — see schema) | 0..1 | The property status:Primitive::CharacterString contains a description of the status of stratigraphic point (e.g., for… |

### `StratigraphicSection`

A type of stratigraphic section used to define a globally agreed standard period of geologic time. This class does not have any properties beyond those inherited from StratigraphicSection.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `geologicSetting` | (oneOf — see schema) | 0..1 | The property geologicSetting:Primitive::CharacterString contains a description of the geologic setting of the stratig… |
| `geologicDescription` | (oneOf — see schema) | 0..1 | The geologicDescription:Primitive::CharacterString contains a description of the geology of the stratigraphic section… |
| `accessibility` | (oneOf — see schema) | 0..1 | The property accessibility:Primitive::CharacterString contains a description of the ability to access the stratigraph… |
| `conservation` | (oneOf — see schema) | 0..1 | The property conservation:Primitive::CharacterString contains a description of measures to conserve the stratigraphic… |

### `TimeOrdinalEra`

The association of an era with a stratotype is optional. In the GSSP approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes are not used. Rather, the association of an Era with geologic units and sections is indirect, via the association of an era with Boundaries, which are in turn tied to Stratotype Points, which occur within host Stratotype Sections. Note that the "German School" defines stratigraphic eras conceptually, without reference to stratotypes.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `end` | (oneOf — see schema) | 0..1 | Younger time boundary of an era |
| `start` | (oneOf — see schema) | 0..1 | Older time boundary of an era |
| `member` | (oneOf — see schema) | 0..1 | Subdivisions of TimeOrdinalEra |

### `TimeOrdinalEraBoundary`

A point in Earth's history which bounds a TimeOrdinalEra.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `position` | (oneOf — see schema) | 0..1 | A point in time corresponding to the era boundary |
| `positionalUncertainty` | (oneOf — see schema) | 0..1 | A measure of the uncertainty in the estimate of the point in time of the era boundary |
| `previousEra` | (oneOf — see schema) | 0..1 | Preceding era |
| `observationalBasis` | (oneOf — see schema) | 0..1 | Observation supporting the existence of the boundary (geochronology, paleontology, etc.) |
| `nextEra` | (oneOf — see schema) | 0..1 | Succeeding era |

### `TimeOrdinalReferenceSystem`

A time reference system comprised of an ordered set of time periods (time ordinal eras).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `referencePoint` | (oneOf — see schema) | 2..* | Two reference points defining the extent of the system |
| `component` | (oneOf — see schema) | 0..1 | TimeOrdinalEra composing the TimeOrdinalReferenceSystem |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `GeochronologicEraRank` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../gsmscimlBasic/gsmscimlBasicSchema.json#GeologicEventAbstractDescription`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [examplegsmGeologicTimeMinimal.json](examples/examplegsmGeologicTimeMinimal.json)
- [stratigraphic_section_lower_jurassic_GSO.json](examples/stratigraphic_section_lower_jurassic_GSO.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicTime`, `GSSP`, `TemporalReferenceSystem`, `TimeScale`, `GeologicAgeDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
