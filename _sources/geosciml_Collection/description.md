# GeoSciML Collection

JSON Schema building block for the `Collection` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 1 feature type, 1 code list, 1 union.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `CollectionTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GSML` | «FeatureType» | JSON-FG Feature |
| `GSMLitem` | «Union» | type discriminator (`oneOf`) |

## Class details

### `GSML`

GSML is a collection class grouping a set of features or types which are members of this collection. A collectionType property provides context or purpose.  Constraint: self.metadata.hierarchylevel=dataset

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `collectionType` | (oneOf — see schema) | 0..1 | The collectionType:CollectionTypeTerm property contains a term from a controlled vocabulary describing the type of co… |
| `member` | `GSMLitem` | 1..* | The member property is an association that links a GSML instance to features and objects to be included as members of… |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `CollectionTypeTerm` | `_(treat as open — no `codeList` annotation)_` |

## Unions

### `GSMLitem`

GSMLItem constrains the collection members to instances of EarthMaterial, GeologicFeature, GM_Object, MappedFeature, AbstractFeatureRelation and OM::SF_SamplingFeature.

Branches (`oneOf`):
- (branch 0)
- (branch 1)
- `Geometry`
- (branch 3)
- (branch 4)
- `iso19156:SF_SamplingFeature` — External type — needs concrete schema URL

## External dependencies

- `../geosciml_GeologyBasic/schema.json#AbstractFeatureRelation`
- `../geosciml_GeologyBasic/schema.json#EarthMaterial`
- `../geosciml_GeologyBasic/schema.json#GeologicFeature`
- `../geosciml_GeologyBasic/schema.json#MappedFeature`
- `https://geojson.org/schema/Geometry.json`
- `https://schemas.opengis.net/json-fg/feature.json`

## Examples

- [Minimal](examples/exampleCollectionMinimal.json) — bare valid instance.
- [Complete](examples/exampleCollectionComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `Collection`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
