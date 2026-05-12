
# gsmBasicGeologyCollection (Schema)

`usgin.bbr.geosci.gsmBasicGeologyCollection` *v0.1*

Basic-profile FeatureCollection. Accepts GeologicUnit, MappedFeature,

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# gsmBasicGeologyCollection

Basic-profile FeatureCollection. Accepts GeologicUnit, MappedFeature,
and the four concrete GeologicStructure subtypes (Contact, Fold,
Foliation, ShearDisplacementStructure). Each item is validated against
its anchor in gsmscimlBasic. EarthMaterial is omitted (UML «Type», not
«FeatureType»).

## Examples

### fc contacts complex GSO
Adapted from Loop3D-GSO/Examples/GSO-ExampleComplexContacts.ttl — all 7 contacts in the worked scenario. Geologic context: the Js Formation (Jurassic sediments) unconformably overlies tilted Paleozoic strata (Os, Ss Formations) that overlie Early Proterozoic Xm metamorphic basement. A Cretaceous granite (Kg) and a Cretaceous diorite dike (Kd) intrude Js and the older units. After igneous activity, erosion exhumed the section, and Late Miocene Ms sediment was deposited on top, sealing the unconformity. The 7 contact features below capture each rock-body interface with its inferred contact type. Homogeneous FeatureCollection (collection-level featureType="Contact"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleComplexContacts.ttl — all 7 contacts in the worked scenario. Geologic context: the Js Formation (Jurassic sediments) unconformably overlies tilted Paleozoic strata (Os, Ss Formations) that overlie Early Proterozoic Xm metamorphic basement. A Cretaceous granite (Kg) and a Cretaceous diorite dike (Kd) intrude Js and the older units. After igneous activity, erosion exhumed the section, and Late Miocene Ms sediment was deposited on top, sealing the unconformity. The 7 contact features below capture each rock-body interface with its inferred contact type. Homogeneous FeatureCollection (collection-level featureType=\"Contact\"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).",
  "type": "FeatureCollection",
  "featureType": "Contact",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "contact.JsOnOs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Js overlies Os — angular unconformity",
        "description": "Angular unconformable contact: Jurassic Js Formation deposited on the erosional surface of Ordovician Os Formation (sedimentary). The OsBoundary-6_2 surface in the source ontology is an Erosional Surface; tilted Paleozoic strata are truncated and the Jurassic sediments rest with angular discordance on the eroded substrate.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preJurassicErosion.Os",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Jurassic erosion truncating Os Formation",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          },
          {
            "type": "Feature",
            "id": "JsDeposition.OnOs",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Js Formation deposition over Os",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/EarlyJurassic",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/LateJurassic"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/OsFormation", "title": "Os Formation (Ordovician) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/angular_unconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.JsOnSs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Js overlies Ss — angular unconformity",
        "description": "Angular unconformable contact: Jurassic Js Formation deposited on the erosional surface of Silurian Ss Formation (sedimentary). The SsBoundary-6_1 surface in the source ontology is an Erosional Surface.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preJurassicErosion.Ss",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Jurassic erosion truncating Ss Formation",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/SsFormation", "title": "Ss Formation (Silurian) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/angular_unconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.JsOnXm",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Js on Xm nonconformity",
        "description": "Nonconformable contact: Jurassic Js Formation (sedimentary) deposited on the eroded surface of the Early Proterozoic Xm Rock Body (medium-grade gneiss). The older surface records pre-Jurassic erosion of crystalline basement.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preJurassicErosion.Xm",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Jurassic erosion of Xm basement",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/XmRockBody", "title": "Xm Rock Body (Early Proterozoic gneiss) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/nonconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.KdInJs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Kd dike intrudes Js — igneous intrusive contact",
        "description": "Igneous intrusive contact: a Cretaceous diorite dike (Kd) cuts the Jurassic Js Formation. In the source ontology this contact is hosted on multiple rock-body boundaries (KdBoundaryInJs-3_1_4, KdBoundaryInJs-3_2_4, etc.) defining the upper and lower walls of the dike where it intrudes Js. Diorite grain size ~0.05 mm (mean).",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "KdIntrusion",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Cretaceous diorite dike emplacement",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/intrusion"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/EarlyCretaceous",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/LateCretaceous"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/KdDike",      "title": "Kd Mafic Dike (Cretaceous) — younger host (intrusive)", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — older host (country rock)", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/igneous_intrusive_contact",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.KgInJs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Kg granite intrudes Js — igneous intrusive contact",
        "description": "Igneous intrusive contact: a Cretaceous granite (Kg) pluton intrudes the Jurassic Js Formation. Source ontology hosts this contact on KgIntrusiveBoundary-4_2 and KgBoundaryIntrudesJs-4_2. Granite grain size ~5 mm (mean).",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "KgIntrusion",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Cretaceous granite pluton emplacement",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/intrusion"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/EarlyCretaceous",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/LateCretaceous"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/KgGranite",   "title": "Kg Granite (Cretaceous) — younger host (intrusive)", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — older host (country rock)", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/igneous_intrusive_contact",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.MsOnJs",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Ms overlies Js — disconformity",
        "description": "Disconformable depositional contact: Late Miocene Ms Formation deposited on the eroded top surface of Jurassic Js Formation (topJs-2_1, an erosional surface). The two units are roughly parallel (no major angular discordance) but separated by a large hiatus from the Cretaceous through most of the Tertiary.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preMioceneErosion.Js",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Miocene erosion of Js, Kg, and Kd",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          },
          {
            "type": "Feature",
            "id": "MsDeposition.OnJs",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Late Miocene deposition of Ms over Js",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tortonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Messinian"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/MsFormation", "title": "Ms Formation (Late Miocene) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/JsFormation", "title": "Js Formation (Jurassic) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/disconformity",
        "stContactDescription": null
      }
    },
    {
      "type": "Feature",
      "id": "contact.MsOnKg",
      "featureType": "Contact",
      "geometry": null,
      "properties": {
        "name": "Ms overlies Kg — nonconformity",
        "description": "Nonconformable contact: Late Miocene Ms Formation deposited on an erosion surface developed across the Cretaceous Kg granite (KgBoundaryErosionSurface-2_3). Sedimentary on plutonic igneous — classical nonconformity.",
        "purpose": "instance",
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "preMioceneErosion.Kg",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Pre-Miocene erosion exhuming Kg granite",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/erosion"
              ]
            }
          },
          {
            "type": "Feature",
            "id": "MsDeposition.OnKg",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Late Miocene deposition of Ms over Kg",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Tortonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Messinian"
            }
          }
        ],
        "relatedFeature": [
          { "href": "https://example.org/loop3d/MsFormation", "title": "Ms Formation (Late Miocene) — younger host", "rel": "youngerHost" },
          { "href": "https://example.org/loop3d/KgGranite",   "title": "Kg Granite (Cretaceous) — older host", "rel": "olderHost" }
        ],
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/nonconformity",
        "stContactDescription": null
      }
    }
  ]
}

```


### fc geologicunit from OGC
Example instance: fc_geologicunit_from_OGC
#### json
```json
{
  "type": "FeatureCollection",
  "featureType": "GeologicUnit",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "hervey-group-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "occurrence": [
          {
            "href": "http://data.geoscience.gov.au/mappedfeature/polygon/6735427298",
            "title": "Mapped occurrence on 1:250000 sheet"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "featureType": "GeologicEvent",
            "id": "hervey-group-depositional-age",
            "geometry": null,
            "place": null,
            "time": null,
            "properties": {
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Frasnian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Famennian"
            }
          }
        ],
        "composition": [
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "hervey-group-fc-sandstone",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
              }
            },
            "proportion": {
              "type": "QuantityRange",
              "uom": {
                "code": "%"
              },
              "value": [
                50.0,
                95.0
              ],
              "definition": "http://resource.geosciml.org/property/proportion",
              "label": "proportion"
            }
          },
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "hervey-group-fc-mudstone",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
              }
            },
            "proportion": {
              "type": "QuantityRange",
              "uom": {
                "code": "%"
              },
              "value": [
                5.0,
                50.0
              ],
              "definition": "http://resource.geosciml.org/property/proportion",
              "label": "proportion"
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "boulton-formation-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "boulton-formation-fc-conglomerate",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/conglomerate"
              }
            }
          }
        ]
      }
    }
  ]
}

```


### fc geologicunits BritishColumbia
Adapted from Loop3D-GSO/Examples/GSO-ExampleBritishColumbiaStrat-v2.ttl — the Lardeau Group of the Kootenay Terrane (southeastern British Columbia), with its three known constituent formations (Akolkolex, Index, Jowett). The Lardeau Group is a Lower Paleozoic metasedimentary–metavolcanic assemblage that has been deformed and metamorphosed to greenschist facies. The source TTL is structurally simpler than the Isle of Wight TTL — it records unit type, label, list of constituent lithologies, and parent–child relationships, but not thickness, depositional setting, age, or bibliographic sources. The FeatureCollection therefore omits those slots. Constituent proportions are not recorded in the TTL (no qualitative Dominant/Subordinate terms either), so `proportion` is left null on every CompositionPart. Homogeneous FeatureCollection (collection-level featureType="GeologicUnit"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleBritishColumbiaStrat-v2.ttl — the Lardeau Group of the Kootenay Terrane (southeastern British Columbia), with its three known constituent formations (Akolkolex, Index, Jowett). The Lardeau Group is a Lower Paleozoic metasedimentary–metavolcanic assemblage that has been deformed and metamorphosed to greenschist facies. The source TTL is structurally simpler than the Isle of Wight TTL — it records unit type, label, list of constituent lithologies, and parent–child relationships, but not thickness, depositional setting, age, or bibliographic sources. The FeatureCollection therefore omits those slots. Constituent proportions are not recorded in the TTL (no qualitative Dominant/Subordinate terms either), so `proportion` is left null on every CompositionPart. Homogeneous FeatureCollection (collection-level featureType=\"GeologicUnit\"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch).",
  "type": "FeatureCollection",
  "featureType": "GeologicUnit",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "LardeauGroup",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Lardeau Group",
        "description": "A Lower Paleozoic metasedimentary–metavolcanic group of the Kootenay Terrane, southeastern British Columbia. Includes the Akolkolex, Index and Jowett Formations. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "hierarchyLink": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": { "href": "#AkolkolexFormation", "title": "Akolkolex Formation", "rel": "containsFormation" }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": { "href": "#IndexFormation",     "title": "Index Formation",     "rel": "containsFormation" }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": { "href": "#JowettFormation",    "title": "Jowett Formation",    "rel": "containsFormation" }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "AkolkolexFormation",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Akolkolex Formation",
        "description": "Constituent formation of the Lardeau Group. Quartzose clastic metasediments — arenite and quartzite lithologies. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/arenite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/quartzite"
            },
            "proportion": null
          }
        ],
        "relatedFeature": [
          { "href": "#LardeauGroup", "title": "Lardeau Group — Akolkolex is a constituent formation", "rel": "isPartOf" }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "IndexFormation",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Index Formation",
        "description": "Constituent formation of the Lardeau Group. Heterolithic metasedimentary unit with arenite, chemical sedimentary material, chlorite–actinolite–epidote metamorphic rock, limestone, marble, undifferentiated metamorphic rock, metasomatic rock, phyllite, quartzite and schist. The breadth of lithologies reflects greenschist-facies metamorphism of a mixed sedimentary–volcaniclastic protolith. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/arenite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/chemical_sedimentary_material"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/marble"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/metamorphic_rock"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/metasomatic_rock"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/phyllite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/quartzite"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/schist"
            },
            "proportion": null
          }
        ],
        "relatedFeature": [
          { "href": "#LardeauGroup", "title": "Lardeau Group — Index is a constituent formation", "rel": "isPartOf" }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "JowettFormation",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Jowett Formation",
        "description": "Constituent formation of the Lardeau Group. Metamorphosed pelitic and metasomatic rocks — schist and metasomatic rock lithologies. Source: GSO Example British Columbia Stratigraphy v2 (Loop3D-GSO).",
        "purpose": "instance",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/metasomatic_rock"
            },
            "proportion": null
          },
          {
            "role": null,
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/schist"
            },
            "proportion": null
          }
        ],
        "relatedFeature": [
          { "href": "#LardeauGroup", "title": "Lardeau Group — Jowett is a constituent formation", "rel": "isPartOf" }
        ]
      }
    }
  ]
}

```


### fc geologicunits IsleOfWight
Adapted from Loop3D-GSO/Examples/GSO-ExampleIsleOfWightStrat-pm1-v2.ttl — a subset of the BGS Isle of Wight stratigraphy showing the Solent Group (SOLT) with two constituent formations (BEL, BOUL) and one basal member (BMBG of BOUL). Demonstrates Group→Formation→Member hierarchy plus stratigraphic `overlies` relationships. Homogeneous FeatureCollection (collection-level featureType="GeologicUnit"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch). Qualitative proportions from the TTL (Dominant_Proportion / Subordinate_Proportion) are translated to approximate QuantityRange % values. Thickness measurements from the TTL are kept only as prose in `description` since Basic GeologicUnit has no thickness slot (that lives in GeoSciML Extension's GeologicUnitDescription).
#### json
```json
{
  "$comment": "Adapted from Loop3D-GSO/Examples/GSO-ExampleIsleOfWightStrat-pm1-v2.ttl — a subset of the BGS Isle of Wight stratigraphy showing the Solent Group (SOLT) with two constituent formations (BEL, BOUL) and one basal member (BMBG of BOUL). Demonstrates Group→Formation→Member hierarchy plus stratigraphic `overlies` relationships. Homogeneous FeatureCollection (collection-level featureType=\"GeologicUnit\"). Validates against schemas/json/4.1/geosciml_basic_featurecollection.json#FeatureCollection (then-branch dispatch). Qualitative proportions from the TTL (Dominant_Proportion / Subordinate_Proportion) are translated to approximate QuantityRange % values. Thickness measurements from the TTL are kept only as prose in `description` since Basic GeologicUnit has no thickness slot (that lives in GeoSciML Extension's GeologicUnitDescription).",
  "type": "FeatureCollection",
  "featureType": "GeologicUnit",
  "conformsTo": [
    "https://ext.iide.dev/schemas/geosciml/basic/4.1/json/features.json/4.1/geosciml_basic_featurecollection.json"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "SOLT",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Solent Group",
        "description": "Interbedded silty clays, calcareous clays and limestone; predominantly non-marine, freshwater to brackish water, fluvial/terrestrial; locally fully marine. Regional Isle of Wight thickness 0–200 m (not proved in PM1 borehole). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/SOLT. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Solent Group (SOLT)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/SOLT"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for dominant constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for subordinate constituent — limestone (LMST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/LMST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/subordinate",
              "label": "qualitative — subordinate proportion; numeric range 5–25 % is a placeholder. Source TTL records only the qualitative term gsoc:Subordinate_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [5, 25]
            }
          }
        ],
        "hierarchyLink": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": {
              "href": "#BEL",
              "title": "Bembridge Limestone Formation (BEL)",
              "rel": "containsFormation"
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": {
              "href": "#BOUL",
              "title": "Bouldnor Formation (BOUL)",
              "rel": "containsFormation"
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BA",
            "title": "Barton Group (BA) — Solent Group overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "SOLT.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Priabonian",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "lacustrine setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine"
                },
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "fluvial / river plain setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/river-plain"
                },
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "marine setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/marine"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "BEL",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Bembridge Limestone Formation, Solent Group",
        "description": "Shallow freshwater & subaerial; shelly limestone with interbedded mudstone. Regional IOW thickness 0–85 m (not proved in PM1). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BEL. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Bembridge Limestone Formation (BEL)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BEL"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for dominant constituent — limestone (LMST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/LMST"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for subordinate constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/subordinate",
              "label": "qualitative — subordinate proportion; numeric range 5–25 % is a placeholder. Source TTL records only the qualitative term gsoc:Subordinate_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [5, 25]
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "#SOLT",
            "title": "Solent Group — BEL is a constituent formation",
            "rel": "isPartOf"
          },
          {
            "href": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/HEHI",
            "title": "Headon Hill Formation (HEHI) — BEL overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "BEL.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Priabonian (BEL)",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "lacustrine setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine"
                },
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "subaerial setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/subaerial"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "BOUL",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Bouldnor Formation, Solent Group",
        "description": "Brackish/freshwater with pedogenized clays; interbedded clay and silt with organic beds. Swamp/marsh depositional setting. Regional IOW thickness 0–11 m (not proved in PM1). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BOUL. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Bouldnor Formation (BOUL)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BOUL"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for main body constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/formation",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/main_body",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          }
        ],
        "hierarchyLink": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/geologicunitpartrole/constituent_unit",
            "targetUnit": {
              "href": "#BMBG",
              "title": "Bembridge Marls Member (BMBG)",
              "rel": "containsMember"
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "#SOLT",
            "title": "Solent Group — BOUL is a constituent formation",
            "rel": "isPartOf"
          },
          {
            "href": "#BEL",
            "title": "Bembridge Limestone Formation — BOUL overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "BOUL.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Rupelian (BOUL)",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Rupelian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Rupelian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "swamp or marsh setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/swamp-or-marsh"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "id": "BMBG",
      "featureType": "GeologicUnit",
      "geometry": null,
      "properties": {
        "name": "Bembridge Marls Member of Bouldnor Formation, Solent Group",
        "description": "Mudstone-dominated with subordinate limestone interbeds; includes sands and is shelly. Marginal-marine to non-marine, shoreline setting. Regional IOW thickness 0–34 m (not proved in PM1). BGS Lexicon: https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BMBG. Sources: Hooker et al. (2009) doi:10.1130/2009.2452(12); BGS Geology of England and Wales Cookbook doi:10.1144/GOEWP; ISBN 9780751837773; ISBN 9780852727720.",
        "purpose": "instance",
        "classifier": [
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "label": "BGS Lexicon NamedRockUnit — Bembridge Marls Member (BMBG)",
            "codeSpace": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit",
            "value": "https://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/BMBG"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for dominant constituent — silty mudstone (SLMDST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/SLMDST"
          },
          {
            "type": "Category",
            "definition": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "label": "BGS earth material class for subordinate constituent — limestone (LMST)",
            "codeSpace": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName",
            "value": "https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/LMST"
          }
        ],
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/member",
        "composition": [
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/mudstone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/dominant",
              "label": "qualitative — dominant proportion; numeric range 50–95 % is a placeholder. Source TTL records only the qualitative term gsoc:Dominant_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [50, 95]
            }
          },
          {
            "role": "http://resource.geosciml.org/classifier/cgi/compoundmaterialconstituentpartrole/interbedded_part",
            "material": {
              "properties": { "purpose": "typicalNorm" },
              "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/limestone"
            },
            "proportion": {
              "type": "QuantityRange",
              "definition": "http://resource.geosciml.org/concept/proportion/subordinate",
              "label": "qualitative — subordinate proportion; numeric range 5–25 % is a placeholder. Source TTL records only the qualitative term gsoc:Subordinate_Proportion, with no measured percentage.",
              "uom": { "code": "%" },
              "value": [5, 25]
            }
          }
        ],
        "relatedFeature": [
          {
            "href": "#BOUL",
            "title": "Bouldnor Formation — BMBG is a constituent member (basal)",
            "rel": "isPartOf"
          },
          {
            "href": "#BEL",
            "title": "Bembridge Limestone Formation — BMBG overlies",
            "rel": "overlies"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "id": "BMBG.deposition",
            "featureType": "GeologicEvent",
            "geometry": null,
            "properties": {
              "name": "Deposition during Priabonian (BMBG)",
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/deposition"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Priabonian",
              "eventEnvironment": [
                {
                  "type": "Category",
                  "definition": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "label": "shoreline setting",
                  "codeSpace": "http://resource.geosciml.org/classifier/cgi/eventenvironment",
                  "value": "http://resource.geosciml.org/classifier/cgi/eventenvironment/shoreline"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}

```


### fc mixed from OGC
Example instance: fc_mixed_from_OGC
#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "featureType": "GeologicUnit",
      "id": "hervey-group-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "typicalNorm",
        "geologicUnitType": "http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit",
        "rank": "http://resource.geosciml.org/classifier/cgi/stratigraphicrank/group",
        "composition": [
          {
            "role": "http://inspire.ec.europa.eu/codelist/CompositionPartRoleValue/unspecifiedPartRole",
            "material": {
              "type": "Feature",
              "featureType": "RockMaterial",
              "id": "mixed-fc-sandstone",
              "geometry": null,
              "place": null,
              "time": null,
              "properties": {
                "lithology": "http://resource.geosciml.org/classifier/cgi/simplelithology/sandstone"
              }
            }
          }
        ]
      }
    },
    {
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "mappedfeature-gu-1",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              149.12,
              -35.31
            ],
            [
              149.45,
              -35.31
            ],
            [
              149.45,
              -35.58
            ],
            [
              149.12,
              -35.58
            ],
            [
              149.12,
              -35.31
            ]
          ]
        ]
      },
      "place": null,
      "time": null,
      "properties": {
        "resolutionRepresentativeFraction": 250000,
        "mappingFrame": "http://resource.geoscience.gov.au/vocabulary/mappingframe/top-of-bedrock",
        "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/exposed",
        "specification": {
          "href": "http://data.geoscience.gov.au/feature/geologicunit/hervey-group-1",
          "title": "Hervey Group"
        }
      }
    },
    {
      "type": "Feature",
      "featureType": "ShearDisplacementStructure",
      "id": "lake-george-fault-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "occurrence": [
          {
            "href": "http://data.geoscience.gov.au/mappedfeature/line/lake-george-fault-mf-1",
            "title": "Lake George Fault trace"
          }
        ],
        "geologicHistory": [
          {
            "type": "Feature",
            "featureType": "GeologicEvent",
            "id": "lake-george-fault-age",
            "geometry": null,
            "place": null,
            "time": null,
            "properties": {
              "eventProcess": [
                "http://resource.geosciml.org/classifier/cgi/eventprocess/faulting"
              ],
              "olderNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Devonian",
              "youngerNamedAge": "http://resource.geosciml.org/classifier/ics/ischart/Carboniferous"
            }
          }
        ],
        "faultType": "http://resource.geosciml.org/classifier/cgi/faulttype/normal_fault"
      }
    },
    {
      "type": "Feature",
      "featureType": "MappedFeature",
      "id": "mappedfeature-fault-1",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            149.387,
            -35.124
          ],
          [
            149.412,
            -35.198
          ],
          [
            149.435,
            -35.271
          ],
          [
            149.461,
            -35.344
          ]
        ]
      },
      "place": null,
      "time": null,
      "properties": {
        "positionalAccuracy": {
          "type": "Quantity",
          "uom": {
            "code": "m"
          },
          "value": 250.0,
          "definition": "http://www.opengis.net/def/property/OGC/0/PositionalAccuracy",
          "label": "positional accuracy"
        },
        "resolutionRepresentativeFraction": 250000,
        "mappingFrame": "http://resource.geoscience.gov.au/vocabulary/mappingframe/earth-surface",
        "exposure": "http://resource.geosciml.org/classifier/cgi/exposure/exposed",
        "specification": {
          "href": "http://data.geoscience.gov.au/feature/fault/lake-george-fault-1",
          "title": "Lake George Fault"
        }
      }
    },
    {
      "type": "Feature",
      "featureType": "Contact",
      "id": "contact-devonian-basement-1",
      "geometry": null,
      "place": null,
      "time": null,
      "properties": {
        "purpose": "instance",
        "contactType": "http://resource.geosciml.org/classifier/cgi/contacttype/unconformity"
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://schemas.usgin.org/geosci-json/gsmBasicGeologyCollection/gsmBasicGeologyCollectionSchema.json
description: "Basic-profile FeatureCollection. Accepts GeologicUnit, MappedFeature,\nand
  the four concrete GeologicStructure subtypes (Contact, Fold,\nFoliation, ShearDisplacementStructure).
  Each item is validated against\nits anchor in gsmscimlBasic. EarthMaterial is omitted
  (UML \xABType\xBB, not\n\xABFeatureType\xBB)."
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
            $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#GeologicUnit
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
            $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#Contact
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Fold
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#Fold
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: Foliation
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#Foliation
        - if:
            required:
            - featureType
            properties:
              featureType:
                const: ShearDisplacementStructure
          then:
            $ref: https://usgin.github.io/geosci-json/_sources/gsmscimlBasic/gsmscimlBasicSchema.json#ShearDisplacementStructure
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

* YAML version: [schema.yaml](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmBasicGeologyCollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geosci-json/build/annotated/bbr/geosci/gsmBasicGeologyCollection/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geosci-json/_sources/gsmBasicGeologyCollection/context.jsonld)

## Sources

* [GeoSciML 4.1 — FC profile composed across building blocks](https://github.com/usgin/geosci-json/blob/main/bb-grouping.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geosci-json](https://github.com/usgin/geosci-json)
* Path: `_sources/gsmBasicGeologyCollection`

