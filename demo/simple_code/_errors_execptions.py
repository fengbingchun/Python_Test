'''
错误和异常测试代码
reference： http://www.runoob.com/python3/python3-errors-execptions.html
'''

# 1.
while True:
        try:
            x = int(input("Please enter a number: "))
            break
        # 一个try语句可能包含多个except子句,分别来处理不同的特定的异常. 最多只有一个分支会被执行
        except ValueError:
            print("Oops! That was no valid number. Try again")
print()

# 2.
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    # try except语句还有一个可选的else子句, 如果使用这个子句,那么必须放在所有的except子句之后. 这个子句将在try子句没有发生任何异常的时候执行
    else:
        print("result is:", result)
    finally: # 无论是否发生异常都将执行最后的代码
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
#divide("2", "1")
