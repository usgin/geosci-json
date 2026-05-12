
# gsmEarthMaterialCollection (Schema)

`usgin.bbr.geosci.gsmEarthMaterialCollection` *v0.1*

FeatureCollection profile collecting EarthMaterial features with rich

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmEarthMaterialCollection

FeatureCollection profile collecting EarthMaterial features with rich
description content. Root featureType values are the four concrete (or
first-class) EarthMaterial subtypes — Mineral, OrganicMaterial,
RockMaterial, CompoundMaterial. None of these are «FeatureType» in the
UML (all are «Type»), so the profile injects the JSON-FG Feature
envelope around each via `wrapAsFeature: true`. The inherited
`gbEarthMaterialDescription` slot (from the EarthMaterial parent) is
constrained on RockMaterial and CompoundMaterial branches to require
the corresponding concrete Extension description class.

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
            "$comment": "RockMaterialDescription — content shape, not strictly required by schema",
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
$id: https://schemas.usgin.org/geosci-json/gsmEarthMaterialCollection/gsmEarthMaterialCollectionSchema.json
description: "FeatureCollection profile collecting EarthMaterial features with rich\ndescription
  content. Root featureType values are the four concrete (or\nfirst-class) EarthMaterial
  subtypes \u2014 Mineral, OrganicMaterial,\nRockMaterial, CompoundMaterial. None
  of these are \xABFeatureType\xBB in the\nUML (all are \xABType\xBB), so the profile
  injects the JSON-FG Feature\nenvelope around each via `wrapAsFeature: true`. The
  inherited\n`gbEarthMaterialDescription` slot (from the EarthMaterial parent) is\nconstrained
  on RockMaterial and CompoundMaterial branches to require\nthe corresponding concrete
  Extension description class."
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
                  $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterialExtension/gsmEarthMaterialExtensionSchema.json#Mineral
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
                  $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterialExtension/gsmEarthMaterialExtensionSchema.json#OrganicMaterial
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
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#RockMaterial
                  - type: object
                    properties:
                      gbEarthMaterialDescription:
                        type: array
                        items:
                          $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterialExtension/gsmEarthMaterialExtensionSchema.json#RockMaterialDescription
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
                  - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#CompoundMaterial
                  - type: object
                    properties:
                      gbEarthMaterialDescription:
                        type: array
                        items:
                          $ref: https://usgin.github.io/geosci-json/_sources/gsmEarthMaterialExtension/gsmEarthMaterialExtensionSchema.json#CompoundMaterialDescription
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

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmEarthMaterialCollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmEarthMaterialCollection/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmEarthMaterialCollection/context.jsonld)

## Sources

* [GeoSciML 4.1 — FC profile composed across building blocks](https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmEarthMaterialCollection`

