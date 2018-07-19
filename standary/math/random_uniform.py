import random

# 传入最小值和最大值 min + (max - min) * random()
for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
