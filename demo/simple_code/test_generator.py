# Blog: https://blog.csdn.net/fengbingchun/article/details/120240229

var = 1
if var == 1:
    # reference: https://docs.python.org/3/reference/expressions.html#yieldexpr
    def echo(value=None):
        print("Execution starts when 'next()' is called for the first time.")
        try:
            while True:
                try:
                    value = (yield value)
                    print("value:", value)
                except Exception as e:
                    value = e
        finally:
            print("Don't forget to clean up when 'close()' is called.")

    generator = echo(1) # 此处echo函数并未真的执行,返回generator对象
    print("object:", generator)
    print(next(generator)) # 当调用next或__next__时,echo函数才正式开始执行
    print(next(generator))
    print("start send"); print(generator.send(10)); print("end send")
    generator.throw(TypeError, "spam")
    generator.close()
elif var == 2:
    # reference: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    mylist = [x*x for x in range(3)]  # mylist is an iterable,  you store all the values in memory
    for i in mylist:
        print(i)

    # Generators are iterators, a kind of iterable you can only iterate over once.
    # Generators do not store all the values in memory, they generate the values on the fly
    mygenerator = (x*x for x in range(3))
    for i in mygenerator:
        print(i)
    for i in mygenerator:
        print(i) # 第二次for in不会有任何值输出, generators can only be used once

    # yield is a keyword that is used like return, except the function will return a generator
    def create_generator():
        print("start ...")
        mylist = range(3)
        for i in mylist:
            yield i*i

    mygenerator2 = create_generator() # create a generator
    print("object:", mygenerator2) # mygenerator2 is an object
    print("value:", mygenerator2.__next__())
    for i in mygenerator2:
        print(i)
    for i in mygenerator2:
        print(i) # 第二次for in不会有任何值输出

    # To master yield, you must understand that when you call the function, the code you have
    # written in the function body does not run. The function only returns the generator object.
    # Then, your code will continue from where it left off each time for uses the generator.
elif var == 3:
    # reference: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
    # The yield statement suspends function’s execution and sends a value back to the caller, but retains enough
    # state to enable function to resume where it is left off. When resumed, the function continues execution
    # immediately after the last yield run.
    def simpleGeneratorFun():
        yield 1
        yield 2
        yield 3

    for value in simpleGeneratorFun():
        print(value)

    # An infinite generator function that prints next square number. It starts with 1
    def nextSquare():
        i = 1
        # An Infinite loop to generate squares
        while True:
            yield i*i
            i += 1 # Next execution resumes from this point

    print("object:", nextSquare())
    for num in nextSquare():
        if num > 100:
            break
        print(num) # the first value is 1

    print("go on:")
    print("object:", nextSquare())
    for num in nextSquare():
        if num > 200:
            break
        print(num) # note: the first value is still 1, instead of 121

print("test finish")
