'''含有关键字参数的装饰器'''

import random


def use_logging(func):
    def wrapper(*args, **kwargs):
        print('do some sting')
        return func(*args, **kwargs)
    return wrapper


@use_logging
def foo(name):
    print('my name is {}'.format(name))


@use_logging
def foo2(name, age):
    print('my name is {0}, age is {1}'.format(name, age))


@use_logging
def foo3(name, age, height=None):
    print('my name is {name}, age is {age}'.format(name = name, age = age))


s1 = [1, 2]
s1.
foo('song')

foo2('song', 29)

foo3('song', 12, height=23)
