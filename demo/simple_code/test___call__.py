# Blog: https://blog.csdn.net/fengbingchun/article/details/122330858

var = 2
if var == 1:
    # https://www.geeksforgeeks.org/__call__-in-python/
    class Example:
        def __init__(self):
            print("Instance Created")

        # Defining __call__ method
        def __call__(self):
            print("Instance is called via special method")

    e = Example() # Instance created # __init__ method will be called
    e() # Instance is called via special method # __call__ method will be called
elif var == 2:
    class Product:
        def __init__(self):
            print("Instance Created")

        # Defining __call__ method
        def __call__(self, a, b): # 可以定义任意参数
            print(a * b)

    ans = Product()  # Instance created # __init__ method will be called
    ans(10, 20) # 200 # __call__ method will be called
    ans.__call__(10, 20) # 等价于ans(10, 20)

print("test finish")
