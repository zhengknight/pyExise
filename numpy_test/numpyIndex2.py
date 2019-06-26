#encoding=gbk
"""
https://blog.csdn.net/lm_is_dc/article/details/81098805
2.1 一个冒号:进行切片
通过冒号来切片，通过逗号来区分维度。一维与列表完全一致 多维时同理 。
"""
import numpy as np

np.random.seed(10)
arr=np.random.randint(10,50,size=(3,4))
print(arr)
#获取前两行数据
print(arr[0:2])
print("///////////////////")
#获取前两行的前两列数据
print(arr[0:2,0:2])
print("///////////////////")
#逗号左边切的是第一个维度（行），逗号右边切的是第二个维度（列）
#获取二维数组前两列数据
print(arr[:,0:2])
print("///////////////////")
"""
两个冒号::进行切片
一维

将数据反转，例如[1,2,3]—->[3,2,1
"""
#创建一维数组
arr=np.arange(0,10)
print(arr)

print(arr[::-1])
#创建一个3行3列的二维数组
arr=np.linspace(0,9,num=9,endpoint=False).reshape((3,3))
print(arr)
#反转行
print(arr[::-1])
#反转列
print(arr[:,::-1])
#全反转
print(arr[::-1,::-1])