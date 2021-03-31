'''
列表测试代码
reference: http://www.runoob.com/python3/python3-list.html
'''

# 1. 访问列表中的值：使用下标索引来访问列表中的值，同样也可以使用方括号的形式截取字符
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]:", list1[0])
print ("list2[1:5]:", list2[1:5])
print("\n")

# 2. 更新列表：可以对列表的数据项进行修改或更新，也可以使用append()方法来添加列表项
list1 = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为:", list1[2])
list1[2] = 2001
print ("更新后的第三个元素为:", list1[2])
print("\n")

# 3. 删除列表元素：可以使用del语句来删除列表的元素
list1 = ['Google', 'Runoob', 1997, 2000]
print (list1)
del list1[2]
print("删除第三个元素:", list1)
print("\n")

# 4. 列表脚本操作符：列表对+和*的操作符与字符串相似.+号用于组合列表，*号用于重复列表
list1 = [1, 2, 3]; list2 = [4, 5, 6]
list3 = list1 + list2
print("list3:", list3)

list4 = list1 * 4
print("list4:", list4)
print("\n")

# 5. 空列表
list1 = list()
print("list1 size:", len(list1))
list1.append("hello")
list1.append("beijing")
print("list1 size:", len(list1))
print("list1[1]:", list1[1])
print("\n")

# 6. 赋值
list1 = [[1, 2, 3], [4, 5, 6]]
print("list1:", list1)
a, b = list1
print("a:", a)
print("b:", b)
print("\n")

