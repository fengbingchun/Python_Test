'''
运算符测试代码
reference: http://www.runoob.com/python3/python3-basic-operators.html
'''

# 1. 算术运算符：+、-、*、/、%、**(幂)、//(取整除)
a = 21; b = 10; c = 0
print("a =", a); print("b =", b)

c = a + b
print("a + b =", c)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", a/b)
print("a % b =", a%b)

a = 5; b = 3
print("a ** b =", a**b)
print("a // b =", a//b)
print()

# 2. 比较运算符：==、!=、>、<、>=、<=
a = 4; b =2;
if (a == b):
    print("a == b")
else:
    print("a != b")
print()

# 3. 赋值运算符： =、+=、-=、*=、/=、%=、**=、//=
a = 10; b = 3;
a+=b
print("a+=b:", a)
print()

# 4. 位运算符：&、|、^(位异或)、~、<<(左移)、>>(右移)
a = 60      # 60 = 0011 1100
b = 13      # 13 = 0000 1101
c = 0
c = a & b   # 12 = 0000 1100
print("a & b =", c)
c = a << 2  # 240 = 1111 0000
print("a << 2 =", c)
print()

# 5. 逻辑运算符：and、or、not
a = 10; b = 20
if (a and b):
	print("a和b都为true")
else:
	print("a和b有一个不为true")
print()

# 6. 成员运算符：in(如果在指定的序列中找到值返回True，否则返回False)、not in
a = 10; b = 20
list = [1, 2, 3, 4, 5 ];
if (a in list):
   print ("变量a在给定的列表中list中")
else:
   print ("变量a不在给定的列表中list中")

if (b not in list):
   print ("变量b不在给定的列表中list中")
else:
   print ("变量b在给定的列表中list中")
print()

# 7. 身份运算符： is(判断两个标识符是不是引自一个对象)、is not
a = 20; b = 20
if (a is b): print("a和b有相同的标识")
else: print("a和b没有相同的标识")

if (id(a) == id(b)): print("a和b有相同的标识")  # id:此函数用于获取对象内存地址
else: print ("a和b没有相同的标识")

b = 30
if (a is b): print("a和b有相同的标识")
else: print("a和b没有相同的标识")

if (a is not b): print("a和b没有相同的标识")
else: print("a和b有相同的标识")
