import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem

class Site11Spider(scrapy.Spider):
    name = 'site11'
    start_urls = ['https://www.saps.gov.za/crimestop/wanted/list.php']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }


    def parse(self, response):
        base_url = 'https://www.saps.gov.za/crimestop/wanted/'
        paths = response.xpath('//div[@class="col-md-14 cust-td-border"]//table//td//a/@href').getall()
        criminals_urls = [base_url + path for path in paths ]
        for url in criminals_urls :
            yield Request(
                url,
                callback=self.parse_infos
            )

    def parse_infos(self,response):
        loader = ItemLoader(CriminalsItem(),response)
        loader.add_value('first_name',response.xpath('//h2/text()')[0].get().split()[0])
        loader.add_value('last_name',response.xpath('//h2/text()')[0].get().split()[1])
        loader.add_xpath('gender','//table[@class="table table-bordered table-hover table-striped"]//b[contains(text(),"Gender")]/parent::td/following-sibling::td/text()')
        loader.add_value('country','ZAF')
        loader.add_value('address','')
        loader.add_value('date_of_birth','')
        loader.add_value('source_url',response.url)
        try:
            loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
        except:
            pass
        yield loader.load_item()
