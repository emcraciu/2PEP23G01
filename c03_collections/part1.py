from collections import Counter

with open("data.txt",'r') as file:
    data = file.read()

words = data.split()
print(words)

counter = Counter(words)
print(counter)


