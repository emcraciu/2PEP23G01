from collections import Counter

with open("data.txt",'r') as file:
    data = file.read()

words = data.split()
print(words)

counter = Counter(words)
print(counter)

print(type(counter))
print(counter.keys())
print(counter.values())
counter['new'] = 4
print(counter)
counter['new'] += 5
print(counter)

counter = Counter("""aaabcd""")
print(counter)
