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
