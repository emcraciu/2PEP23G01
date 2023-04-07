import time
from multiprocessing import Process, Queue

def f(q:Queue):
    time.sleep(10)
    q.put([42, None, 'hello'])
    print('done', __name__, f.__name__)

def d(q:Queue):
    # while q.empty():
    #     time.sleep(0.1)
    print(q.get(timeout=5), __name__, d.__name__)



if __name__ == '__main__':
    q = Queue()
    my_d = Process(target=d, args=(q,))
    my_f = Process(target=f, args=(q,))
    my_d.start()
    my_f.start()
    # print(q.get())    # prints "[42, None, 'hello']"
    my_f.join()
    my_d.join()