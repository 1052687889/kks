import aiohttp
from urllib.parse import urlparse
import asyncio
from tools.conf import setting
class Request(object):
    __session_pool = {}

    def __init__(self, url, callback=None, method:str='GET', headers:dict=None, body:bytes=None,
                 cookies=None, meta=None, encoding:str='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None,timeout:int=None,proxy:str=None):
        self.url = url
        self.callback = callback,
        self.method = str(method).upper()
        self.headers = headers if headers else setting['DEFAUT_HEADER']
        self.body = body
        self.cookies = cookies if cookies else {}
        self.timeout=timeout if timeout else setting['DEFAULT_TIMEOUT']
        self.meta = meta
        self.encoding = encoding
        self.priority = priority
        self.dont_filter = dont_filter
        self.errback = errback
        self.flags = flags
        self.proxy=proxy

    @property
    def hostName(self)->str:
        parsed_uri = urlparse(self.url)
        return parsed_uri.netloc

    def get_params(self)->dict:
        return {
            'url':self.url,
            'headers':self.headers,
            'cookies':self.cookies,
            'timeout':self.timeout,
            'proxy':self.proxy,
        }




















