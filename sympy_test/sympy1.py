#encoding=gbk
"""
https://zhuanlan.zhihu.com/p/70111190练习题1
2 * x + 3 * y - 1 + 2 * z *x=0
3 * x + 2 * y + 3 - 2 * z *y=0
x * x - y * y +1=0
"""

from sympy import solve, symbols
"""
x,y,z=symbols('x,y,z')
f1 = 2 * x + 3 * y - 1 + 2 * z *x
f2 = 3 * x + 2 * y + 3 - 2 * z *y
f3 = x * x - y * y +1
#solve([f1 ,f2 ,f3])
print(solve([f1 ,f2 ,f3],[x,y,z]))

"""
#https://blog.csdn.net/bryant_meng/article/details/83586740
x,y,z= symbols('x,y,z')
f1 = 2*x - y + z - 10
f2 = 3*x + 2*y - z - 16
f3 = x + 6*y - z - 28
print(solve([f1,f2,f3]))