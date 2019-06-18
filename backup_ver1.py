#备份文件夹脚本程序演示
# -*- coding：utf-8 -*-
import os
import time

#需要备份源目录
#目录中带空格的需要用双引号引起来，不然会截断
soure=[r'C:\Users\zk\Pictures', r'"C:\Users\zk\Documents\WeChat Files\zhengknight\Files"']
#目标目录
target_dir=r'e:\backup'

target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+ '.zip'

#目标文件夹不存在时创建该文件夹
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(soure))

print('Zip command is')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

