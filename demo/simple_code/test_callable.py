# Blog: https://blog.csdn.net/fengbingchun/article/details/122154674

var = 2
if var == 1:
    # reference: https://www.geeksforgeeks.org/callable-in-python/
    def Geek():
        return 5
  
    # an object is created of Geek()
    let = Geek; print(callable(let)) # True
    let2 = Geek(); print(callable(let2)) # False
  
    # a test variable
    num = 5 * 5; print(callable(num)) # False

    class Geek2:
        def __call__(self):
            print('Hello GeeksforGeeks 2')
  
    # Suggests that the Geek2 class is callable
    print(callable(Geek2)) # True
  
    # This proves that class is callable
    GeekObject2 = Geek2()
    # an instance of a class with a __call__ method
    GeekObject2() # this is calling the __call__ method, Hello GeeksforGeeks 2

    class Geek3:
        def testFunc(self):
            print('Hello GeeksforGeeks 3')
  
    # Suggests that the Geek3 class is callable
    print(callable(Geek3)) # True
  
    # the Geek3 class is callable, but the instance of Geek3 is not callable() and it returns a runtime error
    GeekObject3 = Geek3()
    # The object will be created but returns an error on calling
    GeekObject3() # TypeError: 'Geek3' object is not callable
elif var == 2:
    # reference: https://pythonsimplified.com/what-is-a-callable-in-python/
    # 内置函数也是函数,因此它们也是可调用的,即callable()返回True. 所有的内置函数都是可调用的
    print(callable(min)) # True
    print(callable(max)) # True
    print(callable(print)) # True
    print(callable(int)) # True, int class
    print(callable(float)) # True, float class

    print(callable(str)) # True, str class
    print(callable(list)) # True, list class

    # 所有用户定义的函数也是可调用的
    def hello(user):
        print(f"Welcome to Python Simplified, {user}")

    print(callable(hello)) # True

    # lambda函数也是可调用的
    print(callable(lambda x: x**2)) # True

    # 用户定义的类也是可调用的
    class Rectangle:
        def __init__(self, width, height):
            self.height = height
            self.width = width
        def area(self):
            return self.width * self.area

    print(callable(Rectangle)) # True

    # 所有内置方法也是可调用的
    my_list = [1,2,3,4,5]
    print(callable(my_list.append)) # True

print("test finish")
