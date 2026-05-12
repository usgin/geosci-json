# GeoSciML TimeScale

JSON Schema building block for the `TimeScale` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 5 data types, 1 code list.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeochronologicBoundary` | «DataType» | plain JSON object |
| `GeochronologicEra` | «DataType» | plain JSON object |
| `GeochronologicEraRank` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicTimescale` | «DataType» | plain JSON object |
| `NumericEraBoundary` | «DataType» | plain JSON object |
| `StandardGlobalNumericalAge` | «DataType» | plain JSON object |

## Class details

### `GeochronologicBoundary`

A GeochronologicBoundary is a boundary between two geochronologic time periods.

**Supertype**: `TimeOrdinalEraBoundary` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `stratotype` | (oneOf — see schema) | 0..1 | The property stratotype is an association between a GeochronologicBoundary and a StratigraphicPoint that are associat… |

### `GeochronologicEra`

A GeochronologicEra is a period of time between two GeochronologicBoundaries. The association of a GeochronologicEra with a stratotype is optional. In the GSSP approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes are not used. Rather, the association of an era with geologic units and sections is indirect, via the association of an era with boundaries, which are in turn tied to stratotype points, which occur within host stratotype sections.

**Supertype**: `TimeOrdinalEra` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `rank` | (oneOf — see schema) | 0..1 | The property rank:GeochronologicEraRank contains a term from a vocabulary describing the rank of the time period (e.g… |
| `stratotype` | (oneOf — see schema) | 0..1 | The property stratotype is an association between a GeochronologicEra and StratigraphicSection that describes a type … |

### `GeologicTimescale`

The classic "Geologic Timescale" (http://www.stratigraphy.org/index.php/ics-chart-timescale) comprising an ordered, hierarchical set of named "eras" is an example of an Ordinal Temporal Reference System. It may be calibrated with reference to a numeric Temporal Coordinate System, but is, in principle, defined independently.  Constraint: Structure association is with GeochronologicEra

**Supertype**: `TimeOrdinalReferenceSystem` (cross-BB).

### `NumericEraBoundary`

NumericEraBoundary is used for pre-Ediacaran and Pleistocene / Holocene boundaries in the standard timescale where boundaries are not defined by a material reference but as numerical values.

**Supertype**: `TimeOrdinalEraBoundary` (cross-BB).

### `StandardGlobalNumericalAge`

A standard numeric age point (a numeric analogue to a 'golden spike') is applicable to the formal subdivision of the Precambrian, and perhaps the Pleistocene/Holocene boundary ( http://www.stratigraphy.org/index.php/ics-chart-timescale). The boundary is not defined from a physical stratotype, although it can be influence by some, but placed at a convenient numerical value.  Constraint: value(status)=="GSSA"

**Supertype**: [`NumericEraBoundary`](#NumericEraBoundary) (this BB).

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `GeochronologicEraRank` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../geosciml_TemporalReferenceSystem/schema.json#TimeOrdinalEra`
- `../geosciml_TemporalReferenceSystem/schema.json#TimeOrdinalEraBoundary`
- `../geosciml_TemporalReferenceSystem/schema.json#TimeOrdinalReferenceSystem`

## Examples

- [Minimal](examples/exampleTimeScaleMinimal.json) — bare valid instance.
- [Complete](examples/exampleTimeScaleComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `TimeScale`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
