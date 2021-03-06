'''
random() 每次调用的时候都生成不同的值，并且在它重复任何数字之前有一个很大的周期。
这对于生成唯一值及其变体很有用，但有时以不同的方式处理相同的数据集是很有用的。
一种技术是用一个程序生成随机数并保存他们以通过单独的步骤进行处理。然而，
对于大量数据可能不实用，所以，random 模块包含了 seed() 函数用于初始化伪随机数生成器以生成预期的一组值。

种子值用于控制根据公式生成的伪随机数序列的第一个值，并且由于公式是确定的，
所以种子改变后它实际上设置了生成的完整序列。传入 seed()  的参数可以是任何可哈希的对象。
默认使用基于平台的随机源（如果可用），否则，使用当前时间。
'''
import random

random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')

print()
