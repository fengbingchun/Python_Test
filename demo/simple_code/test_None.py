# Blog: https://blog.csdn.net/fengbingchun/article/details/119358832

var = None; print(var) # None
if var is None:
    print("var has a value of None") # print
else:
    print("var:", var)

print(type(None)) # <class 'NoneType'>

a = ''; print(a == None) # False
b = []; print(b == None) # False
c = 0; print(c == None) # False
d = False; print(c == None) # False

L = [None] * 5; print(L) # [None, None, None, None, None]

def func():
    x = 3
obj = func(); print(obj) # None

def func2():
    return None
obj2 = func2(); print(obj2) # None

def func3():
    return
obj3 = func3(); print(obj3) # None

def func4(x, y=None):
    if y is not None:
        print("y:", y)
    else:
        print("y is None")
    print("x:", x)
x = [1, 2]; obj4 = func4(x) # y is None
y = [3, 4]; obj4 = func4(x, y) # y: [3, 4]
