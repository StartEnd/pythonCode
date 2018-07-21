'''类装饰器'''
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('self decoratot running')
        self._func()
        print('self decorator stop')


@Foo
def bar():
    print('bar')


bar()
