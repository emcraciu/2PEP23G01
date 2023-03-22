import matplotlib.pyplot as plt
import time
import timeit
from time import sleep


def my_time():
    sleep(3)

start = time.time()
my_time()
end = time.time()
print(end - start)
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))


if __name__ == "__main__":
    #print(timeit.timeit('my_time()', setup="from __main__ import my_time", number=3)) # total time is 9s


    fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
    fig1.dpi = 200
    ay1.plot([1,2,3], [5,5,5], label="TEST1")
    ay2.plot([2,3,4], [4,4,4], label="TEST2")
    ay1.legend()
    ay2.legend()
    plt.xlabel('seconds')
    plt.ylabel('km')
    plt.title("My example Graph")
    plt.show()