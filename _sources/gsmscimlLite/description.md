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
| `name` | (oneOf - see schema) | 0..1 | If present, the property name:Primitive::CharacterString contains a human-readable display name for the borehole. |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a human-readable description for the borehole. |
| `purpose` | (oneOf - see schema) | 0..1 | If present, the purpose:Primitive::CharacterString property reports the purpose or purposes for which the borehole wa… |
| `status` | (oneOf - see schema) | 0..1 | If present, the property status:Primitive::CharacterString reports the current status of the borehole (e.g., abandone… |
| `drillingMethod` | (oneOf - see schema) | 0..1 | If present, the property drillingMethod:Primitive::CharacterString indicates the drilling method, or methods, used fo… |
| `operator` | (oneOf - see schema) | 0..1 | If present, the property operator:Primitive::CharacterString reports the organisation or agency responsible for commi… |
| `driller` | (oneOf - see schema) | 0..1 | If present, the property driller:Primitive::CharacterString reports the organisation responsible for drilling the bor… |
| `drillStartDate` | (oneOf - see schema) | 0..1 | If present, the property drillStartDate:Primitive::CharacterString reports the date of the start of drilling formatte… |
| `drillEndDate` | (oneOf - see schema) | 0..1 | If present, the property drillEndData:Primitive::CharacterString reports the date of the end of drilling formatted ac… |
| `startPoint` | (oneOf - see schema) | 0..1 | If present, the property startPoint:Primitive::CharacterString indicates the position relative to the ground surface … |
| `inclinationType` | (oneOf - see schema) | 0..1 | If present, the property inclinationType:Primitive::CharacterString indicates the type of inclination of the borehole… |
| `boreholeMaterialCustodian` | (oneOf - see schema) | 0..1 | If present, the property boreholeMaterialCustodian:Primitive::CharacterString reports the organisation that is the cu… |
| `boreholeLength_m` | (oneOf - see schema) | 0..1 | If present, the property boreholeLength_m:Primitive::Number reports the length of a borehole, in metres, as determine… |
| `elevation_m` | (oneOf - see schema) | 0..1 | If present, the property elevation_m:Primitive::Number reports the elevation data, in metres, for the borehole (i.e.,… |
| `elevation_srs` | (oneOf - see schema) | 0..1 | If present, the property elevation_srs:Primitive::CharacterString is a URI of a spatial reference system of the eleva… |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString reports an estimate of the accuracy of the loc… |
| `source` | (oneOf - see schema) | 0..1 | If present, the source:Primitive::CharacterString property describes details and citations to source materials for th… |
| `parentBorehole_uri` | (oneOf - see schema) | 0..1 | When present, the parentBorehole_uri:Primitive::CharacterString contains a URI referring to one or more representatio… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a Geometry defining the extent of the borehole start point. |
| `any` | (oneOf - see schema) | 0..1 | A data provider may add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `ContactView`

ContactView is a simplified view of a GeoSciML MappedFeature with key property values from an associated Contact feature. These properties are summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf - see schema) | 0..1 | If present, the property name:Primitive::CharacterString reports the display name for the Contact. |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString reports the description of the Contact, typically tak… |
| `contactType` | (oneOf - see schema) | 0..1 | If present, the property contactType:Primitive::CharacterString reports the type of Contact (as defined in GeoSciML) … |
| `observationMethod` | (oneOf - see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString reports a metadata snippet indicating how the s… |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString reports quantitative values defining the radiu… |
| `source` | (oneOf - see schema) | 0..1 | If present, the property source:Primitive::CharacterString contains a text describing feature-specific details and ci… |
| `contactType_uri` | (oneOf - see schema) | 0..1 | The property contactType_uri:Primitive::CharacterString reports a URI referring to a controlled concept from a vocabu… |
| `specification_uri` | (oneOf - see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString reports a URI referring the GeoSciML Contact fe… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString reports a URI referring to a metadata record describ… |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the genericSymbolizer:Primitive::CharacterString property contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry defining the extent of the contact feature. |
| `any` | (oneOf - see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `GeologicSpecimenView`

GeologicSpecimenView is a simplified view of a point-located specimen from GeoSciML GeologicSpecimen (an extension of Observations & Measurements - ISO19156) with key property values summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier (eg, an IGSN sample number). Should have the same value as a corresponding GeoSciML Geolog… |
| `label` | (oneOf - see schema) | 0..1 | If present, the property label:Primitive::CharacterString contains a short label for map display. (e.g., a sample num… |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a detailed description of the specimen. |
| `specimenType` | (oneOf - see schema) | 0..1 | If present, the property specimentType:Primitive::CharacterString contains a human readable description of the specim… |
| `materialClass` | (oneOf - see schema) | 0..1 | If present, the property materialClass:Primitive::CharacterString reports the classification of the material that com… |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString contains a description of the positional accur… |
| `samplingTime` | (oneOf - see schema) | 0..1 | If present, the property samplingTime:Primitive::CharacterString reports a date or a date with time of when the speci… |
| `samplingMethod` | (oneOf - see schema) | 0..1 | If present, the property samplingMethod:Primitive::CharacterString reports the method used to collect the specimen (e… |
| `currentLocation` | (oneOf - see schema) | 0..1 | If present, the property currentLocation:Primitive::CharacterString reports the current location of the specimen (e.g… |
| `source` | (oneOf - see schema) | 0..1 | If present, the property source:Primitive::CharacterString reports the citation of the source of the data (e.g., a pu… |
| `specimenType_uri` | (oneOf - see schema) | 0..1 | The property specimentType_uri:Primitive::CharacterString contains a URI link for a specimen type identifier from a c… |
| `materialClass_uri` | (oneOf - see schema) | 0..1 | The property materialClass_uri:Primitive::CharacterString contains a URI link for a class of material drawn from a co… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI link to a metadata document. |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the genericSymbolizer:Primitive::CharacterString property contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry of the specimen (generally a point). |
| `any` | (oneOf - see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `GeologicUnitView`

GeologicUnitView is a simplified view of a GeoSciML MappedFeature feature with key property values from an associated GeologicUnit. The GeologicUnitView property values are summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf - see schema) | 0..1 | If present, the property name:Primitive::CharacterString is a display name for the GeologicUnit. |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString is a description of the GeologicUnit, typically taken… |
| `geologicUnitType` | (oneOf - see schema) | 0..1 | If present, the property geologicUnitType (Primitive::CharacterString) contains the type of GeologicUnit (as defined … |
| `rank` | (oneOf - see schema) | 0..1 | If present, the property rank:Primitive::CharacterString contain the rank of GeologicUnit (as defined by ISC. e.g., g… |
| `lithology` | (oneOf - see schema) | 0..1 | If present, lithology contains a human readable description as Primitive::CharacterString of the GeologicUnit’s litho… |
| `geologicHistory` | (oneOf - see schema) | 0..1 | If present, contains a human readable description in Primitive::CharacterString, possibly formatted with formal synta… |
| `numericOlderAge` | (oneOf - see schema) | 0..1 | If present, the property numericOlderAge age is a numerical representation (Primitive::Number) of the unit’s older ag… |
| `numericYoungerAge` | (oneOf - see schema) | 0..1 | If present, the property numericYoungerAge is a numerical representation (Primitive::Number) of the unit’s younger ag… |
| `observationMethod` | (oneOf - see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString is a metadata snippet indicating how the spatia… |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString is a quantitative value (a numerical value and… |
| `source` | (oneOf - see schema) | 0..1 | If present, the property source:Primitive::CharacterString is human readable text describing feature-specific details… |
| `geologicUnitType_uri` | (oneOf - see schema) | 0..1 | The property geologicUnitType_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a … |
| `representativeLithology_uri` | (oneOf - see schema) | 0..1 | The property representativeLithology_uri:Primitive::CharacterString shall contain a URI referring to a controlled con… |
| `representativeAge_uri` | (oneOf - see schema) | 0..1 | The property representativeAge_uri:Primitive::CharacterString shall contain a URI referring to a controlled concept s… |
| `representativeOlderAge_uri` | (oneOf - see schema) | 0..1 | The property representativeOlderAge_uri:Primitive::CharacterString shall contain a URI referring to a controlled conc… |
| `representativeYoungerAge_uri` | (oneOf - see schema) | 0..1 | The property representativeYoungerAge_uri:Primitive::CharacterString shall contain a URI referring to a controlled co… |
| `specification_uri` | (oneOf - see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString shall contain a URI referring the GeoSciML Geol… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the property genericSymbolizer:CharacterString contains an identifier for a symbol from standard (locally… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GEO::GM_Object contains a geometry defining the extent of the feature of interest. |
| `any` | (oneOf - see schema) | 0..1 | A data provider may add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `GeomorphologicUnitView`

GeomorphologicUnitView is a simplified view of a GeoSciML GeomorphologicUnit. In GeoSciML terms this will be in instance of a MappedFeature with key property values from the associated GeomorphologicUnit feature summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf - see schema) | 0..1 | If present, the property name:Primitive::CharacterString contains a display name for the GeomorphologicUnit. |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains human readable text description of the Geomo… |
| `activity` | (oneOf - see schema) | 0..1 | If present, the property activity:Primitive::CharacterString contains a human readable term to specify if the feature… |
| `geomorphologicFeatureType` | (oneOf - see schema) | 0..1 | If present, the property geomorphologicFeatureType:Primitive::CharacterString contains a human readable term to speci… |
| `unitType` | (oneOf - see schema) | 0..1 | If present, the property unitType:Primitive::CharacterString contains a human readable term for the type of Geomorpho… |
| `lithology` | (oneOf - see schema) | 0..1 | If present, the property lithology:Primitive::CharacterString contains a text, possibly formatted with formal syntax … |
| `geologicHistory` | (oneOf - see schema) | 0..1 | If present, the property geologicHistory:Primitive::CharacterString contains text, possibly formatted with formal syn… |
| `representativeNumericAge` | (oneOf - see schema) | 0..1 | If present, the property representativeNumericAge:Primitive::Number contains a numerical value of the representative … |
| `observationMethod` | (oneOf - see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString contains a metadata snippet indicating how the … |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionAccuracy:Primitive::CharacterString contains quantitative values defining the radius… |
| `source` | (oneOf - see schema) | 0..1 | If present, the source:Primitive::CharacterString property contains text describing feature-specific details and cita… |
| `activity_uri` | (oneOf - see schema) | 0..1 | If present, the activity_uri:Primitive::CharacterString property reports a URI identifier of activity term drawn from… |
| `geomorphologicFeatureType_uri` | (oneOf - see schema) | 0..1 | If present, the property geomorphologicFeatureType_uri:Primitive::CharacterString reports a URI identifier of landfor… |
| `unitType_uri` | (oneOf - see schema) | 0..1 | If present, the property unitType_uri:Primitive::CharacterString reports a URI referring to a controlled concept from… |
| `representativeLithology_uri` | (oneOf - see schema) | 0..1 | The property representativeLithology_uri:Primitive::CharacterString contains a URI referring to a controlled concept … |
| `representativeAge_uri` | (oneOf - see schema) | 0..1 | The property representativeAge_uri:Primitive::CharacterString contains a URI referring to a controlled concept specif… |
| `specification_uri` | (oneOf - see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString contains a URI referring the GeoSciML Geomorpho… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry defining the extent of the feature of interest. |
| `any` | (oneOf - see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `ShearDisplacementStructureView`

ShearDisplacementStructureView is a simplified view of a GeoSciML ShearDisplacementStructure. In GeoSciML terms this will be an instance of a MappedFeature with key property values from the associated ShearDisplacementStructure feature summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `name` | (oneOf - see schema) | 0..1 | If present, the property name:Primitive::CharacterString contains a display name for the ShearDisplacementStructure. |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a human readable text description of the She… |
| `faultType` | (oneOf - see schema) | 0..1 | If present, the property faultType:Primitive::CharacterString contains a human readable description of the type of Sh… |
| `movementType` | (oneOf - see schema) | 0..1 | If present, the property movementType:Primitive::CharacterString contains a human readable summary of the type of mov… |
| `deformationStyle` | (oneOf - see schema) | 0..1 | If present, the property deformationStyle:Primitive::CharacterString contain a human readable description of the styl… |
| `displacement` | (oneOf - see schema) | 0..1 | If present, the property displacement:Primitive::CharacterString contains a text summarising the displacement across … |
| `geologicHistory` | (oneOf - see schema) | 0..1 | If present, the property geologicHistory:Primitive::CharacterString contains a text, possibly formatted with formal s… |
| `numericOlderAge` | (oneOf - see schema) | 0..1 | If present, the property numericOlderAge:Primitive::Number reports the older age of the fault/shear structure, repres… |
| `numericYoungerAge` | (oneOf - see schema) | 0..1 | If present, the property numericYoungerAge:Primitive::Number reports the younger age of the fault/shear structure, re… |
| `observationMethod` | (oneOf - see schema) | 0..1 | If present, the property observationMethod:Primitive::CharacterString contains a metadata snippet indicating how the … |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionAccuracy:Primitive::CharacterString contains quantitative representation defining th… |
| `source` | (oneOf - see schema) | 0..1 | If present, the property source:Primitive::CharacterString contains a text describing feature-specific details and ci… |
| `faultType_uri` | (oneOf - see schema) | 0..1 | The property faultType_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a vocabul… |
| `movementType_uri` | (oneOf - see schema) | 0..1 | The property movementType_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a voca… |
| `deformationStyle_uri` | (oneOf - see schema) | 0..1 | The property deformationStyle_uri:Primitive::CharacterString contains a URI referring to a controlled concept from a … |
| `representativeAge_uri` | (oneOf - see schema) | 0..1 | The property representativeAge_uri:Primitive::CharacterString contains a URI referring to a controlled concept specif… |
| `representativeOlderAge_uri` | (oneOf - see schema) | 0..1 | The property representativeOlderAge_uri:Primitive:CharacterString contains a URI referring to a controlled concept sp… |
| `representativeYoungerAge_uri` | (oneOf - see schema) | 0..1 | The property representativeYoungerAge_uri:Primitive::CharacterString contains a URI referring to a controlled concept… |
| `specification_uri` | (oneOf - see schema) | 0..1 | If present, the property specification_uri:Primitive::CharacterString contains a URI referring the GeoSciML ShearDisp… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI referring to a metadata record descri… |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol from standa… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains a geometry defining the extent of the feature of interest. |
| `any` | (oneOf - see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

### `SiteObservationView`

SiteObservationView is a simplified view of a generally point-located geological observation, like a structural measurement. This is a simplified instance of a sampling geometry from Observations & Measurements (ISO19156) with an associated geological observation. Each tuple should represent a single observation. Key property values are summarised as labels (unconstrained character strings) or arbitrarily selected classifiers to be used for thematic mapping purposes. The latter are the properties suffixed with “_uri” and will contain URIs referring to controlled concepts in published vocabularies.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `identifier` | `string` | 0..1 | Globally unique identifier:Primitive::CharacterString shall uniquely identifies a tuple within the dataset. Identifie… |
| `siteName` | (oneOf - see schema) | 0..1 | If present, the property siteName:Primitive::CharacterString contains the name of the sampling feature at this locati… |
| `observationName` | (oneOf - see schema) | 0..1 | If present, the property observationName:Primitive::CharacterString contains a text identifying the observation. |
| `label` | (oneOf - see schema) | 0..1 | If present, the property label:Primitive::CharacterString contains a short text string to associate with a symbol in … |
| `description` | (oneOf - see schema) | 0..1 | If present, the property description:Primitive::CharacterString contains a text string providing descriptive informat… |
| `featureOfInterest` | (oneOf - see schema) | 0..1 | If present, the property featureOfInterest:Primitive::CharacterString contains a description of the geologic feature … |
| `observedProperty` | (oneOf - see schema) | 0..1 | If present, the property observedProperty:Primitive::CharacterString contains a description of the property reported … |
| `observedValue` | (oneOf - see schema) | 0..1 | If present, the property observedValue:Primitive::CharacterString contains the result of the observation. This field … |
| `observedValueUom` | (oneOf - see schema) | 0..1 | If relevant, the property observedValueUom:Primitive::CharacterString contains the unit of measure for a numerical va… |
| `observationMethod` | (oneOf - see schema) | 0..1 | If present, the observationMethod:Primitive::CharacterString property contains a method description, preferably a ter… |
| `positionalAccuracy` | (oneOf - see schema) | 0..1 | If present, the property positionalAccuracy:Primitive::CharacterString provides an estimate of the position uncertain… |
| `source` | (oneOf - see schema) | 0..1 | If present, the property source:Primitive::CharacterString contains a text description of measurement procedure, proc… |
| `featureOfInterest_uri` | (oneOf - see schema) | 0..1 | The property featureOfInterest:Primitive::CharacterString is functionally equivalent to OM_Observation::featureOfInte… |
| `propertyType_uri` | (oneOf - see schema) | 0..1 | The property propertyType_uri:Primitive:CharacterString is functionally equivalent to OM_Observation::observedPropert… |
| `metadata_uri` | (oneOf - see schema) | 0..1 | If present, the property metadata_uri:Primitive::CharacterString contains a URI link to metadata document. |
| `genericSymbolizer` | (oneOf - see schema) | 0..1 | If present, the property genericSymbolizer:Primitive::CharacterString contains an identifier for a symbol to portray … |
| `symbolRotation` | (oneOf - see schema) | 0..1 | If present, the symbolRotation:Integer property contains an integer value between 0 and 359 to specify rotation of sy… |
| `shape` | GeoJSON `Geometry` | 0..1 | The property shape:GM_Object contains the geometry of the observation site. |
| `any` | (oneOf - see schema) | 0..1 | A data provider can add an arbitrary number of extra properties, as long as the instance is conformant to GML Simple … |

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
