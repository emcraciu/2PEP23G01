from multiprocessing import Process
import json
import time
from time import sleep

import requests


def time_zone(region):
    sleep(3)
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{region}')
    text = response.text
    time_zones = json.loads(text)
    if isinstance(time_zones, list):
        return set(map(lambda a: a.split("/")[1], time_zones))


print(__name__)

if __name__ == '__main__':
    start = time.time()
    processes = []
    for region in ['Africa', 'America', 'Europa']:
        p = Process(target=time_zone, args=(region,))
        p.start()
        processes.append(p)
    sleep(5)
    print('running')
    for p in processes:
        p.join()
    end = time.time()
    print(end - start)
