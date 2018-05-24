[![CircleCI](https://circleci.com/gh/interline-io/osm-extracts.svg?style=svg)](https://circleci.com/gh/interline-io/osm-extracts)

# OSM Extracts

This repository contains [a GeoJSON file](cities.json) that defines the bounding boxes for the cities and regions including the [OSM Extracts by Interline](https://www.interline.io/osm/extracts/) service.

## Propose changes

We welcome pull requests to add new regions or tweak existing ones. When proposing changes, please keep in mind that this service is meant to serve as many users as possible. We unfortunately do not have resources to create extracts for every possible slice of the world. 

If your change cannot be accepted, we suggest you use [PlanetUtils](https://github.com/interline-io/planetutils) to generate your own OSM extracts on your own local computer or server.

## History

OSM Extracts is inspired by Michal Migurski's [Extractotron](https://github.com/migurski/Extractotron) and Mapzen's [Metro Extracts](https://github.com/mapzen/metro-extracts) (both now defunct). This GeoJSON file was originally created from the [Mapzen Metro Extracts cities.json file](https://github.com/mapzen/metro-extracts/blob/master/cities.json) using a [conversion script](scripts/convert_cities.py). We've preserved the commit history of that file, so you can see [all the folks who have contributed to defining these regions over time](https://github.com/interline-io/osm-extracts/commits/master/cities.json).

## Licenses

As Mapzen Metro Extracts was released under the ISC license, we've done the same for this repository.

OSM Extracts by Interline also uses the PlanetUtils library; that is released under the MIT license.
