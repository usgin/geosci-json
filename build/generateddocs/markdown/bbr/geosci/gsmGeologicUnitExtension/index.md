
# gsmGeologicUnitExtension (Schema)

`usgin.bbr.geosci.gsmGeologicUnitExtension` *v0.1*

GeologicUnit extension: detailed unit description structures

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmGeologicUnitExtension

GeoSciML 4.1 building block `gsmGeologicUnitExtension`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeologicUnitDetails`.

Contains 2 data types.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `BeddingDescription` | «DataType» | plain JSON object |
| `GeologicUnitDescription` | «DataType» | plain JSON object |

## Class details

### `BeddingDescription`

BeddingDescription provides a detailed description of the bedding characteristics of a geologic unit.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `beddingPattern` | (oneOf — see schema) | 0..1 | The property beddingPattern (SWE::Category) provides a term from a controlled vocabulary specifying patterns of beddi… |
| `beddingStyle` | (oneOf — see schema) | 0..1 | The property beddingStyle (SWE::Category) provides a term from a controlled vocabulary specifying the style of beddin… |
| `beddingThickness` | (oneOf — see schema) | 0..1 | The property beddingThickness (SWE::Category) provides a term from a controlled vocabulary characterizing the thickne… |

### `GeologicUnitDescription`

GeologicUnitDescription provides for extended description of the characteristics of a geologic unit.

**Supertype**: `GeologicUnitAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `bodyMorphology` | (oneOf — see schema) | 0..1 | The bodyMorphology property (SWE::Category) provides a term from a controlled vocabulary describing the geometry or f… |
| `unitComposition` | (oneOf — see schema) | 0..1 | The unitComposition property (SWE::Category) provides a term from a composition-based classification that requires su… |
| `outcropCharacter` | (oneOf — see schema) | 0..1 | The property outcropCharacter (SWE::Category) provides a term that describes the nature of outcrops formed by a geolo… |
| `unitThickness` | (oneOf — see schema) | 0..1 | The property unitThickness (SWE::QuantityRange) provides a value that represents the typical thickness of the geologi… |
| `bedding` | (oneOf — see schema) | 0..1 | The bedding:BeddingDescription property reports a description of the bedding. |

## External dependencies

- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicUnitAbstractDescription`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [examplegsmGeologicUnitExtensionMinimal.json](examples/examplegsmGeologicUnitExtensionMinimal.json)
- [geologic_unit_la_tojiza_pluton_GSO.json](examples/geologic_unit_la_tojiza_pluton_GSO.json)
- [geologic_unit_lake_holmes_coal_measures_GSO.json](examples/geologic_unit_lake_holmes_coal_measures_GSO.json)
- [geologic_unit_lardeau_group_GSO.json](examples/geologic_unit_lardeau_group_GSO.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicUnitDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### examplegsmGeologicUnitExtensionMinimal
Minimal BeddingDescription instance — no required properties
#### json
```json
{
  "$comment": "Minimal BeddingDescription instance \u2014 no required properties"
}

```


### geologic unit la tojiza pluton GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleLaTojizaPluton.ttl. The source describes the La Tojiza Pluton (intrusive geologic body) with a Cambrian boundary (toj:cambrianBoundaryLaTojiza_2) decomposed into 4 segments. The intruding rock material composition references plutonic constituents; relations to surrounding rocks (gsrl:* properties in TTL) are not encoded here for brevity. Validates as a GeologicUnit feature; lives in gsmGeologicUnitExtension to illustrate Extension-content usage.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleLaTojizaPluton.ttl. The source describes the La Tojiza Pluton (intrusive geologic body) with a Cambrian boundary (toj:cambrianBoundaryLaTojiza_2) decomposed into 4 segments. The intruding rock material composition references plutonic constituents; relations to surrounding rocks (gsrl:* properties in TTL) are not encoded here for brevity. Validates as a GeologicUnit feature; lives in gsmGeologicUnitExtension to illustrate Extension-content usage.",
  "type": "Feature",
  "featureType": "GeologicUnit",
  "id": "https://w3id.org/gso/1.0/ex-plutontojiza#LaTojiza_Pluton",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "name": "La Tojiza Pluton",
    "purpose": "instance",
    "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithodemic_unit",
    "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/intrusion",
    "composition": [
      {
        "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/dominantConstituent",
        "material": {
          "href": "#material-pluton-granitic",
          "title": "Plutonic granitic rock material (Cambrian intrusion)"
        }
      }
    ]
  }
}

```


### geologic unit lake holmes coal measures GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleGeosciAustraliaStratUnit.ttl. The source models Geoscience Australia's Lake Holmes Coal Measures as a gsgu:Formation with a Time_Interval finishing at 27.23 MaY (Late Oligocene). Note: this example file lives in gsmGeologicUnitExtension to illustrate Extension-content usage of GeologicUnit features; the actual validation target is gsmExtendedGeologyCollection (which dispatches featureType=GeologicUnit and requires extension descriptions) or gsmscimlBasic's library schema.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleGeosciAustraliaStratUnit.ttl. The source models Geoscience Australia's Lake Holmes Coal Measures as a gsgu:Formation with a Time_Interval finishing at 27.23 MaY (Late Oligocene). Note: this example file lives in gsmGeologicUnitExtension to illustrate Extension-content usage of GeologicUnit features; the actual validation target is gsmExtendedGeologyCollection (which dispatches featureType=GeologicUnit and requires extension descriptions) or gsmscimlBasic's library schema.",
  "type": "Feature",
  "featureType": "GeologicUnit",
  "id": "http://pid.geoscience.gov.au/feature/asc/gsml/geologicalunit/10056",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "name": "Lake Holmes Coal Measures",
    "purpose": "typicalNorm",
    "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
    "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
    "composition": [
      {
        "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
        "material": {
          "href": "#material-lacustrine-mixed-clastics",
          "title": "Lacustrine red brown and green sand, silt and clay with minor gravel, calcrete and gypsum"
        }
      }
    ]
  }
}

```


### geologic unit lardeau group GSO
Adapted from Loop3D-GSO/Examples/GSO-LardeauGroup.ttl. The source describes the Lardeau Group (Trout Lake area, British Columbia) — a stratigraphic group composed of Ajax fm and Sharon Creek fm (gsrl:stratUnderlies relationships) plus additional formations in the TTL. This example encodes the Group as a top-level GeologicUnit with hierarchyLink references to constituent Formation features (left as href stubs). Source reference: ResearchGate publication 237174271 (structural geology of Lardeau Group near Trout Lake).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-LardeauGroup.ttl. The source describes the Lardeau Group (Trout Lake area, British Columbia) — a stratigraphic group composed of Ajax fm and Sharon Creek fm (gsrl:stratUnderlies relationships) plus additional formations in the TTL. This example encodes the Group as a top-level GeologicUnit with hierarchyLink references to constituent Formation features (left as href stubs). Source reference: ResearchGate publication 237174271 (structural geology of Lardeau Group near Trout Lake).",
  "type": "Feature",
  "featureType": "GeologicUnit",
  "id": "https://w3id.org/gso/1.0/ex-lardeaustrat#Lardeau_Group",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "name": "Lardeau Group",
    "purpose": "typicalNorm",
    "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
    "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
    "hierarchyLink": [
      {
        "role": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "targetUnit": {
          "href": "https://w3id.org/gso/1.0/ex-lardeaustrat#ajaxfm",
          "title": "Ajax Formation (constituent of Lardeau Group)"
        }
      },
      {
        "role": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "targetUnit": {
          "href": "https://w3id.org/gso/1.0/ex-lardeaustrat#sharoncreekfm",
          "title": "Sharon Creek Formation (constituent of Lardeau Group)"
        }
      }
    ]
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmGeologicUnitExtension/gsmGeologicUnitExtensionSchema.json
description: 'GeologicUnit extension: detailed unit description structures

  (GeologicUnitDescription, CompositionPart roles, etc.).'
$defs:
  BeddingDescription:
    $anchor: BeddingDescription
    description: BeddingDescription provides a detailed description of the bedding
      characteristics of a geologic unit.
    type: object
    properties:
      beddingPattern:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: The property beddingPattern (SWE::Category) provides a term from
          a controlled vocabulary specifying patterns of bedding thickness or relationships
          between bedding packages. (e.g., thinning upward, thickening upward).
      beddingStyle:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: The property beddingStyle (SWE::Category) provides a term from
          a controlled vocabulary specifying the style of bedding in a stratified
          geologic unit (e.g. lenticular, irregular, planar, vague, and massive).
      beddingThickness:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
          uniqueItems: true
        description: The property beddingThickness (SWE::Category) provides a term
          from a controlled vocabulary characterizing the thickness of bedding in
          the unit.
  GeologicUnitDescription:
    $anchor: GeologicUnitDescription
    description: GeologicUnitDescription provides for extended description of the
      characteristics of a geologic unit.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicUnitAbstractDescription
      $comment: cross-BB supertype reference to GeologicUnitAbstractDescription in
        BB gsmBasicGeology
    - type: object
      properties:
        bodyMorphology:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: 'The bodyMorphology property (SWE::Category) provides a term
            from a controlled vocabulary describing the geometry or form of a GeologicUnit.
            Examples include: dike (dyke), cone, fan, sheet, etc. The morphology is
            independent of the substance (EarthMaterial) that composes the GeologicUnit
            or process that formed it.'
        unitComposition:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: 'The unitComposition property (SWE::Category) provides a term
            from a composition-based classification that requires summarising the
            overall character of the unit. It is not applicable at the rock material
            or specimen level. Examples are: alkalic, subaluminous, peraluminous,
            I-Type, carbonate, phosphate.'
        outcropCharacter:
          oneOf:
          - type: 'null'
          - type: array
            items:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
            uniqueItems: true
          description: 'The property outcropCharacter (SWE::Category) provides a term
            that describes the nature of outcrops formed by a geologic unit. Examples
            are: bouldery, cliff-forming, ledge-forming, slope-forming, poorly exposed.'
        unitThickness:
          oneOf:
          - type: 'null'
          - $ref: https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json
          description: The property unitThickness (SWE::QuantityRange) provides a
            value that represents the typical thickness of the geologic unit. It is
            always reported as a range.
        bedding:
          oneOf:
          - type: 'null'
          - $ref: '#BeddingDescription'
          description: The bedding:BeddingDescription property reports a description
            of the bedding.
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmGeologicUnitExtension/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmGeologicUnitExtension/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmGeologicUnitExtension/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmGeologicUnitExtension`

