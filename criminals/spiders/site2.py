import scrapy
from scrapy import Request
from criminals.items import CriminalsItem
from scrapy.loader import ItemLoader
import country_converter as coco

class Site2Spider(scrapy.Spider):
    name = 'site2'
    start_urls = ['http://ice.gov/most-wanted/']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        criminals_urls = response.xpath('//span[@class="field-content"]/a/@href').getall()
        for url in criminals_urls:
            yield Request(
                url,
                callback = self.parse_infos
            )

    def parse_infos(self,response):
        loader = ItemLoader(CriminalsItem(),response)

        first_name = response.xpath('//div[contains(text(),"Name")]/following-sibling::div/text()').get().split(',')[0]
        last_name = response.xpath('//div[contains(text(),"Name")]/following-sibling::div/text()').get().split(',')[1]
        loader.add_value('first_name',first_name)
        loader.add_value('last_name',last_name)
        loader.add_xpath('gender','//div[contains(text(),"Gender")]/following-sibling::div/text()')
        loader.add_xpath('country','//div[contains(text(),"Place of Birth")]/following-sibling::div/text()')
        loader.add_value('source_url',response.url)
        loader.add_value('address','')
        loader.add_value('date_of_birth','')
        loader.add_xpath('age','//div[contains(text(),"Age")]/following-sibling::div/text()')
        try:
            loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
        except:
            pass
        yield loader.load_item()
