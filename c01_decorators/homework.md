## Homework

1) Create decorator 'set_args_type' that will:
    - convert all arguments to the decorated function to the specified type
    - if argument cannot be converted to string TypeError will be raised
2) Create decorator 'add_line_number' that will:
    - add line number to output string of decorated function
    - ex if output is 'line 1\nline 2' then output will be transformed to '1 line 1\n2 line 2'
3) Create decorator to count the number of times a function raised an exception 

```python

def set_args_type():
    pass  # <your code here>


def add_line_number():
    pass  # <your code here>


def count_exceptions():
    pass  # <your code here>


@set_args_type(str)
@add_line_number
@count_exceptions
def read_file(name, mode='r'):
    return open(name, mode).read()


read_file(100, 'r')
read_file('part1.py', 'r')
read_file('part1.py', 100)
```
