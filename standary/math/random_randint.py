'''随机整数
random() 生成浮点数。可以将结果转换为整数， 但使用 randint() 直接生成整数更方便。
randint() 的取值范围是其参数的闭区间。数字可以是正数或负数，但第一个值应小于第二个值。
'''

import random

print('[1, 100]:', end=' ')
for i in range(3):
    print(random.randint(1, 100), end=' ')

print()
print('[-5, 5]:', end=' ')
for i in range(3):
    print(random.randint(-5, 5), end=' ')
print()

