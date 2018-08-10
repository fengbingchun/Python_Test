import sys # 引入sys模块

'''
迭代器与生成器测试代码
reference: http://www.runoob.com/python3/python3-iterator-generator.html
'''

# 1. 迭代器: iter
list = [1, 2, 3, 4]
it = iter(list) # 创建迭代器对象
for x in it:
    print(x, end=" ")
print("\n")

# 2. 迭代器: next
list = [1, 2, 3, 4]
it = iter(list) # 创建迭代器对象
#while True:
#    try:
#        print(next(it))
#    except StopIteration:
#        sys.exit()
print(next(it))
print(next(it))
print()

# 3. 生成器: yield
def fibonacci(n): # 生成器函数:斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        # 使用了yield的函数被称为生成器(generator).跟普通函数不同的是,生成器是一个返回迭代器的函数,只能用于迭代操作,更简单点理解生成器就是一个迭代器.在调用生成器运行的过程中,每次遇到yield时函数会暂停并保存当前所有的运行信息,返回yield的值.并在下一次执行next()方法时从当前位置继续运行
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f是一个迭代器,由生成器返回生成
#print(f)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
print()
