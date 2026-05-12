# GeoSciML GeologyBasic

JSON Schema building block for the `GeologyBasic` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 3 feature types, 8 data types, 9 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AbstractFeatureRelation` | «DataType» | plain JSON object |
| `CompositionPart` | «DataType» | plain JSON object |
| `CompositionPartRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `CompoundMaterial` | «DataType» | plain JSON object |
| `DescriptionPurpose` | «CodeList» | URI codelist (`format: uri`) |
| `EarthMaterial` | «DataType» | plain JSON object |
| `EarthMaterialAbstractDescription` | «DataType» | plain JSON object |
| `ExposureTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicFeature` | «FeatureType» | JSON-FG Feature |
| `GeologicUnit` | «FeatureType» | JSON-FG Feature |
| `GeologicUnitAbstractDescription` | «DataType» | plain JSON object |
| `GeologicUnitHierarchy` | «DataType» | plain JSON object |
| `GeologicUnitHierarchyRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicUnitPartRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicUnitTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `LithologyTerm` | «CodeList» | URI codelist (`format: uri`) |
| `MappedFeature` | «FeatureType» | JSON-FG Feature |
| `MappingFrameTerm` | «CodeList» | URI codelist (`format: uri`) |
| `RankTerm` | «CodeList» | URI codelist (`format: uri`) |
| `RockMaterial` | «DataType» | plain JSON object |

## Class details

### `AbstractFeatureRelation`

Association class placeholder to implement relation between geologic features

### `CompositionPart`

CompositionPart represents the composition of a geologic unit in terms of earth material constituents (CompoundMaterial). It decomposes the material making of the unit into parts having distinct roles and proportions.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `role` | (oneOf — see schema) | 0..1 | The property role:CompositionPartRoleTerm defines the relationship of the CompoundMaterial constituent in the geologi… |
| `proportion` | (oneOf — see schema) | 0..1 | The proportion property (SWE::QuantityRange) specifies the fraction of the geologic unit composed of the compound mat… |
| `material` | (oneOf — see schema) | 0..1 | The material:EarthMaterial property contains the material description of the composing part. |

### `CompoundMaterial`

A CompoundMaterial is an EarthMaterial composed of particles made of EarthMaterials, possibly including other CompoundMaterials. This class is provided primarily as an extensibility point for related domain models that wish to import and build on GeoSciML, and wish to define material types that are compound but are not rock or rock-like material. In the context of GeoSciML "RockMaterial" should be used to describe units made of rock.

**Supertype**: [`EarthMaterial`](#EarthMaterial) (this BB).

### `EarthMaterial`

The EarthMaterial class holds a description of a naturally occurring substance in the Earth. EarthMaterial represents material composition or substance, and is thus independent of quantity or location. Ideally, EarthMaterials are defined strictly based on physical properties, but because of standard geological usage, genetic interpretations enter into the description as well.  Constraint: self.metadata.hierarchyLevel=feature

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `color` | (oneOf — see schema) | 0..1 | The color property (SWE::Category) is a term from a controlled vocabulary that specifies the colour of the earth mate… |
| `purpose` | (oneOf — see schema) | 0..1 | The purpose:DescriptionPurpose property provides a specification of the intended purpose or level of abstraction for … |
| `gbEarthMaterialDescription` | (oneOf — see schema) | 0..1 | The property gbEarthMaterialDescription:EarthMaterialAbstractDescription provides a detailed earth material descripti… |

### `EarthMaterialAbstractDescription`

Abstract description class for earth material. This class is a placeholder for further extension in Extension package

### `GeologicFeature`

The abstract GeologicFeature class represents a conceptual feature that is hypothesized to exist coherently in the world. It corresponds with a "legend item" from a traditional geologic map and its instance acts as the "description package". The description package is classified according to its intended purpose as a typicalNorm, definingNorm or instance. GeologicFeature can be used outside the context of a map (it can lack a MappedFeature), for example when describing typical norms (describing expected property from a feature) or defining norms (describing properties required from a feature to be classifying in a group, such as given geologic unit). A GeologicFeature appearing on a map is considered as an “instance”.  Constraint: self.metadata.hierarchyLevel=(feature or dataset or series)

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `observationMethod` | (oneOf — see schema) | 0..1 | The GeologicFeature observationMethod (SWE::Category) specifies the approach to acquiring the collection of attribute… |
| `purpose` | (oneOf — see schema) | 0..1 | The property purpose:DescriptionPurpose specifies the intended purpose/level of abstraction for a given feature or ob… |
| `classifier` | (oneOf — see schema) | 0..1 | The classifier (SWE::Category) contains a standard description or definition of the feature type (e.g., the definitio… |
| `relatedFeature` | (oneOf — see schema) | 0..1 | A relatedFeature is a general structure used to define relationships between any features or objects within GeoSciML.… |
| `geologicHistory` | (oneOf — see schema) | 0..1 | The geologicHistory is an association that relates one or more GeologicEvents to a GeologicFeature to describe their … |
| `occurrence` | (oneOf — see schema) | 0..1 | The occurrence property is an association that links a notional geologic feature with any number of mapped features (… |

### `GeologicUnit`

Conceptually, a GeologicUnit may represent a body of material in the Earth whose complete and precise extent is inferred to exist (e.g., North American Data Model GeologicUnit, Stratigraphic unit in the sense of NACSN, or International Stratigraphic Code ), or a classifier used to characterize parts of the Earth (e.g. lithologic map unit like 'granitic rock' or 'alluvial deposit', surficial units like 'till' or 'old alluvium'). It includes both formal units (i.e. formally adopted and named in an official lexicon) and informal units (i.e. named but not promoted to a lexicon) and unnamed units (i.e., recognizable, described and delineable in the field but not otherwise formalised). In simpler terms, a geologic unit is a package of earth material (generally rock).  Constraint: target of composition is only CompositionPart  Constraint: target of geologicHistory is only GeologicEvent

**Supertype**: [`GeologicFeature`](#GeologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `geologicUnitType` | (oneOf — see schema) | 0..1 | The property geologicUnitType:GeologicUnitTypeTerm provides a term from a controlled vocabulary defining the type of … |
| `rank` | (oneOf — see schema) | 0..1 | The property rank:RankTerm contains a term that classifies the geologic unit in a generalization hierarchy from most … |
| `gbMaterialDescription` | (oneOf — see schema) | 0..1 | The property gbMaterialDescription:EarthMaterialAbstractDescription is a placeholder that provides detailed material … |
| `hierarchyLink` | (oneOf — see schema) | 0..1 | The property hierarchyLink is an association that links a GeologicUnit with a GeologicUnitHierarchy to represent cont… |
| `gbUnitDescription` | (oneOf — see schema) | 0..1 | The property gbUnitDescription:GeologicUnitAbstractDescriptio is a placeholder that provides detailed material descri… |
| `composition` | (oneOf — see schema) | 0..1 | The property composition is an association that links a GeologicUnit with CompositionParts to describe the material c… |

### `GeologicUnitAbstractDescription`

Abstract description class for geologic units. This class is a placeholder for further extension in Extension package

### `GeologicUnitHierarchy`

GeologicUnitHierarchy associates a GeologicUnit with another GeologicUnit that is a proper part of that unit. Parts may be formal or notional. Formal parts refer to a specific body of rock, as in formal stratigraphic members. Notional parts refer to assemblages of particular EarthMaterials with particular internal structure, which may be repeated in various places within a unit (e.g. 'turbidite sequence', 'point bar assemblage', 'leucosome veins').

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `role` | (oneOf — see schema) | 0..1 | The role:GeologicUnitHierarchyRoleTerm property provides a term describing the nature of the parts, e.g. facies, stra… |
| `proportion` | (oneOf — see schema) | 0..1 | The proportion property (SWE::QuantityRange) provides a quantity that represents the fraction of the geologic unit fo… |
| `targetUnit` | `/$defs/SCLinkObject` | 1..1 | The property targetUnit is an association that specifies exactly one GeologicUnit that is a proper part of another Ge… |

### `MappedFeature`

A MappedFeature is part of a geological interpretation. It provides a link between a notional feature (description package) and one spatial representation of it, or part of it (exposures, surface traces and intercepts, etc.). The mapped features are the elements that compose a map, a cross-section, a borehole log, or any other representation. The mappingFrame identifies the domain being mapped by the geometries. For typical geological maps, the mapping frame is the surface of the earth (the 2.5D interface between the surface of the bedrock and whatever sits on it; atmosphere or overburden material for bedrock maps). It can also be abstract frames, such as the arbitrary plane that forms a mine level or a cross-section, the 3D volume enclosing an ore body or the line that approximate the path of a borehole.  Constraint: self.metadata.hierarchyLevel=(feature or dataset or series)  Constraint: self.shape contained in samplingFrame.shape

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `observationMethod` | (oneOf — see schema) | 0..1 | The observationMethod property (SWE::Category) contains an element in a list of categories (a controlled vocabulary) … |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | The positionalAccuracy property (SWE::Quantity) provides a quantitative value defining the radius of an uncertainty b… |
| `resolutionRepresentativeFraction` | (oneOf — see schema) | 0..1 | The property resolutionRepresentativeFraction:Integer is an integer value representing the denominator of the represe… |
| `mappingFrame` | (oneOf — see schema) | 0..1 | The mappingFrame:MappingFrameTerm provides a term from a vocabulary indicating the geometric frame on which the Mappe… |
| `exposure` | (oneOf — see schema) | 0..1 | The exposure:ExposureTerm property provides a term for the nature of the expression of the mapped feature at the eart… |
| `shape` | (oneOf — see schema) | 0..1 | The shape:GM_Object property contains the geometry delimiting the mapped feature. Note that while in most cases, the … |
| `specification` | (oneOf — see schema) | 0..1 | The specification association links an instance of MappedFeature to the GFI_Feature being mapped. In a geological map… |

### `RockMaterial`

RockMaterial is a specialized CompoundMaterial that includes consolidated and unconsolidated materials (such as surficial sediments) as well as mixtures of consolidated and unconsolidated materials. In GeoSciML Basic, Rock Material is essentially a link to a controlled vocabulary (lithology property) and a color (inherited from EarthMaterial). Specific material properties (and CompoundMaterial nesting) are available in GeoSciML Extension.

**Supertype**: [`CompoundMaterial`](#CompoundMaterial) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `lithology` | (oneOf — see schema) | 0..1 | The lithology:LithologyTerm property provides a term identifying the lithology class from a controlled vocabulary. |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `CompositionPartRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `DescriptionPurpose` | `_(treat as open — no `codeList` annotation)_` |
| `ExposureTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicUnitHierarchyRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicUnitPartRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicUnitTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `LithologyTerm` | `_(treat as open — no `codeList` annotation)_` |
| `MappingFrameTerm` | `_(treat as open — no `codeList` annotation)_` |
| `RankTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `https://geojson.org/schema/Geometry.json`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [Minimal](examples/exampleGeologyBasicMinimal.json) — bare valid instance.
- [Complete](examples/exampleGeologyBasicComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GeologyBasic`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
