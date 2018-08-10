'''
面向对象(class)测试代码
reference: http://www.runoob.com/python3/python3-class.html
'''

# 1.
class MyClass:
    """一个简单的类实例"""
    i = 12345

    # 类的方法与普通的函数只有一个特别的区别:它们必须有一个额外的第一个参数名称,按照惯例它的名称是self
    def f(self):
        return 'hello world'

x = MyClass() # 实例化类
# 访问类的属性和方法
print("MyClass类的属性i为:", x.i)
print("MyClass类的方法f输出为:", x.f())
print()

# 2.
class Complex:
    # 类可能会定义一个名为__init__()的特殊方法(构造方法).类定义了__init__()方法的话，类的实例化操作会自动调用__init__()方法
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
print()

# 3.
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
print()

# 4.
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 两个下划线开头，声明该属性为私有,在类外部无法直接进行访问,在类内部方法中使用时用self.***
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s说: 我%d岁." % (self.name, self.age))

p = people('runoob', 10, 30)
p.speak()
print()

# 5. 单继承
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s说:我%d岁了,我在读%d年级"%(self.name, self.age, self.grade))

s = student('ken', 10, 60, 3)
s.speak()
print()

# 6. 多继承
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫%s,我是一个演说家,我演讲的主题是%s" % (self.name, self.topic))

class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
print()

# 7. 方法重写
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')

c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法

# 8. 类的私有属性
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)  # 报错，实例不能访问私有变量
print()

# 9. 类的私有方法
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name:', self.name)
        print('url:', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
#x.__foo()  # 报错
print()

# 10. 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
