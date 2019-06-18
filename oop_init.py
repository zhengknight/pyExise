#encoding=gbk
#类的初始化函数演示
class Person:
    def __init__(self, name):
        self.name=name

    def say_hi(self):
        print('Hello, how are you', self.name)


p=Person('Swaroop')
p.say_hi()
