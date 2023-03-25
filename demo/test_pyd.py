import addr

# Blog: https://blog.csdn.net/fengbingchun/article/details/129765302

def print_addr():
    print("csdn addr:", addr.get_addr("csdn"))
    print("github addr:", addr.get_addr("github"))
    print("other addr:", addr.get_addr("other"))

if __name__ == "__main__":
    print_addr()
    print("test finish")