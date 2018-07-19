'''字符串内置插入语法对比

1. 模版插入
2. 使用%操作符格式化语法
3. 使用str.format()的字符串语法
'''
import string

values = {'var': 'foo'}

t = string.Template('''
        Variable        : $var
        Escape          : $$
        Variable in text: ${var}iable
        ''')

print('TEMPLATE:', t.substitute(values))

s = '''
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
'''

print('INTERPOLATION:', s % values)

s = '''
Variable        : {var}
Escapte         : {{}}
Variable in text: {var}siable
'''

print('FORMAT:', s.format(**values))
