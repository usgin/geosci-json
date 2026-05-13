
# gsmEarthMaterial (Schema)

`usgin.bbr.geosci.gsmEarthMaterial` *v0.1*

EarthMaterial building block. Combines the formerly-separate

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmEarthMaterial

GeoSciML 4.1 building block `gsmEarthMaterial`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `EarthMaterialDetails`.

Contains 14 data types, 6 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AlterationDescription` | «DataType» | plain JSON object |
| `AlterationTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `ChemicalComposition` | «DataType» | plain JSON object |
| `CompoundMaterialDescription` | «DataType» | plain JSON object |
| `ConstituentPart` | «DataType» | plain JSON object |
| `ConstituentPartRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `FabricDescription` | «DataType» | plain JSON object |
| `FabricTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `InorganicFluid` | «DataType» | plain JSON object |
| `MetamorphicDescription` | «DataType» | plain JSON object |
| `Mineral` | «DataType» | plain JSON object |
| `MineralNameTerm` | «CodeList» | URI codelist (`format: uri`) |
| `OrganicMaterial` | «DataType» | plain JSON object |
| `Organism` | «DataType» | plain JSON object |
| `ParticleGeometryDescription` | «DataType» | plain JSON object |
| `ParticleTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `PhysicalDescription` | «DataType» | plain JSON object |
| `PhysicalPropertyTerm` | «CodeList» | URI codelist (`format: uri`) |
| `RockMaterialDescription` | «DataType» | plain JSON object |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `AlterationDescription`

AlterationDescription describes aspects of a geologic unit or earth material that are the result of bulk chemical, mineralogical or physical changes related to change in the physical or chemical environment. It includes weathering, supergene alteration, hydrothermal alteration and metasomatic effects not considered metamorphic. For example, a soil profile description would have to be constructed as a GeologicUnit (geologicUnitType = PedologicUnit) with unit parts representing the various horizons in the profile. Thickness of a weathering profile can be delivered as unitThickness of a GeologicUnit of geologicUnitType equal to "AlterationUnit"

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `alterationType` | (oneOf - see schema) | 0..1 | The property alterationType:AlterationTypeTerm contains a term from a controlled vocabulary of alteration types (e.g.… |
| `alterationProduct` | (oneOf - see schema) | 0..1 | The property alterationProduct is an association between the AlterationDescripton and EarthMaterial describing the ma… |
| `alterationDistribution` | (oneOf - see schema) | 0..1 | The alterationDistribution (SWE::Category) property describes the spatial distribution or geometry of alteration zone… |
| `alterationDegree` | (oneOf - see schema) | 0..1 | The property alterationDegree (SWE::Category) contains a term from a controlled vocabulary to indicate the magnitude … |
| `alterationEvent` | (oneOf - see schema) | 0..1 | The property alterationEvent is an association between an AlterationDescription and a GeologicEvent describing the Ge… |

### `ChemicalComposition`

ChemicalComposition is a kind of EarthMaterialDescription that delivers the chemical composition of a geological unit or earth material, as a list of element or oxide concentrations.

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `chemicalAnalysis` | (oneOf - see schema) | 0..1 | The chemicalAnalysis property (SWE:DataRecord) contains a collection of geochemical results in a form of a DataRecord… |

### `CompoundMaterialDescription`

The CompoundMaterialDescription class is a kind of EarthMaterialDescription that provides an extended description of a compound earth material (i.e., rocks and unconsolidated solid earth materials).

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `compositionCategory` | (oneOf - see schema) | 0..1 | The compositionCategory property (SWE::Category) provides a term from a controlled vocabulary to specify the gross co… |
| `geneticCategory` | (oneOf - see schema) | 0..1 | The property geneticCategory (SWE::Category) provides a term from a controlled vocabulary that represents a summary g… |
| `particleGeometry` | (oneOf - see schema) | 0..1 | The particleGeometry:ParticleGeometryDescription contains an instance of ParticleGeometryDescription. |
| `constituent` | (oneOf - see schema) | 0..1 | The property constituent is an association between a CompoundMaterialDescription and a ConstituentPart that makes up … |

### `ConstituentPart`

The ConstituentPart class describes how Earth materials may be made up of other Earth materials, including the proportion of the constituent part in the whole (e.g., 20%, minor, dominant); and the role that the constituent plays in the whole (e.g., matrix, groundmass, framework, phenocryst, xenolith, vein).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `role` | (oneOf - see schema) | 0..1 | The role:ConstituentPartRoleTerm property contains a term from a controlled vocabulary that describes the role a Cons… |
| `proportion` | (oneOf - see schema) | 0..1 | The proportion property (SWE::QuantityRange) reports the fraction of the whole that is formed by a ConstituentPart in… |
| `constituentMaterial` | (oneOf - see schema) | 0..1 | The constituentMaterial property is an association between a ConstituentPart and an EarthMaterial that specifies the … |
| `constituentParticleGeometry` | (oneOf - see schema) | 0..1 | Description of geometry of individual subset of particles |
| `relatedMaterial` | (oneOf - see schema) | 0..1 | Specifies the ConstituentPart that is playing the target role in the MaterialRelation |

### `FabricDescription`

The FabricDescription data type describes all types of fabrics associated with a CompoundMaterial (i.e., tectonic, metamorphic, sedimentary, igneous fabrics or textures). It denotes a pattern, defined by one or more CompoundMaterial constituents, that is present throughout a rock body when considered at some scale. FabricDescription is defined based on the average configuration of many constituents. Penetrative fabric denotes that these constituents are distributed throughout the rock volume at the scale of observation, and are repeated at distances that are small relative to the scale of the whole, such that they can be considered to pervade the whole uniformly.

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `fabricType` | (oneOf - see schema) | 0..1 | The fabricType:FabricTypeTerm property contains a term from a controlled vocabulary to denote the type of fabric in t… |

### `InorganicFluid`

The fabricType:FabricTypeTerm property contains a term from a controlled vocabulary to denote the type of fabric in the CompoundMaterial (e.g., rapikivi texture, autobrecciation, spaced cleavage, porphyroblastic, cross-bedding). The fabricType describes a pattern, defined by one or more CompoundMaterial constituents, that is present throughout a rock body when considered at some scale. It is defined based on the average configuration of many constituents. Penetrative fabric denotes that these constituents are distributed throughout the rock volume at the scale of observation, and are repeated at distances that are small relative to the scale of the whole, such that they can be considered to pervade the whole uniformly.

**Supertype**: `EarthMaterial` (cross-BB).

### `MetamorphicDescription`

The data type MetamorphicDescription describes the character of metamorphism applied to a CompoundMaterial or GeologicUnit using one or more properties including estimated intensity (grade; e.g. high grade, low grade), characteristic metamorphic mineral assemblages (facies; e.g., greenschist, amphibolite), peak P-T estimates, and protolith material if known. A MetamorphicDescription provides a link to the GeologicEvent associated to the metamorphic event.  Constraint: metamorphicFacies is not null or metamorphicGrade is not null

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `metamorphicFacies` | (oneOf - see schema) | 0..1 | The metamorphicFacies property (SWE::Category) contains a term from a controlled vocabulary that describes a characte… |
| `metamorphicGrade` | (oneOf - see schema) | 0..1 | The metamorphicGrade property (SWE::Category) contains a term from a controlled vocabulary that indicates the intensi… |
| `peakPressureValue` | (oneOf - see schema) | 0..1 | The peakPressureValue property (SWE::Quantity) reports a numerical value to indicate the estimated pressure at peak m… |
| `peakTemperatureValue` | (oneOf - see schema) | 0..1 | The peakTemperatureValue property (SWE::Quantity) reports a numerical value to indicate the estimated temperature at … |
| `protolithLithology` | (oneOf - see schema) | 0..1 | The protolithLithology is an association between a MetamorphicDescription and an EarthMaterial that describes the pre… |
| `metamorphicEvent` | (oneOf - see schema) | 0..1 | The metamorphicEvent property is an association between a MetamorphicDescription and a GeologicEvent that denotes the… |

### `Mineral`

A naturally occurring inorganic element or compound having a periodically repeating arrangement of atoms and a characteristic chemical composition or range of compositions, resulting in distinctive physical properties. Includes mercury as a general exception to the requirement of crystallinity. Also includes crypto-crystalline materials such as chalcedony and amorphous silica.

**Supertype**: `EarthMaterial` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `mineralName` | (oneOf - see schema) | 0..1 | Name of the mineral (eg: orthoclase) or mineral family (eg: feldspar), approved by the International Mineralogical As… |

### `OrganicMaterial`

OrganicMaterial is an EarthMaterial that belongs to the class of chemical compounds having a reduced carbon basis (as distinct from carbonates), and derived from living organisms. It includes high-carbon EarthMaterials such as bitumen, peat, and coal. This class is an empty placeholder for extension at a later date, or by other domain models.

**Supertype**: `EarthMaterial` (cross-BB).

### `Organism`

Organism is a broad class to represent any living or once living things. This is the connection to taxonomy/biology for fossils. This class is an empty placeholder for extension at a later date, or by other domain models.  Constraint: if ParticleGeometrydescription/sourceOrganism is not null, then ParticleGeometryDescription/particleType = "fossil"

### `ParticleGeometryDescription`

ParticleGeometryDescription describes particles in a CompoundMaterial independent of their relationship to each other or their orientation. It is distinguished from Fabric in that the ParticleGeometryDescription remains constant if the material is disaggregated into its constituent particles, whereas Fabric is lost if the material is disaggregated. Properties include the particle size (grainsize), particle sorting (size distribution, e.g., well sorted, poorly sorted, bimodal sorting), particle shape (surface rounding or crystal face development, e.g., well rounded, euhedral, anhedral), and particle aspect ratio (e.g., elongated, platy, bladed, compact, acicular).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `particleType` | (oneOf - see schema) | 0..1 | The particleType:ParticleTypeTerm provides a term from a controlled vocabulary to specify the nature of individual pa… |
| `aspectRatio` | (oneOf - see schema) | 0..1 | The aspectRatio property (SWE::Category) contains a term from a controlled vocabulary describing the geometry of part… |
| `shape` | (oneOf - see schema) | 0..1 | The shape property (SWE::Category) describes, &#x9;the development of crystal faces bounding particles in crystalline… |
| `size` | (oneOf - see schema) | 0..1 | The property size (SWE::QuantityRange) reports the size that specifies particle grainsize. Values may be reported usi… |
| `sorting` | (oneOf - see schema) | 0..1 | The sorting property (SWE::Category) contains a term from a vocabulary that specifies the size distribution of partic… |
| `sourceOrganism` | (oneOf - see schema) | 0..1 | The sourceOrganism property is an association between a ParticleGeometryDescription and an Organism that is the sourc… |

### `PhysicalDescription`

PhysicalDescription is a class that describes the numeric physical properties of a geologic unit (GeologicUnit) earth material (EarthMaterial ), or geologic structure (GeologicStructure) (e.g., density, porosity, magnetic susceptibility, remanent magnetism). These properties are modelled here as scalar numeric values (SWE::Quantity).

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `propertyName` | (oneOf - see schema) | 0..1 | The property propertyName:PhysicalPropertyTerm contains a term from a controlled vocabulary of physical properties of… |
| `propertyMeasure` | (oneOf - see schema) | 0..1 | The propertyMeasure property (SWE::Quantity) is a scalar measurement of the physical property of a rock material, uni… |

### `RockMaterialDescription`

RockMaterialDescription provides extended description of RockMaterial.

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `consolidationDegree` | (oneOf - see schema) | 0..1 | The consolidationDegree property (SWE::Category) contains a term from a controlled vocabulary that specifies the degr… |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `AlterationTypeTerm` | `_(treat as open - no `codeList` annotation)_` |
| `ConstituentPartRoleTerm` | `_(treat as open - no `codeList` annotation)_` |
| `FabricTypeTerm` | `_(treat as open - no `codeList` annotation)_` |
| `MineralNameTerm` | `_(treat as open - no `codeList` annotation)_` |
| `ParticleTypeTerm` | `_(treat as open - no `codeList` annotation)_` |
| `PhysicalPropertyTerm` | `_(treat as open - no `codeList` annotation)_` |

## External dependencies

- `../gsmBasicGeology/gsmBasicGeologySchema.json#CompoundMaterial`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent`
- `../gsmBasicGeology/gsmBasicGeologySchema.json#RockMaterial`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/DataRecord.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [fc_bolsa_quartzite_GSO.json](examples/fc_bolsa_quartzite_GSO.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `EarthMaterialDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### fc bolsa quartzite GSO
Material collection example constructed from Loop3D-GSO GSO-ExampleRockMaterialBolsaQuartzite.ttl. Two features: a RockMaterial (Bolsa Quartzite basal arkose) and one of its Mineral constituents (Quartz). The RockMaterial branch carries a RockMaterialDescription in gbEarthMaterialDescription[]; the Mineral feature uses the inherited EarthMaterialAbstractDescription slot.
#### json
```json
{
  "$comment": "Material collection example constructed from Loop3D-GSO GSO-ExampleRockMaterialBolsaQuartzite.ttl. Two features: a RockMaterial (Bolsa Quartzite basal arkose) and one of its Mineral constituents (Quartz). The RockMaterial branch carries a RockMaterialDescription in gbEarthMaterialDescription[]; the Mineral feature uses the inherited EarthMaterialAbstractDescription slot.",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "RockMaterial",
      "id": "https://w3id.org/gso/1.0/ex-materialCb#Bolsa_Quartzite_Material",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "color": [
          {
            "type": "Category",
            "label": "light grey to white",
            "definition": "http://example.org/cgi/color/light-grey"
          }
        ],
        "purpose": "typicalNorm",
        "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/arkose",
        "gbEarthMaterialDescription": [
          {
            "$comment": "RockMaterialDescription - content shape, not strictly required by schema",
            "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/arkose",
            "consolidationDegree": {
              "type": "Category",
              "definition": "http://resource.geosciml.org/classifier/cgi/consolidationdegree",
              "label": "consolidated",
              "value": "http://resource.geosciml.org/classifier/cgi/consolidationdegree/consolidated"
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "featureType": "Mineral",
      "id": "https://w3id.org/gso/1.0/ex-materialCb#Quartz_grains",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "mineralName": [
          "http://resource.geosciml.org/classifier/cgi/mineralname/quartz"
        ]
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmEarthMaterial/gsmEarthMaterialSchema.json
description: "EarthMaterial building block. Combines the formerly-separate\ngsmEarthMaterialExtension
  DataType library (AlterationDescription,\nCompoundMaterialDescription, ChemicalComposition,
  FabricDescription,\nMetamorphicDescription, PhysicalDescription, ParticleGeometryDescription,\nRockMaterialDescription,
  plus the EarthMaterial subtype \xABType\xBB classes\nMineral, InorganicFluid, OrganicMaterial,
  Organism, ConstituentPart)\nwith the FC profile formerly known as gsmEarthMaterialCollection.\nThe
  merged Feature/FC dispatcher accepts four featureType values\n(Mineral, OrganicMaterial,
  RockMaterial, CompoundMaterial), injecting\nthe JSON-FG Feature envelope around
  each \xABType\xBB class via\n`wrapAsFeature`. The inherited gbEarthMaterialDescription[]
  slot is\nconstrained to RockMaterialDescription or CompoundMaterialDescription\non
  the corresponding branches.\n\nValidates either a single Feature (dispatched by
  `featureType` to one of: Mineral, OrganicMaterial, RockMaterial, CompoundMaterial)
  or a FeatureCollection whose `features[]` items are dispatched the same way."
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
            const: Mineral
      then:
        allOf:
        - $ref: https://schemas.opengis.net/json-fg/feature.json
        - type: object
          required:
          - featureType
          - id
          properties:
            id:
              type: string
        - type: object
          properties:
            properties:
              $ref: '#Mineral'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: OrganicMaterial
      then:
        allOf:
        - $ref: https://schemas.opengis.net/json-fg/feature.json
        - type: object
          required:
          - featureType
          - id
          properties:
            id:
              type: string
        - type: object
          properties:
            properties:
              $ref: '#OrganicMaterial'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: RockMaterial
      then:
        allOf:
        - $ref: https://schemas.opengis.net/json-fg/feature.json
        - type: object
          required:
          - featureType
          - id
          properties:
            id:
              type: string
        - type: object
          properties:
            properties:
              allOf:
              - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#RockMaterial
              - type: object
                properties:
                  gbEarthMaterialDescription:
                    type: array
                    items:
                      $ref: '#RockMaterialDescription'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: CompoundMaterial
      then:
        allOf:
        - $ref: https://schemas.opengis.net/json-fg/feature.json
        - type: object
          required:
          - featureType
          - id
          properties:
            id:
              type: string
        - type: object
          properties:
            properties:
              allOf:
              - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#CompoundMaterial
              - type: object
                properties:
                  gbEarthMaterialDescription:
                    type: array
                    items:
                      $ref: '#CompoundMaterialDescription'
    - if:
        not:
          required:
          - featureType
          properties:
            featureType:
              enum:
              - Mineral
              - OrganicMaterial
              - RockMaterial
              - CompoundMaterial
      then: false
  AlterationDescription:
    $anchor: AlterationDescription
    description: AlterationDescription describes aspects of a geologic unit or earth
      material that are the result of bulk chemical, mineralogical or physical changes
      related to change in the physical or chemical environment. It includes weathering,
      supergene alteration, hydrothermal alteration and metasomatic effects not considered
      metamorphic. For example, a soil profile description would have to be constructed
      as a GeologicUnit (geologicUnitType = PedologicUnit) with unit parts representing
      the various horizons in the profile. Thickness of a weathering profile can be
      delivered as unitThickness of a GeologicUnit of geologicUnitType equal to "AlterationUnit"
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        alterationType:
          oneOf:
          - type: 'null'
          - $ref: '#AlterationTypeTerm'
          description: The property alterationType:AlterationTypeTerm contains a term
            from a controlled vocabulary of alteration types (e.g., potassic, argillic,
            advanced argillic).
        alterationProduct:
          oneOf:
          - type: 'null'
          - type: array
            items:
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
                $comment: by-reference link to EarthMaterial
              - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial
                $comment: cross-BB inline reference to EarthMaterial in BB gsmBasicGeology
            uniqueItems: true
          description: The property alterationProduct is an association between the
            AlterationDescripton and EarthMaterial describing the material resulting
            from the alteration processes, e.g. alteration minerals, saprolite, ferricrete,
            clay, calcrete, skarn, etc. Materials observed in a soil profile could
            be identified using this property.
        alterationDistribution:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The alterationDistribution (SWE::Category) property describes
            the spatial distribution or geometry of alteration zones using a term
            from a controlled vocabulary. e.g., patchy, spotted, banded, veins, vein
            breccia, pervasive, disseminated, etc.
        alterationDegree:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The property alterationDegree (SWE::Category) contains a term
            from a controlled vocabulary to indicate the magnitude of observed alteration.
        alterationEvent:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to GeologicEvent
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent
              $comment: cross-BB inline reference to GeologicEvent in BB gsmBasicGeology
          description: The property alterationEvent is an association between an AlterationDescription
            and a GeologicEvent describing the GeologicEvent associated with the alteration.
  AlterationTypeTerm:
    $anchor: AlterationTypeTerm
    description: 'Refers to a vocabulary of terms describing the dominant alteration
      mineralogy or alteration type, in common usage. Examples include: argillic,
      phyllic, potassic, propylitic, calc-silicate, skarn, deuteric, greisen, serpenitisation,
      weathering, etc.'
    type: string
    format: uri
  ChemicalComposition:
    $anchor: ChemicalComposition
    description: ChemicalComposition is a kind of EarthMaterialDescription that delivers
      the chemical composition of a geological unit or earth material, as a list of
      element or oxide concentrations.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        chemicalAnalysis:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/DataRecord.json
          description: The chemicalAnalysis property (SWE:DataRecord) contains a collection
            of geochemical results in a form of a DataRecord (a collection of fields
            composed of description and values).
  CompoundMaterialDescription:
    $anchor: CompoundMaterialDescription
    description: The CompoundMaterialDescription class is a kind of EarthMaterialDescription
      that provides an extended description of a compound earth material (i.e., rocks
      and unconsolidated solid earth materials).
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        compositionCategory:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The compositionCategory property (SWE::Category) provides a
            term from a controlled vocabulary to specify the gross compositional character
            of a compound material. Composition as used here is loosely construed
            to include both chemical composition and petrographic composition, thus
            multiple values may be applied to a single rock, e.g. metaluminous and
            alkalic, undersaturated and basic, etc. Terms would typically include
            broad chemical classifications such as silicate, carbonate, ferromagnesian,
            oxide. However, this attribute may have different terminology for different
            kinds of rocks - for example sandstone petrographic classification terms
            (e.g. feldspathic) might be placed here.
        geneticCategory:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The property geneticCategory (SWE::Category) provides a term
            from a controlled vocabulary that represents a summary geologic history
            of the material. (i.e., a genetic process classifier term). Examples include
            igneous, sedimentary, metamorphic, shock metamorphic, volcanic, pyroclastic.
        particleGeometry:
          oneOf:
          - type: 'null'
          - $ref: '#ParticleGeometryDescription'
          description: The particleGeometry:ParticleGeometryDescription contains an
            instance of ParticleGeometryDescription.
        constituent:
          oneOf:
          - type: 'null'
          - type: array
            items:
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
                $comment: by-reference link to ConstituentPart
              - $ref: '#ConstituentPart'
            uniqueItems: true
          description: The property constituent is an association between a CompoundMaterialDescription
            and a ConstituentPart that makes up part of the CompoundMaterial.
  ConstituentPart:
    $anchor: ConstituentPart
    description: The ConstituentPart class describes how Earth materials may be made
      up of other Earth materials, including the proportion of the constituent part
      in the whole (e.g., 20%, minor, dominant); and the role that the constituent
      plays in the whole (e.g., matrix, groundmass, framework, phenocryst, xenolith,
      vein).
    type: object
    properties:
      role:
        oneOf:
        - type: 'null'
        - $ref: '#ConstituentPartRoleTerm'
        description: "The role:ConstituentPartRoleTerm property contains a term from
          a controlled vocabulary that describes the role a ConstituentPart plays
          in a CompoundMaterial aggregation. The same EarthMaterial may occur as different
          ConstituentParts playing different roles within one CompoundMaterial. For
          example, feldspar may be present as groundmass (\u201Cgroundmass\u201D is
          a ConstituentPart::role) and as phenocrysts (\u201Cphenocryst\u201D is another
          ConstituentPart::role) within a single igneous rock."
      proportion:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
        description: The proportion property (SWE::QuantityRange) reports the fraction
          of the whole that is formed by a ConstituentPart in a part/whole relationship.
          It is used for the ConstituentPart portion in a CompoundMaterial. It specifies
          the fraction of the EarthMaterial formed by the part (e.g., 20%, minor,
          dominant).
      constituentMaterial:
        oneOf:
        - type: 'null'
        - oneOf:
          - $ref: '#/$defs/SCLinkObject'
            $comment: by-reference link to EarthMaterial
          - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial
            $comment: cross-BB inline reference to EarthMaterial in BB gsmBasicGeology
        description: The constituentMaterial property is an association between a
          ConstituentPart and an EarthMaterial that specifies the EarthMaterial that
          is forming the ConstituentPart.
      constituentParticleGeometry:
        oneOf:
        - type: 'null'
        - $ref: '#ParticleGeometryDescription'
        description: Description of geometry of individual subset of particles
      relatedMaterial:
        oneOf:
        - type: 'null'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to ConstituentPart
            - $ref: '#ConstituentPart'
          uniqueItems: true
        description: Specifies the ConstituentPart that is playing the target role
          in the MaterialRelation
  ConstituentPartRoleTerm:
    $anchor: ConstituentPartRoleTerm
    description: Refers to a vocabulary of terms describing the role played by a constituent
      part of a compound material (eg, matrix, phenocryst)
    type: string
    format: uri
  FabricDescription:
    $anchor: FabricDescription
    description: The FabricDescription data type describes all types of fabrics associated
      with a CompoundMaterial (i.e., tectonic, metamorphic, sedimentary, igneous fabrics
      or textures). It denotes a pattern, defined by one or more CompoundMaterial
      constituents, that is present throughout a rock body when considered at some
      scale. FabricDescription is defined based on the average configuration of many
      constituents. Penetrative fabric denotes that these constituents are distributed
      throughout the rock volume at the scale of observation, and are repeated at
      distances that are small relative to the scale of the whole, such that they
      can be considered to pervade the whole uniformly.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        fabricType:
          oneOf:
          - type: 'null'
          - $ref: '#FabricTypeTerm'
          description: The fabricType:FabricTypeTerm property contains a term from
            a controlled vocabulary to denote the type of fabric in the CompoundMaterial
            (e.g., rapikivi texture, autobrecciation, spaced cleavage, porphyroblastic,
            cross-bedding). The fabricType describes a pattern, defined by one or
            more CompoundMaterial constituents, that is present throughout a rock
            body when considered at some scale. It is defined based on the average
            configuration of many constituents. Penetrative fabric denotes that these
            constituents are distributed throughout the rock volume at the scale of
            observation, and are repeated at distances that are small relative to
            the scale of the whole, such that they can be considered to pervade the
            whole uniformly.
  FabricTypeTerm:
    $anchor: FabricTypeTerm
    description: Refers to a vocabulary of terms describing the type of fabric present
    type: string
    format: uri
  InorganicFluid:
    $anchor: InorganicFluid
    description: The fabricType:FabricTypeTerm property contains a term from a controlled
      vocabulary to denote the type of fabric in the CompoundMaterial (e.g., rapikivi
      texture, autobrecciation, spaced cleavage, porphyroblastic, cross-bedding).
      The fabricType describes a pattern, defined by one or more CompoundMaterial
      constituents, that is present throughout a rock body when considered at some
      scale. It is defined based on the average configuration of many constituents.
      Penetrative fabric denotes that these constituents are distributed throughout
      the rock volume at the scale of observation, and are repeated at distances that
      are small relative to the scale of the whole, such that they can be considered
      to pervade the whole uniformly.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial
      $comment: cross-BB supertype reference to EarthMaterial in BB gsmBasicGeology
    - type: object
  MetamorphicDescription:
    $anchor: MetamorphicDescription
    description: 'The data type MetamorphicDescription describes the character of
      metamorphism applied to a CompoundMaterial or GeologicUnit using one or more
      properties including estimated intensity (grade; e.g. high grade, low grade),
      characteristic metamorphic mineral assemblages (facies; e.g., greenschist, amphibolite),
      peak P-T estimates, and protolith material if known. A MetamorphicDescription
      provides a link to the GeologicEvent associated to the metamorphic event.  Constraint:
      metamorphicFacies is not null or metamorphicGrade is not null'
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        metamorphicFacies:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: The metamorphicFacies property (SWE::Category) contains a term
            from a controlled vocabulary that describes a characteristic mineral assemblages
            indicative of certain metamorphic pressure and temperature conditions.
            Examples include Barrovian metasedimentary zones (e.g., biotite facies,
            kyanite facies) or assemblages developed in rocks of more mafic composition
            (e.g., greenschist facies, amphibolite facies).
        metamorphicGrade:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The metamorphicGrade property (SWE::Category) contains a term
            from a controlled vocabulary that indicates the intensity or rank of metamorphism
            applied to an EarthMaterial (e.g., high metamorphic grade, low metamorphic
            grade). It indicates in a general way the pressure-temperature (PT) environment
            in which the metamorphism took place. The determination of metamorphic
            grade is based on mineral assemblages (i.e., facies) present in a rock
            that are interpreted to have crystallized in equilibrium during a particular
            metamorphic event.
        peakPressureValue:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
          description: The peakPressureValue property (SWE::Quantity) reports a numerical
            value to indicate the estimated pressure at peak metamorphic conditions.
        peakTemperatureValue:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
          description: The peakTemperatureValue property (SWE::Quantity) reports a
            numerical value to indicate the estimated temperature at peak metamorphic
            conditions.
        protolithLithology:
          oneOf:
          - type: 'null'
          - type: array
            items:
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
                $comment: by-reference link to EarthMaterial
              - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial
                $comment: cross-BB inline reference to EarthMaterial in BB gsmBasicGeology
            uniqueItems: true
          description: The protolithLithology is an association between a MetamorphicDescription
            and an EarthMaterial that describes the pre-metamorphic lithology for
            a metamorphosed CompoundMaterial.
        metamorphicEvent:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to GeologicEvent
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent
              $comment: cross-BB inline reference to GeologicEvent in BB gsmBasicGeology
          description: The metamorphicEvent property is an association between a MetamorphicDescription
            and a GeologicEvent that denotes the age, environment and process associated
            with a particular metamorphic assemblage in a GeologicUnit.
  Mineral:
    $anchor: Mineral
    description: A naturally occurring inorganic element or compound having a periodically
      repeating arrangement of atoms and a characteristic chemical composition or
      range of compositions, resulting in distinctive physical properties. Includes
      mercury as a general exception to the requirement of crystallinity. Also includes
      crypto-crystalline materials such as chalcedony and amorphous silica.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial
      $comment: cross-BB supertype reference to EarthMaterial in BB gsmBasicGeology
    - type: object
      properties:
        mineralName:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: '#MineralNameTerm'
            uniqueItems: true
          description: 'Name of the mineral (eg: orthoclase) or mineral family (eg:
            feldspar), approved by the International Mineralogical Association. (eg:
            http://www.mindat.org/mineralindex.php)'
  MineralNameTerm:
    $anchor: MineralNameTerm
    description: Refers to a vocabulary of mineral names
    type: string
    format: uri
  OrganicMaterial:
    $anchor: OrganicMaterial
    description: OrganicMaterial is an EarthMaterial that belongs to the class of
      chemical compounds having a reduced carbon basis (as distinct from carbonates),
      and derived from living organisms. It includes high-carbon EarthMaterials such
      as bitumen, peat, and coal. This class is an empty placeholder for extension
      at a later date, or by other domain models.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterial
      $comment: cross-BB supertype reference to EarthMaterial in BB gsmBasicGeology
    - type: object
  Organism:
    $anchor: Organism
    description: 'Organism is a broad class to represent any living or once living
      things. This is the connection to taxonomy/biology for fossils. This class is
      an empty placeholder for extension at a later date, or by other domain models.  Constraint:
      if ParticleGeometrydescription/sourceOrganism is not null, then ParticleGeometryDescription/particleType
      = "fossil"'
    type: object
  ParticleGeometryDescription:
    $anchor: ParticleGeometryDescription
    description: ParticleGeometryDescription describes particles in a CompoundMaterial
      independent of their relationship to each other or their orientation. It is
      distinguished from Fabric in that the ParticleGeometryDescription remains constant
      if the material is disaggregated into its constituent particles, whereas Fabric
      is lost if the material is disaggregated. Properties include the particle size
      (grainsize), particle sorting (size distribution, e.g., well sorted, poorly
      sorted, bimodal sorting), particle shape (surface rounding or crystal face development,
      e.g., well rounded, euhedral, anhedral), and particle aspect ratio (e.g., elongated,
      platy, bladed, compact, acicular).
    type: object
    properties:
      particleType:
        oneOf:
        - type: 'null'
        - $ref: '#ParticleTypeTerm'
        description: The particleType:ParticleTypeTerm provides a term from a controlled
          vocabulary to specify the nature of individual particles of each constituent
          in an EarthMaterial aggregation, based mostly on their genesis. When applied
          on ParticleDescription for CompoundMaterial, it would characterise all particles
          in aggregate. Use this property on CompoundMaterial to distinguish rocks
          composed of crystals (crystalline rocks) from rocks composed of granular
          particles (clasts, fragments). Examples include ooliths, crystals, pore
          space. Constituent type is determined based on the nature of the particles,
          and ideally is independent of the relationship between particles in a compound
          material aggregation.
      aspectRatio:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: "The aspectRatio property (SWE::Category) contains a term from
          a controlled vocabulary describing the geometry of particles based on the
          ratios of lengths of long, intermediate and short axes of grains. It equates
          to sphericity in sedimentary rocks (i.e., the degree to which the shape
          of a particle approximates a sphere). The formal definition is \u201CA quantitative
          specification based on the ratio of lengths of long, intermediate and short
          axes of grain shape\u201D. (e.g., prolate, slightly flattened, very bladed,
          equant, acicular, tabular)."
      shape:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: The shape property (SWE::Category) describes, &#x9;the development
          of crystal faces bounding particles in crystalline compound materials, and
          &#x9;the surface rounding of grains in sedimentary rocks. Roundness is a
          measure of the sharpness of the edges between surfaces bounding a particle
          The terms shall be a term from a controlled vocabulary and be appropriate
          for the kind of compound material (e.g., for crystalline rocks- euhedral,
          ideoblastic, subhedral, anhedral, xenoblastic; for sedimentary rocks - angular,
          rounded).
      size:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
        description: The property size (SWE::QuantityRange) reports the size that
          specifies particle grainsize. Values may be reported using absolute measurements
          (e.g., range, mean, median, mode, maximum).
      sorting:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: The sorting property (SWE::Category) contains a term from a vocabulary
          that specifies the size distribution of particles in a CompoundMaterial.
          Terminology for sorting in sedimentary rocks is based on the quantitative
          Graphic Standard Deviation (IGSD) scheme proposed by Folk. Example for this
          attribute may include sedimentary terms such as well sorted and poorly sorted,
          or igneous terms such as porphyritic, equigranular, seriate.
      sourceOrganism:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: '#Organism'
          uniqueItems: true
        description: The sourceOrganism property is an association between a ParticleGeometryDescription
          and an Organism that is the source of the fossil particles (sponge spicules,
          bivalve shells, etc.).
  ParticleTypeTerm:
    $anchor: ParticleTypeTerm
    description: Refers to a vocabulary of terms describing the type of particle in
      the compound earth material (eg, bioclast, phenocryst, pyroclast)
    type: string
    format: uri
  PhysicalDescription:
    $anchor: PhysicalDescription
    description: PhysicalDescription is a class that describes the numeric physical
      properties of a geologic unit (GeologicUnit) earth material (EarthMaterial ),
      or geologic structure (GeologicStructure) (e.g., density, porosity, magnetic
      susceptibility, remanent magnetism). These properties are modelled here as scalar
      numeric values (SWE::Quantity).
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        propertyName:
          oneOf:
          - type: 'null'
          - $ref: '#PhysicalPropertyTerm'
          description: The property propertyName:PhysicalPropertyTerm contains a term
            from a controlled vocabulary of physical properties of rock materials
            (e.g., density, porosity, magnetic susceptibility, remnant magnetism,
            permeability, seismic velocity).
        propertyMeasure:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
            uniqueItems: true
          description: The propertyMeasure property (SWE::Quantity) is a scalar measurement
            of the physical property of a rock material, unit or structure.
  PhysicalPropertyTerm:
    $anchor: PhysicalPropertyTerm
    description: Refers to a vocabulary of physical property types (eg, density, porosity,
      magnetic susceptibility, magnetic remanence, conductivity, etc)
    type: string
    format: uri
  RockMaterialDescription:
    $anchor: RockMaterialDescription
    description: RockMaterialDescription provides extended description of RockMaterial.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#EarthMaterialAbstractDescription
      $comment: cross-BB supertype reference to EarthMaterialAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        consolidationDegree:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          description: The consolidationDegree property (SWE::Category) contains a
            term from a controlled vocabulary that specifies the degree to which an
            aggregation of EarthMaterial particles is a distinct solid material. Consolidation
            and induration are related concepts specified by this property. They define
            a continuum from unconsolidated material to very hard rock. Induration
            is the degree to which a consolidated material is made hard, operationally
            determined by how difficult it is to break a piece of the material. Consolidated
            materials may have varying degrees of induration.
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmEarthMaterial/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmEarthMaterial/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](/github/workspace/_sources/gsmEarthMaterial/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmEarthMaterial`

