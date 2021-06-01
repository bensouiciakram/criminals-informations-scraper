import scrapy
from scrapy.loader import ItemLoader 
from criminals.items import CriminalsItem
from datetime import datetime
import pandas as pd 


class Site19Spider(scrapy.Spider):
    name = 'site19'
    allowed_domains = ['dfat.gov.au']
    start_urls = ['https://www.dfat.gov.au/sites/default/files/regulation8_consolidated.xls']

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        with open('list.xls','wb') as file :
            file.write(response.body)
        df = pd.read_excel('list.xls')
        for _,row in df.iterrows():
            loader = ItemLoader(CriminalsItem(),response)
            loader.add_value('full_name',row['Name of Individual or Entity'])
            loader.add_value('date_of_birth',self.get_date_of_birth(row['Date of Birth']))
            loader.add_value('country',row['Citizenship'])
            yield loader.load_item()


    def get_date_of_birth(self,date):
        if not isinstance(date,datetime):
            return date
        return '{}-{}-{}'.format(date.day,date.month,date.year)