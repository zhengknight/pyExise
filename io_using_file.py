poem = '''\
programming is fun
when the work is done
if you wanna make your work also fun:
    use Python!
'''

#打开文件以编辑（Write）
f=open('test.txt','w')
#写入内容
f.write(poem)
#关闭文件
f.close()

#如果没有指定打开方式，默认为读文件方式
f=open('test.txt')

while True:
    line=f.readline()
    #零长度指示
    if len(line)==0:
        break

    print(line,end='')

f.close()
