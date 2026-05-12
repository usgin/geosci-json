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
| `alterationType` | (oneOf — see schema) | 0..1 | The property alterationType:AlterationTypeTerm contains a term from a controlled vocabulary of alteration types (e.g.… |
| `alterationProduct` | (oneOf — see schema) | 0..1 | The property alterationProduct is an association between the AlterationDescripton and EarthMaterial describing the ma… |
| `alterationDistribution` | (oneOf — see schema) | 0..1 | The alterationDistribution (SWE::Category) property describes the spatial distribution or geometry of alteration zone… |
| `alterationDegree` | (oneOf — see schema) | 0..1 | The property alterationDegree (SWE::Category) contains a term from a controlled vocabulary to indicate the magnitude … |
| `alterationEvent` | (oneOf — see schema) | 0..1 | The property alterationEvent is an association between an AlterationDescription and a GeologicEvent describing the Ge… |

### `ChemicalComposition`

ChemicalComposition is a kind of EarthMaterialDescription that delivers the chemical composition of a geological unit or earth material, as a list of element or oxide concentrations.

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `chemicalAnalysis` | (oneOf — see schema) | 0..1 | The chemicalAnalysis property (SWE:DataRecord) contains a collection of geochemical results in a form of a DataRecord… |

### `CompoundMaterialDescription`

The CompoundMaterialDescription class is a kind of EarthMaterialDescription that provides an extended description of a compound earth material (i.e., rocks and unconsolidated solid earth materials).

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `compositionCategory` | (oneOf — see schema) | 0..1 | The compositionCategory property (SWE::Category) provides a term from a controlled vocabulary to specify the gross co… |
| `geneticCategory` | (oneOf — see schema) | 0..1 | The property geneticCategory (SWE::Category) provides a term from a controlled vocabulary that represents a summary g… |
| `particleGeometry` | (oneOf — see schema) | 0..1 | The particleGeometry:ParticleGeometryDescription contains an instance of ParticleGeometryDescription. |
| `constituent` | (oneOf — see schema) | 0..1 | The property constituent is an association between a CompoundMaterialDescription and a ConstituentPart that makes up … |

### `ConstituentPart`

The ConstituentPart class describes how Earth materials may be made up of other Earth materials, including the proportion of the constituent part in the whole (e.g., 20%, minor, dominant); and the role that the constituent plays in the whole (e.g., matrix, groundmass, framework, phenocryst, xenolith, vein).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `role` | (oneOf — see schema) | 0..1 | The role:ConstituentPartRoleTerm property contains a term from a controlled vocabulary that describes the role a Cons… |
| `proportion` | (oneOf — see schema) | 0..1 | The proportion property (SWE::QuantityRange) reports the fraction of the whole that is formed by a ConstituentPart in… |
| `constituentMaterial` | (oneOf — see schema) | 0..1 | The constituentMaterial property is an association between a ConstituentPart and an EarthMaterial that specifies the … |
| `constituentParticleGeometry` | (oneOf — see schema) | 0..1 | Description of geometry of individual subset of particles |
| `relatedMaterial` | (oneOf — see schema) | 0..1 | Specifies the ConstituentPart that is playing the target role in the MaterialRelation |

### `FabricDescription`

The FabricDescription data type describes all types of fabrics associated with a CompoundMaterial (i.e., tectonic, metamorphic, sedimentary, igneous fabrics or textures). It denotes a pattern, defined by one or more CompoundMaterial constituents, that is present throughout a rock body when considered at some scale. FabricDescription is defined based on the average configuration of many constituents. Penetrative fabric denotes that these constituents are distributed throughout the rock volume at the scale of observation, and are repeated at distances that are small relative to the scale of the whole, such that they can be considered to pervade the whole uniformly.

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `fabricType` | (oneOf — see schema) | 0..1 | The fabricType:FabricTypeTerm property contains a term from a controlled vocabulary to denote the type of fabric in t… |

### `InorganicFluid`

The fabricType:FabricTypeTerm property contains a term from a controlled vocabulary to denote the type of fabric in the CompoundMaterial (e.g., rapikivi texture, autobrecciation, spaced cleavage, porphyroblastic, cross-bedding). The fabricType describes a pattern, defined by one or more CompoundMaterial constituents, that is present throughout a rock body when considered at some scale. It is defined based on the average configuration of many constituents. Penetrative fabric denotes that these constituents are distributed throughout the rock volume at the scale of observation, and are repeated at distances that are small relative to the scale of the whole, such that they can be considered to pervade the whole uniformly.

**Supertype**: `EarthMaterial` (cross-BB).

### `MetamorphicDescription`

The data type MetamorphicDescription describes the character of metamorphism applied to a CompoundMaterial or GeologicUnit using one or more properties including estimated intensity (grade; e.g. high grade, low grade), characteristic metamorphic mineral assemblages (facies; e.g., greenschist, amphibolite), peak P-T estimates, and protolith material if known. A MetamorphicDescription provides a link to the GeologicEvent associated to the metamorphic event.  Constraint: metamorphicFacies is not null or metamorphicGrade is not null

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `metamorphicFacies` | (oneOf — see schema) | 0..1 | The metamorphicFacies property (SWE::Category) contains a term from a controlled vocabulary that describes a characte… |
| `metamorphicGrade` | (oneOf — see schema) | 0..1 | The metamorphicGrade property (SWE::Category) contains a term from a controlled vocabulary that indicates the intensi… |
| `peakPressureValue` | (oneOf — see schema) | 0..1 | The peakPressureValue property (SWE::Quantity) reports a numerical value to indicate the estimated pressure at peak m… |
| `peakTemperatureValue` | (oneOf — see schema) | 0..1 | The peakTemperatureValue property (SWE::Quantity) reports a numerical value to indicate the estimated temperature at … |
| `protolithLithology` | (oneOf — see schema) | 0..1 | The protolithLithology is an association between a MetamorphicDescription and an EarthMaterial that describes the pre… |
| `metamorphicEvent` | (oneOf — see schema) | 0..1 | The metamorphicEvent property is an association between a MetamorphicDescription and a GeologicEvent that denotes the… |

### `Mineral`

A naturally occurring inorganic element or compound having a periodically repeating arrangement of atoms and a characteristic chemical composition or range of compositions, resulting in distinctive physical properties. Includes mercury as a general exception to the requirement of crystallinity. Also includes crypto-crystalline materials such as chalcedony and amorphous silica.

**Supertype**: `EarthMaterial` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `mineralName` | (oneOf — see schema) | 0..1 | Name of the mineral (eg: orthoclase) or mineral family (eg: feldspar), approved by the International Mineralogical As… |

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
| `particleType` | (oneOf — see schema) | 0..1 | The particleType:ParticleTypeTerm provides a term from a controlled vocabulary to specify the nature of individual pa… |
| `aspectRatio` | (oneOf — see schema) | 0..1 | The aspectRatio property (SWE::Category) contains a term from a controlled vocabulary describing the geometry of part… |
| `shape` | (oneOf — see schema) | 0..1 | The shape property (SWE::Category) describes, &#x9;the development of crystal faces bounding particles in crystalline… |
| `size` | (oneOf — see schema) | 0..1 | The property size (SWE::QuantityRange) reports the size that specifies particle grainsize. Values may be reported usi… |
| `sorting` | (oneOf — see schema) | 0..1 | The sorting property (SWE::Category) contains a term from a vocabulary that specifies the size distribution of partic… |
| `sourceOrganism` | (oneOf — see schema) | 0..1 | The sourceOrganism property is an association between a ParticleGeometryDescription and an Organism that is the sourc… |

### `PhysicalDescription`

PhysicalDescription is a class that describes the numeric physical properties of a geologic unit (GeologicUnit) earth material (EarthMaterial ), or geologic structure (GeologicStructure) (e.g., density, porosity, magnetic susceptibility, remanent magnetism). These properties are modelled here as scalar numeric values (SWE::Quantity).

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `propertyName` | (oneOf — see schema) | 0..1 | The property propertyName:PhysicalPropertyTerm contains a term from a controlled vocabulary of physical properties of… |
| `propertyMeasure` | (oneOf — see schema) | 0..1 | The propertyMeasure property (SWE::Quantity) is a scalar measurement of the physical property of a rock material, uni… |

### `RockMaterialDescription`

RockMaterialDescription provides extended description of RockMaterial.

**Supertype**: `EarthMaterialAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `consolidationDegree` | (oneOf — see schema) | 0..1 | The consolidationDegree property (SWE::Category) contains a term from a controlled vocabulary that specifies the degr… |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `AlterationTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `ConstituentPartRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FabricTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `MineralNameTerm` | `_(treat as open — no `codeList` annotation)_` |
| `ParticleTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `PhysicalPropertyTerm` | `_(treat as open — no `codeList` annotation)_` |

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
