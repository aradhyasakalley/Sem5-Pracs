data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [7.0, 51.0]
            },
            "properties": {
                "Name": "City A",
                "Population": 100000
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [8.5, 48.8]
            },
            "properties": {
                "Name": "City B",
                "Population": 80000
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [10.0, 53.5]
            },
            "properties": {
                "Name": "City C",
                "Population": 120000
            }
        }
    ]
}


# Printing features in a formatted way
features = data["features"]
for index, feature in enumerate(features):
    print(f"Feature {index+1}: {feature['properties']}")
