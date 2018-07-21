'''装饰器语法糖'''
def use_logging(func):

    def wrapper():
        print('you should do someing')
        return func()

    return wrapper


@use_logging
def foo():
    print('foo')


foo()
