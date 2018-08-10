# _module.py中会使用此文件

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

def print_func(par):
    print("Hello:", par)
    return
