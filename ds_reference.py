#深浅拷贝演示
shoplist=['banana','carrot','apple','onion']

mylist=shoplist

del shoplist[0]
print('shoplist contains',shoplist)
print('mylist\'s content include',mylist)
#深拷贝
print('copy by making a full slice')
mylist=shoplist[:]
del mylist[0]
print('shoplist contains',shoplist)
print('mylist\'s content include',mylist)