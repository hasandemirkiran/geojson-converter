import geojson
import pprint

def main():
    path_to_file = '/home/hasan/Desktop/OCELL/GVM-converter/GVM-data/Stand.geojson'
    with open(path_to_file) as f:
        gj = geojson.load(f)

    features = gj['features']

    for feature in features:
        features['properties'] = {
            'Stand ID': feature['properties']['STAND_'],

        }

if __name__ == '__main__':
    main()