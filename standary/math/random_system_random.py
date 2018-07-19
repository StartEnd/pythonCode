'''系统随机数
一些操作系统提供了一个随机数字生成器，它可以访问随机数生成器引入的更多熵源。
random 通过 SystemRandom 暴露了这个功能，它和 Random 有相同的 API，但是使用  os.urandom()  生成构成其它算法基础的值。

SystemRandom 生成的序列是不可预测的，因为随机性来源于系统，而不是软件（实际上，seed()  和 setstate() 对它都没有影响）。
'''
import random
import time

print('Default Initialization.\n')

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(5):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))
print()

print('Same seed.\n')

seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)
for i in range(5):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))
