import scrapy
from scrapy import Request 
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem
from scrapy.shell import inspect_response



class Site21Spider(scrapy.Spider):
    name = 'site21'
    allowed_domains = ['sesam.search.admin.ch']
    start_urls = ['http://sesam.search.admin.ch/']

    def __init__(self):
        self.search_ids = [20,14,38,35,10,11,16,19,8,15,4,40,42,12,34,18,37,9,21]
        self.search_template = 'https://www.sesam.search.admin.ch/sesam-search-web/pages/search.xhtml?Applikations-Version=1.2.0-60&lang=en&nameNamensteile=&volltextsuche=&sanktionsprogrammId={}&adressatTyp=PERSON&action=searchAction'

    def start_requests(self):
        for id in self.search_ids :
            yield Request(
                self.search_template.format(id)
            )

    def parse(self, response):
        items = response.xpath('//table[@class="trefferliste"]//tr[position()>1]')
        for item in items:
            person = item.xpath('./td[1]//text()').get()
            if not person:
                continue
            loader = ItemLoader(CriminalsItem(),item)
            loader.add_value('full_name',person)
            loader.add_xpath('country','./td[3]//text()')
            yield loader.load_item()
