import  math
import os

'''
输入和输出测试代码
reference: http://www.runoob.com/python3/python3-inputoutput.html
'''

os_name=os.name
if os_name == "posix": # linux
	print("python running on linux")
else: # nt: windows
	print("python running on windows")

# 1. 输出格式美化
# 如果你希望将输出的值转成字符串,可以使用repr()或str()函数来实现
# str(): 函数返回一个用户易读的表达形式
# repr(): 产生一个解释器易读的表达形式
s = 'Hello, Runoob'
print(str(s))
print(repr(s))

# rjust()方法,它可以将字符串靠右,并在左边填充空格
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=',')
    print(repr(x*x*x).rjust(4))

#zfill(),它会在数字的左边填充0
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

# str.format()的基本使用如下:
# 括号及其里面的字符(称作格式化字段)将会被format()中的参数替换
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 在括号中的数字用于指向传入对象在format()中的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
#如果在format()中使用了关键字参数,那么它们的值会指向使用该名字的参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}.'.format('Google', 'Runoob', other='Taobao'))

# '!a'(使用ascii()), '!s'(使用str())和'!r'(使用repr())可以用于在格式化某个值之前对其进行转化
print('常量 PI 的值近似为： {}.'.format(math.pi))
print('常量 PI 的值近似为： {!r}.'.format(math.pi))
# 可选项':'和格式标识符可以跟着字段名. 这就允许对值进行更好的格式化
print('常量 PI 的值近似为 {0:.3f}.'.format(math.pi))

# 在':'后传入一个整数,可以保证该域至少有这么多的宽度
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# %操作符也可以实现字符串格式化. 它将左边的参数作为类似sprintf()式的格式化字符串,而将右边的代入,然后返回格式化后的字符串
print('常量 PI 的值近似为：%5.3f.' % math.pi)

# 2. 读取键盘输入i
# Python提供了input()内置函数从标准输入读入一行文本，默认的标准输入是键盘
str = input("请输入：")
print ("你输入的内容是: ", str)

# 3. 读和写文件
# open()将会返回一个file对象
if os_name == "posix":
	f = open("foo.txt", "w")
else:
	f = open("E:/GitCode/Python_Test/Demo/simple_code/foo.txt", "w")
f.write( "Python 是一个非常好的语言.\n是的，的确非常好!!\n" )
f.close() # 关闭打开的文件

if os_name == "posix":
	f = open("foo.txt", "r")
else:
	f = open("E:/GitCode/Python_Test/Demo/simple_code/foo.txt", "r")
str = f.read()
print(str)
f.close()

if os_name == "posix":
	f = open("foo.txt", "r")
else:
	f = open("E:/GitCode/Python_Test/Demo/simple_code/foo.txt", "r")
str = f.readline()
print(str)

# 迭代一个文件对象然后读取每行
for line in f:
    print(line, end='')
f.close()

# 4. pickle模块
# python的pickle模块实现了基本的数据序列和反序列化
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去,永久存储
# 通过pickle模块的反序列化操作, 我们能够从文件中创建上一次程序保存的对象

# 使用格式化字符串字面值,要在字符串开头的引号/三引号前添加f或F. 在这种字符串中,可以在{和}字符之间输入引用的变量,或字面值的python表达式
print(f"str: {str}")
