x=50
def func():
    global x
    print('x is',x)
    x=2
    print('x changed to',x)



func()
print('x is ',x)