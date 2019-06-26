#encoding=gbk
"""
原方程组
2x+3y+z=4
4x+2y+3z =17
7x+y-z=1

from sympy import *

a = Matrix([[2,3,1],[4,2,3], [7,1,-1]])
b = Matrix([[4],[17],[1]])
x = symarray('x', 3)
p=solve(a*x-b)
print(p)
"""
from sympy import *
x = symbols('x')
y = symbols('y')
res = solve([x+y-3,x-y-1],[x,y])
print(res)