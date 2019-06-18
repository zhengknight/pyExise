#字符串常用操作练习
name='Swaroop'

if name.startswith('Swar'):
    print('Yes,the  string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains string "a"')

if name.find('war')!=-1:
    print('Yes, it contains the string "war"')

delimiter='__*__'
mylist=['brazil','russia','china','india']
print(delimiter.join(mylist))