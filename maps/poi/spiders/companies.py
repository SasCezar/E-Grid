import scrapy


class POISpider(scrapy.Spider):
    name = "POI"
    site_url = "https://www.informazione-aziende.it"
    base_ulrs = {"https://www.informazione-aziende.it/13_INDUSTRIE-TESSILI/Regione_LOMBARDIA?qPg=": 20,
                 "https://www.informazione-aziende.it/47-73-1_FARMACIE/Regione_LOMBARDIA?qPg=": 16}

    def start_requests(self):
        urls = [url + str(i + 1) for url in self.base_ulrs for i in range(self.base_ulrs[url])]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url

        companies = response.xpath('//span[@class="text-capitalize"]/a/@href').getall()

        if companies:
            for company in companies:
                yield scrapy.Request(url=self.site_url + company, callback=self.parse)

        address = response.xpath('//span[@class="street-address"]/text()').get()
        if address:
            name = response.xpath('//span[@itemprop="name"]/text()').get().strip()
            city = response.xpath('//span[@class="locality"]/text()').get().strip()
            cap = response.xpath('//span[@class="postal-code"]/text()').get().strip()
            region = response.xpath('//span[@class="region"]/text()').get().strip()
            state = response.xpath('//td[@data-title="Regione"]/text()').get().strip()
            country = response.xpath('//span[@class="country-name"]/text()').get().strip()
            page = {"url": url, "html": response.text, "name": name, "address": address,
                    "city": city, "cap": cap, "region": region, "state": state, "country": country}

            yield page
