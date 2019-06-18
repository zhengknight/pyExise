#try...finally演示
import sys
import time

f=None
try:
    f=open('test.txt')
    while True:
        line = f.readline()
        if len(line)==0:
            break
        print(line, end='')
        sys.stdout.flush()
        print('Press Ctrl+c now')
        #为了确保能运行一会
        time.sleep(2)
except IOError:
    print('Could not find file poem.txt.')
except KeyboardInterrupt:
    print("!!You canceled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up:closed the file.)")