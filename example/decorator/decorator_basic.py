'''基本的装饰器'''
def use_logging(func):

    def wrapper():
        print('use_logging')
        return func
    return wrapper()


def foo():
    print('foo')


# 因为装饰器 use_logging(foo) 返回的时函数对象wrapper，这条语句相当于  foo = wrapper
foo = use_logging(foo)


foo()  # 执行foo 相当与执行wrapper
