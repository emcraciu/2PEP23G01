"""save decorated function in same variable"""
from functools import wraps




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
@decorator # area = decorator(area)
def area(length: int, width: int):
    print('in function')
    return length*width

# print(area(10, 10))
# print(80*'#')
# area = decorator(area)
# print(area(10, 10))

print(area(10, 10))