from ctypes import *
#import ctypes

print(windll.kernel32)
#dll = ctypes.windll('E:/GitCode/Python_Test/lib/rel/x64_vc12/Test_DLL_1.dll');
dll = CDLL('E:/GitCode/Python_Test/lib/rel/x64_vc12/Test_DLL_1.dll')
#print(mydll)