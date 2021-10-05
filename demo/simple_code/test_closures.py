#Blog: https://blog.csdn.net/fengbingchun/article/details/120616259

var = 3

if var == 1:
    # reference: https://www.geeksforgeeks.org/python-closures/
    def outerFunction(text):
        text = text

        def innerFunction():
            print(text)

        # Note we are returning function WITHOUT parenthesis(括号)
        return innerFunction

    myFunction = outerFunction('Hey!')
    myFunction()
elif var == 2:
    # reference: https://www.geeksforgeeks.org/python-closures/
    def logger(func):
        def log_func(*args):
            print(func(*args))

        # Necessary for closure to work(returning WITHOUT parenthesis)
        return log_func

    def add(x, y):
        return x+y

    add_logger = logger(add)
    add_logger(3, 3)
elif var == 3:
    # reference: https://data-flair.training/blogs/python-closure/
    def outer(x):
        result=0

        def inner(n):
            nonlocal result
            while n>0:
                result+=x*n
                n-=1
            return result # 7*3 + 7*2 + 7 = 42

        return inner

    myfunc=outer(7)
    print(myfunc(3)) # 42

print("test finish")
