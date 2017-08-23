# 函数测试代码
# reference: http://www.runoob.com/python3/python3-function.html

# 1. 函数
def area(width, height):
    return width * height
def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

# 2. 传不可变对象
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b ) # 结果是 2

# 3. 传可变对象
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return

mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)

# 4. 关键字参数
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;

printinfo(age=50, name="runoob");

# 5. 默认参数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;

printinfo(age=50, name="runoob");
print("------------------------")
printinfo(name="runoob");

# 6. 不定长参数
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;

printinfo(10);
printinfo(70, 60, 50);

# 7. 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

# 8. return 语句
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total;

# 调用sum函数
total = sum( 10, 20 );
print ("函数外 : ", total)

# 9. 变量作用域
total = 0; # 这是一个全局变量
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total;

sum( 10, 20 );
print ("函数外是全局变量 : ", total)

# 10. global
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

# 11. nonlocal
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
