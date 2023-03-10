#from asyncio import timeout
from time import sleep

@timeout(9)
def my_function():
    print('start')
    sleep(10)
    print('stop')