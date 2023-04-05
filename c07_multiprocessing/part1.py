from multiprocessing import Pool
import json
from time import sleep

import requests


def time_zone(region):
    sleep(5)
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{region}')
    text = response.text
    time_zones = json.loads(text)
    if isinstance(time_zones, list):
        return set(map(lambda a: a.split("/")[1], time_zones))


# time_zone('Africa')


if __name__ == '__main__':
    with Pool(10) as p:
        print(p.map(time_zone, ['Africa', 'America', 'Europa']))
