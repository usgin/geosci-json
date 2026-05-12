
# gsmBasicGeology (Schema)

`usgin.bbr.geosci.gsmBasicGeology` *v0.1*

GeoSciML 4.1 Basic application schema. Core feature types

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmBasicGeology

GeoSciML 4.1 building block `gsmBasicGeology`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeoSciMLBasic`, `Collection`, `GSML_DataTypes`, `GeologicEvent`, `GeologicStructure`, `GeologyBasic`, `Geomorphology`.

Contains 13 feature types, 21 data types, 22 code lists, 1 union.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AbstractFeatureRelation` | «DataType» | plain JSON object |
| `AnthropogenicGeomorphologicFeature` | «FeatureType» | JSON-FG Feature |
| `AnthropogenicGeomorphologicFeatureTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `CollectionTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `CompositionPart` | «DataType» | plain JSON object |
| `CompositionPartRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `CompoundMaterial` | «DataType» | plain JSON object |
| `Contact` | «FeatureType» | JSON-FG Feature |
| `ContactAbstractDescription` | «DataType» | plain JSON object |
| `ContactTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `ConventionCode` | «CodeList» | URI codelist (`format: uri`) |
| `DescriptionPurpose` | «CodeList» | URI codelist (`format: uri`) |
| `DeterminationMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `EarthMaterial` | «DataType» | plain JSON object |
| `EarthMaterialAbstractDescription` | «DataType» | plain JSON object |
| `EventProcessTerm` | «CodeList» | URI codelist (`format: uri`) |
| `ExposureTerm` | «CodeList» | URI codelist (`format: uri`) |
| `FaultTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `Fold` | «FeatureType» | JSON-FG Feature |
| `FoldAbstractDescription` | «DataType» | plain JSON object |
| `FoldProfileTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `Foliation` | «FeatureType» | JSON-FG Feature |
| `FoliationAbstractDescription` | «DataType» | plain JSON object |
| `FoliationTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GSML` | «FeatureType» | JSON-FG Feature |
| `GSML_GeometricDescriptionValue` | «DataType» | plain JSON object |
| `GSML_LinearOrientation` | «DataType» | plain JSON object |
| `GSML_PlanarOrientation` | «DataType» | plain JSON object |
| `GSML_QuantityRange` | «DataType» | plain JSON object |
| `GSML_Vector` | «DataType» | plain JSON object |
| `GSMLitem` | «Union» | type discriminator (`oneOf`) |
| `GeochronologicEraTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicEvent` | «FeatureType» | JSON-FG Feature |
| `GeologicEventAbstractDescription` | «DataType» | plain JSON object |
| `GeologicFeature` | «FeatureType» | JSON-FG Feature |
| `GeologicStructure` | «FeatureType» | JSON-FG Feature |
| `GeologicUnit` | «FeatureType» | JSON-FG Feature |
| `GeologicUnitAbstractDescription` | «DataType» | plain JSON object |
| `GeologicUnitHierarchy` | «DataType» | plain JSON object |
| `GeologicUnitHierarchyRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicUnitPartRoleTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicUnitTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeomorphologicFeature` | «FeatureType» | JSON-FG Feature |
| `GeomorphologicUnitAbstractDescription` | «DataType» | plain JSON object |
| `LinearDirectedCode` | «CodeList» | URI codelist (`format: uri`) |
| `LithologyTerm` | «CodeList» | URI codelist (`format: uri`) |
| `MappedFeature` | «FeatureType» | JSON-FG Feature |
| `MappingFrameTerm` | «CodeList» | URI codelist (`format: uri`) |
| `NaturalGeomorphologicFeature` | «FeatureType» | JSON-FG Feature |
| `NaturalGeomorphologicFeatureTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `NumericAgeRange` | «DataType» | plain JSON object |
| `PlanarPolarityCode` | «CodeList» | URI codelist (`format: uri`) |
| `RankTerm` | «CodeList» | URI codelist (`format: uri`) |
| `RockMaterial` | «DataType» | plain JSON object |
| `ShearDisplacementStructure` | «FeatureType» | JSON-FG Feature |
| `ShearDisplacementStructureAbstractDescription` | «DataType» | plain JSON object |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `AbstractFeatureRelation`

Association class placeholder to implement relation between geologic features

### `AnthropogenicGeomorphologicFeature`

An anthropogenic geomorphologic feature is a geomorphologic feature (i.e., landform) which has been created by human activity. For example, a dredged channel, midden, open pit or reclaimed land.

**Supertype**: [`GeomorphologicFeature`](#GeomorphologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `anthropogenicGeomorphologicFeatureType` | (oneOf — see schema) | 0..1 | The anthropogenicGeomorphologicFeatureType: AnthropogenicGeomorphologicFeatureTypeTerm is a reference from a controll… |

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

### `GSML`

GSML is a collection class grouping a set of features or types which are members of this collection. A collectionType property provides context or purpose.  Constraint: self.metadata.hierarchylevel=dataset

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `collectionType` | (oneOf — see schema) | 0..1 | The collectionType:CollectionTypeTerm property contains a term from a controlled vocabulary describing the type of co… |
| `member` | `GSMLitem` | 1..* | The member property is an association that links a GSML instance to features and objects to be included as members of… |

### `GSML_GeometricDescriptionValue`

GSML_GeometricDescriptionValue is a special abstract data type for descriptions of planar or linear orientations of a geologic feature. Different subtypes allow specifying direction by direction vector (e.g. dip/dip direction), compass point (e.g. NE), or description (e.g. "toward fold hinge", "below').

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `determinationMethod` | (oneOf — see schema) | 0..1 | The determinationMethod:DeterminationMethodTerm property describes the way the orientation value was determined (e.g.… |
| `descriptiveOrientation` | (oneOf — see schema) | 0..1 | The descriptionOrientation:Primitive::CharacterString contains a textual specification of orientation, possibly refer… |

### `GSML_LinearOrientation`

A linear orientation is composed of a trend (the compass orientation of the line) and a plunge (the angle from the horizontal). This vector may be oriented (pointing in a specific direction) or not.

**Supertype**: [`GSML_GeometricDescriptionValue`](#GSML_GeometricDescriptionValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `directed` | (oneOf — see schema) | 0..1 | The directed:LinearDirectedCode property indicates if the orientation represents a linear feature that is directed, e… |
| `plunge` | (oneOf — see schema) | 0..1 | The property plunge (SWE::QuantityRange) reports the magnitude of the plunge as an angle from horizontal. |
| `trend` | (oneOf — see schema) | 0..1 | The property trend (SWE::QuantityRange) reports the azimuth (compass bearing) value of the linear orientation. |

### `GSML_PlanarOrientation`

A planar orientation is composed of two values; the azimuth (a compass point) and a dip (the angle from the horizontal). Polarity of the plane indicates whether the planar orientation is associated with a directed feature that is overturned, upright, vertical, etc. There are several conventions to encode a planar orientation and this specification does not impose one but provides a convention property to report it. It must be noted that allowance for different conventions makes manipulation of the data more difficult. Therefore it is recommended that user communities adopt a single measurement convention.

**Supertype**: [`GSML_GeometricDescriptionValue`](#GSML_GeometricDescriptionValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `convention` | (oneOf — see schema) | 0..1 | The property convention:ConventionCode contains the convention used for the measurement from a controlled vocabulary. |
| `azimuth` | (oneOf — see schema) | 0..1 | The azimuth (SWE::QuantityRange) property (compass point, bearing etc.) contains the value of the orientation. The co… |
| `dip` | (oneOf — see schema) | 0..1 | The dip (SWE::QuantityRange) reports the angle that the structural surface (e.g. bedding, fault plane) makes with the… |
| `polarity` | (oneOf — see schema) | 0..1 | The polarity:PolarityCode indicates whether the planar orientation is associated with a directed feature that is over… |

### `GSML_QuantityRange`

GSML_QuantityRange is a specialization of SWE Common QuantiytyRange (OGC 08-094r1, Clause 7.2.13) where lower and upper values are made explicit. SWE::QuantityRange uses an array of values (RealPair, see Clause 7.2.1) where the lowest value is the first element and the highest the second. This convenience data type has been created as an alternative encoding for implementations that do no support encoding of arrays in a single field (e.g. DBF) or reference to elements in string encoded arrays1 (eg. Filter Encoding Specification 2.0 – OGC 09-029r2). &nbsp;------------------------- 1 SWE RealPair is encoded as space delimited lists (&lt;swe:value&gt;10 300&lt;/swe:value&gt; in XML) , which demands that clients parse the string to extract each token. To build a WFS/FES query that tests the first element, it requires parsing the string either using string-before(swe:value,' ') or tokenize(swe:value,' '). This is cumbersome at best, or not even supported by the server at worst. 09-026r2 Clause 7.4.4 describes the minimal XPath supports and string parsing is not present.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `lowerValue` | `number` | 1..1 | The property lowerValue:Real contains the lower bound of the range. It shall be a copy of inherited SWE::QuantityRang… |
| `upperValue` | `number` | 1..1 | The property upperValue:Real contains the upper bound of the range. It shall be a copy of inherited SWE::QuantityRang… |

### `GSML_Vector`

A GSML_Vector is a data type representing a linear orientation with a magnitude (a quantity assigned to this vector). If the magnitude is unknown, a GSML_LinearOrientation shall be used.

**Supertype**: [`GSML_LinearOrientation`](#GSML_LinearOrientation) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `magnitude` | (oneOf — see schema) | 0..1 | The magnitude property (SWE::QuantityRange) reports the magnitude of the vector. |

### `GeologicEvent`

A GeologicEvent is an identifiable event during which one or more geological processes act to modify geological entities. It may have a specified geologic age (numeric age or GeochologicEraTerm) and may have specified environments and processes. An example might be a cratonic uplift event during which erosion, sedimentation, and volcanism all take place.

**Supertype**: [`GeologicFeature`](#GeologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `eventProcess` | (oneOf — see schema) | 0..1 | The eventProcess:EventProcessTerm property provides a term from a controlled vocabulary specifying the process or pro… |
| `numericAge` | (oneOf — see schema) | 0..1 | The numericAge:NumericAgeRange property provides an age in absolute year before present (BP). Present is defined by c… |
| `olderNamedAge` | (oneOf — see schema) | 0..1 | The property olderNamedAge:GeochronologicalEraTerm defines the older boundary of age of an event expressed using a ge… |
| `youngerNamedAge` | (oneOf — see schema) | 0..1 | The property youngerNamedAge:GeochronologicalEraTerm defines the younger boundary of age of event expressed using a g… |
| `eventEnvironment` | (oneOf — see schema) | 0..1 | The eventEnvironment property (SWE::Category) is a category from a controlled vocabulary identifying the physical set… |
| `gaEventDescription` | (oneOf — see schema) | 0..1 | The property geEventDescription:GeologicEventAbstractDescription contains a detailed event description. This is a stu… |

### `GeologicEventAbstractDescription`

Stub property class to allow extended event related properties.

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

### `GeologicStructure`

A geologic structure is a configuration of matter in the Earth based on describable inhomogeneity, pattern, or fracture in an earth material. The identity of a GeologicStructure is independent of the material that is the substrate for the structure. The general GeologicFeatureRelation (available in the Extension package) is used to associate penetrative GeologicStructures with GeologicUnits. GeoSciML Basic only provides a limited set of core structures (Contact, Fold, ShearDisplacementStructure and Foliation) with a single property to categorise them. Supplemental properties and geologic structure types are available from the Extension package.

**Supertype**: [`GeologicFeature`](#GeologicFeature) (this BB).

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
| `targetUnit` | (oneOf — see schema) | 1..1 | The property targetUnit is an association that specifies exactly one GeologicUnit that is a proper part of another Ge… |

### `GeomorphologicFeature`

A geomorphologic feature is a kind of GeologicFeature describing the shape and nature of the Earth's land surface. These landforms may be created by natural Earth processes (e.g., river channel, beach, moraine or mountain) or through human (anthropogenic) activity (e.g., dredged channel, reclaimed land, mine waste dumps). In GeoSciML, the geomorphologic feature is modelled as a feature related (through unitDescription property) to a GeologicUnit that composes the form.

**Supertype**: [`GeologicFeature`](#GeologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `unitDescription` | (oneOf — see schema) | 0..1 | The unitDescription property is an association that links the geomorphologic feature to a geologic description (e.g.,… |
| `gmFeatureDescription` | (oneOf — see schema) | 0..1 | The property gmFeatureDescription:GeomorphologicUnitAbstractDescription provides a detailed morphologic description. … |

### `GeomorphologicUnitAbstractDescription`

Detailed geomorphologic unit description placeholder (stub class) for GeomorphologicUnit  Constraint: Only one instance of each subtype is allowed

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

### `NaturalGeomorphologicFeature`

A natural geomorphologic feature is a geomorphologic feature (i.e., landform) that has been created by natural Earth processes. For example, river channel, beach ridge, caldera, canyon, moraine or mud flat.

**Supertype**: [`GeomorphologicFeature`](#GeomorphologicFeature) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `naturalGeomorphologicFeatureType` | (oneOf — see schema) | 0..1 | The property naturalGeomorphologicFeatureType: NaturalGeomorphologicFeatureTypeTerm is a reference from a controlled … |
| `activity` | (oneOf — see schema) | 0..1 | The activity property (SWE::Category) contains a category term from a controlled vocabulary describing the current ac… |

### `NumericAgeRange`

The NumericAgeRange class represents an absolute age assignment using numeric measurement results.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `reportingDate` | (oneOf — see schema) | 0..1 | The reportingDate (SWE::Quantity) property reports a single time coordinate value to report as representative for thi… |
| `olderBoundDate` | (oneOf — see schema) | 0..1 | The olderBoundDate (SWE::Quantity) property reports the older bounding time coordinate in an age range. |
| `youngerBoundDate` | (oneOf — see schema) | 0..1 | The youngerBoundDate (SWE::Quantity) property reports the younger bounding time coordinate in an age range. |

### `RockMaterial`

RockMaterial is a specialized CompoundMaterial that includes consolidated and unconsolidated materials (such as surficial sediments) as well as mixtures of consolidated and unconsolidated materials. In GeoSciML Basic, Rock Material is essentially a link to a controlled vocabulary (lithology property) and a color (inherited from EarthMaterial). Specific material properties (and CompoundMaterial nesting) are available in GeoSciML Extension.

**Supertype**: [`CompoundMaterial`](#CompoundMaterial) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `lithology` | (oneOf — see schema) | 0..1 | The lithology:LithologyTerm property provides a term identifying the lithology class from a controlled vocabulary. |

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

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `AnthropogenicGeomorphologicFeatureTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `CollectionTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `CompositionPartRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `ContactTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `ConventionCode` | `_(treat as open — no `codeList` annotation)_` |
| `DescriptionPurpose` | `_(treat as open — no `codeList` annotation)_` |
| `DeterminationMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `EventProcessTerm` | `_(treat as open — no `codeList` annotation)_` |
| `ExposureTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FaultTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FoldProfileTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `FoliationTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeochronologicEraTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicUnitHierarchyRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicUnitPartRoleTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicUnitTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `LinearDirectedCode` | `_(treat as open — no `codeList` annotation)_` |
| `LithologyTerm` | `_(treat as open — no `codeList` annotation)_` |
| `MappingFrameTerm` | `_(treat as open — no `codeList` annotation)_` |
| `NaturalGeomorphologicFeatureTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `PlanarPolarityCode` | `_(treat as open — no `codeList` annotation)_` |
| `RankTerm` | `_(treat as open — no `codeList` annotation)_` |

## Unions

### `GSMLitem`

GSMLItem constrains the collection members to instances of EarthMaterial, GeologicFeature, GM_Object, MappedFeature, AbstractFeatureRelation and OM::SF_SamplingFeature.

Branches (`oneOf`):
- (branch 0)
- (branch 1)
- `Geometry`
- (branch 3)
- (branch 4)
- `/$defs/SCLinkObject` — External ISO 19156 SF_SamplingFeature — by-reference link

## External dependencies

- `https://geojson.org/schema/Geometry.json`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [contact_complex.json](examples/contact_complex.json)
- [contact_simple.json](examples/contact_simple.json)
- [examplegsmscimlBasicMinimal.json](examples/examplegsmscimlBasicMinimal.json)
- [fc_contacts_complex_GSO.json](examples/fc_contacts_complex_GSO.json)
- [fc_geologicunit_from_OGC.json](examples/fc_geologicunit_from_OGC.json)
- [fc_geologicunits_BritishColumbia.json](examples/fc_geologicunits_BritishColumbia.json)
- [fc_geologicunits_IsleOfWight.json](examples/fc_geologicunits_IsleOfWight.json)
- [fc_heterogeneous_GSO.json](examples/fc_heterogeneous_GSO.json)
- [fc_homogeneous_GSO.json](examples/fc_homogeneous_GSO.json)
- [fc_mixed_from_OGC.json](examples/fc_mixed_from_OGC.json)
- [fold_complex.json](examples/fold_complex.json)
- [fold_simple.json](examples/fold_simple.json)
- [geologic_event_from_GSO.json](examples/geologic_event_from_GSO.json)
- [geologic_unit_complex.json](examples/geologic_unit_complex.json)
- [geologic_unit_simple.json](examples/geologic_unit_simple.json)
- [mapped_feature_complex.json](examples/mapped_feature_complex.json)
- [mapped_feature_simple.json](examples/mapped_feature_simple.json)
- [natural_geomorphologic_feature_complex.json](examples/natural_geomorphologic_feature_complex.json)
- [natural_geomorphologic_feature_simple.json](examples/natural_geomorphologic_feature_simple.json)
- [shear_displacement_structure_complex.json](examples/shear_displacement_structure_complex.json)
- [shear_displacement_structure_simple.json](examples/shear_displacement_structure_simple.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeoSciMLBasic`, `Collection`, `GSML_DataTypes`, `GeologicEvent`, `GeologicStructure`, `GeologyBasic`, `Geomorphology`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### contact complex
Example instance: contact_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "Contact",
  "id": "contact-disconformity-xy",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "purpose": "instance",
    "classifier": [
      {
        "type": "Category",
        "definition": "http://some.org/classifier/contactType",
        "label": "erosional contact",
        "value": "http://some.org/contactType/erosional-contact"
      }
    ],
    "geologicHistory": [
      {
        "type": "Feature",
        "featureType": "GeologicEvent",
        "id": "non-deposition-xy",
        "geometry": null,
        "place": null,
        "time": null,
        "properties": {
          "eventProcess": [
            "http://resource.geosciml.org/classifier/cgi/eventprocess/non-deposition"
          ],
          "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Cambrian",
          "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Ordovician"
        }
      }
    ],
    "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/disconformity"
  }
}

```


### contact simple
Example instance: contact_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "Contact",
  "id": "contact-unconformity-1",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "purpose": "instance",
    "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/unconformity"
  }
}

```


### examplegsmscimlBasicMinimal
Example instance: examplegsmscimlBasicMinimal
#### json
```json
{
  "type": "Feature",
  "id": "anthropogenicgeomorphologicfeature.minimal.1",
  "featureType": "AnthropogenicGeomorphologicFeature",
  "geometry": null,
  "properties": {}
}

```


### fc contacts complex GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleComplexContacts.ttl — all 7 contacts in the worked scenario. Geologic context: the Js Formation (Jurassic sediments) unconformably overlies tilted Paleozoic strata (Os, Ss Formations) that overlie Early Proterozoic Xm metamorphic basement. A Cretaceous granite (Kg) and a Cretaceous diorite dike (Kd) intrude Js and the older units. After igneous activity, erosion exhumed the section, and Late Miocene Ms sediment was deposited on top, sealing the unconformity. The 7 contact features below capture each rock-body interface with its inferred contact type. Homogeneous FeatureCollection (collection-level featureType="Contact"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleComplexContacts.ttl — all 7 contacts in the worked scenario. Geologic context: the Js Formation (Jurassic sediments) unconformably overlies tilted Paleozoic strata (Os, Ss Formations) that overlie Early Proterozoic Xm metamorphic basement. A Cretaceous granite (Kg) and a Cretaceous diorite dike (Kd) intrude Js and the older units. After igneous activity, erosion exhumed the section, and Late Miocene Ms sediment was deposited on top, sealing the unconformity. The 7 contact features below capture each rock-body interface with its inferred contact type. Homogeneous FeatureCollection (collection-level featureType=\"Contact\"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).",
  "type": "FeatureCollection",
  "featureType": "Contact",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "contact.JsOnOs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Js overlies Os — angular unconformity",
        "description": "Angular unconformable contact: Jurassic Js Formation deposited on the erosional surface of Ordovician Os Formation (sedimentary). The OsBoundary-6_2 surface in the source ontology is an Erosional Surface; tilted Paleozoic strata are truncated and the Jurassic sediments rest with angular discordance on the eroded substrate.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preJurassicErosion.Os",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Jurassic erosion truncating Os Formation",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          },
          {
            "type": "Feature",
            "id": "JsDeposition.OnOs",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Js Formation deposition over Os",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/EarlyJurassic",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/LateJurassic"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/OsFormation", "title": "Os Formation (Ordovician) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/angular_unconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.JsOnSs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Js overlies Ss — angular unconformity",
        "description": "Angular unconformable contact: Jurassic Js Formation deposited on the erosional surface of Silurian Ss Formation (sedimentary). The SsBoundary-6_1 surface in the source ontology is an Erosional Surface.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preJurassicErosion.Ss",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Jurassic erosion truncating Ss Formation",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/SsFormation", "title": "Ss Formation (Silurian) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/angular_unconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.JsOnXm",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Js on Xm nonconformity",
        "description": "Nonconformable contact: Jurassic Js Formation (sedimentary) deposited on the eroded surface of the Early Proterozoic Xm Rock Body (medium-grade gneiss). The older surface records pre-Jurassic erosion of crystalline basement.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preJurassicErosion.Xm",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Jurassic erosion of Xm basement",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/XmRockBody", "title": "Xm Rock Body (Early Proterozoic gneiss) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/nonconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.KdInJs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Kd dike intrudes Js — igneous intrusive contact",
        "description": "Igneous intrusive contact: a Cretaceous diorite dike (Kd) cuts the Jurassic Js Formation. In the source ontology this contact is hosted on multiple rock-body boundaries (KdBoundaryInJs-3_1_4, KdBoundaryInJs-3_2_4, etc.) defining the upper and lower walls of the dike where it intrudes Js. Diorite grain size ~0.05 mm (mean).",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "KdIntrusion",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Cretaceous diorite dike emplacement",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/intrusion"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/EarlyCretaceous",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/LateCretaceous"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/KdDike",      "title": "Kd Mafic Dike (Cretaceous) — younger host (intrusive)", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — older host (country rock)", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/igneous_intrusive_contact",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.KgInJs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Kg granite intrudes Js — igneous intrusive contact",
        "description": "Igneous intrusive contact: a Cretaceous granite (Kg) pluton intrudes the Jurassic Js Formation. Source ontology hosts this contact on KgIntrusiveBoundary-4_2 and KgBoundaryIntrudesJs-4_2. Granite grain size ~5 mm (mean).",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "KgIntrusion",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Cretaceous granite pluton emplacement",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/intrusion"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/EarlyCretaceous",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/LateCretaceous"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/KgGranite",   "title": "Kg Granite (Cretaceous) — younger host (intrusive)", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — older host (country rock)", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/igneous_intrusive_contact",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.MsOnJs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Ms overlies Js — disconformity",
        "description": "Disconformable depositional contact: Late Miocene Ms Formation deposited on the eroded top surface of Jurassic Js Formation (topJs-2_1, an erosional surface). The two units are roughly parallel (no major angular discordance) but separated by a large hiatus from the Cretaceous through most of the Tertiary.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preMioceneErosion.Js",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Miocene erosion of Js, Kg, and Kd",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          },
          {
            "type": "Feature",
            "id": "MsDeposition.OnJs",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Late Miocene deposition of Ms over Js",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tortonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Messinian"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/MsFormation", "title": "Ms Formation (Late Miocene) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/disconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.MsOnKg",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Ms overlies Kg — nonconformity",
        "description": "Nonconformable contact: Late Miocene Ms Formation deposited on an erosion surface developed across the Cretaceous Kg granite (KgBoundaryErosionSurface-2_3). Sedimentary on plutonic igneous — classical nonconformity.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preMioceneErosion.Kg",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Miocene erosion exhuming Kg granite",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          },
          {
            "type": "Feature",
            "id": "MsDeposition.OnKg",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Late Miocene deposition of Ms over Kg",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tortonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Messinian"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/MsFormation", "title": "Ms Formation (Late Miocene) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/KgGranite",   "title": "Kg Granite (Cretaceous) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/nonconformity",
        "stContactDescription": null
      }
    }
  ]
}

```


### fc geologicunit from OGC
Example instance: fc_geologicunit_from_OGC
#### json
```json
{
  "type": "FeatureCollection",
  "featureType": "GeologicUnit",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "hervey-group-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "occurrence": [
          {
            "href": "http://data.geoscience.gov.au/mappedfeature/polygon/6735427298",
            "title": "Mapped occurrence on 1:250000 sheet"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "featureType": "GeologicEvent",
            "id": "hervey-group-depositional-age",
            "geometry": null,
            "place": null,
            "time": null,
            "properties": {
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Famennian"
            }
          }
        ],
        "composition": [
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "hervey-group-fc-sandstone",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
              }
            },
            "proportion": {
              "type": "QuantityRange",
              "uom": {
                "code": "%"
              },
              "value": [
                50.0,
                95.0
              ],
              "definition": "http://resource.geosciml.org/property/proportion",
              "label": "proportion"
            }
          },
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "hervey-group-fc-mudstone",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
              }
            },
            "proportion": {
              "type": "QuantityRange",
              "uom": {
                "code": "%"
              },
              "value": [
                5.0,
                50.0
              ],
              "definition": "http://resource.geosciml.org/property/proportion",
              "label": "proportion"
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "boulton-formation-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "boulton-formation-fc-conglomerate",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/conglomerate"
              }
            }
          }
        ]
      }
    }
  ]
}

```


### fc geologicunits BritishColumbia
Adapted from Loop3D-GSO/Examples/GSO-ExampleBritishColumbiaStrat-v2.ttl — the Lardeau Group of the Kootenay Terrane (southeastern British Columbia), with its three known constituent formations (Akolkolex, Index, Jowett). The Lardeau Group is a Lower Paleozoic metasedimentary–metavolcanic assemblage that has been deformed and metamorphosed to greenschist facies. The source TTL is structurally simpler than the Isle of Wight TTL — it records unit type, label, list of constituent lithologies, and parent–child relationships, but not thickness, depositional setting, age, or bibliographic sources. The FeatureCollection therefore omits those slots. Constituent proportions are not recorded in the TTL (no qualitative Dominant/Subordinate terms either), so `proportion` is left null on every CompositionPart. Homogeneous FeatureCollection (collection-level featureType="GeologicUnit"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleBritishColumbiaStrat-v2.ttl — the Lardeau Group of the Kootenay Terrane (southeastern British Columbia), with its three known constituent formations (Akolkolex, Index, Jowett). The Lardeau Group is a Lower Paleozoic metasedimentary–metavolcanic assemblage that has been deformed and metamorphosed to greenschist facies. The source TTL is structurally simpler than the Isle of Wight TTL — it records unit type, label, list of constituent lithologies, and parent–child relationships, but not thickness, depositional setting, age, or bibliographic sources. The FeatureCollection therefore omits those slots. Constituent proportions are not recorded in the TTL (no qualitative Dominant/Subordinate terms either), so `proportion` is left null on every CompositionPart. Homogeneous FeatureCollection (collection-level featureType=\"GeologicUnit\"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).",
  "type": "FeatureCollection",
  "featureType": "GeologicUnit",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "LardeauGroup",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Lardeau Group",
        "description": "A Lower Paleozoic metasedimentary–metavolcanic group of the Kootenay Terrane, southeastern British Columbia. Includes the Akolkolex, Index and Jowett Formations. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "hierarchyLink": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": { "href": "#AkolkolexFormation", "title": "Akolkolex Formation", "rel": "containsFormation" }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": { "href": "#IndexFormation",     "title": "Index Formation",     "rel": "containsFormation" }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": { "href": "#JowettFormation",    "title": "Jowett Formation",    "rel": "containsFormation" }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "AkolkolexFormation",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Akolkolex Formation",
        "description": "Constituent formation of the Lardeau Group. Quartzose clastic metasediments — arenite and quartzite lithologies. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/arenite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/quartzite"
            },
            "proportion": null
          }
        ],
        "relatedFeature": [
          { "href": "#LardeauGroup", "title": "Lardeau Group — Akolkolex is a constituent formation", "rel": "isPartOf" }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "IndexFormation",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Index Formation",
        "description": "Constituent formation of the Lardeau Group. Heterolithic metasedimentary unit with arenite, chemical sedimentary material, chlorite–actinolite–epidote metamorphic rock, limestone, marble, undifferentiated metamorphic rock, metasomatic rock, phyllite, quartzite and schist. The breadth of lithologies reflects greenschist-facies metamorphism of a mixed sedimentary–volcaniclastic protolith. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/arenite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/chemical_sedimentary_material"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/marble"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/metamorphic_rock"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/metasomatic_rock"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/phyllite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/quartzite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/schist"
            },
            "proportion": null
          }
        ],
        "relatedFeature": [
          { "href": "#LardeauGroup", "title": "Lardeau Group — Index is a constituent formation", "rel": "isPartOf" }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "JowettFormation",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Jowett Formation",
        "description": "Constituent formation of the Lardeau Group. Metamorphosed pelitic and metasomatic rocks — schist and metasomatic rock lithologies. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/metasomatic_rock"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/schist"
            },
            "proportion": null
          }
        ],
        "relatedFeature": [
          { "href": "#LardeauGroup", "title": "Lardeau Group — Jowett is a constituent formation", "rel": "isPartOf" }
        ]
      }
    }
  ]
}

```


### fc geologicunits IsleOfWight
Adapted from Loop3D-GSO/Examples/GSO-ExampleIsleOfWightStrat-pm1-v2.ttl — a subset of the BGS Isle of Wight stratigraphy showing the Solent Group (SOLT) with two constituent formations (BEL, BOUL) and one basal member (BMBG of BOUL). Demonstrates Group→Formation→Member hierarchy plus stratigraphic `overlies` relationships. Homogeneous FeatureCollection (collection-level featureType="GeologicUnit"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch). Qualitative proportions from the TTL (Dominant_Proportion / Subordinate_Proportion) are translated to approximate QuantityRange % values. Thickness measurements from the TTL are kept only as prose in `description` since Basic GeologicUnit has no thickness slot (that lives in GeoSciML Extension's GeologicUnitDescription).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleIsleOfWightStrat-pm1-v2.ttl — a subset of the BGS Isle of Wight stratigraphy showing the Solent Group (SOLT) with two constituent formations (BEL, BOUL) and one basal member (BMBG of BOUL). Demonstrates Group→Formation→Member hierarchy plus stratigraphic `overlies` relationships. Homogeneous FeatureCollection (collection-level featureType=\"GeologicUnit\"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch). Qualitative proportions from the TTL (Dominant_Proportion / Subordinate_Proportion) are translated to approximate QuantityRange % values. Thickness measurements from the TTL are kept only as prose in `description` since Basic GeologicUnit has no thickness slot (that lives in GeoSciML Extension's GeologicUnitDescription).",
  "type": "FeatureCollection",
  "featureType": "GeologicUnit",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "SOLT",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Solent Group",
        "description": "Interbedded silty clays, calcareous clays and limestone; predominantly non-marine, freshwater to brackish water, fluvial/terrestrial; locally fully marine. Regional Isle of Wight thickness 0–200 m (not proved in PM1 borehole). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/SOLT. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Solent Group (SOLT)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/SOLT"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for dominant constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for subordinate constituent — limestone (LMST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/LMST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/subordinate",
              "label": "qualitative — subordinate proportion; numeric range 5–25 % is a placeholder. Source TTL records only the qualitative term gsoc:Subordinate_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [5, 25]
            }
          }
        ],
        "hierarchyLink": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": {
              "href": "#BEL",
              "title": "Bembridge Limestone Formation (BEL)",
              "rel": "containsFormation"
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": {
              "href": "#BOUL",
              "title": "Bouldnor Formation (BOUL)",
              "rel": "containsFormation"
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BA",
            "title": "Barton Group (BA) — Solent Group overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "SOLT.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Priabonian",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "lacustrine setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine"
                },
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "fluvial / river plain setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/river-plain"
                },
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "marine setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/marine"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "BEL",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Bembridge Limestone Formation, Solent Group",
        "description": "Shallow freshwater & subaerial; shelly limestone with interbedded mudstone. Regional IOW thickness 0–85 m (not proved in PM1). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BEL. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Bembridge Limestone Formation (BEL)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BEL"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for dominant constituent — limestone (LMST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/LMST"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for subordinate constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/subordinate",
              "label": "qualitative — subordinate proportion; numeric range 5–25 % is a placeholder. Source TTL records only the qualitative term gsoc:Subordinate_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [5, 25]
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "#SOLT",
            "title": "Solent Group — BEL is a constituent formation",
            "rel": "isPartOf"
          },
          {
            "href": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/HEHI",
            "title": "Headon Hill Formation (HEHI) — BEL overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "BEL.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Priabonian (BEL)",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "lacustrine setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine"
                },
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "subaerial setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/subaerial"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "BOUL",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Bouldnor Formation, Solent Group",
        "description": "Brackish/freshwater with pedogenized clays; interbedded clay and silt with organic beds. Swamp/marsh depositional setting. Regional IOW thickness 0–11 m (not proved in PM1). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BOUL. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Bouldnor Formation (BOUL)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BOUL"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for main body constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/main_body",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          }
        ],
        "hierarchyLink": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": {
              "href": "#BMBG",
              "title": "Bembridge Marls Member (BMBG)",
              "rel": "containsMember"
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "#SOLT",
            "title": "Solent Group — BOUL is a constituent formation",
            "rel": "isPartOf"
          },
          {
            "href": "#BEL",
            "title": "Bembridge Limestone Formation — BOUL overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "BOUL.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Rupelian (BOUL)",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Rupelian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Rupelian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "swamp or marsh setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/swamp-or-marsh"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "BMBG",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Bembridge Marls Member of Bouldnor Formation, Solent Group",
        "description": "Mudstone-dominated with subordinate limestone interbeds; includes sands and is shelly. Marginal-marine to non-marine, shoreline setting. Regional IOW thickness 0–34 m (not proved in PM1). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BMBG. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Bembridge Marls Member (BMBG)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BMBG"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for dominant constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for subordinate constituent — limestone (LMST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/LMST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/member",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/subordinate",
              "label": "qualitative — subordinate proportion; numeric range 5–25 % is a placeholder. Source TTL records only the qualitative term gsoc:Subordinate_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [5, 25]
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "#BOUL",
            "title": "Bouldnor Formation — BMBG is a constituent member (basal)",
            "rel": "isPartOf"
          },
          {
            "href": "#BEL",
            "title": "Bembridge Limestone Formation — BMBG overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "BMBG.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Priabonian (BMBG)",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "shoreline setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/shoreline"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}

```


### fc heterogeneous GSO
Heterogeneous FeatureCollection example — collection has NO top-level featureType; each feature carries its own. Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (else-branch dispatch). Members are the 5 single-feature examples in this directory, condensed inline.
#### json
```json
{
  "$comment": "Heterogeneous FeatureCollection example — collection has NO top-level featureType; each feature carries its own. Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (else-branch dispatch). Members are the 5 single-feature examples in this directory, condensed inline.",
  "type": "FeatureCollection",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "event.1",
      "featureType": "GeologicEvent",
      "geometry": null,
      "properties": {
        "name": "Kanimblan Orogeny",
        "eventProcess": [
          "http://resource.geosciml.org/classifier/cgi/eventprocess/deformation"
        ],
        "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tournaisian",
        "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Serpukhovian"
      }
    },
    {
      "type": "Feature",
      "id": "HerveyGroup.1",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Hervey Group",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group"
      }
    },
    {
      "type": "Feature",
      "id": "mappedfeature.1",
      "featureType": "MappedFeature",
      "geometry": {
        "type": "LineString",
        "coordinates": [[132.334, -25.9020], [132.43, -25.9025], [132.67, -25.9030]]
      },
      "properties": {
        "resolutionRepresentativeFraction": 250000,
        "mappingFrame": "http://resource.geosciml.org/classifier/cgi/mappingframe/top-of-bedrock",
        "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/concealed",
        "specification": {
          "href": "https://example.org/geosci-json/fold.1",
          "title": "Inferred fold structure"
        }
      }
    },
    {
      "type": "Feature",
      "id": "GEOMORPH_1",
      "featureType": "NaturalGeomorphologicFeature",
      "geometry": null,
      "properties": {
        "name": "UNNAMED GLACIAL OUTWASH CHANNEL",
        "naturalGeomorphologicFeatureType": "http://inspire.ec.europa.eu/codelist/NaturalGeomorphologicFeatureTypeValue/glacial"
      }
    },
    {
      "type": "Feature",
      "id": "fault.1",
      "featureType": "ShearDisplacementStructure",
      "geometry": null,
      "properties": {
        "name": "Lake George Fault",
        "faultType": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault"
      }
    }
  ]
}

```


### fc homogeneous GSO
Homogeneous FeatureCollection example — collection declares featureType="GeologicEvent" at the top level, so every member must be a GeologicEvent. Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).
#### json
```json
{
  "$comment": "Homogeneous FeatureCollection example — collection declares featureType=\"GeologicEvent\" at the top level, so every member must be a GeologicEvent. Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).",
  "type": "FeatureCollection",
  "featureType": "GeologicEvent",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "event.1",
      "featureType": "GeologicEvent",
      "geometry": null,
      "properties": {
        "name": "Kanimblan Orogeny",
        "eventProcess": [
          "http://resource.geosciml.org/classifier/cgi/eventprocess/deformation"
        ],
        "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tournaisian",
        "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Serpukhovian",
        "numericAge": {
          "reportingDate": {
            "type": "Quantity",
            "definition": "http://resource.geosciml.org/concept/numericage/representativeAge",
            "label": "representative age",
            "uom": { "code": "Ma" },
            "value": 335
          },
          "olderBoundDate": {
            "type": "Quantity",
            "definition": "http://resource.geosciml.org/concept/numericage/olderBound",
            "label": "older bound",
            "uom": { "code": "Ma" },
            "value": 350
          },
          "youngerBoundDate": {
            "type": "Quantity",
            "definition": "http://resource.geosciml.org/concept/numericage/youngerBound",
            "label": "younger bound",
            "uom": { "code": "Ma" },
            "value": 325
          }
        }
      }
    },
    {
      "type": "Feature",
      "id": "HerveyGroup.depositionalAge",
      "featureType": "GeologicEvent",
      "geometry": null,
      "properties": {
        "name": "Hervey Group depositional age",
        "eventProcess": [
          "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
        ],
        "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",
        "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Famennian"
      }
    },
    {
      "type": "Feature",
      "id": "fault.1.age",
      "featureType": "GeologicEvent",
      "geometry": null,
      "properties": {
        "name": "Lake George Fault movement age",
        "eventProcess": [
          "http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"
        ],
        "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
        "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Carboniferous"
      }
    }
  ]
}

```


### fc mixed from OGC
Example instance: fc_mixed_from_OGC
#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "hervey-group-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "composition": [
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "mixed-fc-sandstone",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
              }
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "mappedfeature-gu-1",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              149.12,
              -35.31
            ],
            [
              149.45,
              -35.31
            ],
            [
              149.45,
              -35.58
            ],
            [
              149.12,
              -35.58
            ],
            [
              149.12,
              -35.31
            ]
          ]
        ]
      },
      "place": null,
      "time": null,
      "properties": {
        "resolutionRepresentativeFraction": 250000,
        "mappingFrame": "http://resource.geoscience.gov.au/vocabulary/mappingframe/top-of-bedrock",
        "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/exposed",
        "specification": {
          "href": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1",
          "title": "Hervey Group"
        }
      }
    },
    {
      "type": "Feature",
      "featureType": "ShearDisplacementStructure",
      "id": "lake-george-fault-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "occurrence": [
          {
            "href": "http://data.geoscience.gov.au/mappedfeature/line/lake-george-fault-mf-1",
            "title": "Lake George Fault trace"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "featureType": "GeologicEvent",
            "id": "lake-george-fault-age",
            "geometry": null,
            "place": null,
            "time": null,
            "properties": {
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Carboniferous"
            }
          }
        ],
        "faultType": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault"
      }
    },
    {
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "mappedfeature-fault-1",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            149.387,
            -35.124
          ],
          [
            149.412,
            -35.198
          ],
          [
            149.435,
            -35.271
          ],
          [
            149.461,
            -35.344
          ]
        ]
      },
      "place": null,
      "time": null,
      "properties": {
        "positionalAccuracy": {
          "type": "Quantity",
          "uom": {
            "code": "m"
          },
          "value": 250.0,
          "definition": "http://www.opengis.net/def/property/OGC/0/PositionalAccuracy",
          "label": "positional accuracy"
        },
        "resolutionRepresentativeFraction": 250000,
        "mappingFrame": "http://resource.geoscience.gov.au/vocabulary/mappingframe/earth-surface",
        "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/exposed",
        "specification": {
          "href": "http://data.geoscience.gov.au/feature/fault/lake-george-fault-1",
          "title": "Lake George Fault"
        }
      }
    },
    {
      "type": "Feature",
      "featureType": "Contact",
      "id": "contact-devonian-basement-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/unconformity"
      }
    }
  ]
}

```


### fold complex
Example instance: fold_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "Fold",
  "id": "anticline-complex",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "observationMethod": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifierScheme/cgi/featureobservationmethod",
        "label": "field observation",
        "value": "http://resource.geosciml.org/classifier/cgi/featureobservationmethod/field_observation"
      }
    ],
    "purpose": "instance",
    "occurrence": [
      {
        "href": "http://data.geoscience.gov.au/mappedfeature/fold/anticline-mf-1",
        "title": "Anticline trace – 1:50000 sheet"
      }
    ],
    "geologicHistory": [
      {
        "type": "Feature",
        "featureType": "GeologicEvent",
        "id": "anticline-deformation",
        "geometry": null,
        "place": null,
        "time": null,
        "properties": {
          "eventProcess": [
            "http://resource.geosciml.org/classifier/cgi/eventprocess/folding"
          ],
          "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Silurian",
          "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Devonian"
        }
      }
    ],
    "profileType": "http://resource.geosciml.org/classifier/cgi/foldprofiletype/anticline"
  }
}

```


### fold simple
Example instance: fold_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "Fold",
  "id": "anticline-1",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "purpose": "instance",
    "profileType": "http://resource.geosciml.org/classifier/cgi/foldprofiletype/antiform"
  }
}

```


### geologic event from GSO
Translated from https://geosciml.org/schemas/geosciml/4.0/examples/GSML4-GeologicEvent.xml — Kanimblan Orogeny, a deformation event at 335 Ma (range 325–350 Ma), Tournaisian–Serpukhovian, deep crustal setting. Validates against schemas/json/4.1/geoscimlBasic.json#GeologicEvent.
#### json
```json
{
  "$comment": "Translated from https://geosciml.org/schemas/geosciml/4.0/examples/GSML4-GeologicEvent.xml — Kanimblan Orogeny, a deformation event at 335 Ma (range 325–350 Ma), Tournaisian–Serpukhovian, deep crustal setting. Validates against schemas/json/4.1/geoscimlBasic.json#GeologicEvent.",
  "type": "Feature",
  "id": "event.1",
  "featureType": "GeologicEvent",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/json/4.1/geoscimlBasic.json"
  ],
  "geometry": null,
  "properties": {
    "name": "Kanimblan Orogeny",
    "purpose": "instance",
    "eventProcess": [
      "http://resource.geosciml.org/classifier/cgi/eventprocess/deformation"
    ],
    "numericAge": {
      "reportingDate": {
        "type": "Quantity",
        "definition": "http://resource.geosciml.org/concept/numericage/representativeAge",
        "label": "representative age",
        "uom": { "code": "Ma" },
        "value": 335
      },
      "olderBoundDate": {
        "type": "Quantity",
        "definition": "http://resource.geosciml.org/concept/numericage/olderBound",
        "label": "older bound",
        "uom": { "code": "Ma" },
        "value": 350
      },
      "youngerBoundDate": {
        "type": "Quantity",
        "definition": "http://resource.geosciml.org/concept/numericage/youngerBound",
        "label": "younger bound",
        "uom": { "code": "Ma" },
        "value": 325
      }
    },
    "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tournaisian",
    "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Serpukhovian",
    "eventEnvironment": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
        "label": "deep crustal",
        "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
        "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/deep-crustal"
      }
    ]
  }
}

```


### geologic unit complex
Example instance: geologic_unit_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "GeologicUnit",
  "id": "hervey-group-complex",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "observationMethod": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifierScheme/cgi/featureobservationmethod",
        "label": "synthesis from multiple sources",
        "value": "http://resource.geosciml.org/classifier/cgi/featureobservationmethod/synthesis_from_multiple_sources"
      }
    ],
    "occurrence": [
      {
        "href": "http://data.geoscience.gov.au/mappedfeature/polygon/6735427298",
        "title": "Mapped occurrence on 1:250000 sheet"
      }
    ],
    "purpose": "typicalNorm",
    "classifier": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifierScheme/cgi/geologicunittype",
        "label": "Hervey Group stratigraphic lexicon entry",
        "value": "http://data.geoscience.gov.au/stratlex/unit/hervey-group"
      }
    ],
    "geologicHistory": [
      {
        "type": "Feature",
        "featureType": "GeologicEvent",
        "id": "hervey-group-depositional-age",
        "geometry": null,
        "place": null,
        "time": null,
        "properties": {
          "eventProcess": [
            "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
          ],
          "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",
          "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Famennian",
          "eventEnvironment": [
            {
              "type": "Category",
              "definition": "http://resource.geosciml.org/classifierScheme/cgi/valuequalifier",
              "label": "fluvial to shallow marine",
              "value": "http://resource.geosciml.org/classifier/cgi/geologicenvironment/fluvial"
            }
          ]
        }
      },
      {
        "type": "Feature",
        "featureType": "GeologicEvent",
        "id": "hervey-group-deformation-age",
        "geometry": null,
        "place": null,
        "time": null,
        "properties": {
          "eventProcess": [
            "http://resource.geosciml.org/classifier/cgi/eventprocess/deformation"
          ],
          "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tournaisian",
          "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Serpukhovian"
        }
      }
    ],
    "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
    "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
    "composition": [
      {
        "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
        "material": {
          "type": "Feature",
          "featureType": "RockMaterial",
          "id": "hervey-group-mudstone",
          "geometry": null,
          "place": null,
          "time": null,
          "properties": {
            "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
          }
        },
        "proportion": {
          "type": "QuantityRange",
          "uom": {
            "code": "%"
          },
          "value": [
            5.0,
            50.0
          ],
          "definition": "http://resource.geosciml.org/property/proportion",
          "label": "proportion"
        }
      },
      {
        "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
        "material": {
          "type": "Feature",
          "featureType": "RockMaterial",
          "id": "hervey-group-sandstone",
          "geometry": null,
          "place": null,
          "time": null,
          "properties": {
            "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
          }
        },
        "proportion": {
          "type": "QuantityRange",
          "uom": {
            "code": "%"
          },
          "value": [
            50.0,
            95.0
          ],
          "definition": "http://resource.geosciml.org/property/proportion",
          "label": "proportion"
        }
      }
    ],
    "hierarchyLink": [
      {
        "role": "http://resource.geoscience.gov.au/vocabulary/geologicunit_hierarchy_role/constituent_unit",
        "targetUnit": {
          "type": "Feature",
          "featureType": "GeologicUnit",
          "id": "boulton-formation-1",
          "geometry": null,
          "place": null,
          "time": null,
          "properties": {
            "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
            "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation"
          }
        }
      }
    ]
  }
}

```


### geologic unit simple
Example instance: geologic_unit_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "GeologicUnit",
  "id": "hervey-group-1",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "purpose": "typicalNorm",
    "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
    "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
    "occurrence": [
      {
        "href": "http://data.geoscience.gov.au/mappedfeature/polygon/6735427298",
        "title": "Mapped occurrence on 1:250000 sheet"
      }
    ]
  }
}

```


### mapped feature complex
Example instance: mapped_feature_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "MappedFeature",
  "id": "mappedfeature-fault-complex",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [
        149.387,
        -35.124
      ],
      [
        149.412,
        -35.198
      ],
      [
        149.435,
        -35.271
      ],
      [
        149.461,
        -35.344
      ]
    ]
  },
  "place": {
    "type": "LineString",
    "coordinates": [
      [
        149.387,
        -35.124
      ],
      [
        149.412,
        -35.198
      ],
      [
        149.435,
        -35.271
      ],
      [
        149.461,
        -35.344
      ]
    ]
  },
  "time": null,
  "properties": {
    "observationMethod": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifierScheme/cgi/mappedfeatureobservationmethod",
        "label": "inferred from aeromagnetic survey",
        "value": "http://resource.geosciml.org/classifier/cgi/mappedfeatureobservationmethod/inferred_aeromagnetic_survey"
      }
    ],
    "positionalAccuracy": {
      "type": "Quantity",
      "uom": {
        "code": "m"
      },
      "value": 250.0,
      "definition": "http://www.opengis.net/def/property/OGC/0/PositionalAccuracy",
      "label": "positional accuracy"
    },
    "resolutionRepresentativeFraction": 250000,
    "mappingFrame": "http://resource.geoscience.gov.au/vocabulary/mappingframe/earth-surface",
    "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/concealed",
    "specification": {
      "href": "http://data.geoscience.gov.au/feature/fault/lake-george-fault-1",
      "title": "Lake George Fault"
    }
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/4283"
}

```


### mapped feature simple
Example instance: mapped_feature_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "MappedFeature",
  "id": "mappedfeature-gu-1",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [149.12, -35.31],
        [149.45, -35.31],
        [149.45, -35.58],
        [149.12, -35.58],
        [149.12, -35.31]
      ]
    ]
  },
  "place": null,
  "time": null,
  "properties": {
    "mappingFrame": "http://resource.geoscience.gov.au/vocabulary/mappingframe/top-of-bedrock",
    "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/exposed",
    "specification": {
      "href": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1",
      "title": "Hervey Group"
    }
  }
}

```


### natural geomorphologic feature complex
Example instance: natural_geomorphologic_feature_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "NaturalGeomorphologicFeature",
  "id": "moraine-complex",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [148.210, -36.445],
        [148.290, -36.445],
        [148.290, -36.510],
        [148.210, -36.510],
        [148.210, -36.445]
      ]
    ]
  },
  "place": null,
  "time": null,
  "properties": {
    "observationMethod": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifierScheme/cgi/featureobservationmethod",
        "label": "remote sensing interpretation",
        "value": "http://resource.geosciml.org/classifier/cgi/featureobservationmethod/remote_sensing_interpretation"
      }
    ],
    "purpose": "instance",
    "naturalGeomorphologicFeatureType": "http://resource.geosciml.org/classifier/cgi/geomorphologicfeaturetype/moraine",
    "activity": {
      "type": "Category",
      "definition": "http://resource.geosciml.org/classifierScheme/cgi/geomorphologicactivity",
      "label": "inactive",
      "value": "http://resource.geosciml.org/classifier/cgi/geomorphologicactivity/inactive"
    },
    "unitDescription": [
      {
        "href": "http://data.geoscience.gov.au/feature/geologicunit/glacial-till-1",
        "title": "Pleistocene glacial till"
      }
    ]
  }
}

```


### natural geomorphologic feature simple
Example instance: natural_geomorphologic_feature_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "NaturalGeomorphologicFeature",
  "id": "river-valley-1",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "purpose": "instance",
    "naturalGeomorphologicFeatureType": "http://resource.geosciml.org/classifier/cgi/geomorphologicfeaturetype/river_channel",
    "activity": {
      "type": "Category",
      "definition": "http://resource.geosciml.org/classifierScheme/cgi/geomorphologicactivity",
      "label": "active",
      "value": "http://resource.geosciml.org/classifier/cgi/geomorphologicactivity/active"
    }
  }
}

```


### shear displacement structure complex
Example instance: shear_displacement_structure_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "ShearDisplacementStructure",
  "id": "lake-george-fault-complex",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "observationMethod": [
      {
        "type": "Category",
        "definition": "http://resource.geosciml.org/classifierScheme/cgi/featureobservationmethod",
        "label": "synthesis from multiple sources",
        "value": "http://resource.geosciml.org/classifier/cgi/featureobservationmethod/synthesis_from_multiple_sources"
      }
    ],
    "purpose": "instance",
    "occurrence": [
      {
        "href": "http://data.geoscience.gov.au/mappedfeature/line/lake-george-fault-mf-1",
        "title": "Lake George Fault trace at 1:250000 scale"
      }
    ],
    "geologicHistory": [
      {
        "type": "Feature",
        "featureType": "GeologicEvent",
        "id": "lake-george-fault-age",
        "geometry": null,
        "place": null,
        "time": null,
        "properties": {
          "eventProcess": [
            "http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"
          ],
          "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
          "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Carboniferous"
        }
      }
    ],
    "faultType": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault"
  }
}

```


### shear displacement structure simple
Example instance: shear_displacement_structure_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "ShearDisplacementStructure",
  "id": "lake-george-fault-1",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "purpose": "instance",
    "faultType": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault"
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmBasicGeology/gsmBasicGeologySchema.json
description: 'GeoSciML 4.1 Basic application schema. Core feature types

  (GeologicFeature, MappedFeature, GeologicUnit, GeologicStructure

  subtypes, GeomorphologicFeature, EarthMaterial, Contact, Fold,

  Foliation, ShearDisplacementStructure, GeologicEvent) plus the

  shared GSML_DataTypes and Collection containers. The merged schema

  dispatches all 9 concrete FeatureType classes

  (AnthropogenicGeomorphologicFeature, Contact, Fold, Foliation,

  GeologicEvent, GeologicUnit, MappedFeature,

  NaturalGeomorphologicFeature, ShearDisplacementStructure) and

  accepts either single Features or FeatureCollections at the root.


  Validates either a single Feature (dispatched by `featureType` to one of: AnthropogenicGeomorphologicFeature,
  Contact, Fold, Foliation, GeologicEvent, GeologicUnit, MappedFeature, NaturalGeomorphologicFeature,
  ShearDisplacementStructure) or a FeatureCollection whose `features[]` items are
  dispatched the same way.'
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
            const: AnthropogenicGeomorphologicFeature
      then:
        $ref: '#AnthropogenicGeomorphologicFeature'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: Contact
      then:
        $ref: '#Contact'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: Fold
      then:
        $ref: '#Fold'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: Foliation
      then:
        $ref: '#Foliation'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GeologicEvent
      then:
        $ref: '#GeologicEvent'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GeologicUnit
      then:
        $ref: '#GeologicUnit'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: MappedFeature
      then:
        $ref: '#MappedFeature'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: NaturalGeomorphologicFeature
      then:
        $ref: '#NaturalGeomorphologicFeature'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: ShearDisplacementStructure
      then:
        $ref: '#ShearDisplacementStructure'
    - if:
        not:
          required:
          - featureType
          properties:
            featureType:
              enum:
              - AnthropogenicGeomorphologicFeature
              - Contact
              - Fold
              - Foliation
              - GeologicEvent
              - GeologicUnit
              - MappedFeature
              - NaturalGeomorphologicFeature
              - ShearDisplacementStructure
      then: false
  AbstractFeatureRelation:
    $anchor: AbstractFeatureRelation
    description: Association class placeholder to implement relation between geologic
      features
    type: object
  AnthropogenicGeomorphologicFeature:
    $anchor: AnthropogenicGeomorphologicFeature
    description: An anthropogenic geomorphologic feature is a geomorphologic feature
      (i.e., landform) which has been created by human activity. For example, a dredged
      channel, midden, open pit or reclaimed land.
    allOf:
    - $ref: '#GeomorphologicFeature'
    - type: object
      properties:
        properties:
          type: object
          properties:
            anthropogenicGeomorphologicFeatureType:
              oneOf:
              - type: 'null'
              - $ref: '#AnthropogenicGeomorphologicFeatureTypeTerm'
              description: 'The anthropogenicGeomorphologicFeatureType: AnthropogenicGeomorphologicFeatureTypeTerm
                is a reference from a controlled vocabulary describing the type of
                geomorphologic feature.'
  AnthropogenicGeomorphologicFeatureTypeTerm:
    $anchor: AnthropogenicGeomorphologicFeatureTypeTerm
    description: Refers to a vocabulary of terms describing the type of anthropogenic
      geomorphologic feature
    type: string
    format: uri
  CollectionTypeTerm:
    $anchor: CollectionTypeTerm
    description: 'Types of collections of geological and geophysical objects. Examples:
      "borehole collection", "geological map", "geological model", "geophysical object
      collection" (from INSPIRE)'
    type: string
    format: uri
  CompositionPart:
    $anchor: CompositionPart
    description: CompositionPart represents the composition of a geologic unit in
      terms of earth material constituents (CompoundMaterial). It decomposes the material
      making of the unit into parts having distinct roles and proportions.
    type: object
    properties:
      role:
        oneOf:
        - type: 'null'
        - $ref: '#CompositionPartRoleTerm'
        description: The property role:CompositionPartRoleTerm defines the relationship
          of the CompoundMaterial constituent in the geologic unit, e.g. vein, interbedded
          constituent, layers, dominant constituent.
      proportion:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
        description: The proportion property (SWE::QuantityRange) specifies the fraction
          of the geologic unit composed of the compound material.
      material:
        oneOf:
        - type: 'null'
        - oneOf:
          - $ref: '#/$defs/SCLinkObject'
            $comment: by-reference link to CompoundMaterial
          - $ref: '#CompoundMaterial'
        description: The material:EarthMaterial property contains the material description
          of the composing part.
  CompositionPartRoleTerm:
    $anchor: CompositionPartRoleTerm
    description: This class is a blank placeholder for a vocabulary of terms to describe
      the role that a compositional part plays in a geologic unit.
    type: string
    format: uri
  CompoundMaterial:
    $anchor: CompoundMaterial
    description: A CompoundMaterial is an EarthMaterial composed of particles made
      of EarthMaterials, possibly including other CompoundMaterials. This class is
      provided primarily as an extensibility point for related domain models that
      wish to import and build on GeoSciML, and wish to define material types that
      are compound but are not rock or rock-like material. In the context of GeoSciML
      "RockMaterial" should be used to describe units made of rock.
    allOf:
    - $ref: '#EarthMaterial'
    - type: object
  Contact:
    $anchor: Contact
    description: A contact is a general concept representing any kind of surface separating
      two geologic units, including primary boundaries such as depositional contacts,
      all kinds of unconformities, intrusive contacts, and gradational contacts, as
      well as faults that separate geologic units.
    allOf:
    - $ref: '#GeologicStructure'
    - type: object
      properties:
        properties:
          type: object
          properties:
            contactType:
              oneOf:
              - type: 'null'
              - $ref: '#ContactTypeTerm'
              description: The property contactType:ContactTypeTerm classifies the
                contact (e.g. intrusive, unconformity, bedding surface, lithologic
                boundary, phase boundary) and is a term from a controlled vocabulary.
            stContactDescription:
              oneOf:
              - type: 'null'
              - $ref: '#ContactAbstractDescription'
              description: The property stContactDescription:ContactAbstractDescription
                provides a detailed contact description. This is a stub property in
                GeoSciML Basic since ContactAbstractDescription is an abstract class
                with subtypes defined in GeoSciML Extension.
  ContactAbstractDescription:
    $anchor: ContactAbstractDescription
    description: An abstract class providing a link between classes in GeoSciMLBasic
      and GeoSciMLExtended application schemas.
    type: object
  ContactTypeTerm:
    $anchor: ContactTypeTerm
    description: Refers to a vocabulary of terms describing types of geological contacts
    type: string
    format: uri
  ConventionCode:
    $anchor: ConventionCode
    description: "Suggested values: \"dip dip direction\", \"strike dip right hand
      rule\" (The strike and dip of planar data is listed according to the \u2018right-hand
      rule\u2019 or, as one looks along the strike direction, the surface dips to
      the right.) This list is an indicative list only of terms used to describe the
      convention used for the orientation measurement. Users are encouraged to use
      a vocabulary of terms managed by the CGI vocabularies working group outside
      of this model."
    type: string
    format: uri
  DescriptionPurpose:
    $anchor: DescriptionPurpose
    description: 'Codes used for the specification of the intended purpose/level of
      abstraction for a given feature or object instance, ie the reason for the existence
      of the GeologicFeature. Values: instance, typicalNorm, definingNorm.'
    type: string
    enum:
    - definingNorm
    - instance
    - typicalNorm
  DeterminationMethodTerm:
    $anchor: DeterminationMethodTerm
    description: This class is an empty placeholder for a vocabulary of terms describing
      the method used to determine the measured orientation. Users are encouraged
      to use a vocabulary of terms managed by the CGI vocabularies working group outside
      of this model.
    type: string
    format: uri
  EarthMaterial:
    $anchor: EarthMaterial
    description: 'The EarthMaterial class holds a description of a naturally occurring
      substance in the Earth. EarthMaterial represents material composition or substance,
      and is thus independent of quantity or location. Ideally, EarthMaterials are
      defined strictly based on physical properties, but because of standard geological
      usage, genetic interpretations enter into the description as well.  Constraint:
      self.metadata.hierarchyLevel=feature'
    type: object
    properties:
      color:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: The color property (SWE::Category) is a term from a controlled
          vocabulary that specifies the colour of the earth material. Color schemes
          such as the Munsell rock and soil color schemes may be used.
      purpose:
        oneOf:
        - type: 'null'
        - $ref: '#DescriptionPurpose'
        description: "The purpose:DescriptionPurpose property provides a specification
          of the intended purpose or level of abstraction for the given EarthMaterial.
          The intent is the same a GeologicFeature\u2019s purpose and it shares the
          same vocabulary (instance, typicalNorm, definingNorm)."
      gbEarthMaterialDescription:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: '#EarthMaterialAbstractDescription'
          uniqueItems: true
        description: The property gbEarthMaterialDescription:EarthMaterialAbstractDescription
          provides a detailed earth material description of the part. This property
          is a stub in GeoSciML Basic as EarthMaterialAbstractDescription is abstract
          with subtypes defined in GeoSciML Extension.
  EarthMaterialAbstractDescription:
    $anchor: EarthMaterialAbstractDescription
    description: Abstract description class for earth material. This class is a placeholder
      for further extension in Extension package
    type: object
  EventProcessTerm:
    $anchor: EventProcessTerm
    description: Refers to a vocabulary of terms specifying the process or processes
      that occurred during an event. Examples include deposition, extrusion, intrusion,
      cooling.
    type: string
    format: uri
  ExposureTerm:
    $anchor: ExposureTerm
    description: This class is a blank placeholder for a vocabulary of terms describing
      the nature of the expression of the mapped feature at the earth's surface (eg,
      exposed, concealed)
    type: string
    format: uri
  FaultTypeTerm:
    $anchor: FaultTypeTerm
    description: A vocabulary of terms describing the type of shear displacement structure
      (eg; thrust fault, normal fault, wrench fault)
    type: string
    format: uri
  Fold:
    $anchor: Fold
    description: A fold is formed by one or more systematically curved layers, surfaces,
      or lines in a rock body. A fold denotes a structure formed by the deformation
      of a geologic structure, such as a contact which the original undeformed geometry
      is presumed, to form a structure that may be described by the translation of
      an abstract line (the fold axis) parallel to itself along some curvilinear path
      (the fold profile). Folds have a hinge zone (zone of maximum curvature along
      the surface) and limbs (parts of the deformed surface not in the hinge zone).
      Folds are described by an axial surface, hinge line, profile geometry, the solid
      angle between the limbs, and the relationships between adjacent folded surfaces
      if the folded structure is a Layering fabric.
    allOf:
    - $ref: '#GeologicStructure'
    - type: object
      properties:
        properties:
          type: object
          properties:
            profileType:
              oneOf:
              - type: 'null'
              - $ref: '#FoldProfileTypeTerm'
              description: The property profileType:FoldProfileTypeTerm contains a
                term from a controlled vocabulary specifying the concave/convex geometry
                of fold relative to earth surface, and relationship to younging direction
                in folded strata if known. (e.g., antiform, synform, neutral, anticline,
                syncline, monocline, ptygmatic).
            stFoldDescription:
              oneOf:
              - type: 'null'
              - $ref: '#FoldAbstractDescription'
              description: The property stFoldDescription:FoldAbstractDescription
                provides a detailed fold description. This is a stub property in GeoSciML
                Basic since FoldAbstractDescription is an abstract class with subtypes
                defined in GeoSciML Extension.
  FoldAbstractDescription:
    $anchor: FoldAbstractDescription
    description: An abstract class providing a link between classes in GeoSciMLBasic
      and GeoSciMLExtended application schemas.
    type: object
  FoldProfileTypeTerm:
    $anchor: FoldProfileTypeTerm
    description: Refers to a vocabulary of terms specifying concave/convex geometry
      of fold relative to earth surface, and relationship to younging direction in
      folded strata if known. antiform, synform, neutral, anticline, syncline, monocline,
      ptygmatic
    type: string
    format: uri
  Foliation:
    $anchor: Foliation
    description: A foliation is a planar arrangement of textural or structural features
      in any type of rock. It includes any of a wide variety of penetrative planar
      geological structures that may be present in a rock. Examples include schistosity,
      mylonitic foliation, penetrative bedding structure (lamination), and cleavage.
      Following the proposed definition of gneiss by the NADM Science Language Technical
      Team, penetrative planar foliation defined by layers &gt; 5 mm thick is considered
      Layering.
    allOf:
    - $ref: '#GeologicStructure'
    - type: object
      properties:
        properties:
          type: object
          properties:
            foliationType:
              oneOf:
              - type: 'null'
              - $ref: '#FoliationTypeTerm'
              description: The foliationType:FoliationTypeTerm property specifies
                the type of foliation from a controlled vocabulary. Examples include
                crenulation cleavage, slaty cleavage and schistosity.
            stFoliationDescription:
              oneOf:
              - type: 'null'
              - $ref: '#FoliationAbstractDescription'
              description: The foliationType:FoliationTypeTerm property specifies
                the type of foliation from a controlled vocabulary. Examples include
                crenulation cleavage, slaty cleavage and schistosity.
  FoliationAbstractDescription:
    $anchor: FoliationAbstractDescription
    description: 'An abstract class providing a link between classes in GeoSciMLBasic
      and GeoSciMLExtended application schemas.  Constraint: only one instance of
      each subtype class is allowed'
    type: object
  FoliationTypeTerm:
    $anchor: FoliationTypeTerm
    description: Refers to a vocabular of terms defining the type of foliation (eg,
      crenulation cleavage, gneissic layering, slaty cleavage, schistosity, etc)
    type: string
    format: uri
  GSML:
    $anchor: GSML
    description: 'GSML is a collection class grouping a set of features or types which
      are members of this collection. A collectionType property provides context or
      purpose.  Constraint: self.metadata.hierarchylevel=dataset'
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            collectionType:
              oneOf:
              - type: 'null'
              - $ref: '#CollectionTypeTerm'
              description: The collectionType:CollectionTypeTerm property contains
                a term from a controlled vocabulary describing the type of collection,
                such as Geologic Map, Boreholes, 3D models.
            member:
              type: array
              minItems: 1
              items:
                $ref: '#GSMLitem'
              uniqueItems: true
              description: The member property is an association that links a GSML
                instance to features and objects to be included as members of the
                collection. A collection can be made of heterogeneous items.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GSML_GeometricDescriptionValue:
    $anchor: GSML_GeometricDescriptionValue
    description: GSML_GeometricDescriptionValue is a special abstract data type for
      descriptions of planar or linear orientations of a geologic feature. Different
      subtypes allow specifying direction by direction vector (e.g. dip/dip direction),
      compass point (e.g. NE), or description (e.g. "toward fold hinge", "below').
    type: object
    properties:
      determinationMethod:
        oneOf:
        - type: 'null'
        - $ref: '#DeterminationMethodTerm'
        description: The determinationMethod:DeterminationMethodTerm property describes
          the way the orientation value was determined (e.g. measured, inferred from
          dip slope, etc.) using a reference to a controlled vocabulary.
      descriptiveOrientation:
        oneOf:
        - type: 'null'
        - type: string
        description: The descriptionOrientation:Primitive::CharacterString contains
          a textual specification of orientation, possibly referencing some local
          geography (e.g. "toward fold hinge", "below").
  GSML_LinearOrientation:
    $anchor: GSML_LinearOrientation
    description: A linear orientation is composed of a trend (the compass orientation
      of the line) and a plunge (the angle from the horizontal). This vector may be
      oriented (pointing in a specific direction) or not.
    allOf:
    - $ref: '#GSML_GeometricDescriptionValue'
    - type: object
      properties:
        directed:
          oneOf:
          - type: 'null'
          - $ref: '#LinearDirectedCode'
          description: The directed:LinearDirectedCode property indicates if the orientation
            represents a linear feature that is directed, e.g. clast imbrication,
            mylonitic lineation with sense of shear, slickenlines with displacement
            direction, rather than undirected (like a fold hinge line or intersection
            lineations). A code list will indicate which is the directed end of the
            linear orientation. The value of the property comes from a controlled
            vocabulary.
        plunge:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The property plunge (SWE::QuantityRange) reports the magnitude
            of the plunge as an angle from horizontal.
        trend:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The property trend (SWE::QuantityRange) reports the azimuth
            (compass bearing) value of the linear orientation.
  GSML_PlanarOrientation:
    $anchor: GSML_PlanarOrientation
    description: A planar orientation is composed of two values; the azimuth (a compass
      point) and a dip (the angle from the horizontal). Polarity of the plane indicates
      whether the planar orientation is associated with a directed feature that is
      overturned, upright, vertical, etc. There are several conventions to encode
      a planar orientation and this specification does not impose one but provides
      a convention property to report it. It must be noted that allowance for different
      conventions makes manipulation of the data more difficult. Therefore it is recommended
      that user communities adopt a single measurement convention.
    allOf:
    - $ref: '#GSML_GeometricDescriptionValue'
    - type: object
      properties:
        convention:
          oneOf:
          - type: 'null'
          - $ref: '#ConventionCode'
          description: The property convention:ConventionCode contains the convention
            used for the measurement from a controlled vocabulary.
        azimuth:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The azimuth (SWE::QuantityRange) property (compass point, bearing
            etc.) contains the value of the orientation. The convention property reports
            how azimuth is interpreted (if it is relative to a quadrant).
        dip:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The dip (SWE::QuantityRange) reports the angle that the structural
            surface (e.g. bedding, fault plane) makes with the horizontal measured
            perpendicular to the strike of the structure and in the vertical plane
            as a numeric value or term.
        polarity:
          oneOf:
          - type: 'null'
          - $ref: '#PlanarPolarityCode'
          description: The polarity:PolarityCode indicates whether the planar orientation
            is associated with a directed feature that is overturned, upright, vertical
            etc., using a controlled vocabulary.
  GSML_QuantityRange:
    $anchor: GSML_QuantityRange
    description: "GSML_QuantityRange is a specialization of SWE Common QuantiytyRange
      (OGC 08-094r1, Clause 7.2.13) where lower and upper values are made explicit.
      SWE::QuantityRange uses an array of values (RealPair, see Clause 7.2.1) where
      the lowest value is the first element and the highest the second. This convenience
      data type has been created as an alternative encoding for implementations that
      do no support encoding of arrays in a single field (e.g. DBF) or reference to
      elements in string encoded arrays1 (eg. Filter Encoding Specification 2.0 \u2013
      OGC 09-029r2). &nbsp;------------------------- 1 SWE RealPair is encoded as
      space delimited lists (&lt;swe:value&gt;10 300&lt;/swe:value&gt; in XML) , which
      demands that clients parse the string to extract each token. To build a WFS/FES
      query that tests the first element, it requires parsing the string either using
      string-before(swe:value,' ') or tokenize(swe:value,' '). This is cumbersome
      at best, or not even supported by the server at worst. 09-026r2 Clause 7.4.4
      describes the minimal XPath supports and string parsing is not present."
    type: object
    properties:
      lowerValue:
        type: number
        description: The property lowerValue:Real contains the lower bound of the
          range. It shall be a copy of inherited SWE::QuantityRange::value[0].
      upperValue:
        type: number
        description: The property upperValue:Real contains the upper bound of the
          range. It shall be a copy of inherited SWE::QuantityRange::value[1].
    required:
    - lowerValue
    - upperValue
  GSML_Vector:
    $anchor: GSML_Vector
    description: A GSML_Vector is a data type representing a linear orientation with
      a magnitude (a quantity assigned to this vector). If the magnitude is unknown,
      a GSML_LinearOrientation shall be used.
    allOf:
    - $ref: '#GSML_LinearOrientation'
    - type: object
      properties:
        magnitude:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The magnitude property (SWE::QuantityRange) reports the magnitude
            of the vector.
  GSMLitem:
    $anchor: GSMLitem
    description: GSMLItem constrains the collection members to instances of EarthMaterial,
      GeologicFeature, GM_Object, MappedFeature, AbstractFeatureRelation and OM::SF_SamplingFeature.
    oneOf:
    - oneOf:
      - $ref: '#/$defs/SCLinkObject'
        $comment: by-reference link to EarthMaterial
      - $ref: '#EarthMaterial'
    - oneOf:
      - $ref: '#/$defs/SCLinkObject'
        $comment: by-reference link to GeologicFeature
      - $ref: '#GeologicFeature'
    - $ref: https://geojson.org/schema/Geometry.json
    - oneOf:
      - $ref: '#/$defs/SCLinkObject'
        $comment: by-reference link to MappedFeature
      - $ref: '#MappedFeature'
    - oneOf:
      - $ref: '#/$defs/SCLinkObject'
        $comment: by-reference link to AbstractFeatureRelation
      - $ref: '#AbstractFeatureRelation'
    - $ref: '#/$defs/SCLinkObject'
      $comment: "External ISO 19156 SF_SamplingFeature \u2014 by-reference link"
  GeochronologicEraTerm:
    $anchor: GeochronologicEraTerm
    description: Term from a Geochronological vocabulary
    type: string
    format: uri
  GeologicEvent:
    $anchor: GeologicEvent
    description: A GeologicEvent is an identifiable event during which one or more
      geological processes act to modify geological entities. It may have a specified
      geologic age (numeric age or GeochologicEraTerm) and may have specified environments
      and processes. An example might be a cratonic uplift event during which erosion,
      sedimentation, and volcanism all take place.
    allOf:
    - $ref: '#GeologicFeature'
    - type: object
      properties:
        properties:
          type: object
          properties:
            eventProcess:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#EventProcessTerm'
                uniqueItems: true
              description: The eventProcess:EventProcessTerm property provides a term
                from a controlled vocabulary specifying the process or processes that
                occurred during the event. Examples include deposition, extrusion,
                intrusion, cooling.
            numericAge:
              oneOf:
              - type: 'null'
              - $ref: '#NumericAgeRange'
              description: The numericAge:NumericAgeRange property provides an age
                in absolute year before present (BP). Present is defined by convention
                to be January 1st 1950 (although van der Plitch & Hogg , suggests
                this convention to be restricted to radiocarbon estimations).
            olderNamedAge:
              oneOf:
              - type: 'null'
              - $ref: '#GeochronologicEraTerm'
              description: The property olderNamedAge:GeochronologicalEraTerm defines
                the older boundary of age of an event expressed using a geochronologic
                era defined according to a geologic time scale as per the GeologicTime
                schema (eg, the International Commission on Stratigraphy Chronostratigraphic
                Chart - http://www.stratigraphy.org/index.php/ics-chart-timescale).
            youngerNamedAge:
              oneOf:
              - type: 'null'
              - $ref: '#GeochronologicEraTerm'
              description: The property youngerNamedAge:GeochronologicalEraTerm defines
                the younger boundary of age of event expressed using a geochronologic
                era defined according to a geologic time scale per the GeologicTime
                schema. (eg, the International Commission on Stratigraphy Chronostratigraphic
                Chart - http://www.stratigraphy.org/index.php/ics-chart-timescale).
            eventEnvironment:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
                uniqueItems: true
              description: "The eventEnvironment property (SWE::Category) is a category
                from a controlled vocabulary identifying the physical setting within
                which a GeologicEvent takes place. Event environment is construed
                broadly to include physical settings on the Earth surface specified
                by climate, tectonics, physiography or geography, and settings in
                the Earth\u2019s interior specified by pressure, temperature, chemical
                environment, or tectonics."
            gaEventDescription:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#GeologicEventAbstractDescription'
                uniqueItems: true
              description: The property geEventDescription:GeologicEventAbstractDescription
                contains a detailed event description. This is a stub property in
                GeoSciML Basic since GeologicEventAbstractDescription is abstract
                and with subtypes defined in GeoSciML Extension.
  GeologicEventAbstractDescription:
    $anchor: GeologicEventAbstractDescription
    description: Stub property class to allow extended event related properties.
    type: object
  GeologicFeature:
    $anchor: GeologicFeature
    description: "The abstract GeologicFeature class represents a conceptual feature
      that is hypothesized to exist coherently in the world. It corresponds with a
      \"legend item\" from a traditional geologic map and its instance acts as the
      \"description package\". The description package is classified according to
      its intended purpose as a typicalNorm, definingNorm or instance. GeologicFeature
      can be used outside the context of a map (it can lack a MappedFeature), for
      example when describing typical norms (describing expected property from a feature)
      or defining norms (describing properties required from a feature to be classifying
      in a group, such as given geologic unit). A GeologicFeature appearing on a map
      is considered as an \u201Cinstance\u201D.  Constraint: self.metadata.hierarchyLevel=(feature
      or dataset or series)"
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            observationMethod:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
                uniqueItems: true
              description: The GeologicFeature observationMethod (SWE::Category) specifies
                the approach to acquiring the collection of attribute values that
                constitute an individual feature instance (e.g. point count, brunton
                compass on site, air photo interpretation, field observation, hand
                specimen, laboratory, aerial photography, creative imagination). ObservationMethod
                is a convenience property that provides a simple approach to observation
                metadata when data are reported using a feature view (as opposed to
                observation view). This property corresponds (loosely) to ISO19115
                Lineage.
            purpose:
              oneOf:
              - type: 'null'
              - $ref: '#DescriptionPurpose'
              description: 'The property purpose:DescriptionPurpose specifies the
                intended purpose/level of abstraction for a given feature or object
                instance. The possible values are: instance, typicalNorm, and definingNorm.'
            classifier:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
                uniqueItems: true
              description: The classifier (SWE::Category) contains a standard description
                or definition of the feature type (e.g., the definition of a particular
                geologic unit in a stratigraphic lexicon).
            relatedFeature:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to GeologicFeature
                  - $ref: '#GeologicFeature'
                uniqueItems: true
              description: A relatedFeature is a general structure used to define
                relationships between any features or objects within GeoSciML. Relationships
                are always binary and directional. There is always a single source
                and a single target for a given FeatureRelation (which is abstract
                in GeoSciML Basic). The relationship is always defined from the perspective
                of the Source and is generally an active verb.
            geologicHistory:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to GeologicEvent
                  - $ref: '#GeologicEvent'
                uniqueItems: true
              description: The geologicHistory is an association that relates one
                or more GeologicEvents to a GeologicFeature to describe their age
                or geologic history. Normally, GeoSciML uses the generic relatedFeature::GeologicRelation
                to associate GeologicFeature with other GeologicFeatures, including
                GeologicEvent. However, this design was deemed too complex for GeoSciML
                Basic and is therefore only available from the GeoSciML Extension
                package.
            occurrence:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to MappedFeature
                  - $ref: '#MappedFeature'
                uniqueItems: true
              description: The occurrence property is an association that links a
                notional geologic feature with any number of mapped features (MappedFeature).
                A geologic feature, such as a geologic unit may be linked to mapped
                features from a number of different maps.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeologicStructure:
    $anchor: GeologicStructure
    description: A geologic structure is a configuration of matter in the Earth based
      on describable inhomogeneity, pattern, or fracture in an earth material. The
      identity of a GeologicStructure is independent of the material that is the substrate
      for the structure. The general GeologicFeatureRelation (available in the Extension
      package) is used to associate penetrative GeologicStructures with GeologicUnits.
      GeoSciML Basic only provides a limited set of core structures (Contact, Fold,
      ShearDisplacementStructure and Foliation) with a single property to categorise
      them. Supplemental properties and geologic structure types are available from
      the Extension package.
    allOf:
    - $ref: '#GeologicFeature'
    - type: object
      properties:
        properties:
          type: object
          properties: {}
  GeologicUnit:
    $anchor: GeologicUnit
    description: 'Conceptually, a GeologicUnit may represent a body of material in
      the Earth whose complete and precise extent is inferred to exist (e.g., North
      American Data Model GeologicUnit, Stratigraphic unit in the sense of NACSN,
      or International Stratigraphic Code ), or a classifier used to characterize
      parts of the Earth (e.g. lithologic map unit like ''granitic rock'' or ''alluvial
      deposit'', surficial units like ''till'' or ''old alluvium''). It includes both
      formal units (i.e. formally adopted and named in an official lexicon) and informal
      units (i.e. named but not promoted to a lexicon) and unnamed units (i.e., recognizable,
      described and delineable in the field but not otherwise formalised). In simpler
      terms, a geologic unit is a package of earth material (generally rock).  Constraint:
      target of composition is only CompositionPart  Constraint: target of geologicHistory
      is only GeologicEvent'
    allOf:
    - $ref: '#GeologicFeature'
    - type: object
      properties:
        properties:
          type: object
          properties:
            geologicUnitType:
              oneOf:
              - type: 'null'
              - $ref: '#GeologicUnitTypeTerm'
              description: The property geologicUnitType:GeologicUnitTypeTerm provides
                a term from a controlled vocabulary defining the type of geologic
                unit. Logical constraints of definition of unit and valid property
                cardinalities should be contained in the definition. Use of the CGI
                Geologic Unit Type vocabulary (e.g., http://resource.geosciml.org/classifierscheme/cgi/201211/geologicunittype)
                is recommended.
            rank:
              oneOf:
              - type: 'null'
              - $ref: '#RankTerm'
              description: 'The property rank:RankTerm contains a term that classifies
                the geologic unit in a generalization hierarchy from most local/smallest
                volume to most regional/largest. Examples: group, subgroup, formation,
                member, bed, intrusion, complex, batholith'
            gbMaterialDescription:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#EarthMaterialAbstractDescription'
                uniqueItems: true
              description: The property gbMaterialDescription:EarthMaterialAbstractDescription
                is a placeholder that provides detailed material description. This
                is a stub property in GeoSciML Basic as EarthMaterialAbstractDescription
                is abstract with subtypes defined in GeoSciML Extension.
            hierarchyLink:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#GeologicUnitHierarchy'
                uniqueItems: true
              description: The property hierarchyLink is an association that links
                a GeologicUnit with a GeologicUnitHierarchy to represent containment
                of a part GeologicUnit within another GeologicUnit. It indicates a
                subsidiary unit with its role and proportion with respect to the container
                unit. For example, members are described as part of formations, or
                different facies can be described as parts of a GeologicUnit.
            gbUnitDescription:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#GeologicUnitAbstractDescription'
                uniqueItems: true
              description: The property gbUnitDescription:GeologicUnitAbstractDescriptio
                is a placeholder that provides detailed material description. This
                is a stub property in GeoSciML Basic as GeologicUnitAbstractDescription
                is abstract with subtypes defined in GeoSciML Extension.
            composition:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#CompositionPart'
                uniqueItems: true
              description: The property composition is an association that links a
                GeologicUnit with CompositionParts to describe the material composition
                of the GeologicUnit (e.g., a detailed, instance specific, lithologic
                description)
  GeologicUnitAbstractDescription:
    $anchor: GeologicUnitAbstractDescription
    description: Abstract description class for geologic units. This class is a placeholder
      for further extension in Extension package
    type: object
  GeologicUnitHierarchy:
    $anchor: GeologicUnitHierarchy
    description: GeologicUnitHierarchy associates a GeologicUnit with another GeologicUnit
      that is a proper part of that unit. Parts may be formal or notional. Formal
      parts refer to a specific body of rock, as in formal stratigraphic members.
      Notional parts refer to assemblages of particular EarthMaterials with particular
      internal structure, which may be repeated in various places within a unit (e.g.
      'turbidite sequence', 'point bar assemblage', 'leucosome veins').
    type: object
    properties:
      role:
        oneOf:
        - type: 'null'
        - $ref: '#GeologicUnitHierarchyRoleTerm'
        description: The role:GeologicUnitHierarchyRoleTerm property provides a term
          describing the nature of the parts, e.g. facies, stratigraphic, interbeds,
          geographic, eastern facies.
      proportion:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
        description: The proportion property (SWE::QuantityRange) provides a quantity
          that represents the fraction of the geologic unit formed by the part.
      targetUnit:
        oneOf:
        - $ref: '#/$defs/SCLinkObject'
          $comment: by-reference link to GeologicUnit
        - $ref: '#GeologicUnit'
        description: The property targetUnit is an association that specifies exactly
          one GeologicUnit that is a proper part of another GeologicUnit.
    required:
    - targetUnit
  GeologicUnitHierarchyRoleTerm:
    $anchor: GeologicUnitHierarchyRoleTerm
    description: Role of the unit in the hierarchy
    type: string
    format: uri
  GeologicUnitPartRoleTerm:
    $anchor: GeologicUnitPartRoleTerm
    description: This class is a blank placeholder for a vocabulary of terms describing
      the nature of the parts of a geologic unit, e.g. facies, stratigraphic, interbeds,
      geographic, eastern facies,
    type: string
    format: uri
  GeologicUnitTypeTerm:
    $anchor: GeologicUnitTypeTerm
    description: 'This class is an indicative placeholder only for a vocabulary of
      terms describing the type of geologic unit. Users are encouraged to use the
      vocabulary of unit types provided by the CGI vocabularies working group. Example
      values: GeologicUnit AllostratigraphicUnit AlterationUnit ArtificialGround BiostratigraphicUnit
      ChronostratigraphicUnit DeformationUnit ExcavationUnit GeophysicalUnit LithodemicUnit
      LithogeneticUnit LithologicUnit LithostratigraphicUnit LithotectonicUnit MagnetostratigraphicUnit
      MassMovementUnit Pedoderm PedostratigraphicUnit PolarityChronostratigraphicUnit'
    type: string
    format: uri
  GeomorphologicFeature:
    $anchor: GeomorphologicFeature
    description: A geomorphologic feature is a kind of GeologicFeature describing
      the shape and nature of the Earth's land surface. These landforms may be created
      by natural Earth processes (e.g., river channel, beach, moraine or mountain)
      or through human (anthropogenic) activity (e.g., dredged channel, reclaimed
      land, mine waste dumps). In GeoSciML, the geomorphologic feature is modelled
      as a feature related (through unitDescription property) to a GeologicUnit that
      composes the form.
    allOf:
    - $ref: '#GeologicFeature'
    - type: object
      properties:
        properties:
          type: object
          properties:
            unitDescription:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to GeologicUnit
                  - $ref: '#GeologicUnit'
                uniqueItems: true
              description: The unitDescription property is an association that links
                the geomorphologic feature to a geologic description (e.g., related
                stratigraphic units and earth materials).
            gmFeatureDescription:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#GeomorphologicUnitAbstractDescription'
                uniqueItems: true
              description: The property gmFeatureDescription:GeomorphologicUnitAbstractDescription
                provides a detailed morphologic description. This is a stub property
                in GeoSciML Basic since GeomorphologicUnitAbstractDescription is an
                abstract class with no concrete subtype in GeoSciML Basic.
  GeomorphologicUnitAbstractDescription:
    $anchor: GeomorphologicUnitAbstractDescription
    description: 'Detailed geomorphologic unit description placeholder (stub class)
      for GeomorphologicUnit  Constraint: Only one instance of each subtype is allowed'
    type: object
  LinearDirectedCode:
    $anchor: LinearDirectedCode
    description: eg, "directed" (indicates that the orientation is directed) "directed
      down" (indicates that the linear orientation is directed below the horizon)
      "directed up" (indicates that the linear orientation is directed above the horizon)
      This list is an indicative example list only of terms used to describe the values
      to use for terms related to directedness of linear orientations. Users are encouraged
      to use a vocabulary of terms managed by the CGI vocabularies working group outside
      of this model.
    type: string
    format: uri
  LithologyTerm:
    $anchor: LithologyTerm
    description: Refers to a vocabulary of terms describing the lithology of the compound
      earth material (eg, granite, sandstone, schist)
    type: string
    format: uri
  MappedFeature:
    $anchor: MappedFeature
    description: 'A MappedFeature is part of a geological interpretation. It provides
      a link between a notional feature (description package) and one spatial representation
      of it, or part of it (exposures, surface traces and intercepts, etc.). The mapped
      features are the elements that compose a map, a cross-section, a borehole log,
      or any other representation. The mappingFrame identifies the domain being mapped
      by the geometries. For typical geological maps, the mapping frame is the surface
      of the earth (the 2.5D interface between the surface of the bedrock and whatever
      sits on it; atmosphere or overburden material for bedrock maps). It can also
      be abstract frames, such as the arbitrary plane that forms a mine level or a
      cross-section, the 3D volume enclosing an ore body or the line that approximate
      the path of a borehole.  Constraint: self.metadata.hierarchyLevel=(feature or
      dataset or series)  Constraint: self.shape contained in samplingFrame.shape'
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            observationMethod:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
                uniqueItems: true
              description: The observationMethod property (SWE::Category) contains
                an element in a list of categories (a controlled vocabulary) describing
                how the spatial extent of the mapped feature was determined.
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
              description: The positionalAccuracy property (SWE::Quantity) provides
                a quantitative value defining the radius of an uncertainty buffer
                around a MappedFeature (e.g., a positionalAccuracy of 100 m for a
                line feature defines a buffer polygon of total width 200 m centred
                on the line). The property is equivalent to ISO19115 DQ_PositionalAccuracy.
            resolutionRepresentativeFraction:
              oneOf:
              - type: 'null'
              - type: integer
              description: The property resolutionRepresentativeFraction:Integer is
                an integer value representing the denominator of the representative
                scale of the spatial feature. (i.e., 10000 = the spatial feature is
                intended to be represented at 1:10,000 scale).
            mappingFrame:
              oneOf:
              - type: 'null'
              - $ref: '#MappingFrameTerm'
              description: The mappingFrame:MappingFrameTerm provides a term from
                a vocabulary indicating the geometric frame on which the MappedFeature
                is projected. In most situations, mapped features are projected on
                the earth surface, but there are other contexts, such as a bedrock
                surface beneath surficial cover materials, a mine level, or a cross
                section.
            exposure:
              oneOf:
              - type: 'null'
              - $ref: '#ExposureTerm'
              description: The exposure:ExposureTerm property provides a term for
                the nature of the expression of the mapped feature at the earth's
                surface (e.g., exposed, concealed).
            shape:
              oneOf:
              - type: 'null'
              - $ref: https://geojson.org/schema/Geometry.json
              description: The shape:GM_Object property contains the geometry delimiting
                the mapped feature. Note that while in most cases, the geometry will
                be a 2D polygon, it is not restricted to any dimension. For instance,
                a lithological log can be represented using of 1D geometries (expressed
                linearly from the borehole origin), or a geologic unit can be represented
                using a 3D volume.
            specification:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
                $comment: "External ISO 19156 GFI_Feature \u2014 by-reference link"
              description: The specification association links an instance of MappedFeature
                to the GFI_Feature being mapped. In a geological map, MappedFeatures
                are used to represent GeologicFeatures, but other features from other
                domains could be represented.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  MappingFrameTerm:
    $anchor: MappingFrameTerm
    description: Spatial reference frame within which the MappedFeatures have been
      observed, such as a surface of mapping. (from INSPIRE)
    type: string
    format: uri
  NaturalGeomorphologicFeature:
    $anchor: NaturalGeomorphologicFeature
    description: A natural geomorphologic feature is a geomorphologic feature (i.e.,
      landform) that has been created by natural Earth processes. For example, river
      channel, beach ridge, caldera, canyon, moraine or mud flat.
    allOf:
    - $ref: '#GeomorphologicFeature'
    - type: object
      properties:
        properties:
          type: object
          properties:
            naturalGeomorphologicFeatureType:
              oneOf:
              - type: 'null'
              - $ref: '#NaturalGeomorphologicFeatureTypeTerm'
              description: 'The property naturalGeomorphologicFeatureType: NaturalGeomorphologicFeatureTypeTerm
                is a reference from a controlled vocabulary describing the type of
                geomorphologic feature.'
            activity:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
              description: The activity property (SWE::Category) contains a category
                term from a controlled vocabulary describing the current activity
                status of the geomorphologic feature (e.g., currently active, dormant,
                inactive, reactivated, etc.).
  NaturalGeomorphologicFeatureTypeTerm:
    $anchor: NaturalGeomorphologicFeatureTypeTerm
    description: Refers to a vocabulary of terms describing the type of natural geomorphologic
      feature
    type: string
    format: uri
  NumericAgeRange:
    $anchor: NumericAgeRange
    description: The NumericAgeRange class represents an absolute age assignment using
      numeric measurement results.
    type: object
    properties:
      reportingDate:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The reportingDate (SWE::Quantity) property reports a single time
          coordinate value to report as representative for this NumericAge assignment.
      olderBoundDate:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The olderBoundDate (SWE::Quantity) property reports the older
          bounding time coordinate in an age range.
      youngerBoundDate:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The youngerBoundDate (SWE::Quantity) property reports the younger
          bounding time coordinate in an age range.
  PlanarPolarityCode:
    $anchor: PlanarPolarityCode
    description: 'eg: "upright", "overturned", "vertical" This list is an indicative
      list only of terms used to describe the values to use for expressing overturned
      or upright facing of planar orientation measurements. Users are encouraged to
      use a vocabulary of terms managed by the CGI vocabularies working group outside
      of this model.'
    type: string
    format: uri
  RankTerm:
    $anchor: RankTerm
    description: This class is a blank placeholder for a vocabulary of terms describing
      the rank of a geologic unit (eg, Group, Formation, Member, etc)
    type: string
    format: uri
  RockMaterial:
    $anchor: RockMaterial
    description: RockMaterial is a specialized CompoundMaterial that includes consolidated
      and unconsolidated materials (such as surficial sediments) as well as mixtures
      of consolidated and unconsolidated materials. In GeoSciML Basic, Rock Material
      is essentially a link to a controlled vocabulary (lithology property) and a
      color (inherited from EarthMaterial). Specific material properties (and CompoundMaterial
      nesting) are available in GeoSciML Extension.
    allOf:
    - $ref: '#CompoundMaterial'
    - type: object
      properties:
        lithology:
          oneOf:
          - type: 'null'
          - $ref: '#LithologyTerm'
          description: The lithology:LithologyTerm property provides a term identifying
            the lithology class from a controlled vocabulary.
  ShearDisplacementStructure:
    $anchor: ShearDisplacementStructure
    description: "A shear displacement structure includes all brittle to ductile style
      structures along which displacement has occurred, from a simple, single 'planar'
      brittle or ductile surface to a fault system comprised of tens of strands of
      both brittle and ductile nature. This structure may have some significant thickness
      (a deformation zone) and have an associated body of deformed rock that may be
      considered a deformation unit (which geologicUnitType is \u2018DeformationUnit\u2019)
      which can be associated to the ShearDisplacementStructure using GeologicFeatureRelation
      from the GeoSciML Extension package"
    allOf:
    - $ref: '#GeologicStructure'
    - type: object
      properties:
        properties:
          type: object
          properties:
            faultType:
              oneOf:
              - type: 'null'
              - $ref: '#FaultTypeTerm'
              description: The faultType:FaultTypeTerm property contains a term from
                a controlled vocabulary describing the type of shear displacement
                structure (e.g., thrust fault, normal fault or wrench fault).
            stStructureDescription:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#ShearDisplacementStructureAbstractDescription'
                uniqueItems: true
              description: The property stStructureDescription:ShearDisplacementStructureAbstractDescription
                provides a detailed geologic structure description. This is a stub
                property in GeoSciML Basic since ShearDisplacementStructureAbstractDescription
                is an abstract class with subtypes defined in GeoSciML Extension.
  ShearDisplacementStructureAbstractDescription:
    $anchor: ShearDisplacementStructureAbstractDescription
    description: An abstract class providing a link between classes in GeoSciMLBasic
      and GeoSciMLExtended application schemas.
    type: object
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmBasicGeology/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmBasicGeology/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](/github/workspace/_sources/gsmBasicGeology/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmBasicGeology`

