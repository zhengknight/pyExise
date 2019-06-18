num=23
guess=int(input('enter an integer:'))
if guess==num:
    print('congratulations! you get it!')
    print('but you can not win any prize.')
elif guess<num:
    print('the num you input is  lower than that!')
else:
    print('the number is a little bigger than that!')

print('Done')
