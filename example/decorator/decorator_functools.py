'''解决装饰后函数元信息丢失的问题'''

import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''wrapper will do somestring'''
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)
    return wrapper


@logged
def f(x):
    '''do some things'''
    return x + x * x


print(f(2))

print(f.__name__)
print(f.__doc__)
