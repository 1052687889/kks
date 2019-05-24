import time
import asyncio
from spiders.test import TestSpider

async def main():
    start = time.time()
    await TestSpider.run()
    print(time.time() - start)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
















