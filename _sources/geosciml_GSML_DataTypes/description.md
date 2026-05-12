# GeoSciML GSML_DataTypes

JSON Schema building block for the `GSML_DataTypes` package of **GeoSciML 4.1**, encoding `«FeatureType»` classes as JSON-FG-compliant features and `«DataType»` / `«CodeList»` / `«Union»` classes per **OGC Best Practice 24-017r1** (*UML to JSON Encoding Rules*).

Contains 5 data types, 4 code lists.

## Classes in this BB

| Class | Stereotype | Encoding |
| --- | --- | --- |
| `ConventionCode` | «CodeList» | URI codelist (`format: uri`) |
| `DeterminationMethodTerm` | «CodeList» | URI codelist (`format: uri`) |
| `GSML_GeometricDescriptionValue` | «DataType» | plain JSON object |
| `GSML_LinearOrientation` | «DataType» | plain JSON object |
| `GSML_PlanarOrientation` | «DataType» | plain JSON object |
| `GSML_QuantityRange` | «DataType» | plain JSON object |
| `GSML_Vector` | «DataType» | plain JSON object |
| `LinearDirectedCode` | «CodeList» | URI codelist (`format: uri`) |
| `PlanarPolarityCode` | «CodeList» | URI codelist (`format: uri`) |

## Class details

### `GSML_GeometricDescriptionValue`

GSML_GeometricDescriptionValue is a special abstract data type for descriptions of planar or linear orientations of a geologic feature. Different subtypes allow specifying direction by direction vector (e.g. dip/dip direction), compass point (e.g. NE), or description (e.g. "toward fold hinge", "below').

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `determinationMethod` | (oneOf — see schema) | 0..1 | The determinationMethod:DeterminationMethodTerm property describes the way the orientation value was determined (e.g.… |
| `descriptiveOrientation` | (oneOf — see schema) | 0..1 | The descriptionOrientation:Primitive::CharacterString contains a textual specification of orientation, possibly refer… |

### `GSML_LinearOrientation`

A linear orientation is composed of a trend (the compass orientation of the line) and a plunge (the angle from the horizontal). This vector may be oriented (pointing in a specific direction) or not.

**Supertype**: [`GSML_GeometricDescriptionValue`](#GSML_GeometricDescriptionValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `directed` | (oneOf — see schema) | 0..1 | The directed:LinearDirectedCode property indicates if the orientation represents a linear feature that is directed, e… |
| `plunge` | (oneOf — see schema) | 0..1 | The property plunge (SWE::QuantityRange) reports the magnitude of the plunge as an angle from horizontal. |
| `trend` | (oneOf — see schema) | 0..1 | The property trend (SWE::QuantityRange) reports the azimuth (compass bearing) value of the linear orientation. |

### `GSML_PlanarOrientation`

A planar orientation is composed of two values; the azimuth (a compass point) and a dip (the angle from the horizontal). Polarity of the plane indicates whether the planar orientation is associated with a directed feature that is overturned, upright, vertical, etc. There are several conventions to encode a planar orientation and this specification does not impose one but provides a convention property to report it. It must be noted that allowance for different conventions makes manipulation of the data more difficult. Therefore it is recommended that user communities adopt a single measurement convention.

**Supertype**: [`GSML_GeometricDescriptionValue`](#GSML_GeometricDescriptionValue) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `convention` | (oneOf — see schema) | 0..1 | The property convention:ConventionCode contains the convention used for the measurement from a controlled vocabulary. |
| `azimuth` | (oneOf — see schema) | 0..1 | The azimuth (SWE::QuantityRange) property (compass point, bearing etc.) contains the value of the orientation. The co… |
| `dip` | (oneOf — see schema) | 0..1 | The dip (SWE::QuantityRange) reports the angle that the structural surface (e.g. bedding, fault plane) makes with the… |
| `polarity` | (oneOf — see schema) | 0..1 | The polarity:PolarityCode indicates whether the planar orientation is associated with a directed feature that is over… |

### `GSML_QuantityRange`

GSML_QuantityRange is a specialization of SWE Common QuantiytyRange (OGC 08-094r1, Clause 7.2.13) where lower and upper values are made explicit. SWE::QuantityRange uses an array of values (RealPair, see Clause 7.2.1) where the lowest value is the first element and the highest the second. This convenience data type has been created as an alternative encoding for implementations that do no support encoding of arrays in a single field (e.g. DBF) or reference to elements in string encoded arrays1 (eg. Filter Encoding Specification 2.0 – OGC 09-029r2). &nbsp;------------------------- 1 SWE RealPair is encoded as space delimited lists (&lt;swe:value&gt;10 300&lt;/swe:value&gt; in XML) , which demands that clients parse the string to extract each token. To build a WFS/FES query that tests the first element, it requires parsing the string either using string-before(swe:value,' ') or tokenize(swe:value,' '). This is cumbersome at best, or not even supported by the server at worst. 09-026r2 Clause 7.4.4 describes the minimal XPath supports and string parsing is not present.

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `lowerValue` | `number` | 1..1 | The property lowerValue:Real contains the lower bound of the range. It shall be a copy of inherited SWE::QuantityRang… |
| `upperValue` | `number` | 1..1 | The property upperValue:Real contains the upper bound of the range. It shall be a copy of inherited SWE::QuantityRang… |

### `GSML_Vector`

A GSML_Vector is a data type representing a linear orientation with a magnitude (a quantity assigned to this vector). If the magnitude is unknown, a GSML_LinearOrientation shall be used.

**Supertype**: [`GSML_LinearOrientation`](#GSML_LinearOrientation) (this BB).

Properties (own; inherited properties listed in supertype's BB):

| Name | Type | Mult | Notes |
| --- | --- | --- | --- |
| `magnitude` | (oneOf — see schema) | 0..1 | The magnitude property (SWE::QuantityRange) reports the magnitude of the vector. |

## Code lists

| Class | `codeList` vocab |
| --- | --- |
| `ConventionCode` | `_(treat as open — no `codeList` annotation)_` |
| `DeterminationMethodTerm` | `_(treat as open — no `codeList` annotation)_` |
| `LinearDirectedCode` | `_(treat as open — no `codeList` annotation)_` |
| `PlanarPolarityCode` | `_(treat as open — no `codeList` annotation)_` |

## External dependencies

- `https://schemas.opengis.net/sweCommon/3.0/json/QuantityRange.json`

## Examples

- [Minimal](examples/exampleGSML_DataTypesMinimal.json) — bare valid instance.
- [Complete](examples/exampleGSML_DataTypesComplete.json) — fully-populated example.

## Source

- UML: `geosciml4.1.xmi`, package `GSML_DataTypes`.
- Generator: [tools/ea_uml_to_ogc_schema.py](../../tools/ea_uml_to_ogc_schema.py).
- Resolver: [tools/resolve_geosci_schema.py](../../tools/resolve_geosci_schema.py).
