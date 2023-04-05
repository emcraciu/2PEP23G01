

import aiohttp
import json
import time
import asyncio

my_list = []

async def regions():
    await asyncio.sleep(2.0001)
    my_list.append('test1')
    return my_list



async def time_zone():
    await asyncio.sleep(2.0002)
    my_list.append('test2')
    return my_list


async def get_regions():
        task = await asyncio.gather(time_zone(), regions())
        print(task)
        my_list.append('test3')
        print(task)


if __name__ == "__main__":
    asyncio.run(get_regions())
