'''过滤列表中负数
'''
import random
numbers = [random.randint(-10, 10) for _ in range(10)]
print('Original List:{}'.format(numbers))

print('Common method')


def filter_minus(numbers):
    result = []
    for i in numbers:
        if i >= 0:
            result.append(i)
    return result


print(filter_minus(numbers))

print('Filter Function:')

print(list(filter(lambda x: x >= 0, numbers)))

print('列表解析:')

print([x for x in numbers if x >= 0])
