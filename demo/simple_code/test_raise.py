# Blog: https://blog.csdn.net/fengbingchun/article/details/119818521

var = 6
if var == 1:
    # 1: from子句如果未处理引发的异常,则将打印两个异常
    try:
        print(1/0)
    except Exception as exc:
        raise RuntimeError("Something bad happend") from exc
elif var == 2:
    # 2: 通过在from子句中指定None可以显式抑制异常链
    try:
        print(1/0)
    except:
        raise RuntimeError("Something bad happend") from None
elif var == 3:
    # 3: 如果只想知道某处是否抛出一个异常,并不想处理它,那么只需一个不带任何参数的raise语句即可
    raise # 默认触发RuntimeError异常
elif var == 4:
    # 4: Python中使用raise语句触发一个指定的异常,不带描述信息
    raise Exception
elif var == 5:
    # 5: Python中使用raise语句触发一个指定的异常,带描述信息
    raise Exception("var's value:{}".format(var))
elif var == 6:
    # 6: raise引发的异常由try except(else finally)来捕获并处理
    try:
        num = input("input a number:")
        if (not num.isdigit()):
            raise ValueError("num must be a number")
    except ValueError as err:
        print("excepition:", repr(err))

print("test finish")
