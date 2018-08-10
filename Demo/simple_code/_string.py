'''
字符串测试代码
reference: http://www.runoob.com/python3/python3-string.html
'''

# 1. 访问字符串中的值:Python中单引号和双引号使用完全相同
var1 = 'Hello World!'; var2 = "Runoob"
print ("var1[0]:", var1[0])
print ("var2[1:5]:", var2[1:5])
print()

# 2. 字符串更新
var1 = 'Hello World!'
print ("已更新字符串:", var1[:6] + 'Runoob!')
print()

# 3. 字符串运算符：+、*(重复输出字符串)、[](通过索引获取字符串中字符)、[:](截取字符串中的一部分)、in、not in、r/R(原始字符串)、%
a = "Hello"; b = "Python"
print("a + b输出结果：", a + b)
print("a * 2输出结果：", a * 2)
print("a[1]输出结果：", a[1])
print("a[1:4]输出结果：", a[1:4])

if ("H" in a): print("H在变量a中")
else: print("H不在变量a中")

if ("M" not in a): print("M不在变量a中")
else: print("M在变量a中")

print(r'\n')
print(R'\n')
print("\n")

# 4. 字符串格式化
print ("我叫%s今年%d岁!" % ('小明', 10))
print()

# 5. 三引号：允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
  多行字符串可以使用制表符
TAB(\t)。
也可以使用换行符[\n]。
\nover
"""
print (para_str)
