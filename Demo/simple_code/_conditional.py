'''
条件控制测试代码
reference: http://www.runoob.com/python3/python3-conditional-statements.html
'''

# Python中用elif代替了else if,所以if语句的关键字为if ... elif ... else ...
var1 = 100
if var1:
	print("if 表达式条件为 true")
	print(var1)

var2 = 0
if var2:
	print("if 表达式条件为 true")
	print(var2)

if var1 == 10:
	print("var1 == 10")
elif var1 == 50:
	print("var1 == 50")
else:
	print("var1:", var1)

# 在Python中没有switch ... case语句

print("Good bye!")
