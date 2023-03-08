from functools import wraps


def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'Function "{func.__name__}" was called: {wrapper.calls} times')
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count
def my_func():
    print('x')

my_func()
my_func()
my_func()
my_func()