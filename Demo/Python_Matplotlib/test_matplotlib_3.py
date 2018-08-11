import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

os_name=os.name
if os_name == "posix": # linux
	print("python running on linux")
else: # nt: windows
	print("python running on windows")

# 函数代码块以def关键词开头，后接函数标识符号和圆括号()
def f(t):
	return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# figure()命令是可选的，默认情况下将创建figure(1)
# 可以通过使用递增图形编号多次调用figure()来创建多个图形
plt.figure(1)
# subplot()命令指定numrows, numcols, fignum,其中fignum的范围是从1到numrows * numcols,
# 如果numrows*numcols<10,则subplot命令中的逗号是可选的，因此，子图subplot(211)与subplot(2,1,1)相同
# 可以创建任意数量的子图和轴域
plt.subplot(211)
plt.title('test matplotlib 3')
# plot()是一个通用命令，并且可接受任意数量的参数
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(2,1,2)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
# text()命令可用于在任意位置添加文本，xlabel(), ylabel()和title()用于在指定的位置添加文本
plt.xlabel('x some numbers')
plt.ylabel('y some numbers')
plt.text(2, 0.25, r'$\mu=100,\ \sigma=15$')
plt.grid(True)

plt.figure(2)
if os_name == "posix":
	img = mpimg.imread('../../test_data/lena.png')
else:
	img = mpimg.imread('E:/GitCode/Python_Test/test_data/lena.png')
plt.show()
