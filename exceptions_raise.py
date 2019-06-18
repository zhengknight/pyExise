#异常抛出 演示
class ShortInputException(Exception):
    def __init__(self,length, atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast = atleast

try:
    text = input('Enter somethins-->')
    if len(text)<3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Why did you do me an Eof?')
except ShortInputException as ex:
    print(('ShortInputException:The input is {0} long' +
          ' exepted atleast {1} long').format(ex.length, ex.atleast))
else:
    print('No exception is raised.')