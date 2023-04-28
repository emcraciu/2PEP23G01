import random
import time
from threading import Thread, Lock, RLock

lock = Lock()


# lock1 = Lock()
# lock2 = Lock()

def random_sleep(l: Lock):
    t = random.randint(1, 3)
    print("Sleeping: ", t)
    l.acquire()
    try:
        if t == 2:
            raise ValueError('2 second sleep is not supported')
        time.sleep(t)
    finally:
        # l.release()
        l.acquire(timeout=10)  # this does not work for normal locks (set timeout for workaround)
        l.release()
    print("Completed sleeping: ", t)


processes = []
for i in range(5):
    thd = Thread(target=random_sleep, args=[lock])
    thd.start()
    processes.append(thd)

for thd in processes:
    thd.join()
