# gsmGeologicUnitExtension

GeoSciML 4.1 building block `gsmGeologicUnitExtension`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeologicUnitDetails`.

Contains 2 data types.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `BeddingDescription` | «DataType» | plain JSON object |
| `GeologicUnitDescription` | «DataType» | plain JSON object |

## Class details

### `BeddingDescription`

BeddingDescription provides a detailed description of the bedding characteristics of a geologic unit.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `beddingPattern` | (oneOf - see schema) | 0..1 | The property beddingPattern (SWE::Category) provides a term from a controlled vocabulary specifying patterns of beddi… |
| `beddingStyle` | (oneOf - see schema) | 0..1 | The property beddingStyle (SWE::Category) provides a term from a controlled vocabulary specifying the style of beddin… |
| `beddingThickness` | (oneOf - see schema) | 0..1 | The property beddingThickness (SWE::Category) provides a term from a controlled vocabulary characterizing the thickne… |

### `GeologicUnitDescription`

GeologicUnitDescription provides for extended description of the characteristics of a geologic unit.

**Supertype**: `GeologicUnitAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `bodyMorphology` | (oneOf - see schema) | 0..1 | The bodyMorphology property (SWE::Category) provides a term from a controlled vocabulary describing the geometry or f… |
| `unitComposition` | (oneOf - see schema) | 0..1 | The unitComposition property (SWE::Category) provides a term from a composition-based classification that requires su… |
| `outcropCharacter` | (oneOf - see schema) | 0..1 | The property outcropCharacter (SWE::Category) provides a term that describes the nature of outcrops formed by a geolo… |
| `unitThickness` | (oneOf - see schema) | 0..1 | The property unitThickness (SWE::QuantityRange) provides a value that represents the typical thickness of the geologi… |
| `bedding` | (oneOf - see schema) | 0..1 | The bedding:BeddingDescription property reports a description of the bedding. |

## External dependencies

- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicUnitAbstractDescription`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [examplegsmGeologicUnitExtensionMinimal.json](examples/examplegsmGeologicUnitExtensionMinimal.json)
- [geologic_unit_la_tojiza_pluton_GSO.json](examples/geologic_unit_la_tojiza_pluton_GSO.json)
- [geologic_unit_lake_holmes_coal_measures_GSO.json](examples/geologic_unit_lake_holmes_coal_measures_GSO.json)
- [geologic_unit_lardeau_group_GSO.json](examples/geologic_unit_lardeau_group_GSO.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicUnitDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
