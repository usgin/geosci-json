
# gsmSpecimen (Schema)

`usgin.bbr.geosci.gsmSpecimen` *v0.1*

Specimen building block. The wrapper dispatches two featureType

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmSpecimen

GeoSciML 4.1 building block `gsmSpecimen`. `«FeatureType»` classes are encoded as JSON-FG-compliant features; `«DataType»` / `«CodeList»` / `«Union»` classes follow **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Source UML packages: `LaboratoryAnalysis-Specimen`, `Geochronology`, `GeologicSpecimen`, `LaboratoryAnalysis`.

Contains 8 feature types, 3 data types, 7 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `AnalyticalInstrument` | «FeatureType» | JSON-FG Feature |
| `AnalyticalMethod` | «DataType» | plain JSON object |
| `AnalyticalMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `AnalyticalProcess` | «FeatureType» | JSON-FG Feature |
| `AnalyticalSession` | «FeatureType» | JSON-FG Feature |
| `GeochronologicInterpretation` | «FeatureType» | JSON-FG Feature |
| `GeologicSamplingMethod` | «FeatureType» | JSON-FG Feature |
| `GeologicSamplingMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GeologicSpecimenPreparation` | «DataType» | plain JSON object |
| `GeologicSpecimenPreparationTerm` | «CodeList» | URI codelist (`format: uri`) |
| `Image` | «FeatureType» | JSON-FG Feature |
| `InstrumentTypeTerm` | «CodeList» | URI codelist (`format: uri`) |
| `IsotopicEventType` | «CodeList» | URI codelist (`format: uri`) |
| `IsotopicSystemName` | «CodeList» | URI codelist (`format: uri`) |
| `ReferenceSpecimen` | «FeatureType» | JSON-FG Feature |
| `SF_Specimen` | «FeatureType» | JSON-FG Feature |
| `StatisticalMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `_FeatureDispatch` | «DataType» | plain JSON object |

## Class details

### `AnalyticalInstrument`

The analytical instrument is the category of instrument used to perform an analytical measurement or observation.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `type` | (oneOf — see schema) | 0..1 | The property type:InstrumentTypeTerm reports a term from a controlled vocabulary that describes the category of instr… |
| `model` | (oneOf — see schema) | 0..1 | The property mode:Primitive::CharacterString contains a string identifying the model of instrument used. (e.g., instr… |
| `serialNumber` | (oneOf — see schema) | 0..1 | The property serialNumber:Primitive::CharacterString contains a string that contains the serial number of the machine… |
| `commissionDate` | (oneOf — see schema) | 0..1 | The property commissionDate is an association between an AnalyticalInstrument and a TM_Instant corresponding to the d… |
| `location` | (oneOf — see schema) | 0..1 | The property location is an association between an AnalyticalInstrument and a CIT:Responsibility describing the owner… |
| `usedIn` | (oneOf — see schema) | 0..1 | The property usedIn is an association between an AnalyticalInstrument and an AnalyticalSession identifying an analyti… |

### `AnalyticalMethod`

The AnalyticalMethod provides the name, and published citation, of the analytical method used in an analytical session.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `methodName` | (oneOf — see schema) | 0..1 | The property methodName:AnalyticalMethodTerm contains a term from a controlled vocabulary that describes an analytica… |
| `citation` | (oneOf — see schema) | 0..1 | The citation property is an association between an AnalyticalMethod and a CIT:CI_Citation describing a published desc… |

### `AnalyticalProcess`

An analytical process is a concrete implementation of OM::OM_Process and describes the steps and methods used in an analytical session. It links to an analytical session (data acquisition) or a computational process which produce analytical results.  Constraint: Only for use with OM_Observation/procedure

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `method` | (oneOf — see schema) | 0..1 | The property method is an association that links an AnalyticalProcess to an AnalyticalMethod that describes the type … |
| `computation` | (oneOf — see schema) | 0..1 | The computation property is an association between an AnalyticalProcess and a CIT:ProcessStep that describes the comp… |
| `acquisition` | (oneOf — see schema) | 0..1 | The property acquisition is an association that links an AnalyticalProcess to an AnalyticalSession that describes the… |

### `AnalyticalSession`

This feature type describes the time and operator of a particular laboratory analytical session. AnalyticalSession also has associated links to the type of instrument and analytical method used, processing steps applied to data collected during a session, and instrument parameters unique to that session.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `time` | (oneOf — see schema) | 0..1 | The property time is an association between an AnalyticalSession and a TM_Period describing the time period during wh… |
| `operator` | (oneOf — see schema) | 0..1 | The property operator is an association between an AnalyticalSession and a CIT:CI_Responsability describing the opera… |
| `parameter` | (oneOf — see schema) | 0..1 | The property parameter (OM::NamedValue) contains a name/value pair to describe arbitrary environmental or instrument … |
| `instrument` | (oneOf — see schema) | 0..1 | The property instrument is an association between an AnalyticalSession and an AnalyticalInstrument that describes the… |
| `referenceAnalyses` | (oneOf — see schema) | 0..1 | The property referenceAnalysis is an association between an AnalyticalSession and a ReferenceSpecimen that describes … |

### `GeochronologicInterpretation`

A GeochronologicInterpretation is an interpretation made by a geologist of the age of a specimen made by statistical analysis of a collection of observations. A geologic specimen may have multiple geochronological interpretations made on it, each related to a different observation/result collection.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `interpretedAge` | (oneOf — see schema) | 0..1 | The interpretedAge property is an association between a GeochronologicInterpretation and a GeologicEvent that describ… |
| `isotopicEvent` | (oneOf — see schema) | 0..1 | The isotopicEvent:IsotopicEventType contains a term from a controlled vocabulary that describes any isotopic events t… |
| `isotopicSystem` | (oneOf — see schema) | 0..1 | The property isotopicSystem:IsotopicSystemName contains a term from a controlled vocabulary that describes the isotop… |
| `statisticalMethod` | (oneOf — see schema) | 0..1 | The property statisticalMethod:StatisticalMethodTerm contains a term from a controlled vocabulary that describes the … |
| `interpretedBy` | (oneOf — see schema) | 0..1 | The property interpretedBy is an association between a GeochronologicInterpretation and a CIT:CI_Responsability descr… |
| `citation` | (oneOf — see schema) | 0..1 | The citation property is an association between a GeochronologicInterpretation and a CIT:CI_Citation that describes a… |
| `preferredInterpretation` | (oneOf — see schema) | 0..1 | The property preferredInterpretation:Primitive::Boolean indicates whether this interpretation is the preferred interp… |
| `sourceCollection` | (oneOf — see schema) | 0..1 | The property sourceCollection is an association between a GeochronologicInterpretation and an OM::SF_SamplingFeatureC… |

### `GeologicSamplingMethod`

GeologicSamplingMethod is an implementation of OM::SF_Process to describe the method used to obtain a geologic specimen. Examples include: &#x9;diamond drilling &#x9;percussion drilling &#x9;piston core drilling &#x9;vibro core drilling &#x9;channel sampling &#x9;sea floor dredging &#x9;outcrop sampling  Constraint: Only for use with SF_Specimen/samplingMethod

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `method` | (oneOf — see schema) | 0..1 | The property method:GeologicSamplingMethodTerm is a term from a controlled vocabulary that describes the process used… |
| `parameter` | (oneOf — see schema) | 0..1 | The property parameter (OM::NamedValue) contains a name/value pair to describe arbitrary parameters used in the sampl… |

### `GeologicSpecimenPreparation`

GeologicSpecimenPreparation is an extension of ISO Specimen::preparationStep to allow details of preparation steps to be delivered (e.g., filtration and mesh size, chemical additives, crushing methods, drying parameters, etc.).  Constraint: Only for use with SF_Specimen/processingDetails

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `preparationMethod` | (oneOf — see schema) | 0..1 | The preparationMethod:GeologicSpecimenPreparationTerm contains a term from a controlled vocabulary that describes the… |
| `parameter` | (oneOf — see schema) | 0..1 | The property parameter (OM::NamedValue) contains name/value pair to describe arbitrary parameters used in this prepar… |

### `Image`

The Image feature type is used to describe images of sampling features, for example, photographs of ion microprobe grain mounts.

### `ReferenceSpecimen`

A reference specimen is a specimen with known or accepted values of some property. The citation property describes the location of a published description of these values. Reference specimens include analytical blanks. ReferenceSpecimens are used in quality control procedures to assess method reproducibility. Analytical results from a reference specimen analysed during an AnalyticalSession are delivered in the same way as the results of other specimens analysed in that session.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `referenceDescription` | (oneOf — see schema) | 0..1 | The property referenceDescription is an association between a ReferenceSpecimen and a CIT:CI_Citation that references… |
| `usedIn` | (oneOf — see schema) | 0..1 | The property usedIn is an association between a ReferenceSpecimen and an AnalyticalSession in which the reference spe… |

### `SF_Specimen`

ISO 19156:2011 §8.6 SF_Specimen — a sampling feature representing a physical specimen collected from a sampled feature. Implementation inlines the SF_SamplingFeature parent's properties (sampledFeature, relatedObservation, relatedSamplingFeature, lineage) since the parent is not separately schematised here. External ISO types referenced from properties (OM_Process, OM_Observation, GFI_Feature, TM_Object, LI_Lineage, SF_SamplingFeature) are by-reference only via SCLinkObject.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `sampledFeature` | (oneOf — see schema) | 0..1 | Feature(s) being sampled (1..*, by-reference to ISO 19156 GFI_Feature). Inherited from SF_SamplingFeature. |
| `relatedObservation` | (oneOf — see schema) | 0..1 | Observations whose featureOfInterest is this specimen (0..*, by-reference to ISO 19156 OM_Observation). Inherited fro… |
| `relatedSamplingFeature` | (oneOf — see schema) | 0..1 | Self-association: relations to other SF_SamplingFeature instances (0..*, by-reference). Inherited from SF_SamplingFea… |
| `lineage` | (oneOf — see schema) | 0..1 | Provenance metadata (by-reference to ISO 19115 LI_Lineage). Inherited from SF_SamplingFeature. |
| `materialClass` | SWE 3.0 `Category` | 0..1 | Material class of the specimen (1..1). ISO 19156 types this as ScopedName; encoded here as a SWE Category to carry th… |
| `samplingTime` | `/$defs/SCLinkObject` | 0..1 | Time of sampling (1..1, by-reference to ISO 19108 TM_Object). |
| `samplingMethod` | (oneOf — see schema) | 0..1 | Sampling method (0..1). ISO 19156 types as OM_Process; here implemented as the GeoSciML GeologicSamplingMethod Featur… |
| `samplingLocation` | (oneOf — see schema) | 0..1 | Location where the specimen was sampled (0..1, GeoJSON Geometry). Distinct from the top-level Feature geometry, which… |
| `processingDetails` | (oneOf — see schema) | 0..1 | Processing / preparation steps applied to the specimen (0..*). ISO 19156 types as SpecimenProcessing; here items are … |
| `size` | (oneOf — see schema) | 0..1 | Specimen size as a SWE Quantity (0..1). ISO 19156 types as Measure. |
| `currentLocation` | (oneOf — see schema) | 0..1 | Current physical location of the specimen (0..1). Free text address, URI, or link object to a repository record. |
| `specimenType` | (oneOf — see schema) | 0..1 | Specimen type classifier (0..1). ISO 19156 types as ScopedName; encoded here as a SWE Category. |

### `_FeatureDispatch`

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `AnalyticalMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicSamplingMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `GeologicSpecimenPreparationTerm` | `_(treat as open — no `codeList` annotation)_` |
| `InstrumentTypeTerm` | `_(treat as open — no `codeList` annotation)_` |
| `IsotopicEventType` | `_(treat as open — no `codeList` annotation)_` |
| `IsotopicSystemName` | `_(treat as open — no `codeList` annotation)_` |
| `StatisticalMethodTerm` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `../gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json`
- `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json`
- `https://geojson.org/schema/Geometry.json`
- `https://schemas.opengis.net/json-fg/feature.json`
- `https://schemas.opengis.net/json-fg/featurecollection.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Category.json`
- `https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json`

## Examples

- [specimen_drill_core_segment.json](examples/specimen_drill_core_segment.json)

See [examples.yaml](examples.yaml) for the full manifest.

## Source

- UML: `geosciml4.1.xmi`, package(s) `LaboratoryAnalysis-Specimen`, `Geochronology`, `GeologicSpecimen`, `LaboratoryAnalysis`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).

## Examples

### specimen drill core segment
SF_Specimen example — a drill-core segment from a borehole. Exercises the required SF_SamplingFeature inherited properties (sampledFeature, samplingTime, materialClass) plus optional own properties (samplingMethod, processingDetails, size, currentLocation, specimenType) and the relatedSamplingFeature self-association linking to the parent borehole interval that produced it.
#### json
```json
{
  "$comment": "SF_Specimen example — a drill-core segment from a borehole. Exercises the required SF_SamplingFeature inherited properties (sampledFeature, samplingTime, materialClass) plus optional own properties (samplingMethod, processingDetails, size, currentLocation, specimenType) and the relatedSamplingFeature self-association linking to the parent borehole interval that produced it.",
  "type": "Feature",
  "featureType": "SF_Specimen",
  "id": "https://example.org/specimens/dc-2024-017-seg-3",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "sampledFeature": [
      {
        "href": "https://example.org/geologicunits/hervey-group",
        "rel": "self",
        "title": "Hervey Group (GeologicUnit being sampled)"
      }
    ],
    "relatedSamplingFeature": [
      {
        "href": "https://example.org/boreholes/dc-2024-017",
        "rel": "child-of",
        "title": "DC-2024-017 borehole (parent sampling feature)"
      },
      {
        "href": "https://example.org/boreholeintervals/dc-2024-017/142.4-143.6",
        "rel": "child-of",
        "title": "BoreholeInterval 142.4–143.6 m from which this core segment was retrieved"
      }
    ],
    "relatedObservation": [
      {
        "href": "https://example.org/observations/dc-2024-017-seg-3/xrf-2024-08-12",
        "rel": "described-by",
        "title": "Portable-XRF major element analysis run on 2024-08-12"
      }
    ],
    "materialClass": {
      "type": "Category",
      "label": "sandstone",
      "definition": "http://resource.geosciml.org/classifier/cgi/simplelithology",
      "value": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
    },
    "samplingTime": {
      "href": "https://example.org/time/2024-08-10T11:23:00Z",
      "title": "Recovered 2024-08-10 11:23 UTC"
    },
    "samplingMethod": {
      "href": "https://example.org/methods/diamond-core-drilling",
      "title": "Diamond core drilling (HQ size, triple tube) — referencing a GeologicSamplingMethod feature"
    },
    "processingDetails": [
      {
        "preparationMethod": "http://resource.geosciml.org/classifier/cgi/specimenpreparation/core-split-and-photograph"
      }
    ],
    "currentLocation": "Repository A, Drawer 17, Slot 03",
    "specimenType": {
      "type": "Category",
      "label": "core segment",
      "definition": "http://resource.geosciml.org/classifier/cgi/specimentype",
      "value": "http://resource.geosciml.org/classifier/cgi/specimentype/core-segment"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmSpecimen/context.jsonld",
  "$comment": "SF_Specimen example \u2014 a drill-core segment from a borehole. Exercises the required SF_SamplingFeature inherited properties (sampledFeature, samplingTime, materialClass) plus optional own properties (samplingMethod, processingDetails, size, currentLocation, specimenType) and the relatedSamplingFeature self-association linking to the parent borehole interval that produced it.",
  "type": "Feature",
  "featureType": "SF_Specimen",
  "id": "https://example.org/specimens/dc-2024-017-seg-3",
  "geometry": null,
  "place": null,
  "time": null,
  "properties": {
    "sampledFeature": [
      {
        "href": "https://example.org/geologicunits/hervey-group",
        "rel": "self",
        "title": "Hervey Group (GeologicUnit being sampled)"
      }
    ],
    "relatedSamplingFeature": [
      {
        "href": "https://example.org/boreholes/dc-2024-017",
        "rel": "child-of",
        "title": "DC-2024-017 borehole (parent sampling feature)"
      },
      {
        "href": "https://example.org/boreholeintervals/dc-2024-017/142.4-143.6",
        "rel": "child-of",
        "title": "BoreholeInterval 142.4\u2013143.6 m from which this core segment was retrieved"
      }
    ],
    "relatedObservation": [
      {
        "href": "https://example.org/observations/dc-2024-017-seg-3/xrf-2024-08-12",
        "rel": "described-by",
        "title": "Portable-XRF major element analysis run on 2024-08-12"
      }
    ],
    "materialClass": {
      "type": "Category",
      "label": "sandstone",
      "definition": "http://resource.geosciml.org/classifier/cgi/simplelithology",
      "value": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
    },
    "samplingTime": {
      "href": "https://example.org/time/2024-08-10T11:23:00Z",
      "title": "Recovered 2024-08-10 11:23 UTC"
    },
    "samplingMethod": {
      "href": "https://example.org/methods/diamond-core-drilling",
      "title": "Diamond core drilling (HQ size, triple tube) \u2014 referencing a GeologicSamplingMethod feature"
    },
    "processingDetails": [
      {
        "preparationMethod": "http://resource.geosciml.org/classifier/cgi/specimenpreparation/core-split-and-photograph"
      }
    ],
    "currentLocation": "Repository A, Drawer 17, Slot 03",
    "specimenType": {
      "type": "Category",
      "label": "core segment",
      "definition": "http://resource.geosciml.org/classifier/cgi/specimentype",
      "value": "http://resource.geosciml.org/classifier/cgi/specimentype/core-segment"
    }
  }
}
```

#### ttl
```ttl


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmSpecimen/gsmSpecimenSchema.json
description: "Specimen building block. The wrapper dispatches two featureType\nvalues:
  SF_Specimen (hand-curated \xABFeatureType\xBB, ISO 19156:2011\n\xA78.6 \u2014 inlines
  SF_SamplingFeature's inherited properties since ISO\n19156 isn't in the GeoSciML
  XMI) and ReferenceSpecimen (a GeoSciML\n\xABFeatureType\xBB from the LaboratoryAnalysis-Specimen
  package, used\nfor named reference / type specimens). The rest of the\nLaboratoryAnalysis-Specimen
  library (AnalyticalInstrument,\nAnalyticalSession, GeochronologicInterpretation,\nGeologicSamplingMethod,
  GeologicSpecimenPreparation, Image, etc.)\nstays in `$defs` for cross-reference
  from SF_Specimen and from\nother BBs.\n\nValidates either a single Feature (dispatched
  by `featureType` to one of: SF_Specimen, ReferenceSpecimen) or a FeatureCollection
  whose `features[]` items are dispatched the same way."
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
            const: SF_Specimen
      then:
        $ref: '#SF_Specimen'
    - if:
        required:
        - featureType
        properties:
          featureType:
            const: ReferenceSpecimen
      then:
        $ref: '#ReferenceSpecimen'
    - if:
        not:
          required:
          - featureType
          properties:
            featureType:
              enum:
              - SF_Specimen
              - ReferenceSpecimen
      then: false
  AnalyticalInstrument:
    $anchor: AnalyticalInstrument
    description: The analytical instrument is the category of instrument used to perform
      an analytical measurement or observation.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            type:
              oneOf:
              - type: 'null'
              - $ref: '#InstrumentTypeTerm'
              description: The property type:InstrumentTypeTerm reports a term from
                a controlled vocabulary that describes the category of instrument
                used in an analytical session (e.g., XRF, ICPMS, SHRIMP, etc.).
            model:
              oneOf:
              - type: 'null'
              - type: string
              description: The property mode:Primitive::CharacterString contains a
                string identifying the model of instrument used. (e.g., instrument
                type = XRD, model = Siemens Diffraktometer D500).
            serialNumber:
              oneOf:
              - type: 'null'
              - type: string
              description: The property serialNumber:Primitive::CharacterString contains
                a string that contains the serial number of the machine used in an
                analytical session.
            commissionDate:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                - type: object
                  properties:
                    inXSDDateTime:
                      type: string
                      format: date-time
                    inXSDDate:
                      type: string
                      format: date
                    inXSDgYearMonth:
                      type: string
                      pattern: ^-?\d{4}-\d{2}$
                    inXSDgYear:
                      type: string
                      pattern: ^-?\d{4}$
                  anyOf:
                  - required:
                    - inXSDDateTime
                  - required:
                    - inXSDDate
                  - required:
                    - inXSDgYearMonth
                  - required:
                    - inXSDgYear
                - type: string
                  format: date-time
                - type: string
                  format: date
                $comment: ISO 19108 TM_Instant aligned to W3C OWL-Time time:Instant
                  (https://www.w3.org/TR/owl-time/#time:Instant). Accepts a SCLinkObject
                  by-reference, an OWL-Time Instant object with one of `inXSDDateTime`
                  / `inXSDDate` / `inXSDgYearMonth` / `inXSDgYear`, or a bare ISO
                  8601 string as a convenience alias.
              description: The property commissionDate is an association between an
                AnalyticalInstrument and a TM_Instant corresponding to the date of
                the commissioning of an instrument.
            location:
              oneOf:
              - type: 'null'
              - anyOf:
                - $ref: '#/$defs/SCLinkObject'
                - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
                $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference
                  link or inline CDIF agentInRole"
              description: The property location is an association between an AnalyticalInstrument
                and a CIT:Responsibility describing the owner and the location of
                an instrument.
            usedIn:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to AnalyticalSession
                  - $ref: '#AnalyticalSession'
                uniqueItems: true
              description: The property usedIn is an association between an AnalyticalInstrument
                and an AnalyticalSession identifying an analytical sessions which
                used this instrument.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  AnalyticalMethod:
    $anchor: AnalyticalMethod
    description: The AnalyticalMethod provides the name, and published citation, of
      the analytical method used in an analytical session.
    type: object
    properties:
      methodName:
        oneOf:
        - type: 'null'
        - $ref: '#AnalyticalMethodTerm'
        description: The property methodName:AnalyticalMethodTerm contains a term
          from a controlled vocabulary that describes an analytical method used in
          a session (e.g., XRF mass spectrometry, ICPMS, SHRIMP geochronology).
      citation:
        oneOf:
        - type: 'null'
        - $ref: '#/$defs/SCLinkObject'
          $comment: "External ISO 19115 CI_Citation \u2014 by-reference link only"
        description: The citation property is an association between an AnalyticalMethod
          and a CIT:CI_Citation describing a published description of a particular
          analytical method (e.g., a standard operating procedure document).
  AnalyticalMethodTerm:
    $anchor: AnalyticalMethodTerm
    description: Refers to a vocabulary of terms describing the analytical method
      used in an analytical session (eg; XRF mass spectrometry, ICPMS, SHRIMP geochronology)
    type: string
    format: uri
  AnalyticalProcess:
    $anchor: AnalyticalProcess
    description: 'An analytical process is a concrete implementation of OM::OM_Process
      and describes the steps and methods used in an analytical session. It links
      to an analytical session (data acquisition) or a computational process which
      produce analytical results.  Constraint: Only for use with OM_Observation/procedure'
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            method:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to AnalyticalMethod
                - $ref: '#AnalyticalMethod'
              description: The property method is an association that links an AnalyticalProcess
                to an AnalyticalMethod that describes the type of analytical method
                used to make an observation.
            computation:
              oneOf:
              - type: 'null'
              - $comment: 'Unresolved type: LI_ProcessStep'
                type: object
              description: The computation property is an association between an AnalyticalProcess
                and a CIT:ProcessStep that describes the computational process associated
                with the process.
            acquisition:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to AnalyticalSession
                - $ref: '#AnalyticalSession'
              description: The property acquisition is an association that links an
                AnalyticalProcess to an AnalyticalSession that describes the analytical
                session (e.g., laboratory session) in which an observation was made
                and data acquired.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  AnalyticalSession:
    $anchor: AnalyticalSession
    description: This feature type describes the time and operator of a particular
      laboratory analytical session. AnalyticalSession also has associated links to
      the type of instrument and analytical method used, processing steps applied
      to data collected during a session, and instrument parameters unique to that
      session.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            time:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                - type: object
                  properties:
                    hasBeginning:
                      type: object
                    hasEnd:
                      type: object
                  required:
                  - hasBeginning
                  - hasEnd
                - type: object
                  properties:
                    hasBeginningDateTime:
                      type: string
                    hasEndDateTime:
                      type: string
                  required:
                  - hasBeginningDateTime
                  - hasEndDateTime
                - type: array
                  minItems: 2
                  maxItems: 2
                  items:
                    type: string
                $comment: ISO 19108 TM_Period aligned to W3C OWL-Time time:ProperInterval
                  (https://www.w3.org/TR/owl-time/#time:ProperInterval). Canonical
                  encoding is the OWL-Time object with `hasBeginning`/`hasEnd` (or
                  the shortcut `hasBeginningDateTime`/`hasEndDateTime`). A two-element
                  [startDate, endDate] array is accepted as a convenience alias (OGC
                  code-sprint convention) but is not OWL-Time-canonical; consumers
                  should prefer the object form.
              description: The property time is an association between an AnalyticalSession
                and a TM_Period describing the time period during which the analysis
                was performed.
            operator:
              oneOf:
              - type: 'null'
              - anyOf:
                - $ref: '#/$defs/SCLinkObject'
                - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
                $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference
                  link or inline CDIF agentInRole"
              description: The property operator is an association between an AnalyticalSession
                and a CIT:CI_Responsability describing the operator or organisation
                responsible for the analytical session.
            parameter:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  anyOf:
                  - $ref: '#/$defs/SCLinkObject'
                  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json
                  $comment: "External ISO 19103 NamedValue \u2014 link or inline CDIF
                    variableMeasured (schema:PropertyValue)"
                uniqueItems: true
              description: The property parameter (OM::NamedValue) contains a name/value
                pair to describe arbitrary environmental or instrument setting parameters
                that apply to an entire analytical session (e.g., voltage, current,
                temperature, vacuum). The "name" attribute of NamedValue is a term
                from a controlled vocabulary.
            instrument:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to AnalyticalInstrument
                - $ref: '#AnalyticalInstrument'
              description: The property instrument is an association between an AnalyticalSession
                and an AnalyticalInstrument that describes the instrument used in
                the analytical session.
            referenceAnalyses:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to ReferenceSpecimen
                  - $ref: '#ReferenceSpecimen'
                uniqueItems: true
              description: The property referenceAnalysis is an association between
                an AnalyticalSession and a ReferenceSpecimen that describes a reference
                specimen (i.e., standards, blanks) used in the analytical session.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeochronologicInterpretation:
    $anchor: GeochronologicInterpretation
    description: A GeochronologicInterpretation is an interpretation made by a geologist
      of the age of a specimen made by statistical analysis of a collection of observations.
      A geologic specimen may have multiple geochronological interpretations made
      on it, each related to a different observation/result collection.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            interpretedAge:
              oneOf:
              - type: 'null'
              - oneOf:
                - $ref: '#/$defs/SCLinkObject'
                  $comment: by-reference link to GeologicEvent
                - $ref: https://usgin.github.io/geosci-json/_sources/gsmBasicGeology/gsmBasicGeologySchema.json#GeologicEvent
                  $comment: cross-BB inline reference to GeologicEvent in BB gsmBasicGeology
              description: The interpretedAge property is an association between a
                GeochronologicInterpretation and a GeologicEvent that describes the
                dated event, process and environment.
            isotopicEvent:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#IsotopicEventType'
                uniqueItems: true
              description: The isotopicEvent:IsotopicEventType contains a term from
                a controlled vocabulary that describes any isotopic events that are
                relevant to the interpretation. e.g., closure, isotopic mixing, Pb
                loss, etc.
            isotopicSystem:
              oneOf:
              - type: 'null'
              - $ref: '#IsotopicSystemName'
              description: 'The property isotopicSystem:IsotopicSystemName contains
                a term from a controlled vocabulary that describes the isotopic system
                used to calculate geochronological age. A vocabulary would contain
                values such as: Ar-Ar, K-Ar, Nd-Sm, Pb-Pb, Rb-Sr, Re-Os, U-Pb, etc.'
            statisticalMethod:
              oneOf:
              - type: 'null'
              - $ref: '#StatisticalMethodTerm'
              description: The property statisticalMethod:StatisticalMethodTerm contains
                a term from a controlled vocabulary that describes the statistical
                method used to interpret the results. (e.g., weighted mean, median,
                concordia, discordia, etc)
            interpretedBy:
              oneOf:
              - type: 'null'
              - anyOf:
                - $ref: '#/$defs/SCLinkObject'
                - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json
                $comment: "External ISO 19115 CI_Responsibility \u2014 by-reference
                  link or inline CDIF agentInRole"
              description: The property interpretedBy is an association between a
                GeochronologicInterpretation and a CIT:CI_Responsability describing
                the party responsible for this interpretation.
            citation:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
                $comment: "External ISO 19115 CI_Citation \u2014 by-reference link
                  only"
              description: The citation property is an association between a GeochronologicInterpretation
                and a CIT:CI_Citation that describes authors and other reference information
                for an interpreted age.
            preferredInterpretation:
              oneOf:
              - type: 'null'
              - type: boolean
              description: The property preferredInterpretation:Primitive::Boolean
                indicates whether this interpretation is the preferred interpretation
                (i.e., the analytical data may be reinterpreted).
            sourceCollection:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
                $comment: "External ISO 19156 SF_SamplingFeatureCollection \u2014
                  by-reference link"
              description: The property sourceCollection is an association between
                a GeochronologicInterpretation and an OM::SF_SamplingFeatureCollection
                that lists a collection of OM::SF_SamplingFeature (e.g., a collection
                of burn spots or craters from a SHRIMP analytical session). When legacy
                published data for which the SamplingFeatureCollection is unknown,
                it may be delivered with SamplingFeatureCollection = 'unknown'.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeologicSamplingMethod:
    $anchor: GeologicSamplingMethod
    description: 'GeologicSamplingMethod is an implementation of OM::SF_Process to
      describe the method used to obtain a geologic specimen. Examples include: &#x9;diamond
      drilling &#x9;percussion drilling &#x9;piston core drilling &#x9;vibro core
      drilling &#x9;channel sampling &#x9;sea floor dredging &#x9;outcrop sampling  Constraint:
      Only for use with SF_Specimen/samplingMethod'
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            method:
              oneOf:
              - type: 'null'
              - $ref: '#GeologicSamplingMethodTerm'
              description: The property method:GeologicSamplingMethodTerm is a term
                from a controlled vocabulary that describes the process used to obtain
                or create a geologic specimen. e.g., diamond drilling, percussion
                drilling, piston core drilling, vibro core drilling, channel sampling,
                sea floor dredging, crushing, mineral separation, melting, outcrop
                sampling.
            parameter:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  anyOf:
                  - $ref: '#/$defs/SCLinkObject'
                  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json
                  $comment: "External ISO 19103 NamedValue \u2014 link or inline CDIF
                    variableMeasured (schema:PropertyValue)"
                uniqueItems: true
              description: The property parameter (OM::NamedValue) contains a name/value
                pair to describe arbitrary parameters used in the sampling process.
                The "name" attribute of NamedValue shall be a term from a controlled
                vocabulary.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  GeologicSamplingMethodTerm:
    $anchor: GeologicSamplingMethodTerm
    description: 'Refers to a vocabulary of terms describing the samplingProcess used
      to obtain or create the Specimen. eg: diamond drilling percussion drilling piston
      core drilling vibro core drilling channel sampling sea floor dredging crushing
      mineral separation melting geological hammer'
    type: string
    format: uri
  GeologicSpecimenPreparation:
    $anchor: GeologicSpecimenPreparation
    description: 'GeologicSpecimenPreparation is an extension of ISO Specimen::preparationStep
      to allow details of preparation steps to be delivered (e.g., filtration and
      mesh size, chemical additives, crushing methods, drying parameters, etc.).  Constraint:
      Only for use with SF_Specimen/processingDetails'
    type: object
    properties:
      preparationMethod:
        oneOf:
        - type: 'null'
        - $ref: '#GeologicSpecimenPreparationTerm'
        description: The preparationMethod:GeologicSpecimenPreparationTerm contains
          a term from a controlled vocabulary that describes the method employed for
          the preparation of a geologic specimen for further analysis.
      parameter:
        oneOf:
        - type: 'null'
        - type: array
          items:
            anyOf:
            - $ref: '#/$defs/SCLinkObject'
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json
            $comment: "External ISO 19103 NamedValue \u2014 link or inline CDIF variableMeasured
              (schema:PropertyValue)"
          uniqueItems: true
        description: The property parameter (OM::NamedValue) contains name/value pair
          to describe arbitrary parameters used in this preparation step (e.g., mesh
          size in a sieving process, type of chemical additives, parameters in a mineral
          separation process). The "name" attribute of NamedValue shall be a term
          from a controlled vocabulary.
  GeologicSpecimenPreparationTerm:
    $anchor: GeologicSpecimenPreparationTerm
    description: 'Refers to a vocabulary of terms to describe sample preparation applied
      to geologic specimens, typically in preparation for analytical processes like
      geochemistry or microscopy. eg: crush mineral separation thin section cut polish
      mount acid digestion'
    type: string
    format: uri
  Image:
    $anchor: Image
    description: The Image feature type is used to describe images of sampling features,
      for example, photographs of ion microprobe grain mounts.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties: {}
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  InstrumentTypeTerm:
    $anchor: InstrumentTypeTerm
    description: Refers to a vocabulary of Instrument types (eg; XRF, ICPMS, SHRIMP,
      etc)
    type: string
    format: uri
  IsotopicEventType:
    $anchor: IsotopicEventType
    description: Refers to a vocabulary of terms to describe any isotopic processes
      relevant to the geochronologic interpretation. eg:closure, isotopic mixing,
      Pb loss, etc
    type: string
    format: uri
  IsotopicSystemName:
    $anchor: IsotopicSystemName
    description: Refers to a vocabulary of isotopic systems such as Ar-Ar, K-Ar, Nd-Sm,
      U-Pb, Pb-Pb, Re-Os, etc
    type: string
    format: uri
  ReferenceSpecimen:
    $anchor: ReferenceSpecimen
    description: A reference specimen is a specimen with known or accepted values
      of some property. The citation property describes the location of a published
      description of these values. Reference specimens include analytical blanks.
      ReferenceSpecimens are used in quality control procedures to assess method reproducibility.
      Analytical results from a reference specimen analysed during an AnalyticalSession
      are delivered in the same way as the results of other specimens analysed in
      that session.
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            referenceDescription:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
                $comment: "External ISO 19115 CI_Citation \u2014 by-reference link
                  only"
              description: The property referenceDescription is an association between
                a ReferenceSpecimen and a CIT:CI_Citation that references a citation
                of published analytical results for this standard reference specimen.
            usedIn:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/SCLinkObject'
                    $comment: by-reference link to AnalyticalSession
                  - $ref: '#AnalyticalSession'
                uniqueItems: true
              description: The property usedIn is an association between a ReferenceSpecimen
                and an AnalyticalSession in which the reference specimen was used.
    - required:
      - featureType
      - id
      properties:
        id:
          type: string
  StatisticalMethodTerm:
    $anchor: StatisticalMethodTerm
    description: Refers to a vocabulary describing statistical methods used in interpret
      geochronologic data
    type: string
    format: uri
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
  SF_Specimen:
    $anchor: SF_Specimen
    description: "ISO 19156:2011 \xA78.6 SF_Specimen \u2014 a sampling feature representing
      a physical specimen collected from a sampled feature. Implementation inlines
      the SF_SamplingFeature parent's properties (sampledFeature, relatedObservation,
      relatedSamplingFeature, lineage) since the parent is not separately schematised
      here. External ISO types referenced from properties (OM_Process, OM_Observation,
      GFI_Feature, TM_Object, LI_Lineage, SF_SamplingFeature) are by-reference only
      via SCLinkObject."
    allOf:
    - $ref: https://schemas.opengis.net/json-fg/feature.json
    - type: object
      properties:
        properties:
          type: object
          properties:
            sampledFeature:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#/$defs/SCLinkObject'
                minItems: 1
                uniqueItems: true
              description: Feature(s) being sampled (1..*, by-reference to ISO 19156
                GFI_Feature). Inherited from SF_SamplingFeature.
            relatedObservation:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#/$defs/SCLinkObject'
                uniqueItems: true
              description: Observations whose featureOfInterest is this specimen (0..*,
                by-reference to ISO 19156 OM_Observation). Inherited from SF_SamplingFeature.
            relatedSamplingFeature:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#/$defs/SCLinkObject'
                uniqueItems: true
              description: 'Self-association: relations to other SF_SamplingFeature
                instances (0..*, by-reference). Inherited from SF_SamplingFeature.'
            lineage:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
              description: Provenance metadata (by-reference to ISO 19115 LI_Lineage).
                Inherited from SF_SamplingFeature.
            materialClass:
              $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
              description: Material class of the specimen (1..1). ISO 19156 types
                this as ScopedName; encoded here as a SWE Category to carry the vocabulary
                URI.
            samplingTime:
              $ref: '#/$defs/SCLinkObject'
              description: Time of sampling (1..1, by-reference to ISO 19108 TM_Object).
            samplingMethod:
              oneOf:
              - type: 'null'
              - $ref: '#/$defs/SCLinkObject'
              - $ref: '#GeologicSamplingMethod'
              description: Sampling method (0..1). ISO 19156 types as OM_Process;
                here implemented as the GeoSciML GeologicSamplingMethod FeatureType,
                either by-reference (SCLinkObject) or inline.
            samplingLocation:
              oneOf:
              - type: 'null'
              - $ref: https://geojson.org/schema/Geometry.json
              description: Location where the specimen was sampled (0..1, GeoJSON
                Geometry). Distinct from the top-level Feature geometry, which may
                carry the specimen's current footprint.
            processingDetails:
              oneOf:
              - type: 'null'
              - type: array
                items:
                  $ref: '#GeologicSpecimenPreparation'
                uniqueItems: true
              description: Processing / preparation steps applied to the specimen
                (0..*). ISO 19156 types as SpecimenProcessing; here items are the
                GeoSciML GeologicSpecimenPreparation DataType.
            size:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Quantity.json
              description: Specimen size as a SWE Quantity (0..1). ISO 19156 types
                as Measure.
            currentLocation:
              oneOf:
              - type: 'null'
              - type: string
              - $ref: '#/$defs/SCLinkObject'
              description: Current physical location of the specimen (0..1). Free
                text address, URI, or link object to a repository record.
            specimenType:
              oneOf:
              - type: 'null'
              - $ref: https://schemas.opengis.net/sweCommon/3.0/json/Category.json
              description: Specimen type classifier (0..1). ISO 19156 types as ScopedName;
                encoded here as a SWE Category.
          required:
          - sampledFeature
          - materialClass
          - samplingTime
    - required:
      - featureType
      - id
      properties:
        id:
          type: string

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmSpecimen/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmSpecimen/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmSpecimen/context.jsonld)

## Sources

* [GeoSciML 4.1 UML model (Enterprise Architect XMI export)](https://github.com/usgin/geosci-json/blob/main/geosciml4.1.xmi)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmSpecimen`

