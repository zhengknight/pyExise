#字典使用练习，包括字典的索引、删除、添加
ab={'小明':'xiaoming@163.com','小花':'xiaohua@sohu.com','小张':'xiaozhang@hotmail.com'}

print('小花的邮箱为',ab['小花'])
del ab['小张']

print('字典中的数据项数量为',len(ab))
for key,value in ab.items():
    print(key,'=',value)

for key,value in ab.items():
    print('{}联系方式为{}'.format(key,value))

ab['小狗']='xiaogou@foxmail.com'

if '小狗' in ab:
    print('小狗的邮箱为',ab['小狗'])
