'''没有装饰器实现函数的封装'''
def foo():
    print('foo')


def bar(func):
    func()


def use_logging(func):
    print('do my self logging')
    func()


bar(foo)

use_logging(foo)

'''功能是实现了，但是我们调用的时候不再是调用真正的业务逻辑 foo 函数，
而是换成了 use_logging 函数，这就破坏了原有的代码结构， 
现在我们不得不每次都要把原来的那个 foo 函数作为参数传递给 use_logging 函数，那么有没有更好的方式的呢'''
