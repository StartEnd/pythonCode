'''筛选出集合中能被3整除的元素'''
import random
nums = set([random.randint(1, 100) for _ in range(50)])

print(nums)

result = {x for x in nums if x % 3 == 0}
print(result)
