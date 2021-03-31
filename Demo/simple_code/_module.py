import sys # 导入python标准库中的sys.py模块
import _tmp1 # 导入当前目录下的_tmp1.py
from _tmp2 import fib, fib2 # 导入当前目录下的_tmp2.py中的fib、fib2函数,这个声明不会把整个_tmp2模块导入到当前的命名空间中,它只会将_tmp2里的fib、fi2函数引入进来
#from _tmp2 import * # 把一个模块的所有内容全都导入到当前的命名空间

'''
模块测试代码
reference: http://www.runoob.com/python3/python3-module.html
'''

# 1. 模块
print('命令行参数如下:')
for i in sys.argv: # sys.argv是一个包含命令行参数的列表
   print(i)
print()

print('Python路径为:', sys.path) # sys.path包含了一个Python解释器自动查找所需模块的路径的列表
print()

# 2. import语句
_tmp1.print_func("Runoob") # 现在可以调用tmp1模块里包含的函数了
print()

# 3. from ... import语句
fib(10) # 调用_tmp2.py中fib函数
print("fibonacci:", fib2(100)) # 调用_tmp2.py中的fib2函数
print()

# 4. from ... import *

# 5. __name__属性
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块:', __name__)
print()

# 6. dir()函数: dir函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
print("#### sys1:", dir()) # 获取当前模块的属性列表
print("#### sys2:", dir([])) # 查看列表的方法
print("#### sys3:", dir(()))
print("#### sys4:", dir({}))
print("#### sys5:", dir(_tmp1))
print("#### sys6:", dir(sys))
