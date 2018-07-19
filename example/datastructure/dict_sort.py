'''根据字典中值的大小,对字典进行排序'''

import random

names = "ABCDEFG"

randDic = {x: random.randint(70, 90) for x in names}
print(randDic)

# 使用内置的sorted函数
# 仅仅对键进行了排序,值不见了
print(sorted(randDic))

# 用zip 函数把字典构成一个元组
randTuple = zip(randDic.values(), randDic.keys())
print(sorted(randTuple, reverse=True))

# dict.items(),直接返回元组列表
sort_dic = sorted(randDic.items(), key=lambda x: x[1], reverse=True)
print(sort_dic)
