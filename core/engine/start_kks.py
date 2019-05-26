'''
kks 爬虫初始化
'''
from tools.conf import setting

downloder_middlewares_obj = []

def create_middlewares_obj():
    downloder_middlewares = sorted(((k,v) for k,v in setting['DOWNLOADER_MIDDLEWARES'].items() if v != None),key = lambda x:x[1],reverse = True)
    for middleware,_ in downloder_middlewares:
        sl = middleware.split('.')
        s = '.'.join(sl[1:-1])
        res = __import__(s)
        middleware_obj = getattr(res,sl[-1]).from_crawler(11)
        downloder_middlewares_obj.append(middleware_obj)

def kks_init():
    create_middlewares_obj()




















