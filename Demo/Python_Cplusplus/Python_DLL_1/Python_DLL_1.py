# blog: https://blog.csdn.net/fengbingchun/article/details/80001768
import ctypes

lib = ctypes.cdll.LoadLibrary("E:/GitCode/Python_Test/lib/rel/x64_vc12/Test_DLL_1.dll")

a = 9; b = 3

value = lib.add_(a, b)
print("add result:", value)
value = lib.sub_(a, b)
print("sub result:", value)
print("mul result:", lib.mul_(a, b))
print("div result:", lib.div_(a, b))