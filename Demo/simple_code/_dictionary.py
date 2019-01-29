'''
字典测试代码
reference: http://www.runoob.com/python3/python3-dictionary.html
'''

# 1. 创建字典：字典的每个键值(key=>value)对用冒号(:)分割，整个字典包括在花括号({})中.键必须是唯一的，但值则不必
dict3 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: 37 };
print("dict3:", dict3); print("dict2:", dict2)

# 2. 访问字典里的值：把相应的键放入方括弧. 如果用字典里没有的键访问数据，会输出错误
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict3['Name']: ", dict3['Name'])
print ("dict3['Age']: ", dict3['Age'])
#print ("dict3['Alice']: ", dict3['Alice']) # KeyError: 'Alice'

# 3. 修改字典：向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict3['Age'] = 8;               # 更新 Age
dict3['School'] = "菜鸟教程"  # 添加信息
print ("dict3['Age']: ", dict3['Age'])
print ("dict3['School']: ", dict3['School'])
print("dict3:", dict3)

# 4．删除字典元素：能删单一的元素也能清空字典
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict3['Name'] # 删除键 'Name'
#dict3.clear()     # 删除字典
#del dict3         # 删除字典
print ("dict3['Age']: ", dict3['Age'])
print("dict3:", dict3)
#print ("dict3['School']: ", dict3['School']) # KeyError: 'School'

# 5. 字典键的特性： 创建时如果同一个键被赋值两次，后一个值会被记住
dict3 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
dict3["addr"] = "BeiJing"
print ("dict3['Name']: ", dict3['Name'])
print("dict3:", dict3)

dictx = dict(xx=False, yy=100, zz='spring')
print("dictx:", dictx)
# 注:由print输出字典的值时，每次的值的输出顺序会有所变动
