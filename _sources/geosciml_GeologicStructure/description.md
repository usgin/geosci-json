# GeoSciML GeologicStructure

JSON Schema building block for the `GeologicStructure` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 5 feature types, 4 data types, 4 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `Contact` | «FeatureType» | JSON-FG Feature |
| `ContactAbstractDescription` | «DataType» | plain JSON object |
| `ContactTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `FaultTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `Fold` | «FeatureType» | JSON-FG Feature |
| `FoldAbstractDescription` | «DataType» | plain JSON object |
| `FoldProfileTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `Foliation` | «FeatureType» | JSON-FG Feature |
| `FoliationAbstractDescription` | «DataType» | plain JSON object |
| `FoliationTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicStructure` | «FeatureType» | JSON-FG Feature |
| `ShearDisplacementStructure` | «FeatureType» | JSON-FG Feature |
| `ShearDisplacementStructureAbstractDescription` | «DataType» | plain JSON object |

## Class details

### `Contact`

A contact is a general concept representing any kind of surface separating two geologic units, including primary boundaries such as depositional contacts, all kinds of unconformities, intrusive contacts, and gradational contacts, as well as faults that separate geologic units.

**Supertype**: [`GeologicStructure`](#GeologicStructure) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `contactType` | (oneOf — see schema) | 0..1 | The property contactType:ContactTypeTerm classifies the contact (e.g. intrusive, unconformity, bedding surface, litho… |
| `stContactDescription` | (oneOf — see schema) | 0..1 | The property stContactDescription:ContactAbstractDescription provides a detailed contact description. This is a stub … |

### `ContactAbstractDescription`

An abstract class providing a link between classes in GeoSciMLBasic and GeoSciMLExtended application schemas.

### `Fold`

A fold is formed by one or more systematically curved layers, surfaces, or lines in a rock body. A fold denotes a structure formed by the deformation of a geologic structure, such as a contact which the original undeformed geometry is presumed, to form a structure that may be described by the translation of an abstract line (the fold axis) parallel to itself along some curvilinear path (the fold profile). Folds have a hinge zone (zone of maximum curvature along the surface) and limbs (parts of the deformed surface not in the hinge zone). Folds are described by an axial surface, hinge line, profile geometry, the solid angle between the limbs, and the relationships between adjacent folded surfaces if the folded structure is a Layering fabric.

**Supertype**: [`GeologicStructure`](#GeologicStructure) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `profileType` | (oneOf — see schema) | 0..1 | The property profileType:FoldProfileTypeTerm contains a term from a controlled vocabulary specifying the concave/conv… |
| `stFoldDescription` | (oneOf — see schema) | 0..1 | The property stFoldDescription:FoldAbstractDescription provides a detailed fold description. This is a stub property … |

### `FoldAbstractDescription`

An abstract class providing a link between classes in GeoSciMLBasic and GeoSciMLExtended application schemas.

### `Foliation`

A foliation is a planar arrangement of textural or structural features in any type of rock. It includes any of a wide variety of penetrative planar geological structures that may be present in a rock. Examples include schistosity, mylonitic foliation, penetrative bedding structure (lamination), and cleavage. Following the proposed definition of gneiss by the NADM Science Language Technical Team, penetrative planar foliation defined by layers &gt; 5 mm thick is considered Layering.

**Supertype**: [`GeologicStructure`](#GeologicStructure) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `foliationType` | (oneOf — see schema) | 0..1 | The foliationType:FoliationTypeTerm property specifies the type of foliation from a controlled vocabulary. Examples i… |
| `stFoliationDescription` | (oneOf — see schema) | 0..1 | The foliationType:FoliationTypeTerm property specifies the type of foliation from a controlled vocabulary. Examples i… |

### `FoliationAbstractDescription`

An abstract class providing a link between classes in GeoSciMLBasic and GeoSciMLExtended application schemas.  Constraint: only one instance of each subtype class is allowed

### `GeologicStructure`

A geologic structure is a configuration of matter in the Earth based on describable inhomogeneity, pattern, or fracture in an earth material. The identity of a GeologicStructure is independent of the material that is the substrate for the structure. The general GeologicFeatureRelation (available in the Extension package) is used to associate penetrative GeologicStructures with GeologicUnits. GeoSciML Basic only provides a limited set of core structures (Contact, Fold, ShearDisplacementStructure and Foliation) with a single property to categorise them. Supplemental properties and geologic structure types are available from the Extension package.

**Supertype**: `GeologicFeature` (cross-BB).

### `ShearDisplacementStructure`

A shear displacement structure includes all brittle to ductile style structures along which displacement has occurred, from a simple, single 'planar' brittle or ductile surface to a fault system comprised of tens of strands of both brittle and ductile nature. This structure may have some significant thickness (a deformation zone) and have an associated body of deformed rock that may be considered a deformation unit (which geologicUnitType is ‘DeformationUnit’) which can be associated to the ShearDisplacementStructure using GeologicFeatureRelation from the GeoSciML Extension package

**Supertype**: [`GeologicStructure`](#GeologicStructure) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `faultType` | (oneOf — see schema) | 0..1 | The faultType:FaultTypeTerm property contains a term from a controlled vocabulary describing the type of shear displa… |
| `stStructureDescription` | (oneOf — see schema) | 0..1 | The property stStructureDescription:ShearDisplacementStructureAbstractDescription provides a detailed geologic struct… |

### `ShearDisplacementStructureAbstractDescription`

An abstract class providing a link between classes in GeoSciMLBasic and GeoSciMLExtended application schemas.

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `ContactTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FaultTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FoldProfileTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FoliationTypeTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../geosciml_GeologyBasic/schema.json#GeologicFeature`

## Examples

- [Minimal](examples/exampleGeologicStructureMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeologicStructureComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GeologicStructure`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
