'''装饰器带参数的处理手法'''


def use_logging(lever):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if lever == 'warn':
                print('warning:%s' % func.__name__)
            elif lever == 'info':
                print('info:%s' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@use_logging(lever='warn')   # 相当与@decorator
def foo(name='foo'):
    print('i am %s' % name)


foo()
foo(name='song')
