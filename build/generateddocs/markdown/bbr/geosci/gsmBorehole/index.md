
# gsmBorehole (Schema)

`usgin.bbr.geosci.gsmBorehole` *v0.1*

Borehole feature type and supporting types (BoreholeDetails, intervals,

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmBorehole

GeoSciML 4.1 building block `gsmBorehole`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `Borehole`.

Contains 3 feature types, 2 data types, 4 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `Borehole` | «FeatureType» | JSON-FG Feature |
| `BoreholeDetails` | «DataType» | plain JSON object |
| `BoreholeDrillingMethodCode` | «CodeList» | URI codelist (`format: uri`) |
| `BoreholeInclinationCode` | «CodeList» | URI codelist (`format: uri`) |
| `BoreholeInterval` | «FeatureType» | JSON-FG Feature |
| `BoreholePurposeCode` | «CodeList» | URI codelist (`format: uri`) |
| `BoreholeStartPointCode` | «CodeList» | URI codelist (`format: uri`) |
| `DrillingDetails` | «DataType» | plain JSON object |
| `OriginPosition` | «FeatureType» | JSON-FG Feature |

## Class details

### `Borehole`

A Borehole is the generalized term for any narrow shaft drilled in the ground, either vertically, horizontally, or inclined.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `logElement` | (oneOf — see schema) | 0..1 | The property logElement is an association between a Borehole and a BoreholeInterval instance to describe measured dow… |
| `downholeDrillingDetails` | (oneOf — see schema) | 0..1 | The property downholeDrillingDetails:DrillingDetails specifies the drilling method and borehole diameter for interval… |
| `referenceLocation` | (oneOf — see schema) | 0..1 | The property referenceLocation is an association between a Borehole and an OriginPosition corresponding to the start … |
| `indexData` | (oneOf — see schema) | 0..1 | The property indexData:BoreholeDetails describes metadata about a borehole, such as the operator, the custodian, date… |

### `BoreholeDetails`

BoreholeDetails describes borehole-specific index data, often termed “header information”. It contains metadata about the parties involved in the drilling, the storage of drilled material and other information relevant to the borehole as a whole. Properties that may vary along the borehole path are managed in DrillingDetails

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `operator` | (oneOf — see schema) | 0..1 | The operator property is an association between a BoreholeDetails and a CIT:CI_ResponsibleParty describing the organi… |
| `driller` | (oneOf — see schema) | 0..1 | The driller property is an association between a BoreholeDetails and a CIT:CI_ResponsibleParty describing of the orga… |
| `dateOfDrilling` | (oneOf — see schema) | 0..1 | The property dateOfDrilling:TM_Period describes the time period during which drilling of the borehole occurred. |
| `startPoint` | (oneOf — see schema) | 0..1 | The property startPoint:BoreholeStartPointCode provides a term from a controlled vocabulary indicating the named posi… |
| `inclinationType` | (oneOf — see schema) | 0..1 | The property inclinationType:BoreholeInclinationCode contains a term from a controlled vocabulary indicating the incl… |
| `boreholeMaterialCustodian` | (oneOf — see schema) | 0..1 | The property boreholeMaterialCustodian is an association between BoreholeDetails and a CIT:CI_ResponsibleParty descri… |
| `purpose` | (oneOf — see schema) | 0..1 | The property purpose:BoreholePurposeCode contains a term from a controlled vocabulary describing the purpose for whic… |
| `dataCustodian` | (oneOf — see schema) | 0..1 | The dataCustodian is an association between a BoreholeDetails and a CIT:CI_ResponsibleParty describing the custodian … |
| `boreholeLength` | (oneOf — see schema) | 0..1 | The property boreholeLength (SWE::Quantity) contains a measurement (a value and a unit of measurement) corresponding … |

### `BoreholeInterval`

A BoreholeInterval is similar to a MappedFeature whose shape is 1-D interval and uses the SRS of the containing borehole. The "mappedIntervalBegin" and "mappedIntervalEnd" properties are alternative to the 1D geometry to overcome problems with the delivery and ease of queryability of 1D GML shapes.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `observationMethod` | (oneOf — see schema) | 0..1 | The observationMethod property (SWE::Category) contains a term from a controlled vocabulary that describes the method… |
| `specification` | (oneOf — see schema) | 0..1 | The specification property is an association between a BoreholeInterval and a GFI_Feature, a domain feature that is s… |
| `mappedIntervalBegin` | (oneOf — see schema) | 0..1 | The property mappedIntervalBegin (SWE::Quantity) is a measurement (a value and a unit of measurement) corresponding t… |
| `mappedIntervalEnd` | (oneOf — see schema) | 0..1 | The mappedIntervalEnd property (SWE::Quantity) is a measurement (a value and a unit of measure) corresponding to the … |
| `collectionIdentifier` | (oneOf — see schema) | 0..1 | The collectionIdentifier:ScopedName is a string unique within a scope that identifies a collection which forms a set … |
| `shape` | (oneOf — see schema) | 0..1 | The property shape:GM_Object is a 1-D interval (e.g., a "from" and "to", or "top" and "base" measurement) covering th… |
| `parentBorehole` | (oneOf — see schema) | 0..1 | The property parentBorehole is an association between a BoreholeInterval and a Borehole to which the interval belongs. |

### `DrillingDetails`

DrillingDetails is a class that captures the description of drilling methods and hole diameters down the drilling path. Properties that apply to the Borehole as a whole are managed in BoreholeDetails.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `drillingMethod` | (oneOf — see schema) | 0..1 | The drillingMethod:BoreholeDrillingMethodCode property contains a term from a controlled vocabulary indicating the dr… |
| `boreholeDiameter` | (oneOf — see schema) | 0..1 | The boreholeDiameter property (SWE::Quantity) contains a measurement (a value and a unit of measure) corresponding to… |
| `intervalBegin` | (oneOf — see schema) | 0..1 | The intervalBegin property (SWE::Quantity) contains a measurement (a value and a unit of measurement) that correspond… |
| `intervalEnd` | (oneOf — see schema) | 0..1 | The property intervalEnd (SWE::Quantity) contains a measurement (a value and a unit of measurement) of the measured d… |

### `OriginPosition`

A borehole OriginPosition is a feature corresponding to the start point of a borehole log. This may correspond to the borehole collar location (e.g., kelly bush).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `location` | (oneOf — see schema) | 0..1 | The property location contains a geometry corresponding to the location of the borehole collar. |
| `elevation` | (oneOf — see schema) | 0..1 | The elevation:DirectPosition property is a compromise approach to supply elevation explicitly for location; this is t… |
| `relatedBorehole` | (oneOf — see schema) | 0..1 | The hole that has this collar for its start point |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `BoreholeDrillingMethodCode` | `_(treat as open — no `codeList` annotation)_` |
| `BoreholeInclinationCode` | `_(treat as open — no `codeList` annotation)_` |
| `BoreholePurposeCode` | `_(treat as open — no `codeList` annotation)_` |
| `BoreholeStartPointCode` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.json`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.json`
- `https://geojson.org/schema/Geometry.json`
- `https://geojson.org/schema/Point.json`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [examplegsmBoreholeMinimal.json](examples/examplegsmBoreholeMinimal.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `Borehole`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### examplegsmBoreholeMinimal
Example instance: examplegsmBoreholeMinimal
#### json
```json
{
  "type": "Feature",
  "id": "borehole.minimal.1",
  "featureType": "Borehole",
  "geometry": null,
  "properties": {}
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmBorehole/gsmBoreholeSchema.json
description: 'Borehole feature type and supporting types (BoreholeDetails, intervals,

  collar, log, drilling method).'
$defs:
  Borehole:
    $anchor: Borehole
    description: A Borehole is the generalized term for any narrow shaft drilled in
      the ground, either vertically, horizontally, or inclined.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            logElement:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to BoreholeInterval
                  - $ref: '#BoreholeInterval'
                uniqueItems: true
              description: The property logElement is an association between a Borehole
                and a BoreholeInterval instance to describe measured downhole intervals
                and their observed features.
            downholeDrillingDetails:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#DrillingDetails'
                uniqueItems: true
              description: The property downholeDrillingDetails:DrillingDetails specifies
                the drilling method and borehole diameter for intervals down the borehole.
            referenceLocation:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to OriginPosition
                - $ref: '#OriginPosition'
              description: The property referenceLocation is an association between
                a Borehole and an OriginPosition corresponding to the start point
                of a borehole log. This may correspond to the borehole collar location
                (e.g., kelly bush).
            indexData:
              oneOf:
              - type: 'null'
              - $ref: '#BoreholeDetails'
              description: The property indexData:BoreholeDetails describes metadata
                about a borehole, such as the operator, the custodian, dates of drilling,
                etc.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  BoreholeDetails:
    $anchor: BoreholeDetails
    description: "BoreholeDetails describes borehole-specific index data, often termed
      \u201Cheader information\u201D. It contains metadata about the parties involved
      in the drilling, the storage of drilled material and other information relevant
      to the borehole as a whole. Properties that may vary along the borehole path
      are managed in DrillingDetails"
    type: object
    properties:
      operator:
        oneOf:
        - type: 'null'
        - anyOf:
          - $ref: '#/$defs/SCLinkObject'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
          $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference link
            or inline CDIF agentInRole"
        description: The operator property is an association between a BoreholeDetails
          and a CIT:CI_ResponsibleParty describing the organisation responsible for
          commissioning the borehole (as opposed to actually drilling the borehole).
      driller:
        oneOf:
        - type: 'null'
        - anyOf:
          - $ref: '#/$defs/SCLinkObject'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
          $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference link
            or inline CDIF agentInRole"
        description: The driller property is an association between a BoreholeDetails
          and a CIT:CI_ResponsibleParty describing of the organisation responsible
          for drilling the borehole (as opposed to commissioning the borehole).
      dateOfDrilling:
        oneOf:
        - type: 'null'
        - $ref: '#/$defs/SCLinkObject'
          $comment: "External ISO 19108 TM_Period \u2014 by-reference link"
        description: The property dateOfDrilling:TM_Period describes the time period
          during which drilling of the borehole occurred.
      startPoint:
        oneOf:
        - type: 'null'
        - $ref: '#BoreholeStartPointCode'
        description: The property startPoint:BoreholeStartPointCode provides a term
          from a controlled vocabulary indicating the named position relative to ground
          surface where the borehole commenced. (e.g., natural ground surface, open
          pit floor, underground, offshore)
      inclinationType:
        oneOf:
        - type: 'null'
        - $ref: '#BoreholeInclinationCode'
        description: The property inclinationType:BoreholeInclinationCode contains
          a term from a controlled vocabulary indicating the inclination type of the
          borehole. Appropriate terms would include vertical; inclined up; inclined
          down, horizontal.
      boreholeMaterialCustodian:
        oneOf:
        - type: 'null'
        - type: array
          items:
            anyOf:
            - $ref: '#/$defs/SCLinkObject'
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
            $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference link
              or inline CDIF agentInRole"
          uniqueItems: true
        description: The property boreholeMaterialCustodian is an association between
          BoreholeDetails and a CIT:CI_ResponsibleParty describing the organisation
          that is custodian of the drilled material recovered from the borehole.
      purpose:
        oneOf:
        - type: 'null'
        - type: array
          items:
            $ref: '#BoreholePurposeCode'
          uniqueItems: true
        description: The property purpose:BoreholePurposeCode contains a term from
          a controlled vocabulary describing the purpose for which the borehole was
          drilled. e.g., site investigation, mineral exploration, hydrocarbon exploration,
          water resources.
      dataCustodian:
        oneOf:
        - type: 'null'
        - type: array
          items:
            anyOf:
            - $ref: '#/$defs/SCLinkObject'
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
            $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference link
              or inline CDIF agentInRole"
          uniqueItems: true
        description: The dataCustodian is an association between a BoreholeDetails
          and a CIT:CI_ResponsibleParty describing the custodian (person or organisation)
          that is the custodian of data pertaining to this borehole.
      boreholeLength:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The property boreholeLength (SWE::Quantity) contains a measurement
          (a value and a unit of measurement) corresponding to the "length" of a borehole
          determined by the data provider (i.e., "length" can have different sources,
          like drillers measurement, loggers measurement, survey measurement, etc.).
  BoreholeDrillingMethodCode:
    $anchor: BoreholeDrillingMethodCode
    description: This class is an indicative placeholder only for a vocabulary of
      terms describing the borehole drilling method. Users are encouraged to use a
      vocabulary of terms managed by the CGI vocabularies working group. (eg; auger,
      hand auger, air core, cable tool, diamond core, rotary air blast, etc)
    type: string
    format: uri
  BoreholeInclinationCode:
    $anchor: BoreholeInclinationCode
    description: 'This class is an indicative placeholder only for a vocabulary of
      terms describing the general orientation of a borehole. Users are encouraged
      to use a vocabulary of terms managed by the CGI vocabularies working group.
      For example: vertical horizontal inclined up inclined down'
    type: string
    format: uri
  BoreholeInterval:
    $anchor: BoreholeInterval
    description: A BoreholeInterval is similar to a MappedFeature whose shape is 1-D
      interval and uses the SRS of the containing borehole. The "mappedIntervalBegin"
      and "mappedIntervalEnd" properties are alternative to the 1D geometry to overcome
      problems with the delivery and ease of queryability of 1D GML shapes.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            observationMethod:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
                uniqueItems: true
              description: The observationMethod property (SWE::Category) contains
                a term from a controlled vocabulary that describes the method used
                to observe the properties of the borehole.
            specification:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
                $comment: "External ISO 19156 GFI_Feature \u2014 by-reference link"
              description: The specification property is an association between a
                BoreholeInterval and a GFI_Feature, a domain feature that is sampled
                by the interval (e.g., a GeologicUnit). It is semantically equivalent
                to O&M ISO19156 "sampledFeature".
            mappedIntervalBegin:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
              description: The property mappedIntervalBegin (SWE::Quantity) is a measurement
                (a value and a unit of measurement) corresponding to the measured
                distance of the start of the mapped interval along the path of the
                borehole. The measured value must be less than or equal to the mappedIntervalEnd
                value.
            mappedIntervalEnd:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
              description: The mappedIntervalEnd property (SWE::Quantity) is a measurement
                (a value and a unit of measure) corresponding to the measured distance
                of the end of the mapped interval along the path of the borehole.
                The measured value must be greater than or equal to the mappedIntervalBegin
                value.
            collectionIdentifier:
              oneOf:
              - type: 'null'
              - anyOf:
                - $ref: '#/$defs/SCLinkObject'
                - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.json
                - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.json
                $comment: "External ISO 19103 ScopedName \u2014 link, CDIF definedTerm,
                  or SKOS concept"
              description: The collectionIdentifier:ScopedName is a string unique
                within a scope that identifies a collection which forms a set BoreholeIntervals.
                This allows description of multiple downhole logs for a single borehole.
                The name should identify a particular log observation event.
            shape:
              oneOf:
              - type: 'null'
              - $ref: https://geojson.org/schema/Geometry.json
              description: The property shape:GM_Object is a 1-D interval (e.g., a
                "from" and "to", or "top" and "base" measurement) covering the same
                distance as mappedIntervalBegin and mappedIntervalEnd. The geometry
                shall use a reference to the borehole as the CRS of the containing
                borehole.
            parentBorehole:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to Borehole
                - $ref: '#Borehole'
              description: The property parentBorehole is an association between a
                BoreholeInterval and a Borehole to which the interval belongs.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  BoreholePurposeCode:
    $anchor: BoreholePurposeCode
    description: Place holder for a vocabulary containing terms describing the purpose
      for which the borehole was drilled. eg, mineral exploration, water pumping,
      site evaluation, stratigraphic research, etc
    type: string
    format: uri
  BoreholeStartPointCode:
    $anchor: BoreholeStartPointCode
    description: 'This class is an indicative placeholder only for a vocabulary of
      terms describing the location of the start of a borehole. Users are encouraged
      to use a vocabulary of terms managed by the CGI vocabularies working group.
      Examples may include: natural ground surface - drilling started from a natural
      topographic surface open pit floor or wall - drilling started from the wall
      of an open pit or quarry underground - drilling started from an underground
      location, such as a driveway, chamber or open-stope from pre-existing hole -
      new drill hole spudded off the wall of an existing hole'
    type: string
    format: uri
  DrillingDetails:
    $anchor: DrillingDetails
    description: DrillingDetails is a class that captures the description of drilling
      methods and hole diameters down the drilling path. Properties that apply to
      the Borehole as a whole are managed in BoreholeDetails.
    type: object
    properties:
      drillingMethod:
        oneOf:
        - type: 'null'
        - $ref: '#BoreholeDrillingMethodCode'
        description: The drillingMethod:BoreholeDrillingMethodCode property contains
          a term from a controlled vocabulary indicating the drilling method used.
          Appropriate terms would include rotary air blast, auger, diamond core, air
          core, etc.
      boreholeDiameter:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The boreholeDiameter property (SWE::Quantity) contains a measurement
          (a value and a unit of measure) corresponding to the diameter of the drilled
          hole.
      intervalBegin:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The intervalBegin property (SWE::Quantity) contains a measurement
          (a value and a unit of measurement) that corresponds to the measured distance
          of the start of the interval along the path of the borehole. The measured
          value must be less than or equal to the intervalEnd value.
      intervalEnd:
        oneOf:
        - type: 'null'
        - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
        description: The property intervalEnd (SWE::Quantity) contains a measurement
          (a value and a unit of measurement) of the measured distance of the end
          of the interval along the path of the borehole. The measured value must
          be greater than or equal to the intervalBegin value.
  OriginPosition:
    $anchor: OriginPosition
    description: A borehole OriginPosition is a feature corresponding to the start
      point of a borehole log. This may correspond to the borehole collar location
      (e.g., kelly bush).
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            location:
              oneOf:
              - type: 'null'
              - $ref: https://geojson.org/schema/Point.json
              description: The property location contains a geometry corresponding
                to the location of the borehole collar.
            elevation:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
                $comment: "External ISO 19107 DirectPosition \u2014 by-reference link"
              description: The elevation:DirectPosition property is a compromise approach
                to supply elevation explicitly for location; this is to allow for
                software that cannot process 3-D GM_Point. Null shall be used if elevation
                is unknown. A DirectPosition shall have a dimension of 1, and CRS
                will be a "vertical" CRS (e.g. EPSG CRSs in the range 5600-5799).
            relatedBorehole:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to Borehole
                  - $ref: '#Borehole'
                uniqueItems: true
              description: The hole that has this collar for its start point
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  SCLinkObject:
    title: link object
    description: definition of a link object
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmBorehole/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmBorehole/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmBorehole/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmBorehole`

