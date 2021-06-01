# Scrapy settings for criminals project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'criminals'

SPIDER_MODULES = ['criminals.spiders']
NEWSPIDER_MODULE = 'criminals.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'criminals (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'criminals.middlewares.CriminalsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'criminals.middlewares.CriminalsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'criminals.pipelines.CriminalsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# ---------------------- free proxies rotation-------------#
# ROTATING_PROXY_LIST_PATH = 'proxies.txt' # Path that this library uses to store list of proxies
# NUMBER_OF_PROXIES_TO_FETCH = 5 # Controls how many proxies to use


# DOWNLOADER_MIDDLEWARES = {
#     'rotating_free_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_free_proxies.middlewares.BanDetectionMiddleware': 620,
# }

# DOWNLOADER_MIDDLEWARES  =  { 
# #     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# #     'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
# #     'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
# #     'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware' :  110 , 
#     'tor_ip_rotator.middlewares.TorProxyMiddleware' :  100 
# }
# # USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

# TOR_IPROTATOR_ENABLED  =  True 
# TOR_IPROTATOR_CHANGE_AFTER  = 1

# RETRY_TIMES = 100


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    # 'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    # 'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610,
    # 'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610
}

# FAKEUSERAGENT_PROVIDERS = [
#     'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
#     'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
#     'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # fall back to USER_AGENT value
# ]
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'



# ZYTE_SMARTPROXY_ENABLED = True
# ZYTE_SMARTPROXY_APIKEY = 'f45342d142bf42e9b832496d53cf8264'


# DOWNLOAD_HANDLERS = {
#     "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#     "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
# }

# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

#PLAYWRIGHT_LAUNCH_OPTIONS = {'headless':False,'timeout':0}

# SPLASH_URL = 'http://localhost:8050/'

# SPIDER_MIDDLEWARES = { 
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100, 
# }

# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter' 
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'



RETRY_TIMES = 30


