'''高级模版

string.Template缺省语法可以通过正则表达式来调整,
这个正则表达式一般用来寻找模版内容内变量名字的.
简单的方法是通过delimiter和idpattern的类属性来做调整

下面的实例中,分隔符用%代替了$并且变量名字中必须包含下划线
'''

import string


class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
Delimiter : %%
Replaced  : %with_underscore
Ignored   : %notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
