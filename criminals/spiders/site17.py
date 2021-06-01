import scrapy
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem

class Site17Spider(scrapy.Spider):
    name = 'site17'
    allowed_domains = ['ofsistorage.blob.core.windows.net']
    start_urls = ['https://ofsistorage.blob.core.windows.net/publishlive/ConList.xml']
    custom_settings = {
        'DOWNLOAD_MAXSIZE' : 0,
        'DOWNLOAD_TIMEOUT': 600,
        'FEED_URI':'{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        response.selector.register_namespace('data',"http://schemas.datacontract.org/2004/07/")
        items = response.xpath('//data:ConsolidatedList')
        for item in items:
            loader = ItemLoader(CriminalsItem(),item)
            loader.add_xpath('full_name','.//data:FullName/text()')
            loader.add_xpath('country','.//data:Country/text()')
            loader.add_xpath('gender','.//data:Gender/text()')
            loader.add_value('date_of_birth',self.get_date_of_birth(item))
            yield loader.load_item()


    def get_date_of_birth(self,item):
        day = item.xpath('.//data:DayOfBirth/text()').get()
        month = item.xpath('.//data:MonthOfBirth/text()').get()
        year = item.xpath('.//data:YearOfBirth/text()').get()
        if not day :
            day = ''
        if not month :
            month = ''
        if not year :
            year = ''
        return '{}-{}-{}'.format(day,month,year)