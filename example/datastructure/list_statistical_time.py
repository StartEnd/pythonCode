'''统计序列中元素出现的频率,找出出现次数最多的三个元素'''

import random
import collections

ranList = [random.randint(1, 10) for _ in range(100)]

print(ranList)


# stat = {x: 0 for x in ranList}
stat = dict.fromkeys(ranList, 0)

for key in ranList:
    stat[key] += 1

print(stat)

# stat_tu = [(k, v) for k, v in stat.items()]
stat_tu = tuple(stat.items())
print(stat_tu)

stat_tu_list = sorted(stat_tu, key=lambda x: x[1], reverse=True)

print(stat_tu_list)

print(stat_tu_list[:3])

# 方案二,利用collections.Counter对象

stat_tu2 = collections.Counter(ranList)
print(stat_tu2)
print(stat_tu2.most_common(3))
