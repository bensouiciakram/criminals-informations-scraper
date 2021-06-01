import scrapy
from scrapy.loader import ItemLoader 
from criminals.items import CriminalsItem

class Site5Spider(scrapy.Spider):
    name = 'site5'
    start_urls = ['https://scsanctions.un.org/resources/xml/en/consolidated.xml']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        persons = response.xpath('//INDIVIDUAL')
        for person in persons :
            loader = ItemLoader(CriminalsItem(),response)
            loader.add_value('first_name',person.xpath('.//FIRST_NAME/text()').get())
            loader.add_value('last_name',person.xpath('.//SECOND_NAME/text()').get())
            loader.add_value('gender',person.xpath('.//GENDER/text()').get())
            loader.add_value('country',person.xpath('.//NATIONALITY/VALUE/text()').get())
            loader.add_value('date_of_birth',person.xpath('.//INDIVIDUAL_DATE_OF_BIRTH/DATE/text()').get())
            loader.add_value('address','')
            loader.add_value('source_url',response.url)
            loader.add_value('age','')
            try:
                loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
            except:
                pass
            yield loader.load_item()


