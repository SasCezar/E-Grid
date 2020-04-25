import csv
import urllib

import names
import requests
import yaml

with open('../maps/azuremaps_config.yml', encoding="utf8") as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)

url = "https://atlas.microsoft.com/search/address/json?"

i = 900
addresses = {}
with open("hosp_and_others.csv", "rt", encoding="utf8") as inf, \
    open("../data/h_addresses.csv", "wt", encoding="utf8") as addf, \
    open("../data/hospitals.csv", "wt", encoding="utf8") as outf:

    reader = csv.reader(inf)
    awriter = csv.writer(addf)
    hwriter = csv.writer(outf)

    hospitals = {}
    params = {'subscription-key': configs['subscription_key'], "api-version": "1.0"}

    for line in reader:
        if not line[5] or line[5][0] not in ["3"]:
            continue

        name = line[6].title()
        if "osp" not in name.lower():
            continue

        if name in hospitals:
            continue

        hospitals[name] = []
        address = line[11].title()
        zipcode = line[13]
        city = line[14].title()

        try:
            params['query'] = ", ".join([name, address, zipcode, city])
            print(", ".join([name, address, zipcode, city]))
            encoded = urllib.parse.urlencode(params)

            request_url = url + encoded

            response = requests.get(request_url)

            results = response.json()['results']

            latitude = results[0]['position']['lat']
            longitude = results[0]['position']['lon']
            i +=1
            hospitals[name] = [name, i, names.get_full_name(), "Hospital"]

            awriter.writerow([i, address.replace("\"", "").replace(",", ""), city, "Lombardia", zipcode, "Italy", latitude, longitude])
            hwriter.writerow(hospitals[name])
        except Exception as message:
            print(f"Impossibile to get information because: {message}")

