import random

import requests
import json
import time
from threading import Thread, Event
event = Event()


def time_zone(e: Event, id):
    e.wait()
    time.sleep(random.choice([1,2,3]))#timp pentru executie
    print('Running: ', end='')
    if not e.is_set(): #incheie executia
        print("giving up")
        return
    response = requests.get(f'http://worldtimeapi.org/api/timezone/Europe')
    text = response.text
    time_zones = json.loads(text)
    e.clear()
    if isinstance(time_zones, list):
        time_zone_names = set(map(lambda a: a.split("/")[1], time_zones))
        print( time_zone_names)


def referee(e: Event):
    print('Start: ', end='')
    for i in range(3):
        time.sleep(1)
        print(f'{i}', end='')
    print()
    e.set()


processes = []
for i in range(1):
    thd = Thread(target=referee, args=[event])
    processes.append(thd)

for i in range(1, 6):
    thd = Thread(target=time_zone, args=[event, i])
    processes.append(thd)

for process in processes:
    process.start()

