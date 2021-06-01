import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem
from scrapy_playwright.page import PageCoroutine
from scrapy.shell import inspect_response


class Site10Spider(scrapy.Spider):
    name = 'site10'
    allowed_domains = ['worldbank.org']
    start_urls = [
        'https://www.worldbank.org/en/projects-operations/procurement/debarred-firms',
        'https://apigwext.worldbank.org/dvsvc/v1.0/json/APPLICATION/ADOBE_EXPRNCE_MGR/FIRM/SANCTIONED_FIRM'
    ]
    headers = {
        'apikey':'z9duUaFUiEUYSHs97CU38fcZO7ipOPvm'
    }

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv',
    }

    def start_requests(self):
        yield Request(
            self.start_urls[0],
            )
        yield Request(
            self.start_urls[1],
            meta={
                'table':'api'
            },
            headers=self.headers
        )

    def parse(self, response):
        if response.meta.get('table',None):
            data = response.json()
            persons = data['response']['ZPROCSUPP']
            for person in persons: 
                loader = ItemLoader(CriminalsItem(),response)
                loader.add_value('country',person['COUNTRY_NAME'])
                loader.add_value('address',person['SUPP_ADDR'])
                loader.add_value('firm_name',person['SUPP_NAME'])
                yield loader.load_item()
        else:
            table2 = response.xpath('//table')[2]
            items = table2.xpath('.//tr[position() > 1]')
            for item in items:
                loader = ItemLoader(CriminalsItem(),item)
                loader.add_xpath('firm_name','./td[1]/p[1]/b/text()')
                loader.add_xpath('address','./td[1]/p[2]/text()')
                loader.add_xpath('country','.//td[1]/p[3]/b/text()')
                yield loader.load_item()

    