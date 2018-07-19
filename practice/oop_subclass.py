class SchoolMembr:
    '''代表任何学校里的成员'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMembr):
    '''代表以为老师'''

    def __init__(self, name, age, salary):
        SchoolMembr.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMembr.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMembr):
    '''代表一位学生'''

    def __init__(self, name, age, marks):
        SchoolMembr.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMembr.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs.Shrividya', 40, 300)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()
