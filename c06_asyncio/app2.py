"""
get all regions using asyncio

http://worldtimeapi.org/api/timezone/

'America, Asia, Europe, Pacific ...'

this should be obtained as fast as possible
"""

import aiohttp
import json
import time
import asyncio


async def regions(session):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/')
    text = await response.text()
    locations = json.loads(text)
    return set(map(lambda a: a.split('/')[0], locations))


async def time_zone(session, region):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{region}')
    text = await response.text()
    time_zones = json.loads(text)
    if isinstance(time_zones, list):
        return set(map(lambda a: a.split("/")[1], time_zones))


async def get_regions():
    async with aiohttp.ClientSession() as session:
        task = await asyncio.gather(regions(session), time_zone(session, "America"))
        print(task[1])


if __name__ == "__main__":
    asyncio.run(get_regions())
