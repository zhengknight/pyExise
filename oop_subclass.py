#encoding=gbk
#类继承示例

class SchoolMember:
    '''代表学校里的任何成员'''
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print('Initializing memeber {}'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('name:{},age:{}'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    '''代表以为教师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary=salary
        print('(Initialized teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print("Initialized student {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Student's marks is {:d}".format(self.marks))

t=Teacher("Mrs Liu",40,30000)
s=Student("xiao zhang",20,85)

#打印空白行
print()

members=[t,s]
for member in members:
    member.tell()