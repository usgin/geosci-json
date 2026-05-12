# GeoSciML GeologicEvent

JSON Schema building block for the `GeologicEvent` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 1 feature type, 2 data types, 2 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `EventProcessTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeochronologicEraTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicEvent` | «FeatureType» | JSON-FG Feature |
| `GeologicEventAbstractDescription` | «DataType» | plain JSON object |
| `NumericAgeRange` | «DataType» | plain JSON object |

## Class details

### `GeologicEvent`

A GeologicEvent is an identifiable event during which one or more geological processes act to modify geological entities. It may have a specified geologic age (numeric age or GeochologicEraTerm) and may have specified environments and processes. An example might be a cratonic uplift event during which erosion, sedimentation, and volcanism all take place.

**Supertype**: `GeologicFeature` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `eventProcess` | (oneOf — see schema) | 0..1 | The eventProcess:EventProcessTerm property provides a term from a controlled vocabulary specifying the process or pro… |
| `numericAge` | (oneOf — see schema) | 0..1 | The numericAge:NumericAgeRange property provides an age in absolute year before present (BP). Present is defined by c… |
| `olderNamedAge` | (oneOf — see schema) | 0..1 | The property olderNamedAge:GeochronologicalEraTerm defines the older boundary of age of an event expressed using a ge… |
| `youngerNamedAge` | (oneOf — see schema) | 0..1 | The property youngerNamedAge:GeochronologicalEraTerm defines the younger boundary of age of event expressed using a g… |
| `eventEnvironment` | (oneOf — see schema) | 0..1 | The eventEnvironment property (SWE::Category) is a category from a controlled vocabulary identifying the physical set… |
| `gaEventDescription` | (oneOf — see schema) | 0..1 | The property geEventDescription:GeologicEventAbstractDescription contains a detailed event description. This is a stu… |

### `GeologicEventAbstractDescription`

Stub property class to allow extended event related properties.

### `NumericAgeRange`

The NumericAgeRange class represents an absolute age assignment using numeric measurement results.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `reportingDate` | (oneOf — see schema) | 0..1 | The reportingDate (SWE::Quantity) property reports a single time coordinate value to report as representative for thi… |
| `olderBoundDate` | (oneOf — see schema) | 0..1 | The olderBoundDate (SWE::Quantity) property reports the older bounding time coordinate in an age range. |
| `youngerBoundDate` | (oneOf — see schema) | 0..1 | The youngerBoundDate (SWE::Quantity) property reports the younger bounding time coordinate in an age range. |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `EventProcessTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeochronologicEraTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../geosciml_GeologyBasic/schema.json#GeologicFeature`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [Minimal](examples/exampleGeologicEventMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeologicEventComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GeologicEvent`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
