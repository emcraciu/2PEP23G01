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
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(5)
    print('... World!')

asyncio.run(main())
asyncio.run(main())
asyncio.run(main())
asyncio.run(main())