# Blog: https://blog.csdn.net/fengbingchun/article/details/122148775

var = 2
if var == 1:
    # reference: https://docs.python.org/3/tutorial/controlflow.html
    # 与嵌套函数定义一样，lambda函数可以从包含的作用域中引用变量
    def make_incrementor(n):
        # 使用一个lambda表达式来返回一个函数
        return lambda x: x + n

    f = make_incrementor(42)
    print(f(0)) # 42
    print(f(1)) # 43

    def mul():
        # 可以有任意数量的参数,但只能有一个表达式
        return lambda x, y: x * y

    f2 = mul()
    print(f2(5, 6)) # 30

    # 传递一个小函数作为参数
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs) # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
elif var == 2:
    # reference: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
    def cube(y):
        return y*y*y
 
    # lambda定义不包含"return"语句,它始终包含返回的表达式
    lambda_cube = lambda y: y*y*y

    print(cube(5)) # 125
    print(lambda_cube(5)) # 125

    # Python Lambda Function with List Comprehension
    tables = [lambda x=x: x*10 for x in range(1, 11)]
    for table in tables:
        print(table(), end=",") # 10,20,30,40,50,60,70,80,90,100,
    print()

    # Python Lambda Function with if-else
    Max = lambda a, b : a if(a > b) else b
    print(Max(1, 2)) # 2

    # lambda函数不允许多个语句,但是,我们可以创建两个lambda函数,然后调用另一个lambda函数作为第一个函数的参数
    List = [[4, 3, 2], [1, 16, 4, 64], [6, 3, 12, 9]]
    # Sort each sublist
    sortList = lambda x: (sorted(i) for i in x) # 升序排序
    # Get the second largest element
    secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)] # 返回list中的第n-2个元素,其中n为list的长度
    res = secondLargest(List, sortList)
    print(res) # [3, 16, 9]

    ages = [13, 90, 17, 59, 21, 60, 5]
    adults = list(filter(lambda age: age>18, ages)) # filter函数接受一个函数和一个列表作为参数
    print(adults) # [90, 59, 21, 60]

    animals = ['dog', 'cat', 'parrot', 'rabbit']
    uppered_animals = list(map(lambda animal: str.upper(animal), animals)) # map函数接受一个函数和一个列表作为参数
    print(uppered_animals) # ['DOG', 'CAT', 'PARROT', 'RABBIT']

print("test finish")
