
# Blog: https://blog.csdn.net/fengbingchun/article/details/122115500

# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
var = 8
if var == 1:
    # *args允许函数接受任意数量的位置参数
    def addition(*args):
        result = 0
        for i in args:
            result += i
        return result

    # 传递给此addition函数的参数存储在一个元组中,因此可以迭代args变量
    print("addition():", addition())
    print("addition(1, 4):", addition(1, 4))
    print("addition(1, 7, 3):", addition(1, 7, 3))
elif var == 2:
    def arg_printer(a, b, *args):
        print(f"a is {a}")
        print(f"b is {b}")
        print(f"args is {args}")

    # 前两个值被赋予a和b,其余值存储在args元组中
    arg_printer(3, 4, 5, 8, 3)

    # Python希望将关键字参数放在位置参数之后
    # 如果为位置参数赋值,它就成为关键字参数.由于它后面是位置参数,因此会得到一个SyntaxError
    #arg_printer(a=4, 2, 4, 5) # SyntaxError: positional argument follows keyword argument
elif var == 3:
    def addition(a, b, *args, option=True): # option是关键字参数
        result = 0
        if option:
            for i in args:
                result += i
            return a + b + result
        else:
            return result

    print(addition(1,4,5,6,7)) # 23
    print(addition(1,4,5,6,7, option=False)) # 0
elif var == 4:
    # **kwargs允许函数接受任意数量的关键字参数,它收集所有未明确定义的关键字参数,默认**kwargs是一个空字典,每个未定义的关键字参数都作为键值对存储在**kwargs字典中
    def arg_printer(a, b, option=True, **kwargs):
        print(a, b) # 3 4
        print(option) # True
        print(kwargs) # {'param1': 5, 'param2': 6}

    arg_printer(3, 4, param1=5, param2=6)
elif var == 5:
    # 我们可以在函数中同时使用*args和**kwargs,但*args必须放在**kwargs之前
    def arg_printer(a, b, *args, option=True, **kwargs):
        print(a, b) # 1 4
        print(args) # (6, 5)
        print(option) # True
        print(kwargs) # {'param1': 5, 'param2': 6}

    arg_printer(1, 4, 6, 5, param1=5, param2=6)
elif var == 6:
    # 我们可以使用*args打包和解包(pack and unpack)变量
    def arg_printer(*args):
        print(args)

    lst = [1,4,5]
    # 如果我们将一个列表传递给arg_printer,它将作为一个元素存储在args元组中
    arg_printer(lst) # ([1, 4, 5],)
    # 如果我们在lst之前放一个星号,列表中的值将被解包(unpack)并单独存储在args元组中
    arg_printer(*lst) # (1, 4, 5)
    tpl = ('a','b',4)
    # 我们可以传递多个可迭代对象与单个元素一起解包(unpack),所有值都将存储在args元组中
    arg_printer(*lst, *tpl, 5, 6) # (1, 4, 5, 'a', 'b', 4, 5, 6)
elif var == 7:
    # 我们也可以使用关键字参数(keyword argument)进行打包和解包(pack and unpack),
    # 但是作为关键字参数传递的迭代必须是一个映射,比如字典
    def arg_printer(**kwargs):
        print(kwargs)

    dct = {'param1':5, 'param2':8}
    arg_printer(**dct) # {'param1': 5, 'param2': 8}

    # 如果我们还将额外的关键字参数与字典一起传递,它们将组合并存储在kwargs字典中
    arg_printer(param3=9, **dct) # {'param3': 9, 'param1': 5, 'param2': 8}
elif var == 8:
    # reference: https://www.geeksforgeeks.org/args-kwargs-python/
    def myFun(arg1, arg2, arg3):
        print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

    args = ("Geeks", "for", "Geeks")
    myFun(*args) # arg1: Geeks, arg2: for, arg3: Geeks

    kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
    myFun(**kwargs) # arg1: Geeks, arg2: for, arg3: Geeks

print("test finish")
