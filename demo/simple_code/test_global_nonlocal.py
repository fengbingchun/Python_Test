#Blog: https://blog.csdn.net/fengbingchun/article/details/120607063

var = 6

if var == 1:
    # reference: https://www.geeksforgeeks.org/global-local-variables-python/
    def f(): # Creating local variables
        s = "I love Geeksforgeeks" # local vairable
        print("Inside Function:", s)

    f()
    #print("s:", s) # NameError: name 's' is not defined
elif var == 2:
    # reference: https://www.geeksforgeeks.org/global-local-variables-python/
    # Defining and accessing global variables
    def f(): # This function uses global variable s
        print("Inside Function:", s)

    # Global scope
    s = "I love Geeksforgeeks" # global variable,  is used both inside the f function as well as outside the f function
    f()
    print("Outside Function:", s)
elif var == 3:
    # reference: https://www.geeksforgeeks.org/global-local-variables-python/
    # This function has a variable with name same as s
    def f():
        #s += 'GFG' # UnboundLocalError: local variable 's' referenced before assignment
        s = "Me too." # 如果在函数作用域内也定义了同名变量,那么它将仅打印函数内部给出的值,而不是全局值
        print(s)

    s = "I love Geeksforgeeks" # global scope
    f()
    print(s) # I love Geeksforgeeks
elif var == 4:
    # reference: https://www.geeksforgeeks.org/global-local-variables-python/
    # This function modifies the global variable 's'
    def f():
        global s # 如果我们要进行赋值或更改全局变量,我们只需要在函数中使用global关键字
        s += ' GFG'
        print(s)
        s = "Look for Geeksforgeeks Python Section"
        print(s)

    s = "Python is great!" # global scope
    f()
    print(s) # Look for Geeksforgeeks Python Section
elif var == 5:
    # reference: https://www.geeksforgeeks.org/use-of-nonlocal-vs-use-of-global-keyword-in-python/
    def fun():
        var1 = 10

        def gun():
            nonlocal var1 # tell python explicitly that it has to access var1 initialized in fun using the keyword nonlocal
            # global var1; var1 = var1 + 10 # NameError: name 'var1' is not defined
            var1 = var1 + 10
            print(var1) # 20

        gun()
        print(var1) # 20

    fun()
elif var == 6:
    # reference: https://www.geeksforgeeks.org/python-nonlocal-keyword/
    def geek_func():
        geek_name = "geekforgeeks" # local variable to geek_func

        def geek_func1(): # First Inner function
            geek_name = "GeekforGeeks"

            def geek_func2(): # Second Inner function
                nonlocal geek_name # Declairing nonlocal variable
                geek_name = 'GEEKSFORGEEKS'
                print(geek_name) # Printing our nonlocal variable, GEEKSFORGEEKS

            geek_func2() # Calling Second inner function

        geek_func1() # Calling First inner function
        print(geek_name) # Printing local variable to geek_func, geekforgeeks

    geek_func()
print("test finish")
