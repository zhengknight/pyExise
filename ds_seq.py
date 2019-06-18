#序列、切片运算演示
shoplist=['carrot','onion','apple','banana']
name='chinese'

#下标索引法
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Charactor 0 is',name[0])
#切片索引法
print('列表中所有数据',shoplist[0:3])
print('列表中所有数据',shoplist[:])
print('列表中1-3项数据',shoplist[1:3])
print('第2项以后的数据',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print(shoplist[:-1])
#指定步长为2
print(shoplist[1::2])
