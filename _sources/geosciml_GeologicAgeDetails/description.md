# GeoSciML GeologicAgeDetails

JSON Schema building block for the `GeologicAgeDetails` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 1 data type.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeologicEventDescription` | «DataType» | plain JSON object |

## Class details

### `GeologicEventDescription`

GeologicEventDescription provides extended description of geologic events through links to GeochronologicEras in the GeologicTimescale schema.

**Supertype**: `GeologicEventAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `olderGeochronologicEra` | (oneOf — see schema) | 0..1 | Link to description of the GeochronologicEra that corresponds to the older estimated age of a geologic feature. |
| `youngerGeochronologicEra` | (oneOf — see schema) | 0..1 | Link to description of the GeochronologicEra that corresponds to the younger estimated age of a geologic feature. |
| `prototype` | (oneOf — see schema) | 0..1 | Reference stratigraphic point for stratigraphic events |

## External dependencies

- `../geosciml_GeologicEvent/schema.json#GeologicEventAbstractDescription`
- `../geosciml_TimeScale/schema.json#GeochronologicEra`

## Examples

- [Minimal](examples/exampleGeologicAgeDetailsMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeologicAgeDetailsComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GeologicAgeDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
