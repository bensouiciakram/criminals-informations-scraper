import scrapy
from scrapy.loader import ItemLoader 
from criminals.items import CriminalsItem


class Site15Spider(scrapy.Spider):
    name = 'site15'
    allowed_domains = ['treasury.gov']
    start_urls = ['https://www.treasury.gov/ofac/downloads/consolidated/consolidated.xml']

    def parse(self, response):
        response.selector.register_namespace('data','http://tempuri.org/sdnList.xsd')
        items = response.xpath('//data:sdnEntry')
        for item in items :
            loader = ItemLoader(CriminalsItem(),item)
            loader.add_xpath('first_name','.//data:aka[1]//data:firstName[1]/text()')
            loader.add_xpath('last_name','.//data:aka[1]//data:lastName[1]/text()')
            loader.add_xpath('date_of_birth','.//data:dateOfBirth[1]/text()')
            loader.add_xpath('country','.//data:country//text()')
            yield loader.load_item()




