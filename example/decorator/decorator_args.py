'''带参数的装饰器'''
def use_logging(func):
    def wrapper(*args):
        print('do some sting')
        return func(*args)
    return wrapper


@use_logging
def foo(name):
    print('my name is {}'.format(name))


@use_logging
def foo2(name, age):
    print('my name is {0}, age is {1}'.format(name, age))


foo('song')


foo2('song', 29)
