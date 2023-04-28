import random
import time
from threading import Thread, RLock

lock = RLock()


def random_sleep(r: RLock):
    t = random.randint(1, 3)
    print("Sleeping: ", t)
    r.acquire()
    try:
        if t == 2:
            raise ValueError('2 second sleep is not supported')
        time.sleep(t)
    finally:
        r.acquire()  # this works for rLock
        print('got lock again')
        r.release()
        print('released')
        r.release()
    print("Completed sleeping: ", t)


processes = []
for i in range(5):
    thd = Thread(target=random_sleep, args=[lock])
    thd.start()
    processes.append(thd)

for thd in processes:
    thd.join()

# exampel
print(80 * "#")
example_lock = RLock()


def func2(r):
    r.acquire()
    print('in function 2')
    r.release()


def func1(r: RLock):
    r.acquire()
    func2(r)
    r.release()


processes = []
for i in range(5):
    thd = Thread(target=func1, args=[example_lock])
    thd.start()
    processes.append(thd)

for thd in processes:
    thd.join()
