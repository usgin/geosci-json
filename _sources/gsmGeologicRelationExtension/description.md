# gsmGeologicRelationExtension

GeoSciML 4.1 building block `gsmGeologicRelationExtension`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeologicRelation`.

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

- `../gsmscimlBasic/gsmscimlBasicSchema.json#AbstractFeatureRelation`

## Examples

- [examplegsmGeologicRelationExtensionMinimal.json](examples/examplegsmGeologicRelationExtensionMinimal.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicRelation`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
