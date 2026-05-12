# GeoSciML Geomorphology

JSON Schema building block for the `Geomorphology` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 3 feature types, 1 data type, 2 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AnthropogenicGeomorphologicFeature` | «FeatureType» | JSON-FG Feature |
| `AnthropogenicGeomorphologicFeatureTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeomorphologicFeature` | «FeatureType» | JSON-FG Feature |
| `GeomorphologicUnitAbstractDescription` | «DataType» | plain JSON object |
| `NaturalGeomorphologicFeature` | «FeatureType» | JSON-FG Feature |
| `NaturalGeomorphologicFeatureTypeTerm` | «CodeList» | URI codelist (`format: uri`) |

## Class details

### `AnthropogenicGeomorphologicFeature`

An anthropogenic geomorphologic feature is a geomorphologic feature (i.e., landform) which has been created by human activity. For example, a dredged channel, midden, open pit or reclaimed land.

**Supertype**: [`GeomorphologicFeature`](#GeomorphologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `anthropogenicGeomorphologicFeatureType` | (oneOf — see schema) | 0..1 | The anthropogenicGeomorphologicFeatureType: AnthropogenicGeomorphologicFeatureTypeTerm is a reference from a controll… |

### `GeomorphologicFeature`

A geomorphologic feature is a kind of GeologicFeature describing the shape and nature of the Earth's land surface. These landforms may be created by natural Earth processes (e.g., river channel, beach, moraine or mountain) or through human (anthropogenic) activity (e.g., dredged channel, reclaimed land, mine waste dumps). In GeoSciML, the geomorphologic feature is modelled as a feature related (through unitDescription property) to a GeologicUnit that composes the form.

**Supertype**: `GeologicFeature` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `unitDescription` | (oneOf — see schema) | 0..1 | The unitDescription property is an association that links the geomorphologic feature to a geologic description (e.g.,… |
| `gmFeatureDescription` | (oneOf — see schema) | 0..1 | The property gmFeatureDescription:GeomorphologicUnitAbstractDescription provides a detailed morphologic description. … |

### `GeomorphologicUnitAbstractDescription`

Detailed geomorphologic unit description placeholder (stub class) for GeomorphologicUnit  Constraint: Only one instance of each subtype is allowed

### `NaturalGeomorphologicFeature`

A natural geomorphologic feature is a geomorphologic feature (i.e., landform) that has been created by natural Earth processes. For example, river channel, beach ridge, caldera, canyon, moraine or mud flat.

**Supertype**: [`GeomorphologicFeature`](#GeomorphologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `naturalGeomorphologicFeatureType` | (oneOf — see schema) | 0..1 | The property naturalGeomorphologicFeatureType: NaturalGeomorphologicFeatureTypeTerm is a reference from a controlled … |
| `activity` | (oneOf — see schema) | 0..1 | The activity property (SWE::Category) contains a category term from a controlled vocabulary describing the current ac… |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `AnthropogenicGeomorphologicFeatureTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `NaturalGeomorphologicFeatureTypeTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../geosciml_GeologyBasic/schema.json#GeologicFeature`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`

## Examples

- [Minimal](examples/exampleGeomorphologyMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeomorphologyComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `Geomorphology`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
