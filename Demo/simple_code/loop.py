# 循环语句测试代码
# reference: http://www.runoob.com/python3/python3-loop.html

# 1. while
n = 100
sum = 0
counter = 1

while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

# 2. while ... else
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# 3. for
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

# 4. for ... else
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# 5. range
for i in range(5):
    print(i)

for i in range(5, 9):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

list1 = list(range(5))
print(list1)

# 6. break
for letter in 'Runoob':
    if letter == 'b':
        break
    print('当前字母为 :', letter)

var = 10
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!")

# 7. continue
for letter in 'Runoob':
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 1
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

# 8. break else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# 9. pass
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)
print("Good bye!")
