import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem


class Site14Spider(scrapy.Spider):
    name = 'site14'
    allowed_domains = ['europa.eu']
    start_urls = ['https://www.europarl.europa.eu/meps/en/full-list/']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopkrstuvwxyz'
        self.search_template = 'https://www.europarl.europa.eu/meps/en/full-list/xml/{}'

    def start_requests(self):
        for ch in self.alphabet:
            yield Request(
                self.search_template.format(ch),
                meta={
                    'character':ch
                }

            )

    def parse(self, response):
        persons = response.xpath('//mep')
        for person in persons: 
            loader = ItemLoader(CriminalsItem(),person)
            loader.add_xpath('full_name','.//fullname/text()')
            loader.add_xpath('country','.//country/text()')
            loader.add_value('source_url','https://www.europarl.europa.eu/meps/en/full-list/{}'.format(response.meta['character']))
            yield loader.load_item()
