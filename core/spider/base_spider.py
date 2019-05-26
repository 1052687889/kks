import asyncio
from core.http.request import Request
from core.sch import ManageReq
from core.downloder import Downloder
from core.engine.start_kks import kks_init
from core.engine.handle import Handle
class BaseSpider(object):
    name = ''
    allowed_domains = []
    start_urls = []
    def __init__(self, *args, **kwargs):
        pass

class Spider(BaseSpider):
    def __init__(self):
        super().__init__()

    @classmethod
    async def start_request(cls):
        for url in cls.start_urls:
            yield Request(url=url,callback=cls.parse)

    def parse(self):
        print('Spider parse')

    @classmethod
    async def run(cls):
        kks_init()
        async for req in cls.start_request():
            Handle.Request(request=req)
            # ManageReq.add_request(req)
        await asyncio.gather(*Downloder.task_list())



if __name__ == "__main__":
    bs = Spider()




