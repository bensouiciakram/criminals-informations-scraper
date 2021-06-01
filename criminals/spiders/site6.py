import scrapy
import chompjs
from scrapy import Request
from scrapy.loader import ItemLoader
from criminals.items import CriminalsItem


class Site6Spider(scrapy.Spider):

    name = 'site6'  
    start_urls = ['https://ws-public.interpol.int/notices/v1/red?&resultPerPage=160&page=1']

    # def __init__(self):
    #     self.search_template = 'https://ws-public.interpol.int/notices/v1/red?&resultPerPage=100&page={}'

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }


    def parse(self,response):
        print('in_parse')
        data = chompjs.parse_js_object(response.text, json_params={'strict': False})
        persons = data["_embedded"]["notices"]
        for person in persons :
            print(person)
            loader = ItemLoader(CriminalsItem(),response)
            loader.add_value('first_name',person['name'])
            loader.add_value('last_name',person['forename'])
            loader.add_value('country',person["nationalities"])
            loader.add_value('date_of_birth',person["date_of_birth"])
            
            gender_url_id = person["_links"]['self']['href'].split('/')[-1]
            base_url = 'https://www.interpol.int/How-we-work/Notices/View-Red-Notices#'
            loader.add_value('source_url',base_url + gender_url_id)
            loader.add_value('address','')
            try:
                loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
            except:
                pass
            yield Request(
                person["_links"]['self']['href'],
                callback = self.parse_gender,
                meta = {'loader':loader},
                dont_filter=True            )

    def parse_gender(self,response):
        loader = response.meta['loader']
        data = chompjs.parse_js_object(response.text, json_params={'strict': False})
        if data["sex_id"] == 'M':
            loader.add_value('gender','Male')
        else:
            loader.add_value('gender','Female')
        yield loader.load_item()