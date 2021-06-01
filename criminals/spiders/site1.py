import scrapy
import json
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem



class Site1Spider(scrapy.Spider):
    name = 'site1'
    start_urls = ['https://api.fbi.gov/wanted/v1/list/']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        data = json.loads(response.text)
        items = data['items']
        for item in items :
            loader = ItemLoader(CriminalsItem(),response)
            loader.add_value('contry',item["nationality"])
            first_name = item['title'].split()[0]
            last_name = item['title'].split()[1]
            loader.add_value('first_name',first_name)
            loader.add_value('last_name',last_name)
            loader.add_value('gender',item['sex'])
            loader.add_value('source_url',item['url'])
            loader.add_value('dates_of_birth',item['dates_of_birth_used'])
            try:
                loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
            except:
                pass
            yield loader.load_item()


