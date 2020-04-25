import csv
import json

import names

mappings = {}
i = 100
with open("../maps/geo_addresses.json", "rt", encoding="utf8") as inf, \
    open("../data/poi.csv", "wt", encoding="utf8") as poif, \
    open("../data/producer.csv", "wt", encoding="utf8") as prodf, \
    open("../data/addresses.csv", "wt", encoding="utf8") as addf:

    poi_writer = csv.writer(poif)
    prod_writer = csv.writer(prodf)
    add_writer = csv.writer(addf)
    for line in inf:
        obj = json.loads(line)
        address = obj['address']
        if address not in mappings:
            city = obj['city']
            state = obj['state']
            zipcode = obj['cap']
            country = obj['country']

            lat = obj['latitude']
            lon = obj['longitude']
            i += 1
            mappings[address] = [i, address, city, state, zipcode, country, lat, lon]

        add_id = mappings[address][0]

        if obj['type'] == "Pharmacy":
            poi_writer.writerow([obj['name'].replace("\"", ""), add_id, names.get_full_name(),obj["type"]])
        else:
            if obj["type"] == 1:
                obj["type"] = "Electronics"
            prod_writer.writerow([obj['name'].replace("\"", ""), add_id, obj['type']])

    for address in mappings:
        add_writer.writerow(mappings[address])
