import os
import sys
import json
import argparse

def load_cities(path):
    with open(path) as f:
        cities = json.load(f)

    features = []
    for city in cities:
        x1, y1, x2, y2 = [float(city['bbox'][k]) for k in ('left', 'bottom', 'right', 'top')]
        feature = dict(type='Feature', id=city['id'])
        feature['geometry'] = dict(type='Polygon')
        feature['geometry']['coordinates'] = [[[x1, y1], [x1, y2], [x2, y2], [x2, y1], [x1, y1]]]
        feature['properties'] = dict(name=city['name'])
        features.append(feature)
    return dict(type='FeatureCollection', features=features)

def write_extracts(path, fc):
    with open(path, 'wb') as f:
        json.dump(fc, f, sort_keys=True, indent=2)

if __name__ == "__main__":
    inpath = sys.argv[1]
    outpath = sys.argv[2]
    if os.path.exists(outpath):
        print "File exists, exiting: %s"%(outpath)
    else:
        write_extracts(outpath, load_cities(inpath))