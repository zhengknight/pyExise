#with使用演示
with open('test.txt') as f:
    for line in f:
        print(line,end='')