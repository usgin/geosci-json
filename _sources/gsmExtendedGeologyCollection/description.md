# gsmExtendedGeologyCollection

Extended-profile FeatureCollection. Accepts the full set of 9 Basic
featureType values (AnthropogenicGeomorphologicFeature, Contact, Fold,
Foliation, GeologicEvent, GeologicUnit, MappedFeature,
NaturalGeomorphologicFeature, ShearDisplacementStructure). Each
Feature additionally requires its description slot(s) to be concrete
Extension classes where one exists; FTs without an extension
description slot (Anthropogenic / NaturalGeomorphologicFeature,
MappedFeature) are pass-through.
