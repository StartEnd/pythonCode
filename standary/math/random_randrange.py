'''randrange() 是从范围中选择值的更一般形式。
randrange() 支持 step 参数，除了开始和结束值,
所以它完全等同于从range(start, stop, step) 中选择一个随机值。
它效率更高，因为范围实际上并没有构建。
'''
import random

for i in range(3):
    print(random.randrange(1, 101, 5), end=' ')
