from tools.conf import setting
import aiohttp
import asyncio
from core.sch import ManageReq
from core.http.request import Request
from core.error import RequestListEmptyException
import time

class Downloder(object):
    __session_num = setting.SESSION_NUM # 下载请求数
    __request_list_empty_cnt = 0

    @staticmethod
    def task_list():
        return [Downloder.downloder_task() for _ in range(Downloder.__session_num)]

    @staticmethod
    async def downloder_task():
        cnt = 0
        async with asyncio.Semaphore(1):
            async with aiohttp.ClientSession() as session:
                while True:
                    try:
                        req = ManageReq.get_request()
                        try:
                            if req.method == "GET":
                                async with session.get(**req.get_params()) as html:
                                    response = await html.text(encoding=req.encoding)
                                    print(response[0:100].encode())
                                    # exit(0)
                                    # print(response[0:500].encode())
                            elif req.method == "POST":
                                async with session.post(req.url) as html:
                                    response = await html.text(encoding=req.encoding)
                                    print(response[0:20].encode())
                            else:
                                print('method error')
                        except aiohttp.client_exceptions.ServerDisconnectedError as e:
                            print(e)
                        cnt = 0
                    except RequestListEmptyException as e:
                        if cnt < Downloder.__request_list_empty_cnt:
                            cnt += 1
                            await asyncio.sleep(1)
                        else:
                            # print('爬虫结束')
                            return

asyncio.ensure_future(Downloder.downloder_task())

if __name__ == "__main__":
    start = time.time()
    for i in range(500):
        ManageReq.add_request(Request(url='http://www.baidu.com'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(Downloder.task_list()))
    print(time.time() - start)

















