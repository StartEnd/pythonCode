'''为元组中的每个元素命名,提高可读性'''
import random
import collections

names = 'ABCDEFGH'
sexs = ['male', 'famale']

students = [(x, random.randint(12, 18), random.choice(sexs)) for x in names]

print(students)

# 方法1,利用类似枚举的定义替换
NAME, AGE, SEX = range(3)

print(students[1][NAME])
print(students[2][SEX])


# 方法2,直接用nameTuple存储

Student = collections.namedtuple('Student', ['name', 'age', 'sex'])

students_tuple = [Student(x, y, z) for x, y, z in students]

print(students_tuple[1].name)

stu1 = Student('song', 12, 'famale')
print(stu1.name)
