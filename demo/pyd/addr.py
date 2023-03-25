from inspect import currentframe, getframeinfo

def get_addr(label):
    if label == "csdn":
        return "https://blog.csdn.net/fengbingchun/"
    elif label == "github":
        return "https://github.com/fengbingchun"
    else:
        print("#### FileName: %s, Line Number: %d, label: %s" % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno, label))
        raise Exception("Error: Unsupported address")
