'''多个同时生成器
除了模块级别的函数之外，random 包含了一个 Random 类管理集合随机数生成器的内部状态。
前面描述的所有函数都可以作为 Random 实例的可用方法，并且每个实例可以被单独初始化使用，而不会影响其他实例的返回值。

在一个具有良好原生随机值种子的系统上，实例以一个唯一状态运行。
然而，如果没有好的平台随机数生成器，实例很可能被使用当前时间播种，然后就产生了相同的值。
'''
import random
import time

print('Default Initialization. \n')
r1 = random.Random()
r2 = random.Random()

for i in range(5):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))


print('\nSame seed:\n')

seed = time.time()

r1 = random.Random(seed)
r2 = random.Random(seed)

for i in range(5):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))
