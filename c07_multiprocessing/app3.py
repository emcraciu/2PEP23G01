import time
from multiprocessing import Queue, Process


def gen_num(q: Queue):
    for i in range(2000, 10000):
        q.put(i)


def factorial1(q: Queue):
    time.sleep(0.2)  # there is a non-zero possibility that q may be empty at start and result in immediate return
    while not q.empty():
        n = q.get()
        result = 1
        for i in range(1, n + 1):
            result *= i
        # print(result) # we can't print values larger than 4300 digits in tha corresponding base


if __name__ == '__main__':
    q = Queue()

    processes = []

    p = Process(target=gen_num, args=(q,))
    p.start()

    for _ in range(12):
        x = Process(target=factorial1, args=(q,))
        x.start()
        processes.append(x)

    p.join()
    for y in processes:
        y.join()

    print(q.qsize())
