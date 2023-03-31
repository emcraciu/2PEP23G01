# from time import sleep
# def main():
#     print('Hello ...')
#     sleep(5)
#     print('... World!')
#
# if __name__ == '__main__':
#     main()
#     main()
#

import aiohttp
import json
import time
import asyncio

import asyncio


# async def main():
#     print('Hello ...')
#     await asyncio.sleep(5)
#     print('... World!')

# asyncio.run(main())
# asyncio.run(main())
# asyncio.run(main())
# asyncio.run(main())

async def get_word_time():
    async with aiohttp.ClientSession() as session:
        responses = []
        # time.sleep(1)  # this will be executed syncronius
        for i in range(1):
            start = time.time()
            response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/')
            responses.append(response)
            end = time.time()
            print('Response time', end - start)
        for response in responses:
            text = await response.text()
            print('Response text', text)


async def main():
    task = await asyncio.gather(*(get_word_time() for _ in range(10)))


if __name__ == "__main__":
    # asyncio.run(get_word_time())
    asyncio.run(main())
