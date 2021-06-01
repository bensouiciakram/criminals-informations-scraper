import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader 
from criminals.items import CriminalsItem


class Site13Spider(CrawlSpider):
    name = 'site13'
    allowed_domains = ['cia.gov']
    start_urls = ['https://www.cia.gov/resources/world-leaders/foreign-governments']

    rules = (
        Rule(LinkExtractor(allow=r'resources/government/'), callback='parse_item', follow=True),
    )

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }


    def parse_item(self, response):
        country = response.url.split('/')[-2]
        names = response.xpath('//div[@class="free-form-content__content wysiwyg-wrapper"]//p/text()').getall()
        for name in names :
            loader =  ItemLoader(CriminalsItem(),response)
            loader.add_value('source_url',response.url)
            loader.add_value('country',country)
            loader.add_value('full_name',name)
            yield loader.load_item()
