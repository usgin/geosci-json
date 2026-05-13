
# gsmCompleteGeology (Schema)

`usgin.bbr.geosci.gsmCompleteGeology` *v0.1*

Complete-coverage FeatureCollection profile. Superset of

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmCompleteGeology/gsmCompleteGeologySchema.json
description: 'Complete-coverage FeatureCollection profile. Superset of

  gsmExtendedGeology that additionally dispatches every Feature-shaped

  class across the extension BBs: relations

  (GeologicFeatureRelation, MaterialRelation), materials

  (CompoundMaterial, Mineral, OrganicMaterial, RockMaterial), and

  geologic-time anchors (GeochronologicEra, GeochronologicBoundary,

  GlobalStratotypePoint, GlobalStratotypeSection, StratigraphicPoint,

  StratigraphicSection). The same per-Basic-FT description-slot

  narrowing and the same relatedFeature[] anyOf constraint apply.

  Use when you want a single FC schema that accepts any GeoSciML

  Feature in the model (Basic + Extension + relations + materials +

  time anchors) at the FC''s top-level features[] array.'
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
            required:
            - featureType
            properties:
              featureType:
                const: GeologicFeatureRelation
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicRelationExtension/gsmGeologicRelationExtensionSchema.json#GeologicFeatureRelation
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: MaterialRelation
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicRelationExtension/gsmGeologicRelationExtensionSchema.json#MaterialRelation
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: CompoundMaterial
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#CompoundMaterial
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Mineral
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterial/gsmEarthMaterialSchema.json#Mineral
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: OrganicMaterial
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterial/gsmEarthMaterialSchema.json#OrganicMaterial
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: RockMaterial
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#RockMaterial
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: GeochronologicEra
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#GeochronologicEra
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: GeochronologicBoundary
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#GeochronologicBoundary
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: GlobalStratotypePoint
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#GlobalStratotypePoint
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: GlobalStratotypeSection
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#GlobalStratotypeSection
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: StratigraphicPoint
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#StratigraphicPoint
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: StratigraphicSection
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmGeologicTime/gsmGeologicTimeSchema.json#StratigraphicSection
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
                  - GeologicFeatureRelation
                  - MaterialRelation
                  - CompoundMaterial
                  - Mineral
                  - OrganicMaterial
                  - RockMaterial
                  - GeochronologicEra
                  - GeochronologicBoundary
                  - GlobalStratotypePoint
                  - GlobalStratotypeSection
                  - StratigraphicPoint
                  - StratigraphicSection
          then: false

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmCompleteGeology/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmCompleteGeology/schema.yaml)

## Sources

* [GeoSciML 4.1 - FC profile composed across building blocks](https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmCompleteGeology`

