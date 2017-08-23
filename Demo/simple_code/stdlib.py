# 标准库测试代码
# reference：http://www.runoob.com/python3/python3-stdlib.html

import os
#import glob
import sys
#import re
import math
#import random
#from urllib.request import urlopen
from datetime import date
import zlib
from timeit import Timer

# 1. os
print(os.getcwd()) # 返回当前的工作目录
print(dir(os)) # returns a list of all module functions

# 2. glob

# 3. sys
print(sys.argv)

# 4. re
#print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
#re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# 5. math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

# 6. random
#print(random.choice(['apple', 'pear', 'banana']))

# 7. 访问互联网
#for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#    line = line.decode('utf-8')  # Decoding the binary data to text.
#    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#        print(line)

# 8. datatime
print(date.today())

# 9. zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

# 10. timeit
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())