data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [122.0, 10.0],
            },
            "properties": {
                "Name": "RedwoodCity",
                "time": 14.0,
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [102.0, 0.0],
                    [103.0, 1.0],
                    [104.0, 0.0],
                    [105.0, 1.0],
                ],
            },
            "properties": {
                "Name": "USA",
                "time": 24.0,
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [100.0, 0.0],
                        [101.0, 0.0],
                        [101.0, 1.0],
                        [100.0, 1.0],
                        [100.0, 0.0],
                    ],
                ],
            },
            "properties": {
                "Name": "Ghatkopar",
                "prop1": {"this": "that"},
                "time": 15.0,
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [115.0, 20.0],
            },
            "properties": {
                "Name": "HongKong",
                "time": 25.0,
            },
        },
    ],
}

# Printing features in a formatted way
features = data["features"]
for index, feature in enumerate(features):
    print(f"Feature {index+1}: {feature['properties']}")
