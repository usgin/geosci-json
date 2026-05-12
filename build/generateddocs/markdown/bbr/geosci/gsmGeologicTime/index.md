
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

A point in geologic time defined by a stratotype. Aligns to time:Instant from W3C OWL-Time (https://www.w3.org/TR/owl-time/). Cox & Richard 2015, 'A formal model for the geologic timescale and GSSP': the boundary's instant is anchored to the rock record via the `stratotype` property, which references a StratigraphicPoint (typically a GSSP if ratified by ICS).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `stratotype` | (oneOf — see schema) | 0..1 | The StratigraphicPoint that defines this boundary in the rock record. Inline Feature or by-reference SCLinkObject. |

### `GeochronologicEra`

A named interval of geologic time (Eon, Era, Period, Epoch, Age, biozone, etc.). Aligns to time:ProperInterval from W3C OWL-Time (https://www.w3.org/TR/owl-time/). Cox & Richard 2015, 'A formal model for the geologic timescale and GSSP': `start` / `end` map to time:hasBeginning / time:hasEnd (both linking to GeochronologicBoundary ≡ time:Instant); `member[]` expresses sub-era containment (Allen time:intervalContains). The optional `stratotype` anchors the era to a defining rock section.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `rank` | `string(uri)` | 0..1 | Chronostratigraphic / geochronologic rank (URI from the ICS chart vocabulary or equivalent: Eon, Era, Period, Epoch, … |
| `start` | (oneOf — see schema) | 0..1 | Lower boundary of this era (time:hasBeginning). Inline GeochronologicBoundary Feature or by-reference SCLinkObject. |
| `end` | (oneOf — see schema) | 0..1 | Upper boundary of this era (time:hasEnd). Inline GeochronologicBoundary Feature or by-reference SCLinkObject. |
| `member` | (oneOf — see schema) | 0..1 | Sub-eras contained within this era (time:intervalContains). Array of by-reference links or inline GeochronologicEra F… |
| `stratotype` | (oneOf — see schema) | 0..1 | Defining stratigraphic section for this era (the rock-record anchor). Inline StratigraphicSection Feature or by-refer… |

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

- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEventAbstractDescription`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [examplegsmGeologicTimeMinimal.json](examples/examplegsmGeologicTimeMinimal.json)
- [geochronologic_boundary_simple.json](examples/geochronologic_boundary_simple.json)
- [geochronologic_era_complex.json](examples/geochronologic_era_complex.json)
- [geochronologic_era_lower_jurassic_GSO.json](examples/geochronologic_era_lower_jurassic_GSO.json)
- [geochronologic_era_simple.json](examples/geochronologic_era_simple.json)

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


### geochronologic boundary simple
Example instance: geochronologic_boundary_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "GeochronologicBoundary",
  "id": "ics-base-cambrian",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "stratotype": {
      "type": "Feature",
      "featureType": "StratigraphicPoint",
      "id": "ics-base-cambrian-gssp",
      "geometry": {"type": "Point", "coordinates": [117.0, 31.0]},
      "place": null,
      "time": null,
      "properties": {
        "primaryGuidingCriterion": "First appearance datum of trace fossil Treptichnus pedum",
        "status": "ratified GSSP"
      }
    }
  }
}

```


### geochronologic era complex
Example instance: geochronologic_era_complex
#### json
```json
{
  "type": "Feature",
  "featureType": "GeochronologicEra",
  "id": "arizona-zappodachus-zone",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "rank": "http://resource.geosciml.org/classifier/ics/ischart/biozone",
    "start": {
      "href": "http://resource.geosciml.org/classifier/ics/ischart/BaseMesoproterozoic",
      "title": "base of Mesoproterozoic"
    },
    "end": {
      "type": "Feature",
      "featureType": "GeochronologicBoundary",
      "id": "beckers-butte-tuff-boundary",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "stratotype": {
          "type": "Feature",
          "featureType": "StratigraphicPoint",
          "id": "beckers-butte-tuff-point",
          "geometry": null,
          "place": null,
          "time": null,
          "properties": {
            "primaryGuidingCriterion": "eruption of Beckers Butte Tuff, a thin widespread marker assumed to be synchronously deposited across the region",
            "status": "proposed"
          }
        }
      }
    },
    "member": [
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Neoproterozoic", "title": "Neoproterozoic"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Mesoproterozoic", "title": "Mesoproterozoic"}
    ],
    "stratotype": {
      "href": "http://resource.usgs.gov/stratigraphicSection/347378",
      "title": "Theodore Roosevelt Dam Section, Arizona"
    }
  }
}

```


### geochronologic era lower jurassic GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleEpochLowerJurassic.ttl. The source TTL describes a chronostratigraphic Series (`Lower_Jurassic_Series`, gsgu:Series) that `gsoc:hosts gstime:LowerJurassic2012` — the time-side ICS Epoch. Encoded here as a GeochronologicEra (≡ time:ProperInterval per OWL-Time / Cox & Richard 2015) representing the Lower Jurassic Epoch. The Epoch is bounded by the base-of-Hettangian GSSP (= base of Jurassic, ratified at Kuhjoch, Austria) and the base-of-Bajocian (the top of Toarcian / base of Middle Jurassic). The Series rock unit from the TTL is referenced via `stratotype`. As the TTL notes, the ICS time scale does not formally define stratotypes for its Geochronologic Eras; the stratotype here is the GeoSciML-side rock-unit anchor.
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleEpochLowerJurassic.ttl. The source TTL describes a chronostratigraphic Series (`Lower_Jurassic_Series`, gsgu:Series) that `gsoc:hosts gstime:LowerJurassic2012` — the time-side ICS Epoch. Encoded here as a GeochronologicEra (≡ time:ProperInterval per OWL-Time / Cox & Richard 2015) representing the Lower Jurassic Epoch. The Epoch is bounded by the base-of-Hettangian GSSP (= base of Jurassic, ratified at Kuhjoch, Austria) and the base-of-Bajocian (the top of Toarcian / base of Middle Jurassic). The Series rock unit from the TTL is referenced via `stratotype`. As the TTL notes, the ICS time scale does not formally define stratotypes for its Geochronologic Eras; the stratotype here is the GeoSciML-side rock-unit anchor.",
  "type": "Feature",
  "featureType": "GeochronologicEra",
  "id": "http://resource.geosciml.org/classifier/ics/ischart/LowerJurassic",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "rank": "http://resource.geosciml.org/classifier/ics/ischart/Epoch",
    "start": {
      "href": "http://resource.geosciml.org/classifier/ics/ischart/BaseJurassic",
      "rel": "time:hasBeginning",
      "title": "Base of Jurassic (= base of Hettangian; ratified GSSP at Kuhjoch, Austria)"
    },
    "end": {
      "href": "http://resource.geosciml.org/classifier/ics/ischart/BaseBajocian",
      "rel": "time:hasEnd",
      "title": "Base of Bajocian (= top of Toarcian, beginning of Middle Jurassic)"
    },
    "member": [
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Hettangian",   "title": "Hettangian Age"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Sinemurian",   "title": "Sinemurian Age"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Pliensbachian","title": "Pliensbachian Age"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Toarcian",     "title": "Toarcian Age"}
    ],
    "stratotype": {
      "href": "https://w3id.org/gso/ex-timelowerjurassic#Lower_Jurassic_Series",
      "rel": "isHostedBy",
      "title": "Lower_Jurassic_Series (chronostratigraphic Series; the rock-record host of this Epoch per gsoc:hosts in the source TTL)"
    }
  }
}

```


### geochronologic era simple
Example instance: geochronologic_era_simple
#### json
```json
{
  "type": "Feature",
  "featureType": "GeochronologicEra",
  "id": "ics-devonian",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "rank": "http://resource.geosciml.org/classifier/ics/ischart/Period",
    "start": {
      "href": "http://resource.geosciml.org/classifier/ics/ischart/BaseDevonian",
      "title": "base of Devonian"
    },
    "end": {
      "href": "http://resource.geosciml.org/classifier/ics/ischart/BaseDevonianTop",
      "title": "top of Devonian"
    },
    "member": [
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Lochkovian", "title": "Lochkovian"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Pragian",    "title": "Pragian"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Emsian",     "title": "Emsian"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Eifelian",   "title": "Eifelian"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Givetian",   "title": "Givetian"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",   "title": "Frasnian"},
      {"href": "http://resource.geosciml.org/classifier/ics/ischart/Famennian",  "title": "Famennian"}
    ]
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmGeologicTime/gsmGeologicTimeSchema.json
description: "Geologic time, age, and chronostratigraphy: TimeScale, GSSP boundary\npoints,
  TemporalReferenceSystem, plus the GeologicAgeDetails extension\n(which contributes
  GeologicEventDescription, the concrete description\nclass used by GeologicEvent.gaEventDescription).
  The dispatcher\nadditionally exposes two hand-curated featureTypes \u2014\nGeochronologicEra
  and GeochronologicBoundary \u2014 that align to W3C\nOWL-Time (https://www.w3.org/TR/owl-time/)
  per Cox & Richard 2015\n\"A formal model for the geologic timescale and GSSP\":
  Era \u2261\ntime:ProperInterval and Boundary \u2261 time:Instant, with start/end\nmapping
  to time:hasBeginning/time:hasEnd and member to\ntime:intervalContains. Both reference
  the existing XMI-derived\nStratigraphicPoint / StratigraphicSection anchors for
  the\nrock-record link.\n\nValidates either a single Feature (dispatched by `featureType`
  to one of: GeochronologicEra, GeochronologicBoundary, GlobalStratotypePoint, GlobalStratotypeSection,
  StratigraphicPoint, StratigraphicSection) or a FeatureCollection whose `features[]`
  items are dispatched the same way."
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
            const: GeochronologicEra
      then:
        $ref: '#GeochronologicEra'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: GeochronologicBoundary
      then:
        $ref: '#GeochronologicBoundary'
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
              - GeochronologicEra
              - GeochronologicBoundary
              - GlobalStratotypePoint
              - GlobalStratotypeSection
              - StratigraphicPoint
              - StratigraphicSection
      then: false
  GeochronologicBoundary:
    $anchor: GeochronologicBoundary
    description: 'A point in geologic time defined by a stratotype. Aligns to time:Instant
      from W3C OWL-Time (https://www.w3.org/TR/owl-time/). Cox & Richard 2015, ''A
      formal model for the geologic timescale and GSSP'': the boundary''s instant
      is anchored to the rock record via the `stratotype` property, which references
      a StratigraphicPoint (typically a GSSP if ratified by ICS).'
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            stratotype:
              description: The StratigraphicPoint that defines this boundary in the
                rock record. Inline Feature or by-reference SCLinkObject.
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
              - $ref: '#StratigraphicPoint'
          required:
          - stratotype
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeochronologicEra:
    $anchor: GeochronologicEra
    description: "A named interval of geologic time (Eon, Era, Period, Epoch, Age,
      biozone, etc.). Aligns to time:ProperInterval from W3C OWL-Time (https://www.w3.org/TR/owl-time/).
      Cox & Richard 2015, 'A formal model for the geologic timescale and GSSP': `start`
      / `end` map to time:hasBeginning / time:hasEnd (both linking to GeochronologicBoundary
      \u2261 time:Instant); `member[]` expresses sub-era containment (Allen time:intervalContains).
      The optional `stratotype` anchors the era to a defining rock section."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            rank:
              type: string
              format: uri
              description: 'Chronostratigraphic / geochronologic rank (URI from the
                ICS chart vocabulary or equivalent: Eon, Era, Period, Epoch, Age,
                biozone, etc.).'
            start:
              description: Lower boundary of this era (time:hasBeginning). Inline
                GeochronologicBoundary Feature or by-reference SCLinkObject.
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
              - $ref: '#GeochronologicBoundary'
            end:
              description: Upper boundary of this era (time:hasEnd). Inline GeochronologicBoundary
                Feature or by-reference SCLinkObject.
              oneOf:
              - $ref: '#/$defs/SCLinkObject'
              - $ref: '#GeochronologicBoundary'
            member:
              description: Sub-eras contained within this era (time:intervalContains).
                Array of by-reference links or inline GeochronologicEra Features.
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                  - $ref: '#GeochronologicEra'
                uniqueItems: true
            stratotype:
              description: Defining stratigraphic section for this era (the rock-record
                anchor). Inline StratigraphicSection Feature or by-reference SCLinkObject.
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
              - $ref: '#StratigraphicSection'
          required:
          - rank
          - start
          - end
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
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
    - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEventAbstractDescription
      $comment: cross-BB supertype reference to GeologicEventAbstractDescription in
        BB gsmBasicGeology
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

