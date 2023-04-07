from multiprocessing import Process, Queue
import json
import time
from time import sleep
import requests


def region(region: Queue):
    response = requests.get(f'http://worldtimeapi.org/api/timezone')
    text = response.text
    time_zones = json.loads(text)
    if isinstance(time_zones, list):
        for reg in set(map(lambda a: a.split("/")[0], time_zones)):
            region.put(reg)


def time_zone(region: Queue):
    reg = region.get()
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{reg}')
    text = response.text
    time_zones = json.loads(text)
    if isinstance(time_zones, list):
        print(set(map(lambda a: a.split("/")[1], time_zones)))
    else:
        print("not list", time_zones)


print(__name__)

if __name__ == '__main__':
    q = Queue()
    start = time.time()
    processes = []
    for _ in range(3):
        x = Process(target=time_zone, args=(q,))
        x.start()
        processes.append(x)

    p = Process(target=region, args=(q,))
    p.start()
    print('running')
    time.sleep(10)

    for y in processes:
        y.join()
    end = time.time()
    p.join()
    print(end - start)
