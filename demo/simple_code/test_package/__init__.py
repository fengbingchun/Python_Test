# reference: https://towardsdatascience.com/whats-init-for-me-d70a312da583

var = 4

print("import package: test_package")

if var == 1: # 第一种方式,导入模块中所有内容
    # from .module import *
    from .foo import *
    from .bar import *
    from .baz import *
elif var == 2: # 第二种方式,指定模块中要导入的内容,同一模块中若导入多个函数，中间用逗号分割: from .module import func1, func2
    # from .module import func
    from .foo import foo_func
    from .bar import bar_func
    from .baz import baz_func
elif var == 3: # 第三种方式
    import test_package.foo
    import test_package.bar
    import test_package.baz
elif var == 4: # 使用__all__
    __all__ = ["foo", "bar"]
