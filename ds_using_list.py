#This is my shoplist
shoplist=['apple','mongo','cherry','banana']

print('I have',len(shoplist),'items to buy')
print('These items are',end=' ')
for item in shoplist:
    print(item,end=' ')

print('\nI also have to purchase rice')
shoplist.append('rice')
print('My shoplist is now',shoplist)

print('I have to order my shoplist')
shoplist.sort()
print("Sorted shopping list is",shoplist)

print('The first item i will buy is',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)