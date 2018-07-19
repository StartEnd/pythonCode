'''筛选出字典中值高于90的项'''
import random

names = 'ABCDEFG'
scores = {x: random.randint(60, 100) for x in names}
print(scores)


# 基本方法遍历筛选,python3 中 iteritems 变为了item
result = {}
for k, v in scores.items():
    if v >= 90:
        result[k] = v

print(result)

print('利用字典解析')

print({k: v for k, v in scores.items() if v >= 90})
