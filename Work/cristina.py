import asyncio
import random
import aiohttp

async def generate_password(session):
    response = await session.request(method='GET', url=f"https://www.random.org/integers/?num=10&min=0&max=255&col=1&base=10&format=plain&rnd=new")
    text = await response.text()
    #print(text)
    random_nr_list = text.split()
    nr_random = random.choice(random_nr_list)
    return nr_random


async def main():
    async with aiohttp.ClientSession() as session:
        random_list = await asyncio.gather(*(generate_password(session) for _ in range(10)))
        random_list = list(map(int, random_list))
        password = ''.join(chr(x) for x in random_list)
        print( f"Your new password is: {password}")


if __name__ == '__main__':
    asyncio.run(main())

