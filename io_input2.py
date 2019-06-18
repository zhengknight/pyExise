#用户输入输出改进版

import re


def reverse(text):
    return text[::-1]

#使用re包提取用户录入字符串中的字母
def extractAlpha(text):
    list_alpha = re.findall(r'[A-Za-z]',text)
    '''print(list_alpha),findall返回的是一个字母列表，需要转换为字符串
    第一种方式是使用for循环打印，只是打印到控制台，print并不返回任何东西，
    第二种方式是使用字符串的join函数，用return返回字符串本身
    for item in list_alpha:
        print(item, end='')'''
    str_alpha = ''.join(list_alpha)
    return str_alpha.lower()
#将所有字母小写


def is_palindrome(text):
    return text==reverse(text)

something=input('Please enter text-->')
#str1=extractAlpha(something)
#extractAlpha(something)

if is_palindrome(extractAlpha(something)):
    print('是的，该字符串是回文！')
else:
    print('No，这个字符串不是回文！')


