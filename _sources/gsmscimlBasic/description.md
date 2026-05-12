# gsmscimlBasic

GeoSciML 4.1 building block `gsmscimlBasic`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeoSciMLBasic`, `Collection`, `GSML_DataTypes`, `GeologicEvent`, `GeologicStructure`, `GeologyBasic`, `Geomorphology`.

Contains 13 feature types, 20 data types, 22 code lists, 1 union.

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
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [contact_complex.json](examples/contact_complex.json)
- [contact_simple.json](examples/contact_simple.json)
- [examplegsmscimlBasicMinimal.json](examples/examplegsmscimlBasicMinimal.json)
- [fc_heterogeneous_GSO.json](examples/fc_heterogeneous_GSO.json)
- [fc_homogeneous_GSO.json](examples/fc_homogeneous_GSO.json)
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
