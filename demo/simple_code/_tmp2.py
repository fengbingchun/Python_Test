﻿# _module.py中会使用此文件

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块:', __name__)

#  斐波那契(fibonacci)数列模块
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
    return

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
