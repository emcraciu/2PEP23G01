## Quiz
https://www.classmarker.com/

## Homework


Create a List like object that will have methods specific for counting objects inside the list by using the Counter class
Counter should be updated automatically for at lest 2 methods (append, pop) but I recommend trying to do this for all
methods that update the list and try to not repeat the same code for each method

Create a class for a list like object based on UserList wrapper
https://docs.python.org/3/library/collections.html#collections.UserList
That object should have a method to return a Counter objects
https://docs.python.org/3/library/collections.html#collections.Counter
for all objects in the list


```python 
# example to test code
class Example(UserList):
    pass # your code here

x = Example(['1', '2', '3'])
x.get_counter() # returns Counter({'1':1, '2':1 '3':1})
x.append(3)
x.get_counter() # returns Counter({'1':1, '2':1 '3':2})
```