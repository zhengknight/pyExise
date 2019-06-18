#encoding=gbk
#类变量（class variable）与对象变量（object variable）示例

class Robot:
    #表示一个带名字的机器人
    #定义一个类变量用于机器人数量计数
    population=0
    def __init__(self, name):
        self.name = name
        print('robot {0} created'.format(self.name))

        #当此初始化函数被调用时，机器人数量加1
        Robot.population += 1

    def destoy(self):
        print('{0} is died'.format(self.name))
        Robot.population -=1

        if Robot.population==0:
            print('{0} is the last one'.format(self.name))
        else:
            print('We still have {0} robots'.format(Robot.population))

    def say_hi(self):
        '''来自机器人的真诚问候
        没问题你做的到。'''
        print('Greetings, my master call me {0}'.format(self.name))

    @classmethod
    def how_many(cls):
        ''''打印出当前的机器人的数量'''
        print('We have {:d} robots'.format(cls.population))

droid1=Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2=Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('Robots can do something here')

print("Robots have done there work , let's destroy them")
droid1.destoy()
droid2.destoy()
droid2.how_many()
Robot.how_many()

