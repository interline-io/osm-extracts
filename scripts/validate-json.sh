#!/bin/bash
npm install -g ajv-cli
ajv validate -s cities-schema.json -d cities.json --verbose