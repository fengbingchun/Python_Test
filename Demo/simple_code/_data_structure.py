'''
数据结构测试代码
reference: http://www.runoob.com/python3/python3-data-structure.html
'''

# 1. Python中列表的方法
a = [66.25, 333, 333, 1, 1234.5]
print("count:", a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1); print("insert:", a)
a.append(333); print("append:", a)
print("index:", a.index(333))
a.remove(333); print("remove:", a)
a.reverse(); print("reverse:", a)
a.sort(); print("sort:", a)
print("pop:", a.pop())
print()

# 2. 列表推导式
vec = [2, 4, 6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])
print([3*x for x in vec if x > 3])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
print()

# 3. 嵌套列表解析
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
print()

# 4. del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]; print(a)
del a[2:4]; print(a)
del a[:]; print(a)
print()

# 5. 元组
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
print()

# 6. 集合:是一个无序不重复元素的序列
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print()

# 7. 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print(tel)
print('guido' in tel)
print('jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))
print()

# 8. 遍历技巧
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i, end=",")
print()

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, end=",")
print()

