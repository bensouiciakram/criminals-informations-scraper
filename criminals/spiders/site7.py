import scrapy
from scrapy import Request 
import chompjs
from scrapy.loader import ItemLoader 
from criminals.items import CriminalsItem

class Site7Spider(scrapy.Spider):

    name = 'site7'
    def __init__(self):
        self.search_template = 'https://ws-public.interpol.int/notices/v1/un/persons?page={}'

    def start_requests(self):
        for page_id in range(1,9):
            yield Request(
                self.search_template.format(page_id)
            )

    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def parse(self,response):
        print('in_parse')
        data = chompjs.parse_js_object(response.text, json_params={'strict': False})
        persons = data["_embedded"]["notices"]
        for person in persons :
            loader = ItemLoader(CriminalsItem(),response)
            loader.add_value('first_name',person['name'])
            loader.add_value('last_name',person['forename'])
            loader.add_value('date_of_birth',person["date_of_birth"])
            try:
                loader.add_values('full_name',loader._values['first_name'] + loader._values['last_name'])
            except:
                pass
            gender_url_id = person["_links"]['self']['href'].split('/')[-1]
            base_url = 'https://www.interpol.int/How-we-work/Notices/View-Red-Notices#'
            loader.add_value('source_url',base_url + gender_url_id)
            loader.add_value('address','')
            yield Request(
                person["_links"]['self']['href'],
                callback = self.parse_gender,
                meta = {'loader':loader},
                dont_filter=True  )

    def parse_gender(self,response):
        loader = response.meta['loader']
        data = chompjs.parse_js_object(response.text, json_params={'strict': False})
        loader.add_value('country',data["country_of_birth_id"])
        if data["sex_id"] == 'M':
            loader.add_value('gender','Male')
        else:
            loader.add_value('gender','Female')
        yield loader.load_item()