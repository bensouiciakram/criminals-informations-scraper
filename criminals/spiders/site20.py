import scrapy
import pandas as pd 
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem

class Site20Spider(scrapy.Spider):
    name = 'site20'
    allowed_domains = ['github.io']
    start_urls = ['http://everypolitician.github.io/everypolitician-names/names.csv']

    def parse(self, response):
        with open('names.csv','wb') as file :
            file.write(response.body)

        df = pd.read_csv('names.csv')
        for _,row in df.iterrows():
            loader = ItemLoader(CriminalsItem(),response)
            loader.add_value('full_name',row['name'])
            loader.add_value('country',row['country'])
            yield loader.load_item()