
# gsmExtendedGeologyCollection (Schema)

`usgin.bbr.geosci.gsmExtendedGeologyCollection` *v0.1*

Extended-profile FeatureCollection. Accepts the same featureType values

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmExtendedGeologyCollection

Extended-profile FeatureCollection. Accepts the same featureType values
as gsmBasicGeologyCollection, but each Feature additionally requires
its description slot(s) to be concrete Extension classes. MappedFeature
is pass-through (no Extension description slot).

## Examples

### fc extended minimal
Minimal Extended-profile FeatureCollection. The Extended profile dispatches on featureType into the Basic anchors with extra description-slot constraints. Each constraint only fires when the slot is present, so a minimal instance with no description content still validates and exercises the dispatcher routing.
#### json
```json
{
  "$comment": "Minimal Extended-profile FeatureCollection. The Extended profile dispatches on featureType into the Basic anchors with extra description-slot constraints. Each constraint only fires when the slot is present, so a minimal instance with no description content still validates and exercises the dispatcher routing.",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "ext.minimal.gu.1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit"
      }
    },
    {
      "type": "Feature",
      "featureType": "Contact",
      "id": "ext.minimal.contact.1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/conformable_contact"
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmExtendedGeologyCollection/gsmExtendedGeologyCollectionSchema.json
description: 'Extended-profile FeatureCollection. Accepts the same featureType values

  as gsmBasicGeologyCollection, but each Feature additionally requires

  its description slot(s) to be concrete Extension classes. MappedFeature

  is pass-through (no Extension description slot).'
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
                const: GeologicUnit
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#GeologicUnit
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
                        $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterialExtension/gsmEarthMaterialExtensionSchema.json#CompoundMaterialDescription
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: MappedFeature
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#MappedFeature
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Contact
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#Contact
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
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#Fold
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
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#Foliation
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
                const: ShearDisplacementStructure
          then:
            allOf:
            - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#ShearDisplacementStructure
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
            not:
              required:
              - featureType
              properties:
                featureType:
                  enum:
                  - GeologicUnit
                  - MappedFeature
                  - Contact
                  - Fold
                  - Foliation
                  - ShearDisplacementStructure
          then: false

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmExtendedGeologyCollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmExtendedGeologyCollection/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmExtendedGeologyCollection/context.jsonld)

## Sources

* [GeoSciML 4.1 — FC profile composed across building blocks](https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmExtendedGeologyCollection`

