# 迭代器与生成器测试代码
# reference: http://www.runoob.com/python3/python3-iterator-generator.html

import sys # 引入sys模块

# 1. 迭代器: iter
list=[1,2,3,4]
it = iter(list) # 创建迭代器对象
for x in it:
    print (x, end=" ")
print("\n")

# 2. 迭代器： next
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

#while True:
#    try:
#        print(next(it))
#    except StopIteration:
#        sys.exit()
print(next(it))
print(next(it))

# 3. 生成器: yield
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#print(f)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()