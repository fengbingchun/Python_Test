import numpy as np
from typing import Callable

# Blog: https://blog.csdn.net/fengbingchun/article/details/125284883

# 1. ...是一个python对象,叫Ellipsis
print(type(...)) # output: <class 'ellipsis'>
print(...) # output: Ellipsis
print(Ellipsis) #  output: Ellipsis
print(bool(...)) # output: True

# 3. slice: we can not have multiple ellipsis in a single slicing
array = np.random.rand(2, 4) # a 2-dimensional matrix of order 2*4(rows*cols)
print(array); print(array[...]); print(array[Ellipsis]) # they are all equivalent
print(array[..., 0]); print(array[:,0]); print(array[Ellipsis, 0]) # they are all equivalent
print(array[0, ...])

# 4. type hints
# 当函数的参数类型允许为Any
def inject(get_next_item: Callable[..., str]) -> None:
    ...

def foo(x: ...) -> None:
    ...

# 当函数的返回类型为Any
class flow:
    def __understand__(self, name: str, value: ...) -> None:
        ...

# 5. used as Pass Statement inside Functions
# foo1 and foo2 styles are same
def foo1():
    pass

def foo2():
    ...

# 6. used as a default argument value
def foo3(x = ...):
    return x

def foo4(x = None):
    return x

print("foo3:", foo3) # output: foo3: <function foo3 at 0x7f4e7ffcf5e0>
print("foo4:", foo4) # output: foo4: <function foo4 at 0x7f4e7ffcf550>

print("\ntest finish")
