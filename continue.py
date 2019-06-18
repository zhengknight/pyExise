while True:
    s=input('enter something:')
    if s=='quit':
        break
    if len(s)<3:
        print('lenth is too short!')
        continue
    print('lenth is sufficient!')