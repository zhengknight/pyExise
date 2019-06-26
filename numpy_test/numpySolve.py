#encoding=gbk
"""
https://blog.csdn.net/jayloncheng/article/details/80003182
1，解线性方程组
example：
     2x + 3y = 5
     x   + 3y = 3
  求解代码及结果如下 ：
        解得 x=2,y=1/3.
"""
import numpy as np
from numpy.linalg import solve
a=np.mat([[2,3],[1,3]])#系数矩阵
b=np.mat([5,3]).T    #常数项列矩阵
x=solve(a,b)        #方程组的解
print(x)

"""
2，解非线性方程组
example:
    x*x + 2y = 5
    x + y  =  1
求解代码及结果如下：
         x=3,y=-2 ;
         x=-1,y=2.
"""

from scipy.optimize import fsolve
def func(paramlist):
    x,y=paramlist[0],paramlist[1]
    return [ x**2+2*y-5,
            x+y-1 ]
s=fsolve(func,[0,0])
print(s)