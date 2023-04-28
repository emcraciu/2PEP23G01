# race 5 functions
# - they must start at the same time
# - we are only interested in the fastest
# - use threading
import random
import time
from threading import Thread, Event

event = Event()


def runner(e: Event, id):
    e.wait()
    print('Running: ', end='')
    counter = 0
    while counter < 3:
        counter += 1
        time.sleep(1 / id)
        if not e.isSet():
            break
        print(f'{id}', end='')
    else:
        e.clear()


def referee(e: Event):
    print('Start: ', end='')
    for i in range(3):
        time.sleep(0.3)
        print(f'{i}', end='')
    print()
    e.set()


processes = []
for i in range(1):
    thd = Thread(target=referee, args=[event])
    processes.append(thd)

for i in range(1, 6):
    thd = Thread(target=runner, args=[event, i])
    processes.append(thd)

for process in processes:
    process.start()
