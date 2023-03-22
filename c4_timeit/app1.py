"""sorting random number list
- generate random list = 100
- time the function using timeit
"""
import timeit
from random import randint
import matplotlib.pyplot as plt

def random_generator(nr_iter):
    result = []
    for _ in range(nr_iter):
        result.append(randint(10000, 20000))
        result.sort()
    return result

x = []
y = []

for i in range(100, 2000, 100):
    result = timeit.timeit(f"random_generator({i})", setup="from __main__ import random_generator", number=100)
    print(result)
    x.append(i)
    y.append(result)

fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
fig1.dpi = 200
ay1.plot(x, y, label="RANDOM GENERATOR")
ay2.plot(x, y, label="SECOND GENERATOR")
ay1.legend()
ay2.legend()
plt.xlabel('number of objects')
plt.ylabel('execution time')
plt.title("My example Graph")
plt.show()