from core.spider.base_spider import Spider

class TestSpider(Spider):
    name = 'test_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com' for _ in range(100)]

    def parse(self):
        print('TestSpider parse')
