
# gsmExtendedGeologyCollection (Schema)

`usgin.bbr.geosci.gsmExtendedGeologyCollection` *v0.1*

Extended-profile FeatureCollection. Accepts the full set of 9 Basic

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmExtendedGeologyCollection

Extended-profile FeatureCollection. Accepts the full set of 9 Basic
featureType values (AnthropogenicGeomorphologicFeature, Contact, Fold,
Foliation, GeologicEvent, GeologicUnit, MappedFeature,
NaturalGeomorphologicFeature, ShearDisplacementStructure). Each
Feature additionally requires its description slot(s) to be concrete
Extension classes where one exists; FTs without an extension
description slot (Anthropogenic / NaturalGeomorphologicFeature,
MappedFeature) are pass-through.

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


### fc hammersley fault traces GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleHammerslyData.ttl (Hamersley region, Western Australia). The source TTL distinguishes between fault STRUCTURES (Moona Fault, fault_A1, fault_A2, fault_3496 - typed as gsfa:High_Angle_Fault) and fault TRACES on the earth surface (faulttrace_11445, faulttrace_15546, faulttrace_3496, faulttrace_7439 - typed as gsfa:Fault and hosted by gsoc:earthsurface, isPartOf the parent fault structure). The traces correspond well to MappedFeature instances representing the surface expression of a buried/subsurface ShearDisplacementStructure. This FC encodes the four fault traces as MappedFeature features and notes the spatial-relationship attributes (gsrl:spatiallyTouches, gsrl:spatiallyTruncates) in comments. The Extended profile's MappedFeature branch is pass-through (no extension description slot), so this validates against the same dispatcher as the Basic profile would.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleHammerslyData.ttl (Hamersley region, Western Australia). The source TTL distinguishes between fault STRUCTURES (Moona Fault, fault_A1, fault_A2, fault_3496 - typed as gsfa:High_Angle_Fault) and fault TRACES on the earth surface (faulttrace_11445, faulttrace_15546, faulttrace_3496, faulttrace_7439 - typed as gsfa:Fault and hosted by gsoc:earthsurface, isPartOf the parent fault structure). The traces correspond well to MappedFeature instances representing the surface expression of a buried/subsurface ShearDisplacementStructure. Spatial relations between traces (gsrl:spatiallyTouches, gsrl:spatiallyTruncates) and a fault-vs-contact crosscutting relation (gsrl:crosscuts) from the source TTL are encoded here as GeologicFeatureRelation Feature items in each source's relatedFeature[] array - which the gsmExtendedGeologyCollection profile narrows from the Basic AbstractFeatureRelation to anyOf [SCLinkObject, GeologicFeatureRelation, MaterialRelation]. The relation's `relatedFeature` property carries the target as an SCLinkObject (mirroring OGC's AbstractFeatureRelation shape). The Extended profile's MappedFeature branch is pass-through (no extension description slot).",
  "type": "FeatureCollection",
  "conformsTo": [
    "https://schemas.usgin.org/geosci-json/gsmExtendedGeologyCollection/gsmExtendedGeologyCollectionSchema.json"
  ],
  "features": [
    {
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "https://w3id.org/gso/ex-hammersly#faulttrace_11445",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "name": "Fault trace 11445 (surface expression of Fault A1)",
        "purpose": "instance",
        "specification": {
          "href": "https://w3id.org/gso/ex-hammersly#fault_A1",
          "title": "Fault A1 (High_Angle_Fault) - buried structure this trace expresses"
        }
      }
    },
    {
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "https://w3id.org/gso/ex-hammersly#faulttrace_15546",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "name": "Fault trace 15546 (surface expression of Fault A2)",
        "purpose": "instance",
        "specification": {
          "href": "https://w3id.org/gso/ex-hammersly#fault_A2",
          "title": "Fault A2 (High_Angle_Fault)"
        }
      }
    },
    {
      "$comment": "Per source TTL: spatiallyTouches faulttrace_7439, spatiallyTruncates faulttrace_11445 and faulttrace_15546.",
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "https://w3id.org/gso/ex-hammersly#faulttrace_3496",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "name": "Fault or shear zone trace 3496",
        "purpose": "instance",
        "specification": {
          "href": "https://w3id.org/gso/ex-hammersly#fault_3496",
          "title": "Fault 3496 (High_Angle_Fault)"
        },
        "relatedFeature": [
          {
            "type": "Feature",
            "featureType": "GeologicFeatureRelation",
            "id": "https://w3id.org/gso/ex-hammersly#faulttrace_3496-spatiallyTouches-faulttrace_7439",
            "geometry": null,
            "properties": {
              "relationship": "https://w3id.org/gso/geologicrelation/spatiallyTouches",
              "relatedFeature": {
                "href": "https://w3id.org/gso/ex-hammersly#faulttrace_7439",
                "title": "Fault trace 7439 (Moona Fault) - end-to-end contact with faulttrace_3496"
              }
            }
          },
          {
            "type": "Feature",
            "featureType": "GeologicFeatureRelation",
            "id": "https://w3id.org/gso/ex-hammersly#faulttrace_3496-spatiallyTruncates-faulttrace_11445",
            "geometry": null,
            "properties": {
              "relationship": "https://w3id.org/gso/geologicrelation/spatiallyTruncates",
              "relatedFeature": {
                "href": "https://w3id.org/gso/ex-hammersly#faulttrace_11445",
                "title": "Fault trace 11445 (Fault A1) - truncated by faulttrace_3496"
              }
            }
          },
          {
            "type": "Feature",
            "featureType": "GeologicFeatureRelation",
            "id": "https://w3id.org/gso/ex-hammersly#faulttrace_3496-spatiallyTruncates-faulttrace_15546",
            "geometry": null,
            "properties": {
              "relationship": "https://w3id.org/gso/geologicrelation/spatiallyTruncates",
              "relatedFeature": {
                "href": "https://w3id.org/gso/ex-hammersly#faulttrace_15546",
                "title": "Fault trace 15546 (Fault A2) - truncated by faulttrace_3496"
              }
            }
          }
        ]
      }
    },
    {
      "$comment": "Moona Fault trace; per source TTL crosscuts basejeerinah (the base-of-Jeerinah-Formation contact).",
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "https://w3id.org/gso/ex-hammersly#faulttrace_7439",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "name": "Fault trace 7439 (Moona Fault surface expression)",
        "purpose": "instance",
        "specification": {
          "href": "https://w3id.org/gso/ex-hammersly#MoonaFault",
          "title": "Moona Fault (High_Angle_Fault)"
        },
        "relatedFeature": [
          {
            "type": "Feature",
            "featureType": "GeologicFeatureRelation",
            "id": "https://w3id.org/gso/ex-hammersly#faulttrace_7439-crosscuts-basejeerinah",
            "geometry": null,
            "properties": {
              "relationship": "https://w3id.org/gso/geologicrelation/crosscuts",
              "relatedFeature": {
                "href": "https://w3id.org/gso/ex-hammersly#basejeerinah",
                "title": "Base of Jeerinah Formation (contact crosscut by Moona Fault)"
              }
            }
          }
        ]
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmExtendedGeologyCollection/gsmExtendedGeologyCollectionSchema.json
description: 'Extended-profile FeatureCollection. Accepts the full set of 9 Basic

  featureType values (AnthropogenicGeomorphologicFeature, Contact, Fold,

  Foliation, GeologicEvent, GeologicUnit, MappedFeature,

  NaturalGeomorphologicFeature, ShearDisplacementStructure). Each

  Feature additionally requires its description slot(s) to be concrete

  Extension classes where one exists; FTs without an extension

  description slot (Anthropogenic / NaturalGeomorphologicFeature,

  MappedFeature) are pass-through. The profile also narrows every

  feature''s relatedFeature[] items: where Basic accepts

  `oneOf [SCLinkObject, AbstractFeatureRelation]`, the Extended profile

  additionally requires each AbstractFeatureRelation instance to be one

  of the two concrete subtypes from gsmGeologicRelationExtension

  (GeologicFeatureRelation or MaterialRelation), while still allowing

  by-reference SCLinkObject.'
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmExtendedGeologyCollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmExtendedGeologyCollection/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmExtendedGeologyCollection/context.jsonld)

## Sources

* [GeoSciML 4.1 - FC profile composed across building blocks](https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmExtendedGeologyCollection`

