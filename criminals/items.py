# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import country_converter as coco

def convert_to_iso3(country):
    return coco.convert(names=country,to='ISO3')


class CriminalsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    gender = scrapy.Field()
    country = scrapy.Field(
        output_processor = convert_to_iso3
    )
    date_of_birth = scrapy.Field()
    address = scrapy.Field()
    source_url  = scrapy.Field()
    age = scrapy.Field()    
    firm_name = scrapy.Field()
    full_name = scrapy.Field()

