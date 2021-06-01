import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem


class Site4Spider(scrapy.Spider):

    name = 'site4'
    start_urls = ['https://nationalcrimeagency.gov.uk/most-wanted-search']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        base_url = 'https://www.nationalcrimeagency.gov.uk'
        criminals_relative_urls = response.xpath('//div[@class="pull-none item-image"]/a/@href').getall()
        criminals_urls = [base_url + url for url in criminals_relative_urls]
        for url in criminals_urls :
            yield Request(
                    url,
                    callback=self.parse_infos
            )
    def parse_infos(self,response):
        loader = ItemLoader(CriminalsItem(),response)
        loader.add_value('source_url',response.url)
        first_name = response.xpath('//h2[@itemprop="headline"]/text()').get().strip().split(' ',1)[0]
        last_name = response.xpath('//h2[@itemprop="headline"]/text()').get().strip().split(' ',1)[1]
        loader.add_value('first_name',first_name)
        loader.add_value('last_name',last_name)
        loader.add_xpath('gender','//span[contains(text(),"Sex")]/following-sibling::span[1]/text()')
        loader.add_xpath('address','//span[contains(text(),"Location")]/following-sibling::span[1]/text()')
        loader.add_value('date_of_birth','')
        loader.add_value('age','')
        try:
            loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
        except:
            pass
        yield loader.load_item()