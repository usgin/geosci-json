
# gsmExtendedGeology (Schema)

`usgin.bbr.geosci.gsmExtendedGeology` *v0.1*

Extended-profile FeatureCollection. Functionally equivalent to OGC's

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmExtendedGeology/gsmExtendedGeologySchema.json
description: 'Extended-profile FeatureCollection. Functionally equivalent to OGC''s

  geosciml_extension_featurecollection.json: accepts the 9 Basic

  featureType values (AnthropogenicGeomorphologicFeature, Contact,

  Fold, Foliation, GeologicEvent, GeologicUnit, MappedFeature,

  NaturalGeomorphologicFeature, ShearDisplacementStructure) AND the 6

  Extension structure featureType values (DisplacementEvent,

  FoldSystem, Joint, Layering, Lineation, NonDirectionalStructure).

  Each Basic Feature additionally requires its description slot(s) to

  be the concrete Extension class where one exists; Extension FTs are

  already concrete and validate against their own anchors. The profile

  also narrows every feature''s relatedFeature[] items: where Basic

  accepts `oneOf [SCLinkObject, AbstractFeatureRelation]`, the

  Extended profile additionally requires each AbstractFeatureRelation

  instance to be one of the concrete subtypes from

  gsmGeologicRelationExtension (GeologicFeatureRelation or

  MaterialRelation), while still allowing by-reference SCLinkObject.'
allOf:
- $ref: https://schemas.opengis.net/json-fg/featurecollection.json
- type: object
  properties:
    features:
      type: array
      items:
        allOf:
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: AnthropogenicGeomorphologicFeature
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#AnthropogenicGeomorphologicFeature
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Contact
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#Contact
            - type: object
              properties:
                properties:
                  type: object
                  properties:
                    stContactDescription:
                      $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#ContactDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Fold
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#Fold
            - type: object
              properties:
                properties:
                  type: object
                  properties:
                    stFoldDescription:
                      $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#FoldDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Foliation
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#Foliation
            - type: object
              properties:
                properties:
                  type: object
                  properties:
                    stFoliationDescription:
                      $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#FoliationDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: GeologicEvent
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent
            - type: object
              properties:
                properties:
                  type: object
                  properties:
                    gaEventDescription:
                      type: array
                      items:
                        $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#GeologicEventDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: GeologicUnit
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicUnit
            - type: object
              properties:
                properties:
                  type: object
                  properties:
                    gbUnitDescription:
                      type: array
                      items:
                        $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicUnitExtension/gsmGeologicUnitExtensionSchema.json#GeologicUnitDescription
                    gbMaterialDescription:
                      type: array
                      items:
                        $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterial/gsmEarthMaterialSchema.json#CompoundMaterialDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: MappedFeature
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#MappedFeature
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: NaturalGeomorphologicFeature
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#NaturalGeomorphologicFeature
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: ShearDisplacementStructure
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#ShearDisplacementStructure
            - type: object
              properties:
                properties:
                  type: object
                  properties:
                    stStructureDescription:
                      type: array
                      items:
                        $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#ShearDisplacementStructureDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: DisplacementEvent
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#DisplacementEvent
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: FoldSystem
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#FoldSystem
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Joint
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#Joint
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Layering
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#Layering
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Lineation
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#Lineation
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: NonDirectionalStructure
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicStructureExtension/gsmGeologicStructureExtensionSchema.json#NonDirectionalStructure
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
                  - DisplacementEvent
                  - FoldSystem
                  - Joint
                  - Layering
                  - Lineation
                  - NonDirectionalStructure
          then: false
- type: object
  properties:
    features:
      type: array
      items:
        type: object
        properties:
          properties:
            type: object
            properties:
              relatedFeature:
                type: array
                items:
                  anyOf:
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#/$defs/SCLinkObject
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicRelationExtension/gsmGeologicRelationExtensionSchema.json#GeologicFeatureRelation
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicRelationExtension/gsmGeologicRelationExtensionSchema.json#MaterialRelation

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmExtendedGeology/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmExtendedGeology/schema.yaml)

## Sources

* [GeoSciML 4.1 - FC profile composed across building blocks](https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmExtendedGeology`

