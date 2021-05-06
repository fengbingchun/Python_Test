'''
元组测试代码
reference: http://www.runoob.com/python3/python3-tuple.html
'''

# 1. 创建元组：使用小括号，在括号中添加元素，并使用逗号隔开
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
print(tup1); print(tup2); print(tup3)
tup1 = () # 创建空元组
print(tup1)
print("\n")

# 2. 访问元组：元组可以使用下标索引来访问元组中的值
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5]) #(2, 3, 4, 5)
print("\n")

# 3. 修改元组：元组中的元素值是不允许修改的，但可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
#tup1[0] = 100 # 修改元组元素操作是非法的
# 创建一个新的元组
tup3 = tup1 + tup2 # 元组中的元素类型可以不相同
print (tup3)
print("\n")

# 4. 删除元组：元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
print (tup)
del tup
print ("删除后的元组tup: ")
#print (tup) # NameError: name 'tup' is not defined
print("\n")

# 5. 元组内置函数：len、min、max、tuple(seq)(将列表转换为元组)
tuple1 = ('5', '4', '8')
print("len:", len(tuple1))
print("min:", min(tuple1))
print("max", max(tuple1))
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
print("list1:", list1)
tuple1=tuple(list1)
print("tuple1:", tuple1)
