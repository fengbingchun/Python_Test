# Blog: https://blog.csdn.net/fengbingchun/article/details/119774806

class FileWriter(object):
    def __init__(self, file_name):
        print("run __init__")
        self.file_name = file_name

    def __enter__(self):
        print("run __enter__")
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, type, value, traceback):
        print("run __exit__")
        print("type:", type); print("value:", value); print("traceback:", traceback)
        self.file.close()

print("test FileWriter:")
with FileWriter('tmp.txt') as f:
    print("start write")
    f.write('hello world')
    print("end write")

class ExceptionTest(object):
    def __enter__(self):
        print("run __enter__")
        return self

    def __exit__(self, type, value, traceback):
        print("run __exit__")
        print("type:", type); print("value:", value); print("traceback:", traceback)
        return False # return True # 注意返回True和False的区别:返回True则跳过异常,继续执行with语句之后的语句

    def divide_by_0(self):
        v = 10/0

print("\ntest ExceptionTest:")
with ExceptionTest() as ex:
    ex.divide_by_0()

print("test finish")
