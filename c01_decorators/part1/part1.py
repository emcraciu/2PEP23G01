"""We are trying to print some lines before and after our function"""
from functools import wraps


def area(length: int, width: int):
    return length*width

# print(type(area(10, 11)))
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This function has some other docstring"""
        print('print before')
        result = str(func(*args, **kwargs))
        print('print after')
        return result

    return wrapper

# print(type(decorator(area)))

my_decorated_function = decorator(area)
# print(my_decorated_function(12, 13))
# print(type(my_decorated_function(12, 13)))
result = my_decorated_function(12, 13)
print(result)
print(type(result))

print(area.__name__)
print(my_decorated_function.__name__)