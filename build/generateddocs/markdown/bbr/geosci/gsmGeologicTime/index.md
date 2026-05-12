
# gsmGeologicTime (Schema)

`usgin.bbr.geosci.gsmGeologicTime` *v0.1*

Geologic time, age, and chronostratigraphy: TimeScale, GSSP boundary

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmGeologicTime

GeoSciML 4.1 building block `gsmGeologicTime`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `GeologicTime`, `GSSP`, `TemporalReferenceSystem`, `TimeScale`, `GeologicAgeDetails`.

Contains 4 feature types, 10 data types, 1 code list.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `GeochronologicBoundary` | «DataType» | plain JSON object |
| `GeochronologicEra` | «DataType» | plain JSON object |
| `GeochronologicEraRank` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicEventDescription` | «DataType» | plain JSON object |
| `GeologicTimescale` | «DataType» | plain JSON object |
| `GlobalStratotypePoint` | «FeatureType» | JSON-FG Feature |
| `GlobalStratotypeSection` | «FeatureType» | JSON-FG Feature |
| `NumericEraBoundary` | «DataType» | plain JSON object |
| `StandardGlobalNumericalAge` | «DataType» | plain JSON object |
| `StratigraphicPoint` | «FeatureType» | JSON-FG Feature |
| `StratigraphicSection` | «FeatureType» | JSON-FG Feature |
| `TimeOrdinalEra` | «DataType» | plain JSON object |
| `TimeOrdinalEraBoundary` | «DataType» | plain JSON object |
| `TimeOrdinalReferenceSystem` | «DataType» | plain JSON object |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `GeochronologicBoundary`

A GeochronologicBoundary is a boundary between two geochronologic time periods.

**Supertype**: [`TimeOrdinalEraBoundary`](#TimeOrdinalEraBoundary) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `stratotype` | (oneOf — see schema) | 0..1 | The property stratotype is an association between a GeochronologicBoundary and a StratigraphicPoint that are associat… |

### `GeochronologicEra`

A GeochronologicEra is a period of time between two GeochronologicBoundaries. The association of a GeochronologicEra with a stratotype is optional. In the GSSP approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes are not used. Rather, the association of an era with geologic units and sections is indirect, via the association of an era with boundaries, which are in turn tied to stratotype points, which occur within host stratotype sections.

**Supertype**: [`TimeOrdinalEra`](#TimeOrdinalEra) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `rank` | (oneOf — see schema) | 0..1 | The property rank:GeochronologicEraRank contains a term from a vocabulary describing the rank of the time period (e.g… |
| `stratotype` | (oneOf — see schema) | 0..1 | The property stratotype is an association between a GeochronologicEra and StratigraphicSection that describes a type … |

### `GeologicEventDescription`

GeologicEventDescription provides extended description of geologic events through links to GeochronologicEras in the GeologicTimescale schema.

**Supertype**: `GeologicEventAbstractDescription` (cross-BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `olderGeochronologicEra` | (oneOf — see schema) | 0..1 | Link to description of the GeochronologicEra that corresponds to the older estimated age of a geologic feature. |
| `youngerGeochronologicEra` | (oneOf — see schema) | 0..1 | Link to description of the GeochronologicEra that corresponds to the younger estimated age of a geologic feature. |
| `prototype` | (oneOf — see schema) | 0..1 | Reference stratigraphic point for stratigraphic events |

### `GeologicTimescale`

The classic "Geologic Timescale" (http://www.stratigraphy.org/index.php/ics-chart-timescale) comprising an ordered, hierarchical set of named "eras" is an example of an Ordinal Temporal Reference System. It may be calibrated with reference to a numeric Temporal Coordinate System, but is, in principle, defined independently.  Constraint: Structure association is with GeochronologicEra

**Supertype**: [`TimeOrdinalReferenceSystem`](#TimeOrdinalReferenceSystem) (this BB).

### `GlobalStratotypePoint`

A type of stratigraphic point used to define a globally agreed point in geologic time. This class does not have any properties beyond those inherited from StratigraphicPoint.  Constraint: value(status)=="GSSP"

**Supertype**: [`StratigraphicPoint`](#StratigraphicPoint) (this BB).

### `GlobalStratotypeSection`

A type of stratigraphic section used to define a globally agreed standard period of geologic time  Constraint: value(status)=="GSSP"

**Supertype**: [`StratigraphicSection`](#StratigraphicSection) (this BB).

### `NumericEraBoundary`

NumericEraBoundary is used for pre-Ediacaran and Pleistocene / Holocene boundaries in the standard timescale where boundaries are not defined by a material reference but as numerical values.

**Supertype**: [`TimeOrdinalEraBoundary`](#TimeOrdinalEraBoundary) (this BB).

### `StandardGlobalNumericalAge`

A standard numeric age point (a numeric analogue to a 'golden spike') is applicable to the formal subdivision of the Precambrian, and perhaps the Pleistocene/Holocene boundary ( http://www.stratigraphy.org/index.php/ics-chart-timescale). The boundary is not defined from a physical stratotype, although it can be influence by some, but placed at a convenient numerical value.  Constraint: value(status)=="GSSA"

**Supertype**: [`NumericEraBoundary`](#NumericEraBoundary) (this BB).

### `StratigraphicPoint`

A point in the stratigraphic record used to define a geochronologic boundary or point in geologic time.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `primaryGuidingCriterion` | (oneOf — see schema) | 0..1 | The property primaryGuidingCriterion:Primitive::CharacterString contains a description of the primary criterion used … |
| `additionalCorrelationProperty` | (oneOf — see schema) | 0..1 | The property additionnalCorrelationProperty:Primitive::CharacterString contains any additional criteria used to estab… |
| `status` | (oneOf — see schema) | 0..1 | The property status:Primitive::CharacterString contains a description of the status of stratigraphic point (e.g., for… |

### `StratigraphicSection`

A type of stratigraphic section used to define a globally agreed standard period of geologic time. This class does not have any properties beyond those inherited from StratigraphicSection.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `geologicSetting` | (oneOf — see schema) | 0..1 | The property geologicSetting:Primitive::CharacterString contains a description of the geologic setting of the stratig… |
| `geologicDescription` | (oneOf — see schema) | 0..1 | The geologicDescription:Primitive::CharacterString contains a description of the geology of the stratigraphic section… |
| `accessibility` | (oneOf — see schema) | 0..1 | The property accessibility:Primitive::CharacterString contains a description of the ability to access the stratigraph… |
| `conservation` | (oneOf — see schema) | 0..1 | The property conservation:Primitive::CharacterString contains a description of measures to conserve the stratigraphic… |

### `TimeOrdinalEra`

The association of an era with a stratotype is optional. In the GSSP approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes are not used. Rather, the association of an Era with geologic units and sections is indirect, via the association of an era with Boundaries, which are in turn tied to Stratotype Points, which occur within host Stratotype Sections. Note that the "German School" defines stratigraphic eras conceptually, without reference to stratotypes.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `end` | (oneOf — see schema) | 0..1 | Younger time boundary of an era |
| `start` | (oneOf — see schema) | 0..1 | Older time boundary of an era |
| `member` | (oneOf — see schema) | 0..1 | Subdivisions of TimeOrdinalEra |

### `TimeOrdinalEraBoundary`

A point in Earth's history which bounds a TimeOrdinalEra.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `position` | (oneOf — see schema) | 0..1 | A point in time corresponding to the era boundary |
| `positionalUncertainty` | (oneOf — see schema) | 0..1 | A measure of the uncertainty in the estimate of the point in time of the era boundary |
| `previousEra` | (oneOf — see schema) | 0..1 | Preceding era |
| `observationalBasis` | (oneOf — see schema) | 0..1 | Observation supporting the existence of the boundary (geochronology, paleontology, etc.) |
| `nextEra` | (oneOf — see schema) | 0..1 | Succeeding era |

### `TimeOrdinalReferenceSystem`

A time reference system comprised of an ordered set of time periods (time ordinal eras).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `referencePoint` | (oneOf — see schema) | 2..* | Two reference points defining the extent of the system |
| `component` | (oneOf — see schema) | 0..1 | TimeOrdinalEra composing the TimeOrdinalReferenceSystem |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `GeochronologicEraRank` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../gsmscimlBasic/gsmscimlBasicSchema.json#GeologicEventAbstractDescription`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [examplegsmGeologicTimeMinimal.json](examples/examplegsmGeologicTimeMinimal.json)
- [stratigraphic_section_lower_jurassic_GSO.json](examples/stratigraphic_section_lower_jurassic_GSO.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `GeologicTime`, `GSSP`, `TemporalReferenceSystem`, `TimeScale`, `GeologicAgeDetails`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### examplegsmGeologicTimeMinimal
Example instance: examplegsmGeologicTimeMinimal
#### json
```json
{
  "type": "Feature",
  "id": "globalstratotypepoint.minimal.1",
  "featureType": "GlobalStratotypePoint",
  "geometry": null,
  "properties": {}
}

```


### stratigraphic section lower jurassic GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleEpochLowerJurassic.ttl. The source TTL defines a Series-level chronostratigraphic unit `Lower_Jurassic_Series` (gsgu:Series, hosts gstime:LowerJurassic2012). gsmGeologicTime's dispatchable FTs are stratotype-related (StratigraphicSection, StratigraphicPoint, GlobalStratotypePoint, GlobalStratotypeSection); encoding the Lower Jurassic Series here as a StratigraphicSection whose geologicDescription summarises the Series scope. The link to the ICS time-scale Era is by-reference.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleEpochLowerJurassic.ttl. The source TTL defines a Series-level chronostratigraphic unit `Lower_Jurassic_Series` (gsgu:Series, hosts gstime:LowerJurassic2012). gsmGeologicTime's dispatchable FTs are stratotype-related (StratigraphicSection, StratigraphicPoint, GlobalStratotypePoint, GlobalStratotypeSection); encoding the Lower Jurassic Series here as a StratigraphicSection whose geologicDescription summarises the Series scope. The link to the ICS time-scale Era is by-reference.",
  "type": "Feature",
  "featureType": "StratigraphicSection",
  "id": "https://w3id.org/gso/ex-timelowerjurassic#Lower_Jurassic_Series",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "name": "Lower Jurassic Series (reference section context)",
    "purpose": "typicalNorm",
    "geologicDescription": "Series-level chronostratigraphic unit corresponding to the Lower Jurassic Epoch (gstime:LowerJurassic2012, ICS 2017). The ICS time scale does not define stratotypes for the Geochronologic Eras it defines; this example encodes the host association between the Lower Jurassic rock-based Series and the ICS Epoch.",
    "geologicSetting": "Global lithostratigraphic equivalent of the Lower Jurassic Epoch."
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmGeologicTime/gsmGeologicTimeSchema.json
description: 'Geologic time, age, and chronostratigraphy: TimeScale, GSSP boundary

  points, TemporalReferenceSystem, plus the GeologicAgeDetails extension.


  Validates either a single Feature (dispatched by `featureType` to one of: GlobalStratotypePoint,
  GlobalStratotypeSection, StratigraphicPoint, StratigraphicSection) or a FeatureCollection
  whose `features[]` items are dispatched the same way.'
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
            const: GlobalStratotypePoint
      then:
        $ref: '#GlobalStratotypePoint'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GlobalStratotypeSection
      then:
        $ref: '#GlobalStratotypeSection'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: StratigraphicPoint
      then:
        $ref: '#StratigraphicPoint'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: StratigraphicSection
      then:
        $ref: '#StratigraphicSection'
    - if:
        not:
          required:
          - featureType
          properties:
            featureType:
              enum:
              - GlobalStratotypePoint
              - GlobalStratotypeSection
              - StratigraphicPoint
              - StratigraphicSection
      then: false
  GeochronologicBoundary:
    $anchor: GeochronologicBoundary
    description: A GeochronologicBoundary is a boundary between two geochronologic
      time periods.
    allOf:
    - $ref: '#TimeOrdinalEraBoundary'
    - type: object
      properties:
        stratotype:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to StratigraphicPoint
            - $ref: '#StratigraphicPoint'
          description: The property stratotype is an association between a GeochronologicBoundary
            and a StratigraphicPoint that are associated with the boundary. A GeochronologicBoundary
            can be associated with more than one StratigraphicPoints, but only one
            may have GSSP ratified status. The others are proposed equivalents.
  GeochronologicEra:
    $anchor: GeochronologicEra
    description: A GeochronologicEra is a period of time between two GeochronologicBoundaries.
      The association of a GeochronologicEra with a stratotype is optional. In the
      GSSP approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes
      are not used. Rather, the association of an era with geologic units and sections
      is indirect, via the association of an era with boundaries, which are in turn
      tied to stratotype points, which occur within host stratotype sections.
    allOf:
    - $ref: '#TimeOrdinalEra'
    - type: object
      properties:
        rank:
          oneOf:
          - type: 'null'
          - $ref: '#GeochronologicEraRank'
          description: The property rank:GeochronologicEraRank contains a term from
            a vocabulary describing the rank of the time period (e.g., eon, era, period,
            stage).
        stratotype:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to StratigraphicSection
            - $ref: '#StratigraphicSection'
          description: The property stratotype is an association between a GeochronologicEra
            and StratigraphicSection that describes a type section that names the
            physical location or outcrop of a particular reference exposure of a stratigraphic
            sequence or stratigraphic boundary. A unit stratotype is the agreed reference
            point for a particular stratigraphic unit and a boundary stratotype is
            the reference for a particular boundary between strata (Wikipedia).
  GeochronologicEraRank:
    $anchor: GeochronologicEraRank
    description: 'This list is an indicative list only of terms used to describe the
      rank of time periods defined by the International Commission on Stratigraphy.
      Users are encouraged to use vocabulary of terms owned by the ICS or CGI vocabularies
      working group and managed outside of this model. For example: eon era period
      epoch age'
    type: string
    format: uri
  GeologicEventDescription:
    $anchor: GeologicEventDescription
    description: GeologicEventDescription provides extended description of geologic
      events through links to GeochronologicEras in the GeologicTimescale schema.
    allOf:
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#GeologicEventAbstractDescription
      $comment: cross-BB supertype reference to GeologicEventAbstractDescription in
        BB gsmscimlBasic
    - type: object
      properties:
        olderGeochronologicEra:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to GeochronologicEra
            - $ref: '#GeochronologicEra'
          description: Link to description of the GeochronologicEra that corresponds
            to the older estimated age of a geologic feature.
        youngerGeochronologicEra:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to GeochronologicEra
            - $ref: '#GeochronologicEra'
          description: Link to description of the GeochronologicEra that corresponds
            to the younger estimated age of a geologic feature.
        prototype:
          oneOf:
          - type: 'null'
          - oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to StratigraphicPoint
            - $ref: '#StratigraphicPoint'
          description: Reference stratigraphic point for stratigraphic events
  GeologicTimescale:
    $anchor: GeologicTimescale
    description: 'The classic "Geologic Timescale" (http://www.stratigraphy.org/index.php/ics-chart-timescale)
      comprising an ordered, hierarchical set of named "eras" is an example of an
      Ordinal Temporal Reference System. It may be calibrated with reference to a
      numeric Temporal Coordinate System, but is, in principle, defined independently.  Constraint:
      Structure association is with GeochronologicEra'
    allOf:
    - $ref: '#TimeOrdinalReferenceSystem'
    - type: object
  GlobalStratotypePoint:
    $anchor: GlobalStratotypePoint
    description: 'A type of stratigraphic point used to define a globally agreed point
      in geologic time. This class does not have any properties beyond those inherited
      from StratigraphicPoint.  Constraint: value(status)=="GSSP"'
    allOf:
    - $ref: '#StratigraphicPoint'
    - type: object
      properties:
        properties:
          type: object
          properties: {}
  GlobalStratotypeSection:
    $anchor: GlobalStratotypeSection
    description: 'A type of stratigraphic section used to define a globally agreed
      standard period of geologic time  Constraint: value(status)=="GSSP"'
    allOf:
    - $ref: '#StratigraphicSection'
    - type: object
      properties:
        properties:
          type: object
          properties: {}
  NumericEraBoundary:
    $anchor: NumericEraBoundary
    description: NumericEraBoundary is used for pre-Ediacaran and Pleistocene / Holocene
      boundaries in the standard timescale where boundaries are not defined by a material
      reference but as numerical values.
    allOf:
    - $ref: '#TimeOrdinalEraBoundary'
    - type: object
  StandardGlobalNumericalAge:
    $anchor: StandardGlobalNumericalAge
    description: 'A standard numeric age point (a numeric analogue to a ''golden spike'')
      is applicable to the formal subdivision of the Precambrian, and perhaps the
      Pleistocene/Holocene boundary ( http://www.stratigraphy.org/index.php/ics-chart-timescale).
      The boundary is not defined from a physical stratotype, although it can be influence
      by some, but placed at a convenient numerical value.  Constraint: value(status)=="GSSA"'
    allOf:
    - $ref: '#NumericEraBoundary'
    - type: object
  StratigraphicPoint:
    $anchor: StratigraphicPoint
    description: A point in the stratigraphic record used to define a geochronologic
      boundary or point in geologic time.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            primaryGuidingCriterion:
              oneOf:
              - type: 'null'
              - type: string
              description: The property primaryGuidingCriterion:Primitive::CharacterString
                contains a description of the primary criterion used to establish
                the stratigraphic point.
            additionalCorrelationProperty:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  type: string
                uniqueItems: true
              description: The property additionnalCorrelationProperty:Primitive::CharacterString
                contains any additional criteria used to establish the stratigraphic
                point.
            status:
              oneOf:
              - type: 'null'
              - type: string
              description: The property status:Primitive::CharacterString contains
                a description of the status of stratigraphic point (e.g., formally
                accepted, etc.).
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  StratigraphicSection:
    $anchor: StratigraphicSection
    description: A type of stratigraphic section used to define a globally agreed
      standard period of geologic time. This class does not have any properties beyond
      those inherited from StratigraphicSection.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            geologicSetting:
              oneOf:
              - type: 'null'
              - type: string
              description: The property geologicSetting:Primitive::CharacterString
                contains a description of the geologic setting of the stratigraphic
                section.
            geologicDescription:
              oneOf:
              - type: 'null'
              - type: string
              description: The geologicDescription:Primitive::CharacterString contains
                a description of the geology of the stratigraphic section (e.g., lithology,
                paleontology, paleogeography, etc.).
            accessibility:
              oneOf:
              - type: 'null'
              - type: string
              description: The property accessibility:Primitive::CharacterString contains
                a description of the ability to access the stratigraphic section.
            conservation:
              oneOf:
              - type: 'null'
              - type: string
              description: The property conservation:Primitive::CharacterString contains
                a description of measures to conserve the stratigraphic section.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  TimeOrdinalEra:
    $anchor: TimeOrdinalEra
    description: The association of an era with a stratotype is optional. In the GSSP
      approach recommended by ICS for the Global Geologic Timescale, Unit Stratotypes
      are not used. Rather, the association of an Era with geologic units and sections
      is indirect, via the association of an era with Boundaries, which are in turn
      tied to Stratotype Points, which occur within host Stratotype Sections. Note
      that the "German School" defines stratigraphic eras conceptually, without reference
      to stratotypes.
    type: object
    properties:
      end:
        oneOf:
        - type: 'null'
        - oneOf:
          - $ref: '#/$defs/SCLinkObject'
            $comment: by-reference link to TimeOrdinalEraBoundary
          - $ref: '#TimeOrdinalEraBoundary'
        description: Younger time boundary of an era
      start:
        oneOf:
        - type: 'null'
        - oneOf:
          - $ref: '#/$defs/SCLinkObject'
            $comment: by-reference link to TimeOrdinalEraBoundary
          - $ref: '#TimeOrdinalEraBoundary'
        description: Older time boundary of an era
      member:
        oneOf:
        - type: 'null'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to TimeOrdinalEra
            - $ref: '#TimeOrdinalEra'
          uniqueItems: true
        description: Subdivisions of TimeOrdinalEra
  TimeOrdinalEraBoundary:
    $anchor: TimeOrdinalEraBoundary
    description: A point in Earth's history which bounds a TimeOrdinalEra.
    type: object
    properties:
      position:
        oneOf:
        - type: 'null'
        - $ref: '#/$defs/SCLinkObject'
          $comment: "External ISO 19108 TM_Instant \u2014 by-reference link"
        description: A point in time corresponding to the era boundary
      positionalUncertainty:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: A measure of the uncertainty in the estimate of the point in
          time of the era boundary
      previousEra:
        oneOf:
        - type: 'null'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to TimeOrdinalEra
            - $ref: '#TimeOrdinalEra'
          uniqueItems: true
        description: Preceding era
      observationalBasis:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: '#/$defs/SCLinkObject'
            $comment: "External ISO 19156 OM_Observation \u2014 by-reference link"
          uniqueItems: true
        description: Observation supporting the existence of the boundary (geochronology,
          paleontology, etc.)
      nextEra:
        oneOf:
        - type: 'null'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to TimeOrdinalEra
            - $ref: '#TimeOrdinalEra'
          uniqueItems: true
        description: Succeeding era
  TimeOrdinalReferenceSystem:
    $anchor: TimeOrdinalReferenceSystem
    description: A time reference system comprised of an ordered set of time periods
      (time ordinal eras).
    type: object
    properties:
      referencePoint:
        type: array
        minItems: 2
        items:
          oneOf:
          - $ref: '#/$defs/SCLinkObject'
            $comment: by-reference link to TimeOrdinalEraBoundary
          - $ref: '#TimeOrdinalEraBoundary'
        uniqueItems: true
        description: Two reference points defining the extent of the system
      component:
        oneOf:
        - type: 'null'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/SCLinkObject'
              $comment: by-reference link to TimeOrdinalEra
            - $ref: '#TimeOrdinalEra'
          uniqueItems: true
        description: TimeOrdinalEra composing the TimeOrdinalReferenceSystem
    required:
    - referencePoint
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmGeologicTime/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmGeologicTime/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](/github/workspace/_sources/gsmGeologicTime/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmGeologicTime`

