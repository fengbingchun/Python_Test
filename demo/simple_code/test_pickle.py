import pickle
import sys

# Blog: https://blog.csdn.net/fengbingchun/article/details/125584682

def dictionary_dump_load():
    # reference: https://docs.python.org/zh-cn/3/library/pickle.html
    data = {
        'a': [1, 2.0, 3+4j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
    }

    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    with open('data.pickle', 'rb') as f:
        data2 = pickle.load(f)

    print("dictionary data:", data2) # dictionary data: {'a': [1, 2.0, (3+4j)], 'b': ('character string', b'byte string'), 'c': {False, True, None}}

class example_class:
    # reference: https://realpython.com/python-pickle-module/
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)

def donot_support_lambda():
    square = lambda x : x * x # dill module support lambda serializes
    my_pickle = pickle.dumps(square) # AttributeError: Can't pickle local object 'donot_support_lamda.<locals>.<lambda>'

def func_add(a, b):
    return (a+b)

def main():
    dictionary_dump_load()

    my_object = example_class()
    my_pickled_object = pickle.dumps(my_object)  # Pickling the object
    print(f"pickled object: {my_pickled_object}") # pickled object: b'\x80\x04\x95!\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\rexample_class\x94\x93\x94)\x81\x94.'

    my_object.a_dict = None

    my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
    print(f"unpickled object: {my_unpickled_object.a_dict}") # unpickled object: {'first': 'a', 'second': 2, 'third': [1, 2, 3]}

    # 可通过pickle.HIGHEST_PROTOCOL获取python解释器支持的最高协议,通过pickle.DEFAULT_PROTOCOL获取python解释器支持的默认协议
    print(f"python version: {sys.version}, the highest protocol supported by the interpreter: {pickle.HIGHEST_PROTOCOL}") # python version: 3.10.4 (main, Mar 31 2022, 08:41:55) [GCC 7.5.0], the highest protocol supported by the interpreter: 5
    print(f"python version: {sys.version}, default version: { pickle.DEFAULT_PROTOCOL}") # python version: 3.10.4 (main, Mar 31 2022, 08:41:55) [GCC 7.5.0], default version: 4

    #donot_support_lambda()

    # Python函数和类都可以序列化和反序列化
    with open('data2.pickle', 'wb') as f:
        pickle.dump(func_add, f) # dump function

    with open('data2.pickle', 'rb') as f:
        add = pickle.load(f)

    print("2+3=", add(2, 3)) # 2+3= 5

    print("test finish")

if __name__ == '__main__':
    main()