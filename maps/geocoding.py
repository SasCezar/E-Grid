import json
import urllib

import requests
import yaml


def geolocalize(configs):
    url = "https://atlas.microsoft.com/search/address/json?"

    params = {'subscription-key': configs['subscription_key'], "api-version": "1.0"}

    with open("poi/result_p&t.json", "rt", encoding="utf8") as inf, \
            open("geo_addresses.json", "wt", encoding="utf8") as outf:
        for line in inf:
            obj = json.loads(line)
            address = obj['address']
            cap = obj['cap']
            region = obj['region']
            state = obj['state']
            try:
                params['query'] = ", ".join([address, cap, region, state])

                encoded = urllib.parse.urlencode(params)

                request_url = url + encoded

                response = requests.get(request_url)

                results = response.json()['results']

                # response['results'][0]['address']['countrySecondarySubdivision']
                latitude = results[0]['position']['lat']
                longitude = results[0]['position']['lon']

                obj['latitude'] = latitude
                obj['longitude'] = longitude

                obj['type'] = "Pharmacy" if "farmaci" in obj['url'].lower() else "Textile"
                str_obj = json.dumps(obj, ensure_ascii=False)

                outf.write(str_obj + "\n")

            except Exception as message:
                print(f"Impossibile to get information because: {message}")


if __name__ == '__main__':
    with open('azuremaps_config.yml', encoding="utf8") as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)

    geolocalize(configs)
