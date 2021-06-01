import scrapy
from scrapy.loader import ItemLoader 
from criminals.items import CriminalsItem
from itemloaders.processors  import TakeFirst


class Site16Spider(scrapy.Spider):
    name = 'site16'
    allowed_domains = ['treasury.gov']
    start_urls = ['https://www.treasury.gov/ofac/downloads/sdn.xml']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }    

    def parse(self, response):
        response.selector.register_namespace('data','http://tempuri.org/sdnList.xsd')
        items = response.xpath('//data:sdnEntry')
        for item in items :
            if not item.xpath('.//data:sdnType/text()').get() == 'Individual':
                continue
            loader = ItemLoader(CriminalsItem(),item)
            loader.add_xpath('first_name','.//data:aka[1]//data:firstName[1]/text()')
            loader.add_xpath('last_name','.//data:aka[1]//data:lastName[1]/text()')
            if not (loader._values.get('first_name',None) and loader._values.get('last_name',None) ):
                continue
            loader.add_value('full_name',loader._values['first_name'][0] +' '+ loader._values['last_name'][0])
            loader.add_xpath('date_of_birth','.//data:dateOfBirth[1]/text()',TakeFirst())
            loader.add_xpath('country','.//data:country[1]//text()',TakeFirst())
            if item.xpath('.//data:idType/text()').get() == 'Gender':
                loader.add_value('gender',self.get_gender(item))
            yield loader.load_item()


    def get_gender(self,item):
        gender = item.xpath('.//data:idNumber/text()').get().split(',')[0]
        return gender