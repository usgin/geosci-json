# GeoSciML GSSP

JSON Schema building block for the `GSSP` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 4 feature types.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GlobalStratotypePoint` | «FeatureType» | JSON-FG Feature |
| `GlobalStratotypeSection` | «FeatureType» | JSON-FG Feature |
| `StratigraphicPoint` | «FeatureType» | JSON-FG Feature |
| `StratigraphicSection` | «FeatureType» | JSON-FG Feature |

## Class details

### `GlobalStratotypePoint`

A type of stratigraphic point used to define a globally agreed point in geologic time. This class does not have any properties beyond those inherited from StratigraphicPoint.  Constraint: value(status)=="GSSP"

**Supertype**: [`StratigraphicPoint`](#StratigraphicPoint) (this BB).

### `GlobalStratotypeSection`

A type of stratigraphic section used to define a globally agreed standard period of geologic time  Constraint: value(status)=="GSSP"

**Supertype**: [`StratigraphicSection`](#StratigraphicSection) (this BB).

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

## External dependencies

- `https://schemas.opengis.net/json-fg/feature.json`

## Examples

- [Minimal](examples/exampleGSSPMinimal.json) — bare valid instance.
- [Complete](examples/exampleGSSPComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GSSP`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
