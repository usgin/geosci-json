
# gsmGeologicStructureExtension (Schema)

`usgin.bbr.geosci.gsmGeologicStructureExtension` *v0.1*

Detailed structural-geology types extending the Basic structure

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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
| `contactCharacter` | (oneOf — see schema) | 0..1 | The contactCharacter (SWE::Category) contains a term from a controlled vocabulary that describes the character of the… |
| `orientation` | (oneOf — see schema) | 0..1 | The orientation:GSML_PlanarOrientation property reports the general orientation of the contact surface. |
| `correlatesWith` | (oneOf — see schema) | 0..1 | The correlatesWith property is an association between ContactDescription and a GeochronologicBoundary describing a ge… |

### `DisplacementEvent`

A displacement event is a description of the age, environment and process of a shear displacement event.

**Supertype**: `GeologicEvent` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `incrementalDisplacement` | (oneOf — see schema) | 0..1 | The incrementalDisplacement:DisplacementValue property contains a DisplacementValue reporting the parameters of the d… |

### `DisplacementValue`

A displacement value expresses the displacement on a fault with respect to a planar approximation of its shape.

**Supertype**: `ShearDisplacementStructureAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `hangingWallDirection` | (oneOf — see schema) | 0..1 | The property hangingWallDirection:GSML_LinearOrientation describes the direction of the hanging-wall side of the faul… |
| `movementSense` | (oneOf — see schema) | 0..1 | The property movementSense:MovementSenseTerm contains a term from a controlled vocabulary that describes the movement… |
| `movementType` | (oneOf — see schema) | 0..1 | The property movementType:MovementTypeTerm contains a term from a controlled vocabulary that defines the type of move… |
| `displacementEvent` | (oneOf — see schema) | 0..1 | The property displacementEvent is an association between a Displacement and a GeologicEvent that contains a descripti… |

### `FoldDescription`

FoldDescription is an extended descriptive property of a fold structure.

**Supertype**: `FoldAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `amplitude` | (oneOf — see schema) | 0..1 | The amplitude property (SWE::QuantityRange) reports the length from line segment connecting inflection points on adja… |
| `axialSurfaceOrientation` | (oneOf — see schema) | 0..1 | The property axialSurfaceOrientation:GSML_PlanarOrientation is used to characterize the geometry of a fold. The axial… |
| `geneticModel` | (oneOf — see schema) | 0..1 | The property geneticModel (SWE::Category) contains a term from a controlled vocabulary describing the specification o… |
| `hingeLineCurvature` | (oneOf — see schema) | 0..1 | The hingeLineCurvature property (SWE::Category) contains a term from a controlled vocabulary that describes the varia… |
| `hingeLineOrientation` | (oneOf — see schema) | 0..1 | The property hingeLineOrientation:GSML_LinearOrientation reports the specification of the hinge line orientation for … |
| `hingeShape` | (oneOf — see schema) | 0..1 | The property hingeShape (SWE::Category) reports a term from a controlled vocabulary describing the hinge shape, e.g. … |
| `interLimbAngle` | (oneOf — see schema) | 0..1 | The property interLimbAngle (SWE::Category) contains a term from a controlled vocabulary describing the interlimb ang… |
| `limbShape` | (oneOf — see schema) | 0..1 | The limbShape property (SWE::Category) contains a term from a controlled vocabulary describing the shape of the limb … |
| `span` | (oneOf — see schema) | 0..1 | The span property (SWE::QuantityRange) reports a value describing the linear distance between inflection points in a … |
| `symmetry` | (oneOf — see schema) | 0..1 | The symmetry property (SWE::Category) contains a term from a controlled vocabulary describing the concordance or disc… |
| `system` | (oneOf — see schema) | 0..1 | The system property is an association between a FoldDescription and a FoldSystem that aggregates folds into a system. |

### `FoldSystem`

A FoldSystem is a collection of congruent folds (axis and axial surface are parallel) produced by the same tectonic event. It is sometimes referred to as a "fold train".  Constraint: if periodic=False then count(Wavelength)=0

**Supertype**: `GeologicStructure` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `periodic` | (oneOf — see schema) | 0..1 | The property periodic:Primitive::Boolean reports TRUE if the hinges in a train are regularly spaced, and FALSE otherw… |
| `wavelength` | (oneOf — see schema) | 0..1 | The property wavelength (SWE::QuantityRange) contains a quantitative description of the length between adjacent antif… |
| `foldSystemMember` | (oneOf — see schema) | 0..1 | The foldSystemMember is an association between a FoldSystem and the Folds that are members of that system. |

### `FoliationDescription`

FoliationDescription provides extended descriptive properties for a foliation structure.

**Supertype**: `FoliationAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `definingElement` | (oneOf — see schema) | 0..1 | The property definingElement (SWE::Category) contains a term from a controlled vocabulary describing the kinds of inh… |
| `continuity` | (oneOf — see schema) | 0..1 | The continuity property (SWE::Category) reports a term from a controlled vocabulary to distinguish continuous vs. dis… |
| `intensity` | (oneOf — see schema) | 0..1 | The intensity property (SWE::Category) contains a term from a controlled vocabulary to describe how well the foliatio… |
| `mineralElement` | (oneOf — see schema) | 0..1 | The mineralElement property is an association between FoliationDescription and a Mineral that defines that foliation. |
| `orientation` | (oneOf — see schema) | 0..1 | The orientation:GSML_PlanarOrientation contains an estimate of the planar orientation of the foliation structure. |
| `spacing` | (oneOf — see schema) | 0..1 | The spacing property (SWE::QuantityRange) contains a linear dimension representing the thickness of foliation domains… |

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
| `layerComposition` | (oneOf — see schema) | 0..1 | The layerComposition property is an association between a Layering and a RockMaterial that describes the rock materia… |

### `Lineation`

GeologicStructure defined by aligned elongate elements. Lineation connotes a pervasive linear structure. Includes: flow lines, scratches, striae, slickenlines, linear arrangements of elongate components in sediments, fold hinges (when abundant and closely spaced), elongate minerals, crinkles, and lines of intersection between penetrative planar structures. Class also includes discrete linear structures like boudin, channel axis, tool marks.

**Supertype**: `GeologicStructure` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `lineationType` | (oneOf — see schema) | 0..1 | Type of lineation. Examples include: flow lines, scratches, striae, slickenlines, linear arrangements of elongate com… |
| `definingElement` | (oneOf — see schema) | 0..1 | Kinds of describable inhomogeneity in a rock body that may define a GeologicStructure. Examples include Oriented Part… |
| `intensity` | (oneOf — see schema) | 0..1 | How well the lineation is developed. Terms such as weak, moderate, strong. |
| `mineralElement` | (oneOf — see schema) | 0..1 | Mineral that defines the lineation |
| `orientation` | (oneOf — see schema) | 0..1 | Orientation of the lineation |

### `NetSlipValue`

NetSlipValue is a kind of DisplacementValue that describes the total amount of slip displacement along a structure.

**Supertype**: [`DisplacementValue`](#DisplacementValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `netSlip` | (oneOf — see schema) | 0..1 | The property netSlip:GSML_Vector reports the value of the net slip, expressed as a vector. |
| `slipComponent` | (oneOf — see schema) | 0..1 | The slipComponent:SlipComponents property associates the individual slip components with the net slip values. |

### `NonDirectionalStructure`

Structures present in geology that do not have a preferred orientation Includes small-scale structures that are characteristic of the geologic unit, e.g. herringbone crossbedding, mudcracks, graded bedding, planar lamination, miarolitic cavities, nebulitic structure, trace fossils, fossil molds

**Supertype**: `GeologicStructure` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `structureType` | (oneOf — see schema) | 0..1 | The type of non oriented structure. Examples include miarolitic cavity, flame structure, load cast, shatter cone, tra… |

### `SeparationValue`

SeparationValue is a kind of DisplacementValue that describes the amount of separation displacement across a structure.

**Supertype**: [`DisplacementValue`](#DisplacementValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `separation` | (oneOf — see schema) | 0..1 | The property separation:GSML_Vector reports the apparent offset across a planar feature, reported as a vector. |

### `ShearDisplacementStructureDescription`

ShearDisplacementStructureDescription provides extended descriptive properties of a shear displacement structure (i.e., fault or shear) by extending the abstract property block ShearDisplacementStructureAbstractDescription.

**Supertype**: `ShearDisplacementStructureAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `deformationStyle` | (oneOf — see schema) | 0..1 | The deformationStyle:DeformationStyleTerm contains a term from a vocabulary to describe the style of deformation, i.e… |
| `planeOrientation` | (oneOf — see schema) | 0..1 | The property planeOrientation:GSML_PlanarOrientation contains a description of the orientation of a structure’s plana… |
| `stPhysicalProperty` | (oneOf — see schema) | 0..1 | The property stPhysicalProperty:PhysicalDescription contains a value of generic physical properties not addressed in … |

### `SlipComponents`

SlipComponents is a kind of DisplacementValue that is a representation of slip as a vector resolved into components within a reference frame in which horizontal axes are parallel and perpendicular to the strike of the fault. At least one of heave, horizontalSlip, or throw must not be null.

**Supertype**: [`DisplacementValue`](#DisplacementValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `heave` | (oneOf — see schema) | 0..1 | The property heave:GSML_Vector contains a component of slip in the horizontal, and perpendicular to the strike of the… |
| `horizontalSlip` | (oneOf — see schema) | 0..1 | The property horizontalSlip:GSML_Vector contains a slip component that is horizontal and parallel to strike of the fa… |
| `throw` | (oneOf — see schema) | 0..1 | The property throw:GSML_Vector contains the vertical component of slip. |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `DeformationStyleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `LineationTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `MovementSenseTerm` | `_(treat as open — no `codeList` annotation)_` |
| `MovementTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `NonDirectionalStructureTypeTerm` | `_(treat as open — no `codeList` annotation)_` |

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

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicStructureDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### examplegsmGeologicStructureExtensionMinimal
Example instance: examplegsmGeologicStructureExtensionMinimal
#### json
```json
{
  "type": "Feature",
  "id": "displacementevent.minimal.1",
  "featureType": "DisplacementEvent",
  "geometry": null,
  "properties": {}
}

```


### fc fault displacement events GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleFault2.ttl. The source describes multiple fault structures with associated displacement events. The fault structures themselves are gsmscimlBasic#ShearDisplacementStructure features (referenced by URL via sampledFeature-like links); the EVENTS of fault movement are gsmGeologicStructureExtension#DisplacementEvent features, which is what this BB's dispatcher accepts. Each DisplacementEvent here references the corresponding ShearDisplacementStructure in a by-reference link in `incrementalDisplacement`.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleFault2.ttl. The source describes multiple fault structures with associated displacement events. The fault structures themselves are gsmscimlBasic#ShearDisplacementStructure features (referenced by URL via sampledFeature-like links); the EVENTS of fault movement are gsmGeologicStructureExtension#DisplacementEvent features, which is what this BB's dispatcher accepts. Each DisplacementEvent here references the corresponding ShearDisplacementStructure in a by-reference link in `incrementalDisplacement`.",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "DisplacementEvent",
      "id": "https://w3id.org/gso/1.0/ex-faults#FaultA_movement_event",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "eventProcess": [
          "http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"
        ],
        "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Triassic",
        "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Jurassic"
      }
    },
    {
      "type": "Feature",
      "featureType": "DisplacementEvent",
      "id": "https://w3id.org/gso/1.0/ex-faults#FaultB_movement_event",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "eventProcess": [
          "http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"
        ],
        "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Jurassic",
        "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Cretaceous"
      }
    }
  ]
}

```


### fc kanna thrust faults GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleFaultKannaV4Model.ttl. The source defines four Thrust_Fault structures (D02_fault, Fatigue_fault, Simpson_fault, N01_fault) and their displacement events. Crosscut relationships in the TTL (gsrl:crosscuts) link Fatigue → {D02, N01, Simpson}, indicating Fatigue is the youngest. This FC encodes each fault's displacement event as a DisplacementEvent; the cross-cutting age relationships are conveyed through the olderNamedAge/youngerNamedAge ordering and noted in $comments. The fault structures themselves (ShearDisplacementStructure) live in gsmscimlBasic and are by-reference here.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleFaultKannaV4Model.ttl. The source defines four Thrust_Fault structures (D02_fault, Fatigue_fault, Simpson_fault, N01_fault) and their displacement events. Crosscut relationships in the TTL (gsrl:crosscuts) link Fatigue → {D02, N01, Simpson}, indicating Fatigue is the youngest. This FC encodes each fault's displacement event as a DisplacementEvent; the cross-cutting age relationships are conveyed through the olderNamedAge/youngerNamedAge ordering and noted in $comments. The fault structures themselves (ShearDisplacementStructure) live in gsmscimlBasic and are by-reference here.",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "DisplacementEvent",
      "id": "https://w3id.org/gso/1.0/fautlKannaV4Model#D02_fault_displacement",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "eventProcess": ["http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"]
      }
    },
    {
      "type": "Feature",
      "featureType": "DisplacementEvent",
      "id": "https://w3id.org/gso/1.0/fautlKannaV4Model#Simpson_fault_displacement",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "eventProcess": ["http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"]
      }
    },
    {
      "type": "Feature",
      "featureType": "DisplacementEvent",
      "id": "https://w3id.org/gso/1.0/fautlKannaV4Model#N01_fault_displacement",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "eventProcess": ["http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"]
      }
    },
    {
      "$comment": "Fatigue Thrust fault is the youngest; crosscuts the other three thrusts per the source TTL.",
      "type": "Feature",
      "featureType": "DisplacementEvent",
      "id": "https://w3id.org/gso/1.0/fautlKannaV4Model#Fatigue_fault_displacement",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "eventProcess": ["http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"]
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json
description: 'Detailed structural-geology types extending the Basic structure

  hierarchy: FoldDescription, FoliationDescription, FoldSystem, Joint,

  Fracture, DisplacementEvent, DisplacementValue, Lineation, Layering,

  NonDirectionalStructure, etc.


  Validates either a single Feature (dispatched by `featureType` to one of: DisplacementEvent,
  FoldSystem, Joint, Layering, Lineation, NonDirectionalStructure) or a FeatureCollection
  whose `features[]` items are dispatched the same way.'
if:
  type: object
  required:
  - type
  properties:
    type:
      const: FeatureCollection
then:
  allOf:
  - $ref: https://schemas.opengis.net/json-fg/featurecollection.json
  - type: object
    properties:
      features:
        type: array
        items:
          $ref: '#/$defs/_FeatureDispatch'
else:
  $ref: '#/$defs/_FeatureDispatch'
$defs:
  _FeatureDispatch:
    allOf:
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: DisplacementEvent
      then:
        $ref: '#DisplacementEvent'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: FoldSystem
      then:
        $ref: '#FoldSystem'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: Joint
      then:
        $ref: '#Joint'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: Layering
      then:
        $ref: '#Layering'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: Lineation
      then:
        $ref: '#Lineation'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: NonDirectionalStructure
      then:
        $ref: '#NonDirectionalStructure'
    - if:
        not:
          required:
          - featureType
          properties:
            featureType:
              enum:
              - DisplacementEvent
              - FoldSystem
              - Joint
              - Layering
              - Lineation
              - NonDirectionalStructure
      then: false
  ContactDescription:
    $anchor: ContactDescription
    description: The ContactDescription provides extended descriptive properties of
      a geologic contact. If the contact type is ChronostratigraphicBoundary, it can
      be associated with a geochronologic (i.e., time zone) boundary that may correlate
      with it.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#ContactAbstractDescription
      $comment: cross-BB supertype reference to ContactAbstractDescription in BB gsmBasicGeology
    - type: object
      properties:
        contactCharacter:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The contactCharacter (SWE::Category) contains a term from a
            controlled vocabulary that describes the character of the boundary (e.g.
            abrupt, gradational), as opposed to its type.
        orientation:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_PlanarOrientation
            $comment: cross-BB inline reference to GSML_PlanarOrientation in BB gsmBasicGeology
          description: The orientation:GSML_PlanarOrientation property reports the
            general orientation of the contact surface.
        correlatesWith:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to GeochronologicBoundary
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#GeochronologicBoundary
              $comment: cross-BB inline reference to GeochronologicBoundary in BB
                gsmGeologicTime
          description: The correlatesWith property is an association between ContactDescription
            and a GeochronologicBoundary describing a geochronologic (i.e., time zone)
            boundary that may correlate with it. Therefore, a contact correlation
            with a GeochronologicBoundary SHALL ONLY be allowed when the contactType
            is a ChronostratigraphicBoundary.
  DeformationStyleTerm:
    $anchor: DeformationStyleTerm
    description: A controlled vocabulary of terms describing the style of deformation
      (eg, brittle, ductile).
    type: string
    format: uri
  DisplacementEvent:
    $anchor: DisplacementEvent
    description: A displacement event is a description of the age, environment and
      process of a shear displacement event.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent
      $comment: cross-BB supertype reference to GeologicEvent in BB gsmBasicGeology
    - type: object
      properties:
        properties:
          type: object
          properties:
            incrementalDisplacement:
              oneOf:
              - type: 'null'
              - $ref: '#DisplacementValue'
              description: The incrementalDisplacement:DisplacementValue property
                contains a DisplacementValue reporting the parameters of the displacement.
  DisplacementValue:
    $anchor: DisplacementValue
    description: A displacement value expresses the displacement on a fault with respect
      to a planar approximation of its shape.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#ShearDisplacementStructureAbstractDescription
      $comment: cross-BB supertype reference to ShearDisplacementStructureAbstractDescription
        in BB gsmBasicGeology
    - type: object
      properties:
        hangingWallDirection:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_LinearOrientation
            $comment: cross-BB inline reference to GSML_LinearOrientation in BB gsmBasicGeology
          description: 'The property hangingWallDirection:GSML_LinearOrientation describes
            the direction of the hanging-wall side of the fault or fault-system where
            they are steep enough to define a hanging-wall on the map trace.  Constraint:
            displacementDirection'
        movementSense:
          oneOf:
          - type: 'null'
          - $ref: '#MovementSenseTerm'
          description: The property movementSense:MovementSenseTerm contains a term
            from a controlled vocabulary that describes the movement sense of displacement
            along a geologic structure (e.g., dextral, sinistral).
        movementType:
          oneOf:
          - type: 'null'
          - $ref: '#MovementTypeTerm'
          description: The property movementType:MovementTypeTerm contains a term
            from a controlled vocabulary that defines the type of movement on a shear
            displacement structure (e.g. dip-slip, strike-slip).
        displacementEvent:
          oneOf:
          - type: 'null'
          - type: array
            items:
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
                $comment: by-reference link to DisplacementEvent
              - $ref: '#DisplacementEvent'
            uniqueItems: true
          description: The property displacementEvent is an association between a
            Displacement and a GeologicEvent that contains a description of the age,
            environment and process of a shear displacement event.
  FoldDescription:
    $anchor: FoldDescription
    description: FoldDescription is an extended descriptive property of a fold structure.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#FoldAbstractDescription
      $comment: cross-BB supertype reference to FoldAbstractDescription in BB gsmBasicGeology
    - type: object
      properties:
        amplitude:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The amplitude property (SWE::QuantityRange) reports the length
            from line segment connecting inflection points on adjacent fold limbs
            to the intervening fold hinge.
        axialSurfaceOrientation:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_PlanarOrientation
            $comment: cross-BB inline reference to GSML_PlanarOrientation in BB gsmBasicGeology
          description: The property axialSurfaceOrientation:GSML_PlanarOrientation
            is used to characterize the geometry of a fold. The axial surface of a
            particular fold may be located based on observations of the folded geologic
            structure, but in general it has no direct physical manifestations. As
            a geologic surface, it has geometric properties, including orientation,
            which may be specified by observations at one or more locations, or generalized
            using terminology (upright, inclined, reclined, recumbent, overturned).
            Dip and Dip Direction are one approach to specifying the value.
        geneticModel:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The property geneticModel (SWE::Category) contains a term from
            a controlled vocabulary describing the specification of genetic model
            for fold, e.g. flexural slip, parallel.
        hingeLineCurvature:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The hingeLineCurvature property (SWE::Category) contains a
            term from a controlled vocabulary that describes the variation in orientation
            of fold hinge along trend of fold, distinguishing sheath from cylindrical
            folds (e.g. sheath, dome, basin, cylindrical.).
        hingeLineOrientation:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_LinearOrientation
            $comment: cross-BB inline reference to GSML_LinearOrientation in BB gsmBasicGeology
          description: 'The property hingeLineOrientation:GSML_LinearOrientation reports
            the specification of the hinge line orientation for fold. GSML_LinearOrientation
            allows for a term value specification or a numeric specification of either
            or both the trend and plunge of hinge line. Hinge plunge term examples:
            sub-vertical, steeply plunging, sub-horizontal, reclined and vertical
            for special cases in which hinge plunge is close to axial surface dip.
            0..* cardinality allows for both a numeric specification and a term specification.'
        hingeShape:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The property hingeShape (SWE::Category) reports a term from
            a controlled vocabulary describing the hinge shape, e.g. Rounded vs. angular
            hinge zones. This property has to do with the proportion of the wavelength
            that is considered part of hinge.
        interLimbAngle:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: "The property interLimbAngle (SWE::Category) contains a term
            from a controlled vocabulary describing the interlimb angle using a tightness
            term (e.g. gentle (120-180\xB0), open (70-120\xB0), close (30-70\xB0),
            tight (10-30\xB0), isoclinal (0-10\xB0))."
        limbShape:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The limbShape property (SWE::Category) contains a term from
            a controlled vocabulary describing the shape of the limb (e.g. straight
            vs curved limbs, kink, chevron, sinusoidal, box).
        span:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The span property (SWE::QuantityRange) reports a value describing
            the linear distance between inflection points in a single fold.
        symmetry:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The symmetry property (SWE::Category) contains a term from
            a controlled vocabulary describing the concordance or discordance of bisecting
            surface and axial surface, or the ratio of length of limbs. The folded
            surface may have asymmetry defined by limb length ratio if inflection
            points are defined. The definition based on bisecting surface/axial surface
            angle depends on having multiple surfaces defined such that the axial
            surface may be identified (symmetric, asymmetric).
        system:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to FoldSystem
            - $ref: '#FoldSystem'
          description: The system property is an association between a FoldDescription
            and a FoldSystem that aggregates folds into a system.
  FoldSystem:
    $anchor: FoldSystem
    description: 'A FoldSystem is a collection of congruent folds (axis and axial
      surface are parallel) produced by the same tectonic event. It is sometimes referred
      to as a "fold train".  Constraint: if periodic=False then count(Wavelength)=0'
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicStructure
      $comment: cross-BB supertype reference to GeologicStructure in BB gsmBasicGeology
    - type: object
      properties:
        properties:
          type: object
          properties:
            periodic:
              oneOf:
              - type: 'null'
              - type: boolean
              description: The property periodic:Primitive::Boolean reports TRUE if
                the hinges in a train are regularly spaced, and FALSE otherwise.
            wavelength:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
              description: The property wavelength (SWE::QuantityRange) contains a
                quantitative description of the length between adjacent antiforms
                (or synforms) in a fold train.
            foldSystemMember:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to Fold
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#Fold
                    $comment: cross-BB inline reference to Fold in BB gsmBasicGeology
                uniqueItems: true
              description: The foldSystemMember is an association between a FoldSystem
                and the Folds that are members of that system.
  FoliationDescription:
    $anchor: FoliationDescription
    description: FoliationDescription provides extended descriptive properties for
      a foliation structure.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#FoliationAbstractDescription
      $comment: cross-BB supertype reference to FoliationAbstractDescription in BB
        gsmBasicGeology
    - type: object
      properties:
        definingElement:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The property definingElement (SWE::Category) contains a term
            from a controlled vocabulary describing the kinds of inhomogeneity in
            a rock body that may define a GeologicStructure. Examples include discontinuity,
            shaped surface, oriented particle, material boundary, and layer.
        continuity:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The continuity property (SWE::Category) reports a term from
            a controlled vocabulary to distinguish continuous vs. disjunct cleavages.
        intensity:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The intensity property (SWE::Category) contains a term from
            a controlled vocabulary to describe how well the foliation is developed
            (e.g., weak, moderate, strong).
        mineralElement:
          oneOf:
          - type: 'null'
          - type: array
            items:
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
                $comment: by-reference link to Mineral
              - $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterial/gsmEarthMaterialSchema.json#Mineral
                $comment: cross-BB inline reference to Mineral in BB gsmEarthMaterial
            uniqueItems: true
          description: The mineralElement property is an association between FoliationDescription
            and a Mineral that defines that foliation.
        orientation:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_PlanarOrientation
            $comment: cross-BB inline reference to GSML_PlanarOrientation in BB gsmBasicGeology
          description: The orientation:GSML_PlanarOrientation contains an estimate
            of the planar orientation of the foliation structure.
        spacing:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The spacing property (SWE::QuantityRange) contains a linear
            dimension representing the thickness of foliation domains. It is also
            used for thickness of layers of a given composition.
  Fracture:
    $anchor: Fracture
    description: Fractures are cracks in the earth surface. If there is no displacement
      it is a joint. If there is displacement and you are in the brittle zone it is
      a fault. In the ductile zone, a fracture with displacement with fracture is
      called a shear. FaultSurface as a separate class is not considered necessary
      for GeoSciML 2. Recording observations on FaultSurface should be in observation
      and measurement. The observation needs to be able to distinguish the type of
      measurement made (PropertyType)
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicStructure
      $comment: cross-BB supertype reference to GeologicStructure in BB gsmBasicGeology
    - type: object
      properties:
        properties:
          type: object
          properties: {}
  Joint:
    $anchor: Joint
    description: Fracture across which there is no displacement at the scale of interest.
    allOf:
    - $ref: '#Fracture'
    - type: object
      properties:
        properties:
          type: object
          properties: {}
  Layering:
    $anchor: Layering
    description: A planar foliation is defined by a tabular succession of layers &gt;
      5 mm thick. This definition is based on the proposed definition of gneiss by
      the NADM Science Language Technical Team. The GeologicStructure characteristic
      of gneiss is layering.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#Foliation
      $comment: cross-BB supertype reference to Foliation in BB gsmBasicGeology
    - type: object
      properties:
        properties:
          type: object
          properties:
            layerComposition:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to RockMaterial
                - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#RockMaterial
                  $comment: cross-BB inline reference to RockMaterial in BB gsmBasicGeology
              description: The layerComposition property is an association between
                a Layering and a RockMaterial that describes the rock material that
                may define compositional layering.
  Lineation:
    $anchor: Lineation
    description: 'GeologicStructure defined by aligned elongate elements. Lineation
      connotes a pervasive linear structure. Includes: flow lines, scratches, striae,
      slickenlines, linear arrangements of elongate components in sediments, fold
      hinges (when abundant and closely spaced), elongate minerals, crinkles, and
      lines of intersection between penetrative planar structures. Class also includes
      discrete linear structures like boudin, channel axis, tool marks.'
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicStructure
      $comment: cross-BB supertype reference to GeologicStructure in BB gsmBasicGeology
    - type: object
      properties:
        properties:
          type: object
          properties:
            lineationType:
              oneOf:
              - type: 'null'
              - $ref: '#LineationTypeTerm'
              description: 'Type of lineation. Examples include: flow lines, scratches,
                striae, slickenlines, linear arrangements of elongate components in
                sediments, elongate minerals, crinkles, and lines of intersection
                between penetrative planar structures.'
            definingElement:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
                uniqueItems: true
              description: Kinds of describable inhomogeneity in a rock body that
                may define a GeologicStructure. Examples include Oriented Particle.
            intensity:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
              description: How well the lineation is developed. Terms such as weak,
                moderate, strong.
            mineralElement:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to Mineral
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterial/gsmEarthMaterialSchema.json#Mineral
                    $comment: cross-BB inline reference to Mineral in BB gsmEarthMaterial
                uniqueItems: true
              description: Mineral that defines the lineation
            orientation:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_LinearOrientation
                  $comment: cross-BB inline reference to GSML_LinearOrientation in
                    BB gsmBasicGeology
                uniqueItems: true
              description: Orientation of the lineation
  LineationTypeTerm:
    $anchor: LineationTypeTerm
    description: 'Refers to a vocabulary of terms describing the type of lineation.
      Examples include: flow lines, scratches, striae, slickenlines, linear arrangements
      of elongate components in sediments, elongate minerals, crinkles, and lines
      of intersection between penetrative planar structures.'
    type: string
    format: uri
  MovementSenseTerm:
    $anchor: MovementSenseTerm
    description: Refers to a vocabulary of terms describing the sense of movement
      on a shear displacement structure
    type: string
    format: uri
  MovementTypeTerm:
    $anchor: MovementTypeTerm
    description: Refers to a vocabulary of terms describing the type of movement (eg,
      dip-slip, strike-slip)
    type: string
    format: uri
  NetSlipValue:
    $anchor: NetSlipValue
    description: NetSlipValue is a kind of DisplacementValue that describes the total
      amount of slip displacement along a structure.
    allOf:
    - $ref: '#DisplacementValue'
    - type: object
      properties:
        netSlip:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_Vector
            $comment: cross-BB inline reference to GSML_Vector in BB gsmBasicGeology
          description: The property netSlip:GSML_Vector reports the value of the net
            slip, expressed as a vector.
        slipComponent:
          oneOf:
          - type: 'null'
          - $ref: '#SlipComponents'
          description: The slipComponent:SlipComponents property associates the individual
            slip components with the net slip values.
  NonDirectionalStructure:
    $anchor: NonDirectionalStructure
    description: Structures present in geology that do not have a preferred orientation
      Includes small-scale structures that are characteristic of the geologic unit,
      e.g. herringbone crossbedding, mudcracks, graded bedding, planar lamination,
      miarolitic cavities, nebulitic structure, trace fossils, fossil molds
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicStructure
      $comment: cross-BB supertype reference to GeologicStructure in BB gsmBasicGeology
    - type: object
      properties:
        properties:
          type: object
          properties:
            structureType:
              oneOf:
              - type: 'null'
              - $ref: '#NonDirectionalStructureTypeTerm'
              description: The type of non oriented structure. Examples include miarolitic
                cavity, flame structure, load cast, shatter cone, trace fossil, fossil
                mold
  NonDirectionalStructureTypeTerm:
    $anchor: NonDirectionalStructureTypeTerm
    description: Refers to a vocabulary of terms describing types of non-directional
      structures (eg, miarolitic cavity, flame structure, load cast, shatter cone,
      trace fossil, fossil mold, etc)
    type: string
    format: uri
  SeparationValue:
    $anchor: SeparationValue
    description: SeparationValue is a kind of DisplacementValue that describes the
      amount of separation displacement across a structure.
    allOf:
    - $ref: '#DisplacementValue'
    - type: object
      properties:
        separation:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_Vector
            $comment: cross-BB inline reference to GSML_Vector in BB gsmBasicGeology
          description: The property separation:GSML_Vector reports the apparent offset
            across a planar feature, reported as a vector.
  ShearDisplacementStructureDescription:
    $anchor: ShearDisplacementStructureDescription
    description: ShearDisplacementStructureDescription provides extended descriptive
      properties of a shear displacement structure (i.e., fault or shear) by extending
      the abstract property block ShearDisplacementStructureAbstractDescription.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#ShearDisplacementStructureAbstractDescription
      $comment: cross-BB supertype reference to ShearDisplacementStructureAbstractDescription
        in BB gsmBasicGeology
    - type: object
      properties:
        deformationStyle:
          oneOf:
          - type: 'null'
          - $ref: '#DeformationStyleTerm'
          description: The deformationStyle:DeformationStyleTerm contains a term from
            a vocabulary to describe the style of deformation, i.e. brittle (fault,
            breccia), ductile (shear), brittle-ductile, unknown.
        planeOrientation:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_PlanarOrientation
            $comment: cross-BB inline reference to GSML_PlanarOrientation in BB gsmBasicGeology
          description: "The property planeOrientation:GSML_PlanarOrientation contains
            a description of the orientation of a structure\u2019s planar surface."
        stPhysicalProperty:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterial/gsmEarthMaterialSchema.json#PhysicalDescription
              $comment: cross-BB inline reference to PhysicalDescription in BB gsmEarthMaterial
            uniqueItems: true
          description: The property stPhysicalProperty:PhysicalDescription contains
            a value of generic physical properties not addressed in this model.
  SlipComponents:
    $anchor: SlipComponents
    description: SlipComponents is a kind of DisplacementValue that is a representation
      of slip as a vector resolved into components within a reference frame in which
      horizontal axes are parallel and perpendicular to the strike of the fault. At
      least one of heave, horizontalSlip, or throw must not be null.
    allOf:
    - $ref: '#DisplacementValue'
    - type: object
      properties:
        heave:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_Vector
            $comment: cross-BB inline reference to GSML_Vector in BB gsmBasicGeology
          description: The property heave:GSML_Vector contains a component of slip
            in the horizontal, and perpendicular to the strike of the fault.
        horizontalSlip:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_Vector
            $comment: cross-BB inline reference to GSML_Vector in BB gsmBasicGeology
          description: The property horizontalSlip:GSML_Vector contains a slip component
            that is horizontal and parallel to strike of the fault.
        throw:
          oneOf:
          - type: 'null'
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GSML_Vector
            $comment: cross-BB inline reference to GSML_Vector in BB gsmBasicGeology
          description: The property throw:GSML_Vector contains the vertical component
            of slip.
  SCLinkObject:
    title: link object
    description: SCLinkObject originates from ShapeChange implementation of https://schemas.opengis.net/ogcapi/common/part1/1.0/openapi/schemas/link.json,
      based on RFC 8288 web linking.
    type: object
    required:
    - href
    properties:
      href:
        type: string
        description: Supplies the URI to a remote resource (or resource fragment).
      rel:
        type: string
        description: The type or semantics of the relation.
      type:
        type: string
        description: A hint indicating what the media type of the result of dereferencing
          the link should be.
      hreflang:
        type: string
        description: A hint indicating what the language of the result of dereferencing
          the link should be.
      title:
        type: string
        description: Used to label the destination of a link such that it can be used
          as a human-readable identifier.
      length:
        type: integer

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmGeologicStructureExtension/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmGeologicStructureExtension/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmGeologicStructureExtension`

