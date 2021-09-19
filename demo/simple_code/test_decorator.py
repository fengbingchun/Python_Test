# Blog: https://blog.csdn.net/fengbingchun/article/details/120379734

import functools

var = 8

def another_function(func):
    """ A function that accepts another function """
    def other_func(): # 嵌套函数
        val = "The result of %s is %s" % (func(), eval(func()))
        return val
    return other_func

if var == 1:
    # reference: https://python101.pythonlibrary.org/chapter25_decorators.html
    def a_function():
        """ A pretty useless function """
        return "1+1"

    value = a_function()
    print(value)
    decorator = another_function(a_function)
    print(decorator())
elif var == 2:
    # 对以上示例做些修改,加入装饰器 https://python101.pythonlibrary.org/chapter25_decorators.html
    @another_function # 这里的@称为语法糖
    def a_function():
        """ A pretty useless function """
        return "1+1"

    value = a_function()
    print(value)
elif var == 3:
    # reference: https://python101.pythonlibrary.org/chapter25_decorators.html
    class DecoratorTest(object):
        """ Test regular method vs @classmethod vs @staticmethod """

        def __init__(self):
            """ Constructor """
            pass

        def doubler(self, x):
            """"""
            print("running doubler")
            return x*2

        @classmethod # 可以使用类的实例或直接由类本身作为其第一个参数来调用
        def class_tripler(klass, x):
            """"""
            print("running tripler: %s" % klass)
            return x*3

        @staticmethod # 类中的一个函数,可以在实例化类或不实例化类的情况下调用它
        def static_quad(x):
            """"""
            print("running quad")
            return x*4

    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)
elif var == 4:
    # https://python101.pythonlibrary.org/chapter25_decorators.html
    class Person(object):

        def __init__(self, first_name, last_name):
            """Constructor"""
            self.first_name = first_name
            self.last_name = last_name

        @property # 将类方法转换为属性
        def full_name(self):
            """ Return the full name """
            return "%s %s" % (self.first_name, self.last_name)

    person = Person("Mike", "Driscoll")
    print(person.full_name) # 注意: person.full_name与person.full_name()区别
    print(person.first_name)
    #person.full_name = "Jackalope" # AttributeError: can't set attribute, 不能将属性设置为不同的值,只能间接进行
    person.first_name = "Dan"
    print(person.full_name)
elif var == 5:
    # reference: https://www.geeksforgeeks.org/decorators-in-python/
    def shout(text):
        return text.upper()

    yell = shout # assign the function shout to a variable
    print(yell('Hello'))

    def greet(func): # greet function takes another function as a parameter
        greeting = func("""Hi, I am created by a function passed as an argument.""") # storing the function in a variable
        print (greeting)

    greet(shout)

    def create_adder(x):
        def adder(y):
            return x+y

        return adder # function can return another function

    add_15 = create_adder(15)
    print(add_15(10))
elif var == 6:
    # reference: https://www.geeksforgeeks.org/decorators-in-python/
    def hello_decorator(func): # defining a decorator
        # inner is a Wrapper function in which the argument is called
        # inner function can access the outer local functions like in this case "func"
        @functools.wraps(func) # 内置装饰器@functools.wraps会保留原函数的元信息,将元信息拷贝到装饰器里面的func函数中
        def inner():
            print("Hello, this is before function execution:", func.__name__) # 函数对象的__name__属性,可以拿到函数的名字

            func() # calling the actual function now inside the wrapper function.
            print("This is after function execution")

        return inner

    # defining a function, to be called inside wrapper
    def function_to_be_used():
        print("This is inside the function !!")

    print("decorator before, function name:", function_to_be_used.__name__)
    function_to_be_used() # 装饰器前

    # passing 'function_to_be_used' inside the decorator to control its behavior
    function_to_be_used = hello_decorator(function_to_be_used)
    # 注意:如果上面inner函数定义前不加@functools.wraps,下面的print将输出inner,添加后会输出function_to_be_used
    print("decorator after, function name:", function_to_be_used.__name__)
    function_to_be_used() # 装饰器后

    # above code is equivalent to
    print("==========================")
    @hello_decorator
    def function_to_be_used2():
        print("This is inside the function !!")

    function_to_be_used2()
elif var == 7:
    # reference: https://www.geeksforgeeks.org/decorators-in-python/
    def hello_decorator(func):
        # The inner function takes the argument as *args and **kwargs which means
        # that a tuple of positional arguments or a dictionary of keyword arguments can be passed of any length
        # This makes it a general decorator that can decorate a function having any number of arguments
        @functools.wraps(func)
        def inner(*args, **kwargs): # *args表示所有的位置参数,**kwargs表示所有的关键字参数.之后再将其传到func函数中,这样保证了能完全传递所有参数
            print("before Execution")

            print("call function:", func.__name__)
            returned_value = func(*args, **kwargs) # getting the returned value
            print("after Execution")

            return returned_value # returning the value to the original frame

        return inner

    # adding decorator to the function
    @hello_decorator
    def sum_two_numbers(a, b):
        print("Inside the function")
        return a + b

    a, b = 1, 2

    # getting the value through return of the function
    print("Sum =", sum_two_numbers(a, b))
elif var == 8:
    class decorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print("function name:", self.func.__name__)
            return self.func(*args, **kwargs)

    @decorator
    def add(a, b):
        print("add value:", a+b)

    add(2, 3)

print("test finish")
