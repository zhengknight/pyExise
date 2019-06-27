#encoding=gbk
"""
使用拉格朗日乘数法求极值，代码求偏导数，不再像sympy1.py中手工求偏导数后再构造方程组
"""
from sympy import symbols, diff, solve

x,y,z=symbols('x,y,z')
L=x*x+3*x*y+y*y-x+3*y+z*(x*x-y*y+1)
diff_L_x = diff(L,x)
diff_L_y = diff(L,y)
diff_L_z = diff(L,z)

res = solve([diff_L_x,diff_L_y,diff_L_z],[x,y,z])
print(res)
