import numpy as np
from matplotlib import pyplot as plt

# 一维
a = np.array([1, 2, 3]); print(a) # [1 2 3]
# 等间隔数字的数组
b = np.arange(10); print(b) # [0 1 2 3 4 5 6 7 8 9]

# 二维
c = np.array([[1, 2], [3, 4]]); print(c) # [[1 2]
										 #  [3 4]]
# ndmin指定返回数组的最小维数
d = np.array([1, 2, 3, 4, 5]); print(d) 		 # [1 2 3 4 5]
e = np.array([1, 2, 3, 4, 5], ndmin=2); print(e) # [[1 2 3 4 5]]

# dtype:数组的所需数据类型
f = np.array([1, 2, 3], dtype=complex); print(f) # [1.+0.j 2.+0.j 3.+0.j]

# 使用数组标量类型
dt = np.dtype(np.int32); print(dt) # int32
# int8,int16,int32,int64可替换为等价的字符串'i1', 'i2', 'i4', 'i8'
dt = np.dtype('i8'); print(dt) # int64

# 调整数组shape
a = np.array([[1, 2, 3], [4, 5, 6]]); print(a); # [[1 2 3]
												#  [4 5 6]]
a.shape = (3, 2); print(a)                      # [[1 2]
												#  [3 4]
												#  [5 6]]
a = np.array([[1, 2, 3], [4, 5, 6]]); b = a.reshape(3, 2); print(b) # [[1 2]
												                    #  [3 4]
												                    #  [5 6]]

# ndim:返回数组的维数
a = np.arange(24); print(a.ndim) # 1
# numpy.reshape: 在不改变数据的条件下修改形状
b = a.reshape(2, 4, 3); print(b.ndim) # 3

# itemsize:返回数组中每个元素的字节单位长度
a = np.array([1, 2, 3, 4], dtype=np.int8); print(a.itemsize) # 1
a = np.array([1, 2, 3, 4], dtype=np.float32); print(a.itemsize) # 4

# 空数组
x = np.empty([3, 2], dtype='i1'); print(x) # 数组x的元素为随机值，因为它们未初始化

# 含有5个0的数组，若不指定类型，则默认为float
x = np.zeros(5, dtype=np.int); print(x) # [0 0 0 0 0]
# 含有6个1的二维数组，若不指定类型，则默认为float
x = np.ones([2, 3], dtype=int); print(x) # [[1 1 1]
										 #  [1 1 1]]

# 将列表转换为ndarray
x = [1, 2, 3]
a = np.asarray(x, dtype=float); print(a) # [1. 2. 3.]
# 将元组转换为ndarray
x = (1, 2, 3)
a = np.asarray(x, dtype=complex); print(a) # [1.+0.j 2.+0.j 3.+0.j]

# 使用内置的range()函数创建列表对象
x = range(5); print(x) # range(0, 5)
# 从列表中获得迭代器
it = iter(x); print(it) # <range_iterator object at 0x000000000330BFD0>
# 使用迭代器创建ndarray, fromiter函数从任何可迭代对象构建一个ndarray对象,返回一个新的一维数组
y = np.fromiter(it, dtype=float); print(y) # [0. 1. 2. 3. 4.]

# arange函数返回ndarray对象，包含给定范围内的等间隔值
# numpy.arange(start, stop, step, dtype), start起始值，默认为0;stop终止值，不包含; step间隔，默认为1
x = np.arange(4, dtype=float); print(x) # [0. 1. 2. 3.]
x = np.arange(10, 20, 2); print(x) # [10  12  14  16  18]

# numpy.linspace，此函数类似于arange，在此函数中，指定了范围之间的均匀间隔数量，而不是步长
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
# start,起始值;stop,终止值,如果endpoint为true,该值包含于序列中;num,要生成的等间隔样例数量,默认为50;
# endpoint,序列中是否包含stop值,默认为true;retstep,如果为true,返回样例,以及连续数字之间的步长
x = np.linspace(10, 20, 5); print(x) # [10. 12.5 15. 17.5  20.]
x = np.linspace(10, 20, 5, endpoint=False); print(x) # [10. 12. 14. 16. 18.]
x = np.linspace(1,2,5, retstep=True); print(x) # (array([ 1.  ,  1.25,  1.5 ,  1.75,  2.  ]), 0.25)

# numpy.logspace,此函数返回ndarray对象,包含在对数刻度上均匀分布的数字.刻度的开始和结束端点是某个底数的幂,通常为10
# numpy.logscale(start, stop, num, endpoint, base, dtype)
# base,对数空间的底数，默认为10;其它参数同numpy.linspace
a = np.logspace(1.0, 2.0, num=5); print(a) # [10. 17.7827941 31.6227766 56.23413252 100.]
a = np.logspace(1, 10, num=5, base=2); print(a) # [2. 9.51365692 45.254834 215.2694823 1024.]

# ndarray对象的内容可以通过索引或切片来访问和修改，就像Python的内置容器对象一样;
# 基本切片：通过将start、stop和step参数提供给内置的slice函数来构造一个Python slice对象，用来提前数组的一部分
a = np.arange(10); s = slice(2,7,2); print(a[s]) # [2 4 6]
# 通过将由冒号分隔的切片参数(start:stop:step)直接提供给ndarray对象,也可以获得相同的结果
a = np.arange(10); b = a[2:7:2]; print(b) # [2 4 6]
a = np.arange(10); b = a[2:]; print(b) # [2 3 4 5 6 7 8 9]
a = np.arange(10); b = a[2:5]; print(b) # [2 3 4]
# 切片还可以包括省略号(...),来使选择元组的长度与数组的维度相同
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
b = a[..., 1]; print(b) # [2 4 5]
c = a[1, ...]; print(c) # [3 4 5]

# 高级索引：如果一个ndarray是非元组序列，数据类型为整数或布尔值的ndarray，或者至少一个元素为
# 序列对象的元组，我们就能够用它来索引ndarray，高级索引始终返回数据的副本
# 高级索引:整数：基于N维索引来获取数组中任意元素
x = np.array([[1, 2], [3, 4], [5, 6]])
# y中包括数组x中(0,0), (1,1), (2,0)位置处的元素
y = x[[0,1,2], [0,1,0]]; print(y) # [1 4 5]

# 高级索引：布尔值：当结果对象是布尔运算的结果时，将使用此类型的高级索引
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
y = x[x > 5]; print(y) # [6 7 8 9 10 11]

# ~(取补运算符)来过滤NaN
x = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
y = x[~np.isnan(x)]; print(y) # [1. 2. 3. 4. 5.]

# 从数组中过滤掉非复数元素
x = np.array([1, 2+6j, 5, 3.5+5j])  
y = x[np.iscomplex(x)]; print(y) # [2.0+6.j 3.5+5.j]

# 广播：是指NumPy在算术运算期间处理不同形状的数组的能力, 对数组的算术运算通常在相应的元素上运行
# 如果两个数组的维数不相同，则元素到元素的操作是不可能的。然而，在NumPy中仍然可以对形状不相似的数组进行操作，因为它拥有广播功能。
# 较小的数组会广播到较大数组的大小，以便使它们的形状可兼容
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b; print(c) # [10 40 90 160]

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0]])
b = np.array([1.0,2.0,3.0])
c = a + b; print(c) # [[1.0 2.0 3.0]
                    #  [11. 12. 13.]]

# 数组上的迭代：NumPy包包含一个迭代器对象numpy.nditer。它是一个有效的多维迭代器对象，可以用于在数组上进行迭代。
# 数组的每个元素可使用Python的标准Iterator接口来访问
a = np.arange(0, 60, 5)
a = a.reshape(3,4)
for x in np.nditer(a):
	print(x, end=' ') # 0 5 10 15 20 25 30 35 40 45 50 55

print('\n')
# 修改数组的值: nditer对象的一个可选参数op_flags,其默认值为只读,但可以设置为读写或只写模式.这将允许使用此迭代器修改数组元素
for x in np.nditer(a, op_flags=['readwrite']):
	x[...]=2*x; print(x, end=' ') # 0 10 20 30 40 50 60 70 80 90 100 110

print('\n')
# numpy.raval:返回展开的一维数组，并且按需生成副本。返回的数组和输入数组拥有相同数据类型
a = np.arange(8).reshape(2,4)
b = a.ravel(); print(b) # [0 1 2 3 4 5 6 7]

# numpy.unique: 返回输入数组中的去重元素数组
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
u = np.unique(a); print(u) # [2 5 6 7 8 9]

# 位操作:bitwise_and, bitwise_or, invert, left_shift, right_shift
a,b = 13,17; print(bin(a), bin(b)) # 0b1101 0b10001
c = np.bitwise_and(13, 17); print(c) # 1
c = np.bitwise_or(13, 17); print(c) # 29

# 字符串函数：add, multiply, center, capitalize, title, lower, upper, split, splitlines, strip, join, replace, decode, encode
print(np.char.add(['hello'],[' Spring'])) # ['hell Spring']
print(np.char.multiply('Hello ',3)) # Hello Hello Hello
# numpy.char.center: 此函数返回所需宽度的数组,以便输入字符串位于中心,并使用fillchar在左侧和右侧进行填充
print(np.char.center('hello', 20, fillchar = '*')) # *******hello********
a = np.char.encode('hello', 'cp500'); print(a) # b'\x88\x85\x93\x93\x96'
b = np.char.decode(a, 'cp500'); print(b) # hello

# 三角函数：sin, cos, tan, arcsin, arccos, arctan
a = np.array([0, 30, 45, 60, 90])
b = np.sin(a*np.pi/180); print(b) # [ 0. 0.5 0.70710678 0.8660254 1.]

# 舍入函数: around, floor, ceil
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
b = np.around(a); print(b) # [1. 6. 123. 1. 26.]

# 算数运算：add, subtract, multiply, divide, reciprocal, power, mod 输入数组必须具有相同的形状或符合数组广播规则
a, b = [5, 6], [7, 10]
c = np.subtract(a, b); print(c) # [-2 -4]

# 统计函数：用于从数组中给定的元素中查找最小，最大，百分标准差和方差等, amin, amax, ptp, percentile, median, mean, average, std
a = np.array([1, 2, 3, 4, 5])
print(np.amin(a)) # 1
print(np.median(a)) # 3.0
print(np.mean(a)) # 3.0

# 副本和视图: 在执行函数时，其中一些返回输入数组的副本，而另一些返回视图。 当内容物理存储在另一个位置时，称为副本。
# 另一方面，如果提供了相同内存内容的不同视图，我们将其称为视图
a = np.arange(6); print(a) # [0 1 2 3 4 5]
print(id(a)) # 54667664
b = a
print(id(b)) # 54667664
b.shape = 2,3
print(a); # [[0 1 2]
          #  [3 4 5]]

# IO: ndarray对象可以保存到磁盘文件并从磁盘文件加载
# load()和save()函数处理NumPy二进制文件(带npy扩展名)
# loadtxt()和savetxt()函数处理正常的文本文件
a = np.array([1, 2, 3, 4, 5])
np.save('E:/GitCode/Python_Test/test_data/outfile.npy', a)
b = np.load('E:/GitCode/Python_Test/test_data/outfile.npy')
print(b) # [1 2 3 4 5]

np.savetxt('E:/GitCode/Python_Test/test_data/outfile.txt', a)
b = np.loadtxt('E:/GitCode/Python_Test/test_data/outfile.txt')
print(b) # [1. 2. 3. 4. 5.]

# Matplotlib是Python的绘图库，在http://matplotlib.org/examples/ 中含有大量的matplotlib使用用例
x = np.arange(1,11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y, 'ob')
plt.show()




























































