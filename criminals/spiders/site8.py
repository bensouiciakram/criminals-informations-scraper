import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem

class Site8Spider(scrapy.Spider):
    name = 'site8'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_Australian_criminals']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        data_lists = response.xpath('//ul')[1:16]
        criminals_urls = []
        for listing in data_lists:
            criminals_urls += listing.xpath('./li/a[1]/@href').getall()
        base_url = 'https://en.wikipedia.org'
        for url in criminals_urls :
            yield Request(
                base_url + url,
                callback = self.parse_infos
            )
        
    def parse_infos(self,response):
        loader = ItemLoader(CriminalsItem(),response)
        try:
            first_last = response.xpath('//th[@class="infobox-above"]//text()').get().split(' ',1)
            loader.add_value('first_name',first_last[0])
            loader.add_value('last_name',first_last[1])
        except:
            pass
        try:
            loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
        except:
            pass
        loader.add_value('gender','')
        loader.add_value('country','AUS')
        try:
            loader.add_value('date_of_birth',response.xpath('//th[contains(text(),"Born")]/following-sibling::td/text()')[-1].get())
        except:
            pass
        try:
            age = response.xpath('//th[contains(text(),"Born")]/following-sibling::td/span/text()')[-1].get()
            loader.add_value('age',age)
        except:
            pass
        loader.add_value('source_url',response.url)
        yield loader.load_item()