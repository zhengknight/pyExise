#用户输入输出示例
def reverse(text):
    return text[::-1]

#是否为回文
def is_palindrome(text):
    return text==reverse(text)

something=input('Enter something-->')
if is_palindrome(something):
    print('Yes, it is palindrome.')
else:
    print('No, it is not a palindorme.')




