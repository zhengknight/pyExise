#coding=gbk
#文件备份改进版，以当天日期为目录，默认以时间为zip文件名字，如果用户输入备注则以时间+备注作为文件名字
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
#获取用户输入备注信息
comment = input('请输入备注信息-->')
#检查用户是否输入备注
if len(comment)==0:
   target=today + os.sep + now + '.zip'
else:
    #此处一个物理行换行的时候pycharm自动给加上反斜杠了
    target = today + os.sep + now + '_'\
             +comment.replace(' ','_') + '.zip'
#如果当日文件夹不存在则创建
if not os.path.exists(today):
    os.mkdir(today)
    print('当日文件夹目录创建成功',today)

#构造zip命令行
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('zip_command')
print(zip_command)
print('Running')
if os.system(zip_command)==0:
    print('已成功备份到',target)
else:
    print('备份失败！！！')
