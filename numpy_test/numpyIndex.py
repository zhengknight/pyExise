#encoding=gbk
"""
x[m,n]是通过numpy库引用数组或矩阵中的某一段数据集的一种写法，

m代表第m维，n代表m维中取第几段特征数据。

通常用法：

x[:,n]或者x[n,:]

x[:,n]表示在全部数组（维）中取第n个数据，直观来说，x[:,n]就是取所有集合的第n个数据,
"""
import numpy as np

X = np.array([[0,1],[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15],[16,17],[18,19]])
#output array's dimension
print(X.ndim)
#输出数组的形状shape
print(X.shape)

print(X[:,0])