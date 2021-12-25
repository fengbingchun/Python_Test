from collections import OrderedDict

# Blog: https://blog.csdn.net/fengbingchun/article/details/122140577

var = 2
if var == 1:
    # reference: https://www.geeksforgeeks.org/ordereddict-in-python/
    # 注:在Python 3.7.11中,多次执行以下测试代码,dict和OrderedDict的输出结果始终相同
    # 从python 3.7开始,python dict的插入顺序是有保证的
    print("This is a dict:")
    d = {}
    d["a"] = 1; d["b"] = 2; d["c"] = 3; d["d"] = 4
    for key, value in d.items():
        print(key, value, end=",")

    d["c"] = 5; print("")
    for key, value in d.items():
        print(key, value, end=",")

    d.pop("c"); print("")
    for key, value in d.items():
        print(key, value, end=",")

    d["c"] = 3; print("")
    for key, value in d.items():
        print(key, value, end=",")

    print("\nThis is an Ordered Dict:")
    od = OrderedDict()
    od["a"] = 1; od["b"] = 2; od["c"] = 3; od["d"] = 4
    for key, value in od.items():
        print(key, value, end=",")

    # 如果某个key的值发生变化,key在OrderedDict中的位置保持不变
    od["c"] = 5; print("")
    for key, value in od.items():
        print(key, value, end=",")

    # 删除和重新插入相同的key会将它push到后面作为OrderedDcit,但是,保持插入的顺序
    od.pop("c"); print("")
    for key, value in od.items():
        print(key, value, end=",")

    od["c"] = 3; print("")
    for key, value in od.items():
        print(key, value, end=",")
    print("")
elif var == 2:
    od = OrderedDict()
    print(isinstance(od, OrderedDict)) # True
    print(isinstance(od, dict)) # True

    od["a"] = 1; od["b"] = 2; od["c"] = 3; od["d"] = 4
    # popitem: 返回一个(key, value)键值对.如果last为True,则按LIFO后进先出的顺序返回键值对,否则就按FIFO先进先出的顺序返回键值对
    print(od.popitem(last=True)) # ('d', 4)
    print(od.popitem(last=False)) # ('a', 1)

    od["e"] = 5; od["f"] = 6
    for key, value in od.items():
        print(key, value, end=",") # b 2,c 3,e 5,f 6,
    print("")

    # move_to_end: 将现有key移动到OrderedDict的任一端.如果last为True(默认值),则将item移至末尾;如果last为False,则移至开头;如果key不存在,则触发KeyError
    od.move_to_end("c", last=True)
    for key, value in od.items():
        print(key, value, end=",") # b 2,e 5,f 6,c 3,
    print("")

    od.move_to_end("c", last=False)
    for key, value in od.items():
        print(key, value, end=",") # c 3,b 2,e 5,f 6,
    print("")

    # OrderedDict对象与常规dict比较,对顺序不敏感
    d1 = {"c":3, "b":2, "e":5, "f":6}; print(od == d1) # True
    d2 = {"b":2, "e":5, "f":6, "c":3}; print(od == d2) # True
    print(d1 == d2) # True

    # ​OrderedDict对象之间的相等性判断是顺序敏感的
    od2 = OrderedDict()
    od2["c"] = 3; od2["b"] = 2; od2["e"] = 5; od2["f"] = 6; print(od == od2) # True
    od3 = OrderedDict()
    od3["c"] = 3; od3["b"] = 2; od3["f"] = 6; od3["e"] = 5; print(od3 == od2) # False

print("test finish")
