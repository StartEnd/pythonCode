'''采样
许多模拟器需要来自一组输入值的模拟样本。sample()  函数用于生成不重复样本值，
并且不改变输入序列。这个例子展示了从系统字典中打印随机样本单词。
'''

import random

with open('/usr/share/dict/words', 'rt') as f:
    words = f.readlines()
words = [w.rstrip() for w in words]

for w in random.sample(words, 5):
    print(w)
