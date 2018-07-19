import random

# python3 中,xrange 与 range 已经合并为range()
for i in range(1, 5):
    print('%04.3f' % random.random(), end=' ')
