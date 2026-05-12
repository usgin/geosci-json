
# gsmscimlLite (Schema)

`usgin.bbr.geosci.gsmscimlLite` *v0.1*

GeoSciML 4.1 Lite profile. Flattened "View" classes that summarise

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmscimlLite

GeoSciML 4.1 building block `gsmscimlLite`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeoSciMLLite`.

Contains 7 feature types, 1 data type.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `BoreholeView` | «FeatureType» | JSON-FG Feature |
| `ContactView` | «FeatureType» | JSON-FG Feature |
| `GeologicSpecimenView` | «FeatureType» | JSON-FG Feature |
| `GeologicUnitView` | «FeatureType» | JSON-FG Feature |
| `GeomorphologicUnitView` | «FeatureType» | JSON-FG Feature |
| `ShearDisplacementStructureView` | «FeatureType» | JSON-FG Feature |
| `SiteObservationView` | «FeatureType» | JSON-FG Feature |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `BoreholeView`

BoreholeView is a simplified view of a GeoSciML Borehole. In GeoSciML terms, this will be an instance of a Borehole feature with key property values summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf — see schema) | 0..1 | If present, the property name:Primitive::CharacterString contains a human-readable display name for the borehole. |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a human-readable description for the borehole. |
| `purpose` | (oneOf — see schema) | 0..1 | If present, the purpose:Primitive::CharacterString property reports the purpose or purposes for which the borehole wa… |
| `status` | (oneOf — see schema) | 0..1 | If present, the property status:Primitive::CharacterString reports the current status of the borehole (e.g., abandone… |
| `drillingMethod` | (oneOf — see schema) | 0..1 | If present, the property drillingMethod:Primitive::CharacterString indicates the drilling method, or methods, used fo… |
| `operator` | (oneOf — see schema) | 0..1 | If present, the property operator:Primitive::CharacterString reports the organisation or agency responsible for commi… |
| `driller` | (oneOf — see schema) | 0..1 | If present, the property driller:Primitive::CharacterString reports the organisation responsible for drilling the bor… |
| `drillStartDate` | (oneOf — see schema) | 0..1 | If present, the property drillStartDate:Primitive::CharacterString reports the date of the start of drilling formatte… |
| `drillEndDate` | (oneOf — see schema) | 0..1 | If present, the property drillEndData:Primitive::CharacterString reports the date of the end of drilling formatted ac… |
| `startPoint` | (oneOf — see schema) | 0..1 | If present, the property startPoint:Primitive::CharacterString indicates the position relative to the ground surface … |
| `inclinationType` | (oneOf — see schema) | 0..1 | If present, the property inclinationType:Primitive::CharacterString indicates the type of inclination of the borehole… |
| `boreholeMaterialCustodian` | (oneOf — see schema) | 0..1 | If present, the property boreholeMaterialCustodian:Primitive::CharacterString reports the organisation that is the cu… |
| `boreholeLength_m` | (oneOf — see schema) | 0..1 | If present, the property boreholeLength_m:Primitive::Number reports the length of a borehole, in metres, as determine… |
| `elevation_m` | (oneOf — see schema) | 0..1 | If present, the property elevation_m:Primitive::Number reports the elevation data, in metres, for the borehole (i.e.,… |
| `elevation_srs` | (oneOf — see schema) | 0..1 | If present, the property elevation_srs:Primitive::CharacterString is a URI of a spatial reference system of the eleva… |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString reports an estimate of the accuracy of the loc… |
| `source` | (oneOf — see schema) | 0..1 | If present, the source:Primitive::CharacterString property describes details and citations to source materials for th… |
| `parentBorehole_uri` | (oneOf — see schema) | 0..1 | When present, the parentBorehole_uri:Primitive::CharacterString contains a URI referring to one or more representatio… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a Geometry defining the extent of the borehole start point. |
| `any` | (oneOf — see schema) | 0..1 | A data provider may add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `ContactView`

ContactView is a simplified view of a GeoSciML MappedFeature with key property values from an associated Contact feature. These properties are summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf — see schema) | 0..1 | If present, the property name:Primitive::CharacterString reports the display name for the Contact. |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString reports the description of the Contact, typically tak… |
| `contactType` | (oneOf — see schema) | 0..1 | If present, the property contactType:Primitive::CharacterString reports the type of Contact (as defined in GeoSciML) … |
| `observationMethod` | (oneOf — see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString reports a metadata snippet indicating how the s… |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString reports quantitative values defining the radiu… |
| `source` | (oneOf — see schema) | 0..1 | If present, the property source:Primitive::CharacterString contains a text describing feature-specific details and ci… |
| `contactType_uri` | (oneOf — see schema) | 0..1 | The property contactType_uri:Primitive::CharacterString reports a URI referring to a controlled concept from a vocabu… |
| `specification_uri` | (oneOf — see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString reports a URI referring the GeoSciML Contact fe… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString reports a URI referring to a metadata record describ… |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the genericSymbolizer:Primitive::CharacterString property contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry defining the extent of the contact feature. |
| `any` | (oneOf — see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `GeologicSpecimenView`

GeologicSpecimenView is a simplified view of a point-located specimen from GeoSciML GeologicSpecimen (an extension of Observations & Measurements - ISO19156) with key property values summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier (eg, an IGSN sample number). Should have the same value as a corresponding GeoSciML Geolog… |
| `label` | (oneOf — see schema) | 0..1 | If present, the property label:Primitive::CharacterString contains a short label for map display. (e.g., a sample num… |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a detailed description of the specimen. |
| `specimenType` | (oneOf — see schema) | 0..1 | If present, the property specimentType:Primitive::CharacterString contains a human readable description of the specim… |
| `materialClass` | (oneOf — see schema) | 0..1 | If present, the property materialClass:Primitive::CharacterString reports the classification of the material that com… |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString contains a description of the positional accur… |
| `samplingTime` | (oneOf — see schema) | 0..1 | If present, the property samplingTime:Primitive::CharacterString reports a date or a date with time of when the speci… |
| `samplingMethod` | (oneOf — see schema) | 0..1 | If present, the property samplingMethod:Primitive::CharacterString reports the method used to collect the specimen (e… |
| `currentLocation` | (oneOf — see schema) | 0..1 | If present, the property currentLocation:Primitive::CharacterString reports the current location of the specimen (e.g… |
| `source` | (oneOf — see schema) | 0..1 | If present, the property source:Primitive::CharacterString reports the citation of the source of the data (e.g., a pu… |
| `specimenType_uri` | (oneOf — see schema) | 0..1 | The property specimentType_uri:Primitive::CharacterString contains a URI link for a specimen type identifier from a c… |
| `materialClass_uri` | (oneOf — see schema) | 0..1 | The property materialClass_uri:Primitive::CharacterString contains a URI link for a class of material drawn from a co… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI link to a metadata document. |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the genericSymbolizer:Primitive::CharacterString property contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry of the specimen (generally a point). |
| `any` | (oneOf — see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `GeologicUnitView`

GeologicUnitView is a simplified view of a GeoSciML MappedFeature feature with key property values from an associated GeologicUnit. The GeologicUnitView property values are summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf — see schema) | 0..1 | If present, the property name:Primitive::CharacterString is a display name for the GeologicUnit. |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString is a description of the GeologicUnit, typically taken… |
| `geologicUnitType` | (oneOf — see schema) | 0..1 | If present, the property geologicUnitType (Primitive::CharacterString) contains the type of GeologicUnit (as defined … |
| `rank` | (oneOf — see schema) | 0..1 | If present, the property rank:Primitive::CharacterString contain the rank of GeologicUnit (as defined by ISC. e.g., g… |
| `lithology` | (oneOf — see schema) | 0..1 | If present, lithology contains a human readable description as Primitive::CharacterString of the GeologicUnit’s litho… |
| `geologicHistory` | (oneOf — see schema) | 0..1 | If present, contains a human readable description in Primitive::CharacterString, possibly formatted with formal synta… |
| `numericOlderAge` | (oneOf — see schema) | 0..1 | If present, the property numericOlderAge age is a numerical representation (Primitive::Number) of the unit’s older ag… |
| `numericYoungerAge` | (oneOf — see schema) | 0..1 | If present, the property numericYoungerAge is a numerical representation (Primitive::Number) of the unit’s younger ag… |
| `observationMethod` | (oneOf — see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString is a metadata snippet indicating how the spatia… |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString is a quantitative value (a numerical value and… |
| `source` | (oneOf — see schema) | 0..1 | If present, the property source:Primitive::CharacterString is human readable text describing feature-specific details… |
| `geologicUnitType_uri` | (oneOf — see schema) | 0..1 | The property geologicUnitType_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a … |
| `representativeLithology_uri` | (oneOf — see schema) | 0..1 | The property representativeLithology_uri:Primitive::CharacterString shall contain a URI referring to a controlled con… |
| `representativeAge_uri` | (oneOf — see schema) | 0..1 | The property representativeAge_uri:Primitive::CharacterString shall contain a URI referring to a controlled concept s… |
| `representativeOlderAge_uri` | (oneOf — see schema) | 0..1 | The property representativeOlderAge_uri:Primitive::CharacterString shall contain a URI referring to a controlled conc… |
| `representativeYoungerAge_uri` | (oneOf — see schema) | 0..1 | The property representativeYoungerAge_uri:Primitive::CharacterString shall contain a URI referring to a controlled co… |
| `specification_uri` | (oneOf — see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString shall contain a URI referring the GeoSciML Geol… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the property genericSymbolizer:CharacterString contains an identifier for a symbol from standard (locally… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GEO::GM_Object contains a geometry defining the extent of the feature of interest. |
| `any` | (oneOf — see schema) | 0..1 | A data provider may add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `GeomorphologicUnitView`

GeomorphologicUnitView is a simplified view of a GeoSciML GeomorphologicUnit. In GeoSciML terms this will be in instance of a MappedFeature with key property values from the associated GeomorphologicUnit feature summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf — see schema) | 0..1 | If present, the property name:Primitive::CharacterString contains a display name for the GeomorphologicUnit. |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains human readable text description of the Geomo… |
| `activity` | (oneOf — see schema) | 0..1 | If present, the property activity:Primitive::CharacterString contains a human readable term to specify if the feature… |
| `geomorphologicFeatureType` | (oneOf — see schema) | 0..1 | If present, the property geomorphologicFeatureType:Primitive::CharacterString contains a human readable term to speci… |
| `unitType` | (oneOf — see schema) | 0..1 | If present, the property unitType:Primitive::CharacterString contains a human readable term for the type of Geomorpho… |
| `lithology` | (oneOf — see schema) | 0..1 | If present, the property lithology:Primitive::CharacterString contains a text, possibly formatted with formal syntax … |
| `geologicHistory` | (oneOf — see schema) | 0..1 | If present, the property geologicHistory:Primitive::CharacterString contains text, possibly formatted with formal syn… |
| `representativeNumericAge` | (oneOf — see schema) | 0..1 | If present, the property representativeNumericAge:Primitive::Number contains a numerical value of the representative … |
| `observationMethod` | (oneOf — see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString contains a metadata snippet indicating how the … |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionAccuracy:Primitive::CharacterString contains quantitative values defining the radius… |
| `source` | (oneOf — see schema) | 0..1 | If present, the source:Primitive::CharacterString property contains text describing feature-specific details and cita… |
| `activity_uri` | (oneOf — see schema) | 0..1 | If present, the activity_uri:Primitive::CharacterString property reports a URI identifier of activity term drawn from… |
| `geomorphologicFeatureType_uri` | (oneOf — see schema) | 0..1 | If present, the property geomorphologicFeatureType_uri:Primitive::CharacterString reports a URI identifier of landfor… |
| `unitType_uri` | (oneOf — see schema) | 0..1 | If present, the property unitType_uri:Primitive::CharacterString reports a URI referring to a controlled concept from… |
| `representativeLithology_uri` | (oneOf — see schema) | 0..1 | The property representativeLithology_uri:Primitive::CharacterString contains a URI referring to a controlled concept … |
| `representativeAge_uri` | (oneOf — see schema) | 0..1 | The property representativeAge_uri:Primitive::CharacterString contains a URI referring to a controlled concept specif… |
| `specification_uri` | (oneOf — see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString contains a URI referring the GeoSciML Geomorpho… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry defining the extent of the feature of interest. |
| `any` | (oneOf — see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `ShearDisplacementStructureView`

ShearDisplacementStructureView is a simplified view of a GeoSciML ShearDisplacementStructure. In GeoSciML terms this will be an instance of a MappedFeature with key property values from the associated ShearDisplacementStructure feature summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf — see schema) | 0..1 | If present, the property name:Primitive::CharacterString contains a display name for the ShearDisplacementStructure. |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a human readable text description of the She… |
| `faultType` | (oneOf — see schema) | 0..1 | If present, the property faultType:Primitive::CharacterString contains a human readable description of the type of Sh… |
| `movementType` | (oneOf — see schema) | 0..1 | If present, the property movementType:Primitive::CharacterString contains a human readable summary of the type of mov… |
| `deformationStyle` | (oneOf — see schema) | 0..1 | If present, the property deformationStyle:Primitive::CharacterString contain a human readable description of the styl… |
| `displacement` | (oneOf — see schema) | 0..1 | If present, the property displacement:Primitive::CharacterString contains a text summarising the displacement across … |
| `geologicHistory` | (oneOf — see schema) | 0..1 | If present, the property geologicHistory:Primitive::CharacterString contains a text, possibly formatted with formal s… |
| `numericOlderAge` | (oneOf — see schema) | 0..1 | If present, the property numericOlderAge:Primitive::Number reports the older age of the fault/shear structure, repres… |
| `numericYoungerAge` | (oneOf — see schema) | 0..1 | If present, the property numericYoungerAge:Primitive::Number reports the younger age of the fault/shear structure, re… |
| `observationMethod` | (oneOf — see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString contains a metadata snippet indicating how the … |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionAccuracy:Primitive::CharacterString contains quantitative representation defining th… |
| `source` | (oneOf — see schema) | 0..1 | If present, the property source:Primitive::CharacterString contains a text describing feature-specific details and ci… |
| `faultType_uri` | (oneOf — see schema) | 0..1 | The property faultType_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a vocabul… |
| `movementType_uri` | (oneOf — see schema) | 0..1 | The property movementType_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a voca… |
| `deformationStyle_uri` | (oneOf — see schema) | 0..1 | The property deformationStyle_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a … |
| `representativeAge_uri` | (oneOf — see schema) | 0..1 | The property representativeAge_uri:Primitive::CharacterString contains a URI referring to a controlled concept specif… |
| `representativeOlderAge_uri` | (oneOf — see schema) | 0..1 | The property representativeOlderAge_uri:Primitive:CharacterString contains a URI referring to a controlled concept sp… |
| `representativeYoungerAge_uri` | (oneOf — see schema) | 0..1 | The property representativeYoungerAge_uri:Primitive::CharacterString contains a URI referring to a controlled concept… |
| `specification_uri` | (oneOf — see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString contains a URI referring the GeoSciML ShearDisp… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry defining the extent of the feature of interest. |
| `any` | (oneOf — see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `SiteObservationView`

SiteObservationView is a simplified view of a generally point-located geological observation, like a structural measurement. This is a simplified instance of a sampling geometry from Observations & Measurements (ISO19156) with an associated geological observation. Each tuple should represent a single observation. Key property values are summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `siteName` | (oneOf — see schema) | 0..1 | If present, the property siteName:Primitive::CharacterString contains the name of the sampling feature at this locati… |
| `observationName` | (oneOf — see schema) | 0..1 | If present, the property observationName:Primitive::CharacterString contains a text identifying the observation. |
| `label` | (oneOf — see schema) | 0..1 | If present, the property label:Primitive::CharacterString contains a short text string to associate with a symbol in … |
| `description` | (oneOf — see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a text string providing descriptive informat… |
| `featureOfInterest` | (oneOf — see schema) | 0..1 | If present, the property featureOfInterest:Primitive::CharacterString contains a description of the geologic feature … |
| `observedProperty` | (oneOf — see schema) | 0..1 | If present, the property observedProperty:Primitive::CharacterString contains a description of the property reported … |
| `observedValue` | (oneOf — see schema) | 0..1 | If present, the property observedValue:Primitive::CharacterString contains the result of the observation. This field … |
| `observedValueUom` | (oneOf — see schema) | 0..1 | If relevant, the property observedValueUom:Primitive::CharacterString contains the unit of measure for a numerical va… |
| `observationMethod` | (oneOf — see schema) | 0..1 | If present, the observationMethod:Primitive::CharacterString property contains a method description, preferably a ter… |
| `positionalAccuracy` | (oneOf — see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString provides an estimate of the position uncertain… |
| `source` | (oneOf — see schema) | 0..1 | If present, the property source:Primitive::CharacterString contains a text description of measurement procedure, proc… |
| `featureOfInterest_uri` | (oneOf — see schema) | 0..1 | The property featureOfInterest:Primitive::CharacterString is functionally equivalent to OM_Observation::featureOfInte… |
| `propertyType_uri` | (oneOf — see schema) | 0..1 | The property propertyType_uri:Primitive:CharacterString is functionally equivalent to OM_Observation::observedPropert… |
| `metadata_uri` | (oneOf — see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI link to metadata document. |
| `genericSymbolizer` | (oneOf — see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol to portray … |
| `symbolRotation` | (oneOf — see schema) | 0..1 | If present, the symbolRotation:Integer property contains an integer value between 0 and 359 to specify rotation of sy… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains the geometry of the observation site. |
| `any` | (oneOf — see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `_FeatureDispatch`

## External dependencies

- `https://geojson.org/schema/Geometry.json`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`

## Examples

- [borehole_view_complex.json](examples/borehole_view_complex.json)
- [borehole_view_simple.json](examples/borehole_view_simple.json)
- [contact_view_complex.json](examples/contact_view_complex.json)
- [contact_view_simple.json](examples/contact_view_simple.json)
- [examplegsmscimlLiteMinimal.json](examples/examplegsmscimlLiteMinimal.json)
- [geologic_specimen_view_complex.json](examples/geologic_specimen_view_complex.json)
- [geologic_specimen_view_simple.json](examples/geologic_specimen_view_simple.json)
- [geologic_unit_view_complex.json](examples/geologic_unit_view_complex.json)
- [geologic_unit_view_simple.json](examples/geologic_unit_view_simple.json)
- [geomorphologic_unit_view_simple.json](examples/geomorphologic_unit_view_simple.json)
- [geosciml_lite_featurecollection_geologicunitview.json](examples/geosciml_lite_featurecollection_geologicunitview.json)
- [geosciml_lite_featurecollection_mixed.json](examples/geosciml_lite_featurecollection_mixed.json)
- [shear_displacement_structure_view_complex.json](examples/shear_displacement_structure_view_complex.json)
- [shear_displacement_structure_view_simple.json](examples/shear_displacement_structure_view_simple.json)
- [site_observation_view_complex.json](examples/site_observation_view_complex.json)
- [site_observation_view_simple.json](examples/site_observation_view_simple.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeoSciMLLite`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### borehole view complex
Example instance: borehole_view_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "BoreholeView",
  "id": "borehole-view-complex",
  "geometry": {
    "type": "Point",
    "coordinates": [
      149.252,
      -35.401
    ]
  },
  "time": null,
  "properties": {
    "name": "GRS-001",
    "description": "Mineral exploration diamond drillhole targeting the Hervey Group sandstone aquifer.",
    "purpose": "mineral exploration, groundwater investigation",
    "status": "completed",
    "drillingMethod": "diamond core drilling",
    "operator": "Regional Geological Survey",
    "driller": "Acme Drilling Pty Ltd",
    "drillStartDate": "2018-03-12",
    "drillEndDate": "2018-04-02",
    "startPoint": "natural land surface",
    "inclinationType": "inclined down",
    "boreholeMaterialCustodian": "Geoscience Australia Core Library, Canberra",
    "boreholeLength_m": 312.5,
    "elevation_m": 672.3,
    "elevation_srs": "http://www.opengis.net/def/crs/EPSG/0/5711",
    "positionalAccuracy": "10 m (GNSS survey)",
    "source": "Regional Geological Survey (2018). Drillhole report GRS-001. Open file report OF-2018-07.",
    "metadata_uri": "http://data.geoscience.gov.au/metadata/borehole/grs-001",
    "genericSymbolizer": "BH_Diamond"
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/4283",
  "place": {
    "type": "Point",
    "coordinates": [
      149.252,
      -35.401
    ]
  }
}

```


### borehole view simple
Example instance: borehole_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "BoreholeView",
  "id": "borehole-view-1",
  "geometry": {
    "type": "Point",
    "coordinates": [
      149.252,
      -35.401
    ]
  },
  "time": null,
  "properties": {
    "name": "GRS-001",
    "purpose": "mineral exploration",
    "status": "completed",
    "drillingMethod": "diamond core drilling",
    "boreholeLength_m": 312.5
  }
}

```


### contact view complex
Example instance: contact_view_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "ContactView",
  "id": "contact-view-complex",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [
        149.12,
        -35.31
      ],
      [
        149.28,
        -35.44
      ],
      [
        149.45,
        -35.58
      ]
    ]
  },
  "time": null,
  "properties": {
    "name": "Base of Devonian sequence",
    "description": "Erosional unconformity between Devonian Hervey Group and Ordovician basement. Sharp contact, planar to gently undulating surface.",
    "contactType": "disconformity",
    "observationMethod": "field observation and aerial photograph interpretation",
    "positionalAccuracy": "250 m",
    "source": "Smith, J. et al. (2005). Geology of the Goulburn 1:250000 sheet. Geoscience Australia.",
    "contactType_uri": "http://resource.geosciml.org/classifier/cgi/contacttype/disconformity",
    "specification_uri": "http://data.geoscience.gov.au/feature/contact/base-devonian-1",
    "metadata_uri": "http://data.geoscience.gov.au/metadata/record/67890",
    "genericSymbolizer": "CT_Unconformity"
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/4283",
  "place": {
    "type": "LineString",
    "coordinates": [
      [
        149.12,
        -35.31
      ],
      [
        149.28,
        -35.44
      ],
      [
        149.45,
        -35.58
      ]
    ]
  }
}

```


### contact view simple
Example instance: contact_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "ContactView",
  "id": "contact-view-1",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [
        149.12,
        -35.31
      ],
      [
        149.28,
        -35.44
      ],
      [
        149.45,
        -35.58
      ]
    ]
  },
  "time": null,
  "properties": {
    "name": "Unconformity between Hervey Group and Lachlan Fold Belt basement",
    "contactType": "unconformity",
    "positionalAccuracy": "500 m",
    "contactType_uri": "http://resource.geosciml.org/classifier/cgi/contacttype/unconformity",
    "specification_uri": "http://data.geoscience.gov.au/feature/contact/unconformity-1"
  }
}

```


### examplegsmscimlLiteMinimal
Example instance: examplegsmscimlLiteMinimal
#### json
```json
{
  "type": "Feature",
  "id": "boreholeview.minimal.1",
  "featureType": "BoreholeView",
  "geometry": null,
  "properties": {}
}

```


### geologic specimen view complex
Example instance: geologic_specimen_view_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "GeologicSpecimenView",
  "id": "specimen-view-complex",
  "geometry": {
    "type": "Point",
    "coordinates": [
      149.312,
      -35.475
    ]
  },
  "time": null,
  "properties": {
    "label": "GRS-2019-042",
    "description": "Medium to coarse-grained, well-sorted, sub-angular quartz arenite. White to pale yellow, friable. Collected from outcrop of Hervey Group sandstone on roadcut.",
    "specimenType": "hand specimen",
    "materialClass": "rock",
    "positionalAccuracy": "5 m",
    "samplingTime": "2019-03-15",
    "samplingMethod": "field mapping survey \u2013 hand specimen from outcrop",
    "currentLocation": "Geoscience Australia Sample Repository, Canberra (drawer G-2019-3)",
    "source": "Smith, J. (2019). Goulburn mapping campaign field samples.",
    "specimenType_uri": "http://resource.geosciml.org/classifier/cgi/specimentype/hand_specimen",
    "materialClass_uri": "http://resource.geosciml.org/classifier/cgi/materialclass/rock",
    "metadata_uri": "http://data.geoscience.gov.au/metadata/specimen/GRS-2019-042",
    "genericSymbolizer": "SP_HandSpecimen"
  }
}

```


### geologic specimen view simple
Example instance: geologic_specimen_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "GeologicSpecimenView",
  "id": "specimen-view-1",
  "geometry": {
    "type": "Point",
    "coordinates": [
      149.312,
      -35.475
    ]
  },
  "time": null,
  "properties": {
    "label": "GRS-2019-042",
    "specimenType": "hand specimen",
    "materialClass": "rock",
    "specimenType_uri": "http://resource.geosciml.org/classifier/cgi/specimentype/hand_specimen",
    "materialClass_uri": "http://resource.geosciml.org/classifier/cgi/materialclass/rock"
  }
}

```


### geologic unit view complex
Example instance: geologic_unit_view_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "GeologicUnitView",
  "id": "gu-view-complex",
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
  "time": null,
  "properties": {
    "name": "Hervey Group",
    "description": "Terrigenous to shallow marine, red to white and green, quartzose to lithic sandstone, siltstone, shale and conglomerate; sandstones commonly thick-bedded and massive to cross-stratified.",
    "geologicUnitType": "lithostratigraphic unit",
    "rank": "group",
    "lithology": "sandstone, siltstone, shale and conglomerate (50\u201395% sandstone, 5\u201350% mudstone)",
    "geologicHistory": "Deposited during the Frasnian to Famennian (Late Devonian) in a fluvial to shallow marine environment; subsequently deformed during Tournaisian to Serpukhovian (Early Carboniferous) Kanimblan Orogeny.",
    "numericOlderAge": 382.7,
    "numericYoungerAge": 323.2,
    "observationMethod": "synthesis from multiple sources including field mapping and drill-core logging",
    "positionalAccuracy": "250 m",
    "source": "Raymond, O.L. (ed.) 2009. Surface Geology of Australia, 1:1 000 000 scale dataset, 2009 edition. Geoscience Australia, Canberra.",
    "geologicUnitType_uri": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
    "representativeLithology_uri": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone",
    "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
    "representativeOlderAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",
    "representativeYoungerAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Famennian",
    "specification_uri": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1",
    "metadata_uri": "http://data.geoscience.gov.au/metadata/record/12345",
    "genericSymbolizer": "GU_DevSS"
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/4283",
  "place": {
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
  }
}

```


### geologic unit view simple
Example instance: geologic_unit_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "GeologicUnitView",
  "id": "gu-view-1",
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
  "time": null,
  "properties": {
    "name": "Hervey Group",
    "geologicUnitType": "lithostratigraphic unit",
    "rank": "group",
    "lithology": "sandstone, siltstone and conglomerate",
    "geologicHistory": "Devonian (Frasnian to Famennian) fluvial to shallow marine deposition",
    "representativeLithology_uri": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone",
    "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
    "geologicUnitType_uri": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit"
  }
}

```


### geomorphologic unit view simple
Example instance: geomorphologic_unit_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "GeomorphologicUnitView",
  "id": "geomorph-view-1",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          148.21,
          -36.445
        ],
        [
          148.29,
          -36.445
        ],
        [
          148.29,
          -36.51
        ],
        [
          148.21,
          -36.51
        ],
        [
          148.21,
          -36.445
        ]
      ]
    ]
  },
  "time": null,
  "properties": {
    "name": "Snowy Mountains terminal moraine",
    "geomorphologicFeatureType": "natural",
    "unitType": "moraine",
    "activity": "inactive",
    "geomorphologicFeatureType_uri": "http://resource.geosciml.org/classifier/cgi/geomorphologicfeaturetype/natural",
    "unitType_uri": "http://resource.geosciml.org/classifier/cgi/geomorphologicunittype/moraine"
  }
}

```


### geosciml lite featurecollection geologicunitview
Example instance: geosciml_lite_featurecollection_geologicunitview
#### json
```json
{
  "type": "FeatureCollection",
  "featureType": "GeologicUnitView",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnitView",
      "id": "gu-view-1",
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
      "time": null,
      "properties": {
        "name": "Hervey Group",
        "description": "Terrigenous to shallow marine, red to white and green, quartzose to lithic sandstone, siltstone, shale and conglomerate.",
        "geologicUnitType": "lithostratigraphic unit",
        "rank": "group",
        "lithology": "sandstone, siltstone, shale and conglomerate",
        "geologicHistory": "Frasnian to Famennian (Late Devonian) fluvial to shallow marine deposition",
        "numericOlderAge": 382.7,
        "numericYoungerAge": 358.9,
        "geologicUnitType_uri": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "representativeLithology_uri": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone",
        "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
        "representativeOlderAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",
        "representativeYoungerAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Famennian",
        "specification_uri": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1",
        "genericSymbolizer": "GU_DevSS"
      }
    },
    {
      "type": "Feature",
      "featureType": "GeologicUnitView",
      "id": "gu-view-2",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              149.45,
              -35.31
            ],
            [
              149.78,
              -35.31
            ],
            [
              149.78,
              -35.58
            ],
            [
              149.45,
              -35.58
            ],
            [
              149.45,
              -35.31
            ]
          ]
        ]
      },
      "time": null,
      "properties": {
        "name": "Lachlan Fold Belt Basement",
        "description": "Deformed Ordovician turbidites and volcanic rocks forming the pre-Devonian basement of the Lachlan Orogen.",
        "geologicUnitType": "lithotectonic unit",
        "rank": "supergroup",
        "lithology": "turbiditic sandstone, shale and volcanic rocks",
        "geologicHistory": "Ordovician deep marine turbidite deposition; deformed during Silurian to Devonian Benambran Orogeny",
        "numericOlderAge": 485.4,
        "numericYoungerAge": 419.2,
        "geologicUnitType_uri": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithotectonic_unit",
        "representativeLithology_uri": "http://resource.geosciml.org/classifier/cgi/simplelithology/turbidite",
        "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Ordovician",
        "representativeOlderAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Ordovician",
        "representativeYoungerAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Silurian",
        "specification_uri": "http://data.geoscience.gov.au/feature/geologicunit/lachlan-basement-1",
        "genericSymbolizer": "GU_OrdVol"
      }
    },
    {
      "type": "Feature",
      "featureType": "GeologicUnitView",
      "id": "gu-view-3",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              148.8,
              -35.58
            ],
            [
              149.12,
              -35.58
            ],
            [
              149.12,
              -35.85
            ],
            [
              148.8,
              -35.85
            ],
            [
              148.8,
              -35.58
            ]
          ]
        ]
      },
      "time": null,
      "properties": {
        "name": "Snowy Mountains Granite",
        "description": "Coarse-grained, porphyritic biotite granite intruded during the Silurian as part of the Lachlan Fold Belt I-type granite suite.",
        "geologicUnitType": "lithodemic unit",
        "rank": "pluton",
        "lithology": "granite",
        "geologicHistory": "Silurian magmatic intrusion (~430 Ma)",
        "numericOlderAge": 435.0,
        "numericYoungerAge": 425.0,
        "geologicUnitType_uri": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithodemic_unit",
        "representativeLithology_uri": "http://resource.geosciml.org/classifier/cgi/simplelithology/granite",
        "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Silurian",
        "representativeOlderAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Silurian",
        "representativeYoungerAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Silurian",
        "specification_uri": "http://data.geoscience.gov.au/feature/geologicunit/snowy-mountains-granite-1",
        "genericSymbolizer": "GU_SilGran"
      }
    }
  ]
}

```


### geosciml lite featurecollection mixed
Example instance: geosciml_lite_featurecollection_mixed
#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnitView",
      "id": "gu-view-1",
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
      "time": null,
      "properties": {
        "name": "Hervey Group",
        "geologicUnitType": "lithostratigraphic unit",
        "rank": "group",
        "lithology": "sandstone, siltstone and conglomerate",
        "geologicHistory": "Late Devonian fluvial to shallow marine deposition",
        "geologicUnitType_uri": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "representativeLithology_uri": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone",
        "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
        "specification_uri": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1"
      }
    },
    {
      "type": "Feature",
      "featureType": "ShearDisplacementStructureView",
      "id": "fault-view-1",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            149.387,
            -35.124
          ],
          [
            149.461,
            -35.344
          ]
        ]
      },
      "time": null,
      "properties": {
        "name": "Lake George Fault",
        "faultType": "normal fault",
        "movementType": "dip-slip",
        "geologicHistory": "Devonian to Carboniferous",
        "faultType_uri": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault",
        "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
        "specification_uri": "http://data.geoscience.gov.au/feature/fault/lake-george-fault-1"
      }
    },
    {
      "type": "Feature",
      "featureType": "ContactView",
      "id": "contact-view-1",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            149.12,
            -35.31
          ],
          [
            149.45,
            -35.58
          ]
        ]
      },
      "time": null,
      "properties": {
        "name": "Base of Devonian sequence",
        "contactType": "unconformity",
        "contactType_uri": "http://resource.geosciml.org/classifier/cgi/contacttype/unconformity",
        "specification_uri": "http://data.geoscience.gov.au/feature/contact/base-devonian-1"
      }
    },
    {
      "type": "Feature",
      "featureType": "BoreholeView",
      "id": "borehole-view-1",
      "geometry": {
        "type": "Point",
        "coordinates": [
          149.252,
          -35.401
        ]
      },
      "time": null,
      "properties": {
        "name": "GRS-001",
        "purpose": "mineral exploration",
        "status": "completed",
        "drillingMethod": "diamond core drilling",
        "boreholeLength_m": 312.5,
        "elevation_m": 672.3,
        "elevation_srs": "http://www.opengis.net/def/crs/EPSG/0/5711"
      }
    },
    {
      "type": "Feature",
      "featureType": "SiteObservationView",
      "id": "obs-view-1",
      "geometry": {
        "type": "Point",
        "coordinates": [
          149.312,
          -35.475
        ]
      },
      "time": null,
      "properties": {
        "siteName": "field station FS-42",
        "observedProperty": "planar orientation \u2013 strike and dip",
        "observedValue": "045 / 32",
        "observedValueUom": "degrees",
        "propertyType_uri": "http://resource.geosciml.org/classifierScheme/cgi/observedproperty/planar_orientation",
        "symbolRotation": 45
      }
    }
  ]
}

```


### shear displacement structure view complex
Example instance: shear_displacement_structure_view_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "ShearDisplacementStructureView",
  "id": "fault-view-complex",
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
  "time": null,
  "properties": {
    "name": "Lake George Fault",
    "description": "NNE-trending normal fault with down-thrown east block; forms eastern boundary of Lake George basin. Historically active, with evidence of Holocene movement.",
    "faultType": "normal fault",
    "movementType": "dip-slip",
    "deformationStyle": "brittle",
    "displacement": "estimated maximum vertical displacement ~400 m",
    "geologicHistory": "Initiated in the Devonian, reactivated during Carboniferous Kanimblan Orogeny, most recent movement in the Cenozoic.",
    "observationMethod": "synthesis from geophysical survey, field mapping and borehole data",
    "positionalAccuracy": "100 m",
    "source": "Geoscience Australia (2009). Lake George Fault \u2013 fault characterisation report.",
    "faultType_uri": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault",
    "movementType_uri": "http://resource.geosciml.org/classifier/cgi/faultmovementtype/dip_slip",
    "deformationStyle_uri": "http://resource.geosciml.org/classifier/cgi/deformationstyle/brittle",
    "representativeAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
    "representativeOlderAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
    "representativeYoungerAge_uri": "http://resource.geosciml.org/classifier/ics/ischart/Cenozoic",
    "numericOlderAge": 419.2,
    "numericYoungerAge": 0.0,
    "specification_uri": "http://data.geoscience.gov.au/feature/fault/lake-george-fault-1",
    "metadata_uri": "http://data.geoscience.gov.au/metadata/record/fault-99",
    "genericSymbolizer": "FA_Normal"
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/4283",
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
  }
}

```


### shear displacement structure view simple
Example instance: shear_displacement_structure_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "ShearDisplacementStructureView",
  "id": "fault-view-1",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [
        149.387,
        -35.124
      ],
      [
        149.461,
        -35.344
      ]
    ]
  },
  "time": null,
  "properties": {
    "name": "Lake George Fault",
    "faultType": "normal fault",
    "faultType_uri": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault",
    "specification_uri": "http://data.geoscience.gov.au/feature/fault/lake-george-fault-1"
  }
}

```


### site observation view complex
Example instance: site_observation_view_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "SiteObservationView",
  "id": "obs-view-complex",
  "geometry": {
    "type": "Point",
    "coordinates": [
      149.312,
      -35.475
    ]
  },
  "time": null,
  "properties": {
    "siteName": "field station FS-42",
    "observationName": "bedding orientation at FS-42",
    "label": "045/32",
    "description": "Strike and dip of bedding in Hervey Group sandstone, measured using Brunton compass. Bedding is moderately inclined to the SE.",
    "featureOfInterest": "bedding in Hervey Group sandstone",
    "observedProperty": "planar orientation \u2013 strike and dip (right-hand rule)",
    "observedValue": "045 / 32",
    "observedValueUom": "degrees",
    "observationMethod": "Brunton compass measurement",
    "positionalAccuracy": "5 m",
    "source": "Smith, J. (2019). Field notes, Goulburn mapping campaign, day 3.",
    "featureOfInterest_uri": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1",
    "propertyType_uri": "http://resource.geosciml.org/classifierScheme/cgi/observedproperty/planar_orientation",
    "metadata_uri": "http://data.geoscience.gov.au/metadata/fieldcampaign/goulburn-2019",
    "genericSymbolizer": "SD_StrikeDip",
    "symbolRotation": 45
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/4283",
  "place": {
    "type": "Point",
    "coordinates": [
      149.312,
      -35.475
    ]
  }
}

```


### site observation view simple
Example instance: site_observation_view_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "SiteObservationView",
  "id": "obs-view-1",
  "geometry": {
    "type": "Point",
    "coordinates": [
      149.312,
      -35.475
    ]
  },
  "time": null,
  "properties": {
    "siteName": "field station FS-42",
    "observationName": "bedding orientation measurement",
    "observedProperty": "planar orientation \u2013 strike and dip",
    "observedValue": "045 / 32",
    "observedValueUom": "degrees",
    "symbolRotation": 45
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmscimlLite/gsmscimlLiteSchema.json
description: 'GeoSciML 4.1 Lite profile. Flattened "View" classes that summarise

  Basic/Extension content for lightweight services (GeologicUnitView,

  ContactView, ShearDisplacementStructureView, BoreholeView, etc.).


  Validates either a single Feature (dispatched by `featureType` to one of: BoreholeView,
  ContactView, GeologicSpecimenView, GeologicUnitView, GeomorphologicUnitView, ShearDisplacementStructureView,
  SiteObservationView) or a FeatureCollection whose `features[]` items are dispatched
  the same way.'
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
            const: BoreholeView
      then:
        $ref: '#BoreholeView'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: ContactView
      then:
        $ref: '#ContactView'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GeologicSpecimenView
      then:
        $ref: '#GeologicSpecimenView'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GeologicUnitView
      then:
        $ref: '#GeologicUnitView'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GeomorphologicUnitView
      then:
        $ref: '#GeomorphologicUnitView'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: ShearDisplacementStructureView
      then:
        $ref: '#ShearDisplacementStructureView'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: SiteObservationView
      then:
        $ref: '#SiteObservationView'
    - if:
        not:
          required:
          - featureType
          properties:
            featureType:
              enum:
              - BoreholeView
              - ContactView
              - GeologicSpecimenView
              - GeologicUnitView
              - GeomorphologicUnitView
              - ShearDisplacementStructureView
              - SiteObservationView
      then: false
  BoreholeView:
    $anchor: BoreholeView
    description: "BoreholeView is a simplified view of a GeoSciML Borehole. In GeoSciML
      terms, this will be an instance of a Borehole feature with key property values
      summarised as labels (unconstrained character strings) or arbitrarily selected
      classifiers to be used for thematic mapping purposes. The latter are the properties
      suffixed with \u201C_uri\u201D and will contain URIs referring to controlled
      concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier:Primitive::CharacterString shall
                uniquely identifies a tuple within the dataset. Identifiers shall
                be formatted as URI according to RFC 3986. This URI could be used
                to access more detailed, such as a GeoSciML Basic, representation
                of the feature. identifier SHOULD resolve to a representation of a
                GeoSciML Borehole.
            name:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property name:Primitive::CharacterString
                contains a human-readable display name for the borehole.
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                contains a human-readable description for the borehole.
            purpose:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the purpose:Primitive::CharacterString property
                reports the purpose or purposes for which the borehole was drilled.
                (e.g., mineral exploration, hydrocarbon exploration, hydrocarbon production,
                groundwater monitoring, geothermal), possibly formatted with formal
                syntax.
            status:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property status:Primitive::CharacterString
                reports the current status of the borehole (e.g., abandoned, completed,
                proposed, suspended).
            drillingMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property drillingMethod:Primitive::CharacterString
                indicates the drilling method, or methods, used for this borehole
                (e.g., RAB, auger, diamond core drilling, air core drilling, piston),
                possibly formatted with formal syntax.
            operator:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property operator:Primitive::CharacterString
                reports the organisation or agency responsible for commissioning of
                the borehole (as opposed to the agency which drilled the borehole).
            driller:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property driller:Primitive::CharacterString
                reports the organisation responsible for drilling the borehole (as
                opposed to commissioning the borehole).
            drillStartDate:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property drillStartDate:Primitive::CharacterString
                reports the date of the start of drilling formatted according to ISO8601
                (e.g., 2012-03-17).
            drillEndDate:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property drillEndData:Primitive::CharacterString
                reports the date of the end of drilling formatted according to ISO8601
                (e.g., 2012-03-28).
            startPoint:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property startPoint:Primitive::CharacterString
                indicates the position relative to the ground surface where the borehole
                commenced (e.g., open pit floor or wall, underground, natural land
                surface, sea floor).
            inclinationType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property inclinationType:Primitive::CharacterString
                indicates the type of inclination of the borehole (e.g., vertical,
                inclined up, inclined down, horizontal).
            boreholeMaterialCustodian:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property boreholeMaterialCustodian:Primitive::CharacterString
                reports the organisation that is the custodian of the material recovered
                from the borehole.
            boreholeLength_m:
              oneOf:
              - type: 'null'
              - type: number
              description: If present, the property boreholeLength_m:Primitive::Number
                reports the length of a borehole, in metres, as determined by the
                data provider. Length may have different sources (e.g., driller's
                measurement, logger's measurement, survey measurement).
            elevation_m:
              oneOf:
              - type: 'null'
              - type: number
              description: If present, the property elevation_m:Primitive::Number
                reports the elevation data, in metres, for the borehole (i.e., wellbore)
                start point. This is a compromise approach to allow for delivery of
                legacy 2D data without elevation data, and for software that cannot
                process a 3D GM_Point.
            elevation_srs:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property elevation_srs:Primitive::CharacterString
                is a URI of a spatial reference system of the elevation value. (e.g.,
                mean sea level). Mandatory if elevation_m is populated. The SRS shall
                be a one dimensional vertical SRS (i.e., EPSG code in the range 5600-5799).
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionalAccuracy:Primitive::CharacterString
                reports an estimate of the accuracy of the location of the borehole
                collar location. Ideally, this would be a quantitative estimate of
                accuracy (e.g., 20 metres).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the source:Primitive::CharacterString property
                describes details and citations to source materials for the borehole
                and, if available, providing URLs to reference material and publications
                describing the borehole. This could be a short text synopsis of key
                information that would also be in the metadata record referenced by
                metadata_uri.
            parentBorehole_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: When present, the parentBorehole_uri:Primitive::CharacterString
                contains a URI referring to one or more representations of a parent
                borehole (e.g., a parent well of a sidetrack wellbore). If the borehole
                does not have any parent, this field shall be empty.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                contains a URI referring to a metadata record describing the provenance
                of data.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property genericSymbolizer:Primitive::CharacterString
                contains an identifier for a symbol from standard (locally or community
                defined) symbolization scheme for portrayal.
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object contains a Geometry defining
                the extent of the borehole start point.
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider may add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  ContactView:
    $anchor: ContactView
    description: "ContactView is a simplified view of a GeoSciML MappedFeature with
      key property values from an associated Contact feature. These properties are
      summarised as labels (unconstrained character strings) or arbitrarily selected
      classifiers to be used for thematic mapping purposes. The latter are the properties
      suffixed with \u201C_uri\u201D and will contain URIs referring to controlled
      concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier:Primitive::CharacterString shall
                uniquely identifies a tuple within the dataset. Identifiers shall
                be formatted as URI according to RFC 3986. This URI could be used
                to access more detailed, such as a GeoSciML Basic, representation
                of the feature. It should have the same value as the corresponding
                GeoSciML MappedFeature identifier if available.
            name:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property name:Primitive::CharacterString
                reports the display name for the Contact.
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                reports the description of the Contact, typically taken from an entry
                on a geological map legend.
            contactType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property contactType:Primitive::CharacterString
                reports the type of Contact (as defined in GeoSciML) as a human readable
                label. To report an identifier from a controlled vocabulary, contactType_uri
                shall be used.
            observationMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observationMethod:Primitive::CharacterString
                reports a metadata snippet indicating how the spatial extent of the
                feature was determined. ObservationMethod is a convenience property
                that provides a quick and simple approach to observation metadata
                when data are reported using a feature view (as opposed to observation
                view).
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionalAccuracy:Primitive::CharacterString
                reports quantitative values defining the radius of an uncertainty
                buffer around a MappedFeature (e.g., a positionalAccuracy of 100 m
                for a line feature defines a buffer polygon of total width 200 m centred
                on the line).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property source:Primitive::CharacterString
                contains a text describing feature-specific details and citations
                to source materials, and if available providing URLs to reference
                material and publications describing the contact feature. This could
                be a short text synopsis of key information that would also be in
                the metadata record referenced by metadata_uri.
            contactType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property contactType_uri:Primitive::CharacterString
                reports a URI referring to a controlled concept from a vocabulary
                defining the Contact types.
            specification_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property specification_uri:Primitive::CharacterString
                reports a URI referring the GeoSciML Contact feature that describes
                the instance in detail.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                reports a URI referring to a metadata record describing the provenance
                of data.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the genericSymbolizer:Primitive::CharacterString
                property contains an identifier for a symbol from standard (locally
                or community defined) symbolization scheme for portrayal.
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object contains a geometry defining
                the extent of the contact feature.
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider can add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeologicSpecimenView:
    $anchor: GeologicSpecimenView
    description: "GeologicSpecimenView is a simplified view of a point-located specimen
      from GeoSciML GeologicSpecimen (an extension of Observations & Measurements
      - ISO19156) with key property values summarised as labels (unconstrained character
      strings) or arbitrarily selected classifiers to be used for thematic mapping
      purposes. The latter are the properties suffixed with \u201C_uri\u201D and will
      contain URIs referring to controlled concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier (eg, an IGSN sample number).
                Should have the same value as a corresponding GeoSciML GeologicSpecimen.
                Globally unique identifier:Primitive::CharacterString shall uniquely
                identifies a tuple within the dataset. Identifiers shall be formatted
                as URI according to RFC 3986. This URI could be used to access more
                detailed, such as a GeoSciML Basic, representation of the feature
                If present, the URI should resolve to a representation that corresponds
                to an instance of GeoSciML GeologicSpecimen.
            label:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property label:Primitive::CharacterString
                contains a short label for map display. (e.g., a sample number).
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                contains a detailed description of the specimen.
            specimenType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property specimentType:Primitive::CharacterString
                contains a human readable description of the specimen type (e.g.,
                hand specimen, thin section, drill core). To report an identifier
                from a controlled vocabulary, specimenType_uri shall be used.
            materialClass:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property materialClass:Primitive::CharacterString
                reports the classification of the material that comprises the specimen
                (e.g., rock, sediment, etc.). To report an identifier from a controlled
                vocabulary, materialClass_uri shall be used.
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionalAccuracy:Primitive::CharacterString
                contains a description of the positional accuracy of the sampling
                location. (e.g., 50 metres).
            samplingTime:
              oneOf:
              - type: 'null'
              - type: string
              description: 'If present, the property samplingTime:Primitive::CharacterString
                reports a date or a date with time of when the specimen was collected
                formatted according to ISO 8601. Examples: &nbsp; &#x9;2012-03-28
                &#x9;2008-02-28T14:15:23-05'
            samplingMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property samplingMethod:Primitive::CharacterString
                reports the method used to collect the specimen (e.g., diamond drilling,
                field mapping survey).
            currentLocation:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property currentLocation:Primitive::CharacterString
                reports the current location of the specimen (e.g., a warehouse or
                other repository location).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property source:Primitive::CharacterString
                reports the citation of the source of the data (e.g., a publication,
                map, etc.).
            specimenType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property specimentType_uri:Primitive::CharacterString
                contains a URI link for a specimen type identifier from a controlled
                vocabulary.
            materialClass_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property materialClass_uri:Primitive::CharacterString
                contains a URI link for a class of material drawn from a controlled
                vocabulary.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                contains a URI link to a metadata document.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the genericSymbolizer:Primitive::CharacterString
                property contains an identifier for a symbol from standard (locally
                or community defined) symbolization scheme for portrayal.
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object contains a geometry of the
                specimen (generally a point).
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider can add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeologicUnitView:
    $anchor: GeologicUnitView
    description: "GeologicUnitView is a simplified view of a GeoSciML MappedFeature
      feature with key property values from an associated GeologicUnit. The GeologicUnitView
      property values are summarised as labels (unconstrained character strings) or
      arbitrarily selected classifiers to be used for thematic mapping purposes. The
      latter are the properties suffixed with \u201C_uri\u201D and will contain URIs
      referring to controlled concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier:Primitive::CharacterString shall
                uniquely identifies a tuple within the dataset. Identifiers shall
                be formatted as URI according to RFC 3986. This URI could be used
                to access more detailed, such as a GeoSciML Basic, representation
                of the feature The identifier should have the same value as the corresponding
                GeoSciML MappedFeature identifier, if available.
            name:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property name:Primitive::CharacterString
                is a display name for the GeologicUnit.
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                is a description of the GeologicUnit, typically taken from an entry
                on a geological map legend.
            geologicUnitType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property geologicUnitType (Primitive::CharacterString)
                contains the type of GeologicUnit (as defined in GeoSciML). To report
                an identifier from a controlled vocabulary, geologicUnitType_uri shall
                be used.
            rank:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property rank:Primitive::CharacterString
                contain the rank of GeologicUnit (as defined by ISC. e.g., group,
                formation, member).
            lithology:
              oneOf:
              - type: 'null'
              - type: string
              description: "If present, lithology contains a human readable description
                as Primitive::CharacterString of the GeologicUnit\u2019s lithology,
                possibly formatted with formal syntax. The description can be language-dependent.
                To report an identifier from a controlled vocabulary, representativeLithology_uri
                shall be used."
            geologicHistory:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, contains a human readable description in Primitive::CharacterString,
                possibly formatted with formal syntax, of the age of the GeologicUnit
                (where age is a sequence of events and may include process and environment
                information). To report an identifier from a controlled vocabulary,
                representativeAge_uri, representativeOlderAge_uri, representativeYoungerAge_uri
                shall be used.
            numericOlderAge:
              oneOf:
              - type: 'null'
              - type: number
              description: "If present, the property numericOlderAge age is a numerical
                representation (Primitive::Number) of the unit\u2019s older age in
                million years (Ma)."
            numericYoungerAge:
              oneOf:
              - type: 'null'
              - type: number
              description: "If present, the property numericYoungerAge is a numerical
                representation (Primitive::Number) of the unit\u2019s younger age
                in million years (Ma)."
            observationMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observationMethod:Primitive::CharacterString
                is a metadata snippet indicating how the spatial extent of the feature
                was determined. ObservationMethod is a convenience property that provides
                a simple approach to observation metadata when data are reported using
                a feature view (as opposed to observation view).
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionalAccuracy:Primitive::CharacterString
                is a quantitative value (a numerical value and a unit of length) defining
                the radius of an uncertainty buffer around a MappedFeature (e.g.,
                a positionalAccuracy of 100 m for a line feature defines a buffer
                polygon of total width 200 m centred on the line).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property source:Primitive::CharacterString
                is human readable text describing feature-specific details and citations
                to source materials, and if available provides URLs to reference material
                and publications describing the geologic feature. This could be a
                short text synopsis of key information that would also be in the metadata
                record referenced by metadata_uri.
            geologicUnitType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property geologicUnitType_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept from a vocabulary
                defining the GeologicUnit types.
            representativeLithology_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeLithology_uri:Primitive::CharacterString
                shall contain a URI referring to a controlled concept specifying the
                characteristic or representative lithology of the unit. This may be
                a concept that defines the super-type of all lithology values present
                within a GeologicUnit or a concept defining the lithology of the dominant
                CompositionPart (as defined in GeoSciML) of the unit.
            representativeAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeAge_uri:Primitive::CharacterString
                shall contain a URI referring to a controlled concept specifying the
                most representative stratigraphic age interval for the GeologicUnit.
                This will be defined entirely at the discretion of the data provider
                and may be a single event selected from the geologic feature's geological
                history or a value summarising the all or part of the feature's history.
            representativeOlderAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeOlderAge_uri:Primitive::CharacterString
                shall contain a URI referring to a controlled concept specifying the
                most representative older value in a range of stratigraphic age intervals
                for the GeologicUnit. This will be defined entirely at the discretion
                of the data provider and may be a single event selected from the geologic
                feature's geological history or a value summarising the all or part
                of the feature's history.
            representativeYoungerAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeYoungerAge_uri:Primitive::CharacterString
                shall contain a URI referring to a controlled concept specifying the
                most representative younger value in a range of stratigraphic age
                intervals for the GeologicUnit. This will be defined entirely at the
                discretion of the data provider and may be a single event selected
                from the geologic feature's geological history or a value summarising
                the all or part of the feature's history.
            specification_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property specification_uri:Primitive::CharacterString
                shall contain a URI referring the GeoSciML GeologicUnit feature that
                describes the instance in detail.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                contains a URI referring to a metadata record describing the provenance
                of data.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property genericSymbolizer:CharacterString
                contains an identifier for a symbol from standard (locally or community
                defined) symbolization scheme for portrayal.
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GEO::GM_Object contains a geometry defining
                the extent of the feature of interest.
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider may add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeomorphologicUnitView:
    $anchor: GeomorphologicUnitView
    description: "GeomorphologicUnitView is a simplified view of a GeoSciML GeomorphologicUnit.
      In GeoSciML terms this will be in instance of a MappedFeature with key property
      values from the associated GeomorphologicUnit feature summarised as labels (unconstrained
      character strings) or arbitrarily selected classifiers to be used for thematic
      mapping purposes. The latter are the properties suffixed with \u201C_uri\u201D
      and will contain URIs referring to controlled concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier:Primitive::CharacterString shall
                uniquely identifies a tuple within the dataset. Identifiers shall
                be formatted as URI according to RFC 3986. This URI could be used
                to access more detailed, such as a GeoSciML Basic, representation
                of the feature. If present, the URI should resolve to a representation
                that corresponds to an instance of GeoSciML MappedFeature.
            name:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property name:Primitive::CharacterString
                contains a display name for the GeomorphologicUnit.
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                contains human readable text description of the GeomorphologicUnit,
                typically taken from an entry on a map legend.
            activity:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property activity:Primitive::CharacterString
                contains a human readable term to specify if the feature is changing
                and how fast. E.g. active, dormant, stable. To report an identifier
                from a controlled vocabulary, activity_uri shall be used.
            geomorphologicFeatureType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property geomorphologicFeatureType:Primitive::CharacterString
                contains a human readable term to specify a broad classification of
                landform. (e.g., anthropogenic, natural). To report an identifier
                from a controlled vocabulary, geomorphologicFeatureType_uri shall
                be used.
            unitType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property unitType:Primitive::CharacterString
                contains a human readable term for the type of GeomorphologicUnit
                (e.g., hill, crater, moraine, plain). To report an identifier from
                a controlled vocabulary, unitType_uri shall be used.
            lithology:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property lithology:Primitive::CharacterString
                contains a text, possibly formatted with formal syntax (see ??????),
                for the description of the GeomorphologicUnit's lithological composition.
                To report an identifier from a controlled vocabulary, representativeLithology_uri
                shall be used.
            geologicHistory:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property geologicHistory:Primitive::CharacterString
                contains text, possibly formatted with formal syntax, for the description
                of the age of the GeomorphologicUnit (where age is a sequence of events
                and may include process and environment information). To report identifier
                from a controlled vocabulary, representativeAge_uri shall be used.
            representativeNumericAge:
              oneOf:
              - type: 'null'
              - type: number
              description: If present, the property representativeNumericAge:Primitive::Number
                contains a numerical value of the representative age in million years
                (Ma).
            observationMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observationMethod:Primitive::CharacterString
                contains a metadata snippet indicating how the spatial extent of the
                feature was determined. ObservationMethod is a convenience property
                that provides a quick approach to observation metadata when data are
                reported using a feature view (as opposed to observation view).
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionAccuracy:Primitive::CharacterString
                contains quantitative values defining the radius of an uncertainty
                buffer around a MappedFeature (e.g., a positionalAccuracy of 100 m
                for a line feature defines a buffer polygon of total width 200 m centred
                on the line).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the source:Primitive::CharacterString property
                contains text describing feature-specific details and citations to
                source materials, and if available providing URLs to reference material
                and publications describing the geologic feature. This could be a
                short text synopsis of key information that would also be in the metadata
                record referenced by metadata_uri.
            activity_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the activity_uri:Primitive::CharacterString
                property reports a URI identifier of activity term drawn from a controlled
                vocabulary.
            geomorphologicFeatureType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property geomorphologicFeatureType_uri:Primitive::CharacterString
                reports a URI identifier of landform term drawn from a controlled
                vocabulary.
            unitType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property unitType_uri:Primitive::CharacterString
                reports a URI referring to a controlled concept from a vocabulary
                defining the GeomorphologicUnit types.
            representativeLithology_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeLithology_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept specifying the characteristic
                or representative lithology of the unit. This may be a concept that
                defines the super-type of all lithology values present within a GeomorphologicUnit
                or a concept defining the lithology of the dominant CompositionPart
                (as defined in GeoSciML) of the unit.
            representativeAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeAge_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept specifying the most
                representative stratigraphic age interval for the GeomorphologicUnit.
                This will be defined entirely at the discretion of the data provider.
                Typically geomorphic units are not assigned age ranges.
            specification_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property specification_uri:Primitive::CharacterString
                contains a URI referring the GeoSciML GeomorphologicUnit feature that
                describes the instance in detail.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                contains a URI referring to a metadata record describing the provenance
                of data.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property genericSymbolizer:Primitive::CharacterString
                contains an identifier for a symbol from standard (locally or community
                defined) symbolization scheme for portrayal.
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object contains a geometry defining
                the extent of the feature of interest.
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider can add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  ShearDisplacementStructureView:
    $anchor: ShearDisplacementStructureView
    description: "ShearDisplacementStructureView is a simplified view of a GeoSciML
      ShearDisplacementStructure. In GeoSciML terms this will be an instance of a
      MappedFeature with key property values from the associated ShearDisplacementStructure
      feature summarised as labels (unconstrained character strings) or arbitrarily
      selected classifiers to be used for thematic mapping purposes. The latter are
      the properties suffixed with \u201C_uri\u201D and will contain URIs referring
      to controlled concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier:Primitive::CharacterString shall
                uniquely identifies a tuple within the dataset. Identifiers shall
                be formatted as URI according to RFC 3986. This URI could be used
                to access more detailed, such as a GeoSciML Basic, representation
                of the feature. It should have the same value as the corresponding
                GeoSciML MappedFeature identifier if available.
            name:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property name:Primitive::CharacterString
                contains a display name for the ShearDisplacementStructure.
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                contains a human readable text description of the ShearDisplacementStructure,
                typically taken from an entry on a geological map legend.
            faultType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property faultType:Primitive::CharacterString
                contains a human readable description of the type of ShearDisplacementStructure
                (as defined in GeoSciML). To report an identifier from a controlled
                vocabulary, faultType_uri shall be used.
            movementType:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property movementType:Primitive::CharacterString
                contains a human readable summary of the type of movement (e.g. dip-slip,
                strike-slip) on the ShearDisplacementStructure. To report an identifier
                from a controlled vocabulary, movementType_uri shall be used.
            deformationStyle:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property deformationStyle:Primitive::CharacterString
                contain a human readable description of the style of deformation (e.g.
                brittle, ductile etc.) for the ShearDisplacementStructure. To report
                an identifier from a controlled vocabulary, deformationStyle_uri shall
                be used.
            displacement:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property displacement:Primitive::CharacterString
                contains a text summarising the displacement across the ShearDisplacementStructure.
            geologicHistory:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property geologicHistory:Primitive::CharacterString
                contains a text, possibly formatted with formal syntax, describing
                the age of the ShearDisplacementStructure (where age is a sequence
                of events and may include process and environment information). To
                report identifiers from a controlled vocabulary, representativeAge_uri,
                representativeOlderAge_uri and representativeYoungerAge_uri shall
                be used.
            numericOlderAge:
              oneOf:
              - type: 'null'
              - type: number
              description: If present, the property numericOlderAge:Primitive::Number
                reports the older age of the fault/shear structure, represented million
                years (Ma).
            numericYoungerAge:
              oneOf:
              - type: 'null'
              - type: number
              description: If present, the property numericYoungerAge:Primitive::Number
                reports the younger age of the fault/shear structure, represented
                million years (Ma).
            observationMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observationMethod:Primitive::CharacterString
                contains a metadata snippet indicating how the spatial extent of the
                feature was determined. ObservationMethod is a convenience property
                that provides a quick and dirty approach to observation metadata when
                data are reported using a feature view (as opposed to observation
                view).
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionAccuracy:Primitive::CharacterString
                contains quantitative representation defining the radius of an uncertainty
                buffer around a MappedFeature (e.g., a positionalAccuracy of 100 m
                for a line feature defines a buffer polygon of total width 200 m centred
                on the line).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property source:Primitive::CharacterString
                contains a text describing feature-specific details and citations
                to source materials, and if available providing URLs to reference
                material and publications describing the geologic feature. This could
                be a short text synopsis of key information that would also be in
                the metadata record referenced by metadata_uri.
            faultType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property faultType_uri:Primitive::CharacterString contains
                a URI referring to a controlled concept from a vocabulary defining
                the fault (ShearDisplacementStructure) type.
            movementType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property movementType_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept from a vocabulary
                defining the ShearDisplacementStructure movement type.
            deformationStyle_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property deformationStyle_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept from a vocabulary
                defining the ShearDisplacementStructure deformation style.
            representativeAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeAge_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept specifying the most
                representative stratigraphic age interval for the ShearDisplacementStructure.
                This will be defined entirely at the discretion of the data provider
                and may be a single event selected from the geologic feature's geological
                history or a value summarising all or part of the feature's history.
            representativeOlderAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeOlderAge_uri:Primitive:CharacterString
                contains a URI referring to a controlled concept specifying the most
                representative lower value in a range of stratigraphic age intervals
                for the ShearDisplacementStructure. This will be defined entirely
                at the discretion of the data provider and may be a single event selected
                from the geologic feature's geological history or a value summarising
                all or part of the feature's history.
            representativeYoungerAge_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property representativeYoungerAge_uri:Primitive::CharacterString
                contains a URI referring to a controlled concept specifying the most
                representative upper value in a range of stratigraphic age intervals
                for the ShearDisplacementStructure. This will be defined entirely
                at the discretion of the data provider and may be a single event selected
                from the geologic feature's geological history or a value summarising
                all or part of the feature's history.
            specification_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property specification_uri:Primitive::CharacterString
                contains a URI referring the GeoSciML ShearDisplacementStructure feature
                that describes the instance in detail.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                contains a URI referring to a metadata record describing the provenance
                of data.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property genericSymbolizer:Primitive::CharacterString
                contains an identifier for a symbol from standard (locally or community
                defined) symbolization scheme for portrayal.
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object contains a geometry defining
                the extent of the feature of interest.
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider can add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  SiteObservationView:
    $anchor: SiteObservationView
    description: "SiteObservationView is a simplified view of a generally point-located
      geological observation, like a structural measurement. This is a simplified
      instance of a sampling geometry from Observations & Measurements (ISO19156)
      with an associated geological observation. Each tuple should represent a single
      observation. Key property values are summarised as labels (unconstrained character
      strings) or arbitrarily selected classifiers to be used for thematic mapping
      purposes. The latter are the properties suffixed with \u201C_uri\u201D and will
      contain URIs referring to controlled concepts in published vocabularies."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            identifier:
              type: string
              description: Globally unique identifier:Primitive::CharacterString shall
                uniquely identifies a tuple within the dataset. Identifiers shall
                be formatted as URI according to RFC 3986. This URI could be used
                to access more detailed, such as a GeoSciML Basic, representation
                of the feature. The URI should resolve to an instance of OM_Observation.
            siteName:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property siteName:Primitive::CharacterString
                contains the name of the sampling feature at this location (e.g. a
                station number, a borehole).
            observationName:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observationName:Primitive::CharacterString
                contains a text identifying the observation.
            label:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property label:Primitive::CharacterString
                contains a short text string to associate with a symbol in a visualization/portrayal.
            description:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property description:Primitive::CharacterString
                contains a text string providing descriptive information about the
                observation.
            featureOfInterest:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property featureOfInterest:Primitive::CharacterString
                contains a description of the geologic feature that the observation
                is intended to characterize, e.g. foliation (observed property= orientation),
                a geologic unit (observed property = age, magnetic susceptibility,
                density, uranium content). The property is equivalent to O&M OM_Observation::featureOfInterest.
                To report a URI of the feature of interest, featureOfInterest_uri
                shall be used.
            observedProperty:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observedProperty:Primitive::CharacterString
                contains a description of the property reported in this record. (E.g.
                orientation, age, density, gold content) as a human readable text.
                To report an identifier of the observedProperty from a controlled
                vocabulary, propertyType_uri shall be used.
            observedValue:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property observedValue:Primitive::CharacterString
                contains the result of the observation. This field is implemented
                as a character string to allow reporting various type of values, the
                value may be numeric (e.g., 235) or textual (e.g., red). Units of
                measure shall be reported in observedValueUom.
            observedValueUom:
              oneOf:
              - type: 'null'
              - type: string
              description: If relevant, the property observedValueUom:Primitive::CharacterString
                contains the unit of measure for a numerical value of an observation
                or measurement, preferably from a controlled vocabulary.
            observationMethod:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the observationMethod:Primitive::CharacterString
                property contains a method description, preferably a term from a controlled
                vocabulary, to categorize the observation method. Further details
                on procedure can be put in the source field.
            positionalAccuracy:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property positionalAccuracy:Primitive::CharacterString
                provides an estimate of the position uncertainty for the site location.
                For numerical measurements, include a unit of measure in the description.
                (e.g., 50 metres, poor, good).
            source:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property source:Primitive::CharacterString
                contains a text description of measurement procedure, processing,
                and provenance of data.
            featureOfInterest_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property featureOfInterest:Primitive::CharacterString
                is functionally equivalent to OM_Observation::featureOfInterest of
                IS19156. It contains a URI link to a representation of the feature
                of interest (e.g., a GeoSciML geologic unit or structure).
            propertyType_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: The property propertyType_uri:Primitive:CharacterString
                is functionally equivalent to OM_Observation::observedProperty. It
                contains a URI to a term from a controlled vocabulary of observed
                property types.
            metadata_uri:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property metadata_uri:Primitive::CharacterString
                contains a URI link to metadata document.
            genericSymbolizer:
              oneOf:
              - type: 'null'
              - type: string
              description: If present, the property genericSymbolizer:Primitive::CharacterString
                contains an identifier for a symbol to portray this observation. Conventions
                for symbol identifiers can be adopted within information exchange
                communities.
            symbolRotation:
              oneOf:
              - type: 'null'
              - type: integer
              description: If present, the symbolRotation:Integer property contains
                an integer value between 0 and 359 to specify rotation of symbol at
                this location, e.g. rotation of a geologic strike and dip symbol to
                reflect the strike azimuth. The angular convention shall be geographic
                angle (clockwise with 0 at geographic north pole, therefore 90 degree
                is east).
            shape:
              $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object contains the geometry of the
                observation site.
            any:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $comment: 'Unresolved type: lax'
                  type: object
                uniqueItems: true
              description: A data provider can add an arbitrary number of extra properties,
                as long as the instance is conformant to GML Simple Feature Level
                0.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmscimlLite/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmscimlLite/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](/github/workspace/_sources/gsmscimlLite/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmscimlLite`

