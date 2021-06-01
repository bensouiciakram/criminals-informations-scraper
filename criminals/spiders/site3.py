import scrapy
from scrapy.utils.response import open_in_browser
from scrapy_splash import SplashRequest

class Site3Spider(scrapy.Spider):
    name = 'site3'
    allowed_domains = ['pmddtc.state.gov']
    start_urls = ['https://www.pmddtc.state.gov/ddtc_public?id=ddtc_kb_article_page/']
    
    custom_settings = {
        'FEED_URI': '{}.csv'.format(name),
        'FEED_FORMAT':'csv'
    }

    def start_requests(self):
        yield SplashRequest(
            self.start_urls[0],
            callback=self.parse,
            endpoint = 'render.html',
            args={
                'wait':0.5
            }
        )

    def parse(self, response):
        open_in_browser(response)
