def maximum(x,y):
    if x<y:
        return y
    elif x==y:
        return 'the mumbers are equal.'
    else:
        return x


print(maximum(3,7))
print(maximum(6,6))