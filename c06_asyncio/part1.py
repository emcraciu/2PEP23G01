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

async def main():
    print('Hello ...')
    await asyncio.sleep(5)
    print('... World!')

# asyncio.run(main())
# asyncio.run(main())
# asyncio.run(main())
# asyncio.run(main())

async def get_word_time():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/')

        end = time.time()
        print(end - start)
        print(response)

asyncio.run(get_word_time())

# async def time_getter(session, location='Bucharest', nr=0):
#     while True:
#         if nr == len(time_zones):
#             response = await session.request(method='GET',
#                                              url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
#             my_time = await response.text()
#             time_zones.append(json.loads(my_time))
#             break
#         else:
#             time.sleep(0.1)
#     return json.loads(my_time)
