# GeoSciML Geochronology

JSON Schema building block for the `Geochronology` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 1 feature type, 3 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeochronologicInterpretation` | «FeatureType» | JSON-FG Feature |
| `IsotopicEventType` | «CodeList» | URI codelist (`format: uri`) |
| `IsotopicSystemName` | «CodeList» | URI codelist (`format: uri`) |
| `StatisticalMethodTerm` | «CodeList» | URI codelist (`format: uri`) |

## Class details

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

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `IsotopicEventType` | `_(treat as open — no `codeList` annotation)_` |
| `IsotopicSystemName` | `_(treat as open — no `codeList` annotation)_` |
| `StatisticalMethodTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../geosciml_GeologicEvent/schema.json#GeologicEvent`
- `https://schemas.opengis.net/json-fg/feature.json`

## Examples

- [Minimal](examples/exampleGeochronologyMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeochronologyComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `Geochronology`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
