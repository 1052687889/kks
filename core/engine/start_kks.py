'''
kks 爬虫初始化
'''
from tools.conf import setting
downloder_middlewares = setting['DOWNLOADER_MIDDLEWARES']

def kks_init():
    for k,v in downloder_middlewares.items():
        __import__(k).from_crawler()
        print(k,v)















