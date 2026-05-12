# GeoSciML GeologicRelation

JSON Schema building block for the `GeologicRelation` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 2 data types, 2 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeologicFeatureRelation` | «DataType» | plain JSON object |
| `GeologicRelationshipTerm` | «CodeList» | URI codelist (`format: uri`) |
| `MaterialRelation` | «DataType» | plain JSON object |
| `RelationRoleTerm` | «CodeList» | URI codelist (`format: uri`) |

## Class details

### `GeologicFeatureRelation`

The GeologicFeatureRelation class defines the general structure used to define relationships between any GeoSciML feature types. Relationships are always binary and directional. There is always a single source and a single target. The relationship is always defined from the perspective of the Source and is generally an active verb. Example: a Source may point to an intrusive igneous rock unit. In this case, the Target would point to the appropriate host rock body and the relationship attribute would be 'intrudes'. Other appropriate relationship attributes might include: overlies, offsets, crosscuts, folds, etc. Many other types of relationships can also be accommodated via GeologicRelation, for example, topological relations could be described where they are geologically significant.

**Supertype**: `AbstractFeatureRelation` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `relationship` | (oneOf — see schema) | 0..1 | The relationship:GeologicRelationshipTerm property contains a term from a controlled vocabulary to describe the geolo… |
| `sourceRole` | (oneOf — see schema) | 0..1 | The property sourceRole:RelationRoleProperty contains a term from a controlled vocabulary describing the role played … |
| `targetRole` | (oneOf — see schema) | 0..1 | The property targetRole:RelationRoleTerm contains a term from a controlled vocabulary describing the role played by t… |

### `MaterialRelation`

The MaterialRelation class describes the relationships between constituent parts in an EarthMaterial (e.g. A mineral overgrowth on a phenocryst within a granite). Example: Consider an overgrowth of albite on plagioclase in a granite. The Source would originate with the albite constituentPart description. In this case, the Target would point to the plagioclase constituentPart description and the relationship attribute would be 'overgrowth' and the sourceRole is 'overgrows'. Other appropriate role attributes might include: crosscuts, replaces, etc. for crosscutting and replacement relationships. Inverse relationships must be explicitly recorded.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `relationship` | (oneOf — see schema) | 0..1 | The property relationship:GeologicRelationshipTerm contains a term from a controlled vocabulary to describe the geolo… |
| `sourceRole` | (oneOf — see schema) | 0..1 | The property sourceRole:RelationRoleTerm contains a term that describes the role played by the source earth material … |
| `targetRole` | (oneOf — see schema) | 0..1 | The property targetRole:RelationRoleTerm contains a term describing the role played by the target earth material part… |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `GeologicRelationshipTerm` | `_(treat as open — no `codeList` annotation)_` |
| `RelationRoleTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../geosciml_GeologyBasic/schema.json#AbstractFeatureRelation`

## Examples

- [Minimal](examples/exampleGeologicRelationMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeologicRelationComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GeologicRelation`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
