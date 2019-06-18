#异常、错误处理演示
try:
    text = input('Enter text-->')
except EOFError:
    print('Why did you do me an EOF on me?')
except KeyboardInterrupt:
    print('You canceled it.')
else:
    print('You entered {}'.format(text))