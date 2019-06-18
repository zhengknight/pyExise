#集合使用练习
bri=set(['brazil','russia','india'])
print('india' in bri)
print('usa' in bri)

bric=bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bric.remove('russia')
print(bri&bric)