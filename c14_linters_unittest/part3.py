from unittest.mock import MagicMock

import requests
import json

# get_mock =MagicMock()
# requests.get = get_mock
# requests.get = lambda p: p + 'txt'

def time_getter():
    response = requests.get("http://worldtimeapi.org/api/timezone/")
    print('From function: ', type(response))
    my_time_str = response.text
    print('From function: ', type(response))
    return json.loads(my_time_str)


def my_func(message):
    x = json.loads(message)
    return x


if __name__ == "__main__":
    print(time_getter())
