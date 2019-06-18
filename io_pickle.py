#pickle演示
import pickle

#存储相关对象的文件的名字
shoplistfile='shoplist.data'
#需要购买的物品清单
shoplist=['mongo', 'apple', 'carrot']
#打开文件
f=open(shoplistfile,'wb')
#转储对象至文件
pickle.dump(shoplist,f)
f.close()

#清除shoplist对象
del shoplist

f = open(shoplistfile,'rb')
#从文件转储至对象
storedlist = pickle.load(f)

print(storedlist)