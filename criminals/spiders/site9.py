import scrapy
from scrapy import Request 
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem
from scrapy.shell import inspect_response


class Site9Spider(scrapy.Spider):
    name = 'site9'
    allowed_domains = ['international.gc.ca']
    start_urls = ['https://www.international.gc.ca/world-monde/assets/office_docs/international_relations-relations_internationales/sanctions/sema-lmes.xml']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }


    def parse(self, response):
        persons = response.xpath('//record')
        for person in persons:
            loader = ItemLoader(CriminalsItem(),person)
            loader.add_xpath('country','.//Country//text()')
            loader.add_xpath('last_name','.//LastName//text()')
            loader.add_xpath('first_name','.//GivenName//text()')
            loader.add_xpath('date_of_birth','.//DateOfBirth//text()')
            try:
                loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
            except:
                pass
            yield loader.load_item() 

