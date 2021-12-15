from typing import overload, Union
from typing_extensions import Literal

# Blog: https://blog.csdn.net/fengbingchun/article/details/121959036

var = 2
if var == 1:
    # python3中增加了Function Annotation(函数注解,能够声明类型)的功能,可以使用类型检查工具如mypy达到类型静态检查的效果
    def foo(name: str) -> str:
        return "csdn id:" + name

    print(foo("fengbingchun"))
    #print(foo(5)) # TypeError: can only concatenate str (not "int") to str
elif var == 2:
    # reference: https://stackoverflow.com/questions/59359943/python-how-to-write-typing-overload-decorator-for-bool-arguments-by-value
    # 被装饰的函数的输入类型和输出类型都可以更改,非@overload-decorated定义必须通用
    # The first two overloads use Literal[...] so we can have precise return types:
    @overload
    def myfunc(arg: Literal[True]) -> str: ...

    @overload
    def myfunc(arg: Literal[False]) -> int: ...

    # The last overload is a fallback in case the caller provides a regular bool
    @overload
    def myfunc(arg: bool) -> Union[str, int]: # Union[str, int] == str | int
        ...

    def myfunc(arg:bool) -> Union[int, str]:
        if arg: return "something"
        else: return 0

    print(myfunc(True))
    print(myfunc(False))

    # Variables declared without annotations will continue to have an inferred type of 'bool'
    variable = True
    print(myfunc(variable))

print("test finish")
