import contextlib

# Blog: https://blog.csdn.net/fengbingchun/article/details/120593261

var = 3

if var == 1:
    # reference: https://www.geeksforgeeks.org/context-manager-in-python/
    # 基于类的上下文管理器
    class FileManager():
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_value, exc_traceback):
            self.file.close()

    # loading a file
    with FileManager('test.txt', 'w') as f:
        f.write('Test')

    print(f.closed) # True
elif var == 2:
    # https://medium.com/swlh/3-ways-to-create-context-managers-in-python-a88e3ba536f3
    # 基于生成器的上下文管理器:代替__enter__和__exit__方法,生成器和@contextlib.contextmanager装饰器将在yield语句之前运行所有内容,就好像它是__enter__方法的一部
    # 分一样,产生的值可能是__enter__方法将返回的结果.之后,将运行with块中的内容,作为最后一步,将运行yield语句之后的代码,就好像它是__exit__方法一样
    @contextlib.contextmanager
    def file_hanlder(file_name, file_mode):
        file = open(file_name, file_mode)
        print("open file")
        yield file # yeild之前的代码会在上下文管理器中作为__enter__方法执行,并将结果通过yield返回,所有在yield之后的代码会作为__exit__方法执行
        file.close()
        print("close file")

    with file_hanlder("test.txt", "w") as f:
        f.write("Test2")
        print("write file")

    print(f.closed) # True
elif var == 3:
    # https://medium.com/swlh/3-ways-to-create-context-managers-in-python-a88e3ba536f3
    # 基于函数装饰器的上下文管理器:函数装饰器方法的问题之一是无法访问__enter__方法的返回值
    class file_handler_mixin(contextlib.ContextDecorator):
        def __init__(self, file_name, file_mode):
            self._file_name = file_name
            self._file_mode = file_mode
            self._file = None

        def __enter__(self):
            print(f"Enter Method: File Name {self._file_name}")
            self._file = open(self._file_name, self._file_mode) # 无法从装饰函数访问文件对象
            return self._file

        def __exit__(self,exc_type,exc_value,exc_traceback):
            print(f"Exit Method: File Mode {self._file_mode}")
            self._file.close()

    @file_handler_mixin("test.txt", "w")
    def write_to_file():
        print("Not access to the value returned by the __enter__ method")

    write_to_file()

print("test finish")
