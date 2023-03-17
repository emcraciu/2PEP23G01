from collections import deque

my_q = deque((1,2,3), 4)

print(my_q)
my_q.append(4)
print(my_q)
my_q.append(5)
print(my_q)
my_q.appendleft(6)
print(my_q)
print(my_q.maxlen)
# my_q.maxlen = 5
# my_q.appendleft(7)
# print(my_q)
print(my_q.pop())
print(my_q)
