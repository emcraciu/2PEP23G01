import aiohttp
import json
import time
import asyncio

from datetime import datetime

time_zones = []


async def time_getter(session, location='Bucharest', nr=0):
    response = await session.request(method='GET',
                                     url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
    my_time = await response.text()
    time_zones.append(json.loads(my_time))
    return json.loads(my_time)['datetime']


async def get_local_time(session, location='Europe'):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{location}/')
    text = await response.text()
    locations = json.loads(text)
    return list(map(lambda a: a.split('/')[1], locations))


async def get_word_time():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        task = await asyncio.gather(get_local_time(session, 'Europe'))
        task = await asyncio.gather(*(time_getter(session, location=location, nr=3) for location in task[0]))
        print(task)
        end_time = time.time()
        print(f'total time: {end_time - start_time}')
        print(task[0])


# async def get_time():
#     await asyncio.sleep(2)
#     print(f'finished time: {datetime.now()}')


# print(type(get_time()))
#
#
# async def main():
#     start_time = time.time()
#     await
#     end_time = time.time()
#     print(f'Execution time: {end_time - start_time}')


if __name__ == "__main__":
    asyncio.run(get_word_time())
    # #asyncio.run(main())
    # result = asyncio.gather(main(), main())
    # print(type(result))
    # await result
