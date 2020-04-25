import json

geo_obj = {"type":"FeatureCollection","metadata":{"title":"Companies Positions"}}

points = []
with open("../maps/data.json", "rt", encoding="utf8") as inf, \
        open("../static/my_locations.geojson", "wt", encoding="utf8") as outf:
    for line in inf:
        obj = json.loads(line)

        point = {"type": "Feature", "properties": {"type": obj['type'], "place": obj['name'].title()},
                 "geometry": {"type": "Point", "coordinates": [obj['longitude'], obj["latitude"]]}}

        points.append(point)

    geo_obj['features'] = points
    outf.write(json.dumps(geo_obj, ensure_ascii=False) + "\n")