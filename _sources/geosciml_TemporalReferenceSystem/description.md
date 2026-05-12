# GeoSciML TemporalReferenceSystem

JSON Schema building block for the `TemporalReferenceSystem` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 3 data types.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `TimeOrdinalEra` | «DataType» | plain JSON object |
| `TimeOrdinalEraBoundary` | «DataType» | plain JSON object |
| `TimeOrdinalReferenceSystem` | «DataType» | plain JSON object |

## Class details

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
| `referencePoint` | `/$defs/SCLinkObject` | 2..* | Two reference points defining the extent of the system |
| `component` | (oneOf — see schema) | 0..1 | TimeOrdinalEra composing the TimeOrdinalReferenceSystem |

## External dependencies

- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [Minimal](examples/exampleTemporalReferenceSystemMinimal.json) — bare valid instance.
- [Complete](examples/exampleTemporalReferenceSystemComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `TemporalReferenceSystem`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
