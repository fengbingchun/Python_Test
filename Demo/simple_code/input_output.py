# 输入和输出测试代码
# reference: http://www.runoob.com/python3/python3-inputoutput.html

import  math

# 1. 输出格式美化
s = 'Hello, Runoob'
print(str(s))
print(repr(s))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

print('常量 PI 的值近似为：%5.3f。' % math.pi)

# 2. 读取键盘输入
str = input("请输入：");
print ("你输入的内容是: ", str)

# 3. 读和写文件
f = open("E:/GitCode/Python_Test/Demo/simple_code/foo.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.close() # 关闭打开的文件

f = open("E:/GitCode/Python_Test/Demo/simple_code/foo.txt", "r")
str = f.read()
print(str)
f.close()

f = open("E:/GitCode/Python_Test/Demo/simple_code/foo.txt", "r")
str = f.readline()
print(str)

for line in f:
    print(line, end='')
f.close()

# 4. pickle模块
