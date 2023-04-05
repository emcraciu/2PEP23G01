"""
get all regions using asyncio

http://worldtimeapi.org/api/timezone/

step1 = 'America, Asia, Europe, Pacific ...'
step2 = get all subregions
step3 = user global variable to transfer data between functions
step4 = run time_zone a number of times equal to number of regions

this should be obtained as fast as possible
"""

import aiohttp
import json
import time
import asyncio

region = []

async def regions(session):
    await asyncio.sleep(1)
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/')
    text = await response.text()
    locations = json.loads(text)
    region.extend(set(map(lambda a: a.split('/')[0], locations)))


async def time_zone(session):
    while not region:
        await asyncio.sleep(0.1)
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{region.pop()}')
    text = await response.text()
    time_zones = json.loads(text)
    if isinstance(time_zones, list):
        return set(map(lambda a: a.split("/")[1], time_zones))


async def get_regions():
    async with aiohttp.ClientSession() as session:
        task = await asyncio.gather(regions(session), *(time_zone(session) for _ in range(5)))
        print(task)


if __name__ == "__main__":
    asyncio.run(get_regions())
