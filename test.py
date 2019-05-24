
import aiohttp
import asyncio
import time
import queue
que = queue.Queue()
async def parse():
    async with asyncio.Semaphore(1):  # 限制并发数为5个
        async with aiohttp.ClientSession() as session:
            while True:
                if que.empty():
                    break
                url = que.get()
                try:
                    async with session.get(url) as html:
                        response = await html.text(encoding="utf-8")
                        print(response)
                        exit(0)
                except aiohttp.client_exceptions.ServerDisconnectedError as e:
                    print(e)
asyncio.ensure_future(parse())

if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    urls = ["https://news.online.sh.cn/news/gb/content/2019-05/24/content_9293135.htm" for _ in range(0, 5000)]
    for url in urls:
        que.put(url)
    tasks = [parse() for _ in range(100)] # 这里，如果parse里没有while true的话，这里只会有50个任务，意思就是只会抓取前50页，就结束程序了
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)





