# Blog: https://blog.csdn.net/fengbingchun/article/details/120873371

import sys

var = 4

if var == 1: # 第一种方式,导入模块中所有内容
    import test_package

    test_package.foo_func()
    test_package.bar_func()
    test_package.baz_func()

    test_package.save() # 不能确定调用的是bar.py中的是还是foo.py中的. 由__init__.py决定,会调用后import的
    #test_package._calc() # AttributeError: module 'test_package' has no attribute '_calc'
elif var == 2: # 第二种方式,指定模块中要导入的内容,同一模块中若导入多个函数，中间用逗号分割: from .module import func1, func2
    import test_package

    test_package.foo_func()
    test_package.bar_func()
    test_package.baz_func()
elif var == 3: # 第三种方式
    # 用户可以采用三种不同的使用方法
    method = 3
    if method == 1:
        import test_package

        test_package.foo.foo_func()
        test_package.bar.bar_func()
        test_package.baz.baz_func()
    elif method == 2:
        from test_package import foo, bar, baz # 从包中导入子模块

        foo.foo_func()
        bar.bar_func()
        baz.baz_func()
    elif method == 3:
        import test_package.foo as ex_foo # 从包中导入单个模块
        import test_package.bar as ex_bar
        import test_package.baz as ex_baz

        ex_foo.foo_func()
        ex_bar.bar_func()
        ex_baz.baz_func()

        ex_foo.save()
        ex_bar.save()

        print("csdn addr:", ex_foo.csdn_addr)
        print("sys path:", sys.path)

        print("dir:", dir(ex_foo)) # dir为内置函数,获取指定模块的方法列表,包括变量、函数等等
elif var == 4: # 使用__all__
    from test_package import * # import * 就只会导入__all__列出的成员

    foo.foo_func()
    bar.bar_func()
    #baz.baz_func() # NameError: name 'baz' is not defined
