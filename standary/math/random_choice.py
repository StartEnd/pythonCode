'''随机选择序列值
随机数生成器的一个常见用途是从枚举序列中返回随机项，既是这些值不是数字.
random 模块包含了 choice() 函数用于从序列中随机获取值。
这个例子模拟了投 10000 次硬币正面和反面出现的次数。

这里仅有两个可允许的结果，因此不是使用数字并转换他们，而是直接将 "heads" 和 "tails" 与 choice() 一起时候用。
'''

import random

outcomes = {
    'heads': 0,
    'tails': 0
}

sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Heads: ', outcomes['heads'])
print('Tails: ', outcomes['tails'])
