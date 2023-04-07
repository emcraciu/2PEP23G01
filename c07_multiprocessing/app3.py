from multiprocessing import Queue, Process


def gen_num():
    for i in range(100):
        pass
        # numbers 1000 and 1500


def factorial1(n):

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    q = Queue()

    processes = []
    for _ in range(3):
        x = Process(target=factorial1, args=(q,))
        x.start()
        processes.append(x)

    p = Process(target=gen_num, args=(q,))
    p.start()

    for y in processes:
        y.join()

    p.join()
