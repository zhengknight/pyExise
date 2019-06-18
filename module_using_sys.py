import sys
import os

print('the command line arguments are:')

for i in sys.argv:
    print(i)

print('PYTHONPATH is:',sys.path,'/n')
#打印程序目前所处的目录
print(os.getcwd())