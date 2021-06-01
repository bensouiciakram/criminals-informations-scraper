import scrapy 
import asyncio
from twisted.internet import asyncioreactor
scrapy.utils.reactor.install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import importlib

spiders = []
for spider_id in range(1,22):
    if spider_id == 12:
        continue
    spider_module = importlib.import_module('criminals.spiders.site{}'.format(spider_id))
    spider = getattr(spider_module,'Site{}Spider'.format(spider_id))
    spiders.append(spider)



configure_logging()
settings = get_project_settings()
settings['FEED_URI']= 'site{}'.format(spider_id) + '.csv'
settings['FEED_FORMAT'] = 'csv'
runner = CrawlerRunner(settings=settings)

@defer.inlineCallbacks
def crawl():
    for spider in spiders :
        yield runner.crawl(spider)
    reactor.stop()

crawl()
reactor.run()