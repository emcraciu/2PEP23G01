# execute only during working hours (9-17)
# - working hours prints message
# - outside of working hours function does not execute
# - decorator must receive working hours as argument


import datetime
import time
from datetime import datetime
from functools import wraps


def working_hours(start, stop):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if time.localtime().tm_hour not in range(start.hour, stop.hour):
                return
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@working_hours(datetime.time(hour=9), datetime.time(hour=22))
def alarm():
    print("Wack up")


alarm()


def inception(begin=9, end=17):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if datetime.now().hour not in range(begin, end):
                return None
            func(*args, **kwargs)

        return wrapper

    return decorator


@inception(9, 21)
def alarm():
    print("Wake up!")


alarm()
