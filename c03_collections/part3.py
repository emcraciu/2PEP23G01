from collections import OrderedDict

my_order = OrderedDict()
print(my_order)
x = OrderedDict.fromkeys("cdfga")
print(x)
x = OrderedDict.fromkeys((1, "a"))
print(x)
x = OrderedDict({1: {"a":"b"}})
print(x)
print(x.keys())

x["my_key1"] = 1234
x["my_key2"] = 234
x["my_key3"] = 34
x["my_key4"] = 4
print(x)
print(x.popitem())
print(x)
x.move_to_end('my_key2')

for i in x.items():
    print(i)
