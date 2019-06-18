#coding=gbk
#文件备份改进版，以当天日期为目录，时间为zip文件名字
import os
import time


#需要备份的文件目录列表
source=[r'C:\Users\zk\Pictures', r'"C:\Users\zk\Documents\WeChat Files\zhengknight\Files"']

#目标文件夹
target_dir=r'e:\backup'
#如果目标目录不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#当日文件夹
today=target_dir + os.sep + time.strftime('%Y%m%d')

#将当前时间作为备份的文件名
now = time.strftime('%H%M%S')
#目标文件的完整目录
target=today + os.sep + now + '.zip'
#如果当日文件夹不存在则创建
if not os.path.exists(today):
    os.mkdir(today)
    print('当日文件夹创建成功',today)

#构造zip命令行
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('zip_command')
print(zip_command)
print('Running')
if os.system(zip_command)==0:
    print('已成功备份到',target)
else:
    print('备份失败！！！')
