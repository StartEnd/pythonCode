'''safe_substitute

对比substitute, safe_substitute模版中需要的值如果没有被完全提供的话可以避免发生异常
'''
import string

values = {'var': 'foo'}

t = string.Template('$var is here but $missing is not provided')

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute()    :', t.safe_substitute(values))
