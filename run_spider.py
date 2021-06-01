from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import importlib

spider_id = input('enter the spider id : ')

spider_module = importlib.import_module('criminals.spiders.site{}'.format(spider_id))

spider = getattr(spider_module,'Site{}Spider'.format(spider_id))


settings = get_project_settings()
settings['FEED_URI']= 'site{}'.format(spider_id) + '.csv'
settings['FEED_FORMAT'] = 'csv'

process = CrawlerProcess(settings=settings)
process.crawl(spider)
process.start()