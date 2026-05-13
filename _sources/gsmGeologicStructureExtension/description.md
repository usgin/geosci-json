# gsmGeologicStructureExtension

GeoSciML 4.1 building block `gsmGeologicStructureExtension`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeologicStructureDetails`.

Contains 7 feature types, 9 data types, 5 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `ContactDescription` | «DataType» | plain JSON object |
| `DeformationStyleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `DisplacementEvent` | «FeatureType» | JSON-FG Feature |
| `DisplacementValue` | «DataType» | plain JSON object |
| `FoldDescription` | «DataType» | plain JSON object |
| `FoldSystem` | «FeatureType» | JSON-FG Feature |
| `FoliationDescription` | «DataType» | plain JSON object |
| `Fracture` | «FeatureType» | JSON-FG Feature |
| `Joint` | «FeatureType» | JSON-FG Feature |
| `Layering` | «FeatureType» | JSON-FG Feature |
| `Lineation` | «FeatureType» | JSON-FG Feature |
| `LineationTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `MovementSenseTerm` | «CodeList» | URI codelist (`format: uri`) |
| `MovementTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `NetSlipValue` | «DataType» | plain JSON object |
| `NonDirectionalStructure` | «FeatureType» | JSON-FG Feature |
| `NonDirectionalStructureTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `SeparationValue` | «DataType» | plain JSON object |
| `ShearDisplacementStructureDescription` | «DataType» | plain JSON object |
| `SlipComponents` | «DataType» | plain JSON object |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `ContactDescription`

The ContactDescription provides extended descriptive properties of a geologic contact. If the contact type is ChronostratigraphicBoundary, it can be associated with a geochronologic (i.e., time zone) boundary that may correlate with it.

**Supertype**: `ContactAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `contactCharacter` | (oneOf - see schema) | 0..1 | The contactCharacter (SWE::Category) contains a term from a controlled vocabulary that describes the character of the… |
| `orientation` | (oneOf - see schema) | 0..1 | The orientation:GSML_PlanarOrientation property reports the general orientation of the contact surface. |
| `correlatesWith` | (oneOf - see schema) | 0..1 | The correlatesWith property is an association between ContactDescription and a GeochronologicBoundary describing a ge… |

### `DisplacementEvent`

A displacement event is a description of the age, environment and process of a shear displacement event.

**Supertype**: `GeologicEvent` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `incrementalDisplacement` | (oneOf - see schema) | 0..1 | The incrementalDisplacement:DisplacementValue property contains a DisplacementValue reporting the parameters of the d… |

### `DisplacementValue`

A displacement value expresses the displacement on a fault with respect to a planar approximation of its shape.

**Supertype**: `ShearDisplacementStructureAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `hangingWallDirection` | (oneOf - see schema) | 0..1 | The property hangingWallDirection:GSML_LinearOrientation describes the direction of the hanging-wall side of the faul… |
| `movementSense` | (oneOf - see schema) | 0..1 | The property movementSense:MovementSenseTerm contains a term from a controlled vocabulary that describes the movement… |
| `movementType` | (oneOf - see schema) | 0..1 | The property movementType:MovementTypeTerm contains a term from a controlled vocabulary that defines the type of move… |
| `displacementEvent` | (oneOf - see schema) | 0..1 | The property displacementEvent is an association between a Displacement and a GeologicEvent that contains a descripti… |

### `FoldDescription`

FoldDescription is an extended descriptive property of a fold structure.

**Supertype**: `FoldAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `amplitude` | (oneOf - see schema) | 0..1 | The amplitude property (SWE::QuantityRange) reports the length from line segment connecting inflection points on adja… |
| `axialSurfaceOrientation` | (oneOf - see schema) | 0..1 | The property axialSurfaceOrientation:GSML_PlanarOrientation is used to characterize the geometry of a fold. The axial… |
| `geneticModel` | (oneOf - see schema) | 0..1 | The property geneticModel (SWE::Category) contains a term from a controlled vocabulary describing the specification o… |
| `hingeLineCurvature` | (oneOf - see schema) | 0..1 | The hingeLineCurvature property (SWE::Category) contains a term from a controlled vocabulary that describes the varia… |
| `hingeLineOrientation` | (oneOf - see schema) | 0..1 | The property hingeLineOrientation:GSML_LinearOrientation reports the specification of the hinge line orientation for … |
| `hingeShape` | (oneOf - see schema) | 0..1 | The property hingeShape (SWE::Category) reports a term from a controlled vocabulary describing the hinge shape, e.g. … |
| `interLimbAngle` | (oneOf - see schema) | 0..1 | The property interLimbAngle (SWE::Category) contains a term from a controlled vocabulary describing the interlimb ang… |
| `limbShape` | (oneOf - see schema) | 0..1 | The limbShape property (SWE::Category) contains a term from a controlled vocabulary describing the shape of the limb … |
| `span` | (oneOf - see schema) | 0..1 | The span property (SWE::QuantityRange) reports a value describing the linear distance between inflection points in a … |
| `symmetry` | (oneOf - see schema) | 0..1 | The symmetry property (SWE::Category) contains a term from a controlled vocabulary describing the concordance or disc… |
| `system` | (oneOf - see schema) | 0..1 | The system property is an association between a FoldDescription and a FoldSystem that aggregates folds into a system. |

### `FoldSystem`

A FoldSystem is a collection of congruent folds (axis and axial surface are parallel) produced by the same tectonic event. It is sometimes referred to as a "fold train".  Constraint: if periodic=False then count(Wavelength)=0

**Supertype**: `GeologicStructure` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `periodic` | (oneOf - see schema) | 0..1 | The property periodic:Primitive::Boolean reports TRUE if the hinges in a train are regularly spaced, and FALSE otherw… |
| `wavelength` | (oneOf - see schema) | 0..1 | The property wavelength (SWE::QuantityRange) contains a quantitative description of the length between adjacent antif… |
| `foldSystemMember` | (oneOf - see schema) | 0..1 | The foldSystemMember is an association between a FoldSystem and the Folds that are members of that system. |

### `FoliationDescription`

FoliationDescription provides extended descriptive properties for a foliation structure.

**Supertype**: `FoliationAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `definingElement` | (oneOf - see schema) | 0..1 | The property definingElement (SWE::Category) contains a term from a controlled vocabulary describing the kinds of inh… |
| `continuity` | (oneOf - see schema) | 0..1 | The continuity property (SWE::Category) reports a term from a controlled vocabulary to distinguish continuous vs. dis… |
| `intensity` | (oneOf - see schema) | 0..1 | The intensity property (SWE::Category) contains a term from a controlled vocabulary to describe how well the foliatio… |
| `mineralElement` | (oneOf - see schema) | 0..1 | The mineralElement property is an association between FoliationDescription and a Mineral that defines that foliation. |
| `orientation` | (oneOf - see schema) | 0..1 | The orientation:GSML_PlanarOrientation contains an estimate of the planar orientation of the foliation structure. |
| `spacing` | (oneOf - see schema) | 0..1 | The spacing property (SWE::QuantityRange) contains a linear dimension representing the thickness of foliation domains… |

### `Fracture`

Fractures are cracks in the earth surface. If there is no displacement it is a joint. If there is displacement and you are in the brittle zone it is a fault. In the ductile zone, a fracture with displacement with fracture is called a shear. FaultSurface as a separate class is not considered necessary for GeoSciML 2. Recording observations on FaultSurface should be in observation and measurement. The observation needs to be able to distinguish the type of measurement made (PropertyType)

**Supertype**: `GeologicStructure` (cross-BB).

### `Joint`

Fracture across which there is no displacement at the scale of interest.

**Supertype**: [`Fracture`](#Fracture) (this BB).

### `Layering`

A planar foliation is defined by a tabular succession of layers &gt; 5 mm thick. This definition is based on the proposed definition of gneiss by the NADM Science Language Technical Team. The GeologicStructure characteristic of gneiss is layering.

**Supertype**: `Foliation` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `layerComposition` | (oneOf - see schema) | 0..1 | The layerComposition property is an association between a Layering and a RockMaterial that describes the rock materia… |

### `Lineation`

GeologicStructure defined by aligned elongate elements. Lineation connotes a pervasive linear structure. Includes: flow lines, scratches, striae, slickenlines, linear arrangements of elongate components in sediments, fold hinges (when abundant and closely spaced), elongate minerals, crinkles, and lines of intersection between penetrative planar structures. Class also includes discrete linear structures like boudin, channel axis, tool marks.

**Supertype**: `GeologicStructure` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `lineationType` | (oneOf - see schema) | 0..1 | Type of lineation. Examples include: flow lines, scratches, striae, slickenlines, linear arrangements of elongate com… |
| `definingElement` | (oneOf - see schema) | 0..1 | Kinds of describable inhomogeneity in a rock body that may define a GeologicStructure. Examples include Oriented Part… |
| `intensity` | (oneOf - see schema) | 0..1 | How well the lineation is developed. Terms such as weak, moderate, strong. |
| `mineralElement` | (oneOf - see schema) | 0..1 | Mineral that defines the lineation |
| `orientation` | (oneOf - see schema) | 0..1 | Orientation of the lineation |

### `NetSlipValue`

NetSlipValue is a kind of DisplacementValue that describes the total amount of slip displacement along a structure.

**Supertype**: [`DisplacementValue`](#DisplacementValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `netSlip` | (oneOf - see schema) | 0..1 | The property netSlip:GSML_Vector reports the value of the net slip, expressed as a vector. |
| `slipComponent` | (oneOf - see schema) | 0..1 | The slipComponent:SlipComponents property associates the individual slip components with the net slip values. |

### `NonDirectionalStructure`

Structures present in geology that do not have a preferred orientation Includes small-scale structures that are characteristic of the geologic unit, e.g. herringbone crossbedding, mudcracks, graded bedding, planar lamination, miarolitic cavities, nebulitic structure, trace fossils, fossil molds

**Supertype**: `GeologicStructure` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `structureType` | (oneOf - see schema) | 0..1 | The type of non oriented structure. Examples include miarolitic cavity, flame structure, load cast, shatter cone, tra… |

### `SeparationValue`

SeparationValue is a kind of DisplacementValue that describes the amount of separation displacement across a structure.

**Supertype**: [`DisplacementValue`](#DisplacementValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `separation` | (oneOf - see schema) | 0..1 | The property separation:GSML_Vector reports the apparent offset across a planar feature, reported as a vector. |

### `ShearDisplacementStructureDescription`

ShearDisplacementStructureDescription provides extended descriptive properties of a shear displacement structure (i.e., fault or shear) by extending the abstract property block ShearDisplacementStructureAbstractDescription.

**Supertype**: `ShearDisplacementStructureAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `deformationStyle` | (oneOf - see schema) | 0..1 | The deformationStyle:DeformationStyleTerm contains a term from a vocabulary to describe the style of deformation, i.e… |
| `planeOrientation` | (oneOf - see schema) | 0..1 | The property planeOrientation:GSML_PlanarOrientation contains a description of the orientation of a structure’s plana… |
| `stPhysicalProperty` | (oneOf - see schema) | 0..1 | The property stPhysicalProperty:PhysicalDescription contains a value of generic physical properties not addressed in … |

### `SlipComponents`

SlipComponents is a kind of DisplacementValue that is a representation of slip as a vector resolved into components within a reference frame in which horizontal axes are parallel and perpendicular to the strike of the fault. At least one of heave, horizontalSlip, or throw must not be null.

**Supertype**: [`DisplacementValue`](#DisplacementValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `heave` | (oneOf - see schema) | 0..1 | The property heave:GSML_Vector contains a component of slip in the horizontal, and perpendicular to the strike of the… |
| `horizontalSlip` | (oneOf - see schema) | 0..1 | The property horizontalSlip:GSML_Vector contains a slip component that is horizontal and parallel to strike of the fa… |
| `throw` | (oneOf - see schema) | 0..1 | The property throw:GSML_Vector contains the vertical component of slip. |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `DeformationStyleTerm` | `_(treat as open - no `codeList` annotation)_` |
| `LineationTypeTerm` | `_(treat as open - no `codeList` annotation)_` |
| `MovementSenseTerm` | `_(treat as open - no `codeList` annotation)_` |
| `MovementTypeTerm` | `_(treat as open - no `codeList` annotation)_` |
| `NonDirectionalStructureTypeTerm` | `_(treat as open - no `codeList` annotation)_` |

## External dependencies

- `../gsmBasicGeology/gsmBasicGeologySchema.json#ContactAbstractDescription`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#Fold`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#FoldAbstractDescription`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#Foliation`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#FoliationAbstractDescription`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#GSML_LinearOrientation`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#GSML_PlanarOrientation`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#GSML_Vector`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicStructure`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#RockMaterial`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#ShearDisplacementStructureAbstractDescription`
- `../gsmEarthMaterial/gsmEarthMaterialSchema.json#Mineral`
- `../gsmEarthMaterial/gsmEarthMaterialSchema.json#PhysicalDescription`
- `../gsmGeologicTime/gsmGeologicTimeSchema.json#GeochronologicBoundary`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [examplegsmGeologicStructureExtensionMinimal.json](examples/examplegsmGeologicStructureExtensionMinimal.json)
- [fc_fault_displacement_events_GSO.json](examples/fc_fault_displacement_events_GSO.json)
- [fc_kanna_thrust_faults_GSO.json](examples/fc_kanna_thrust_faults_GSO.json)
- [fold_system_simple.json](examples/fold_system_simple.json)
- [lineation_complex.json](examples/lineation_complex.json)
- [lineation_simple.json](examples/lineation_simple.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicStructureDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
