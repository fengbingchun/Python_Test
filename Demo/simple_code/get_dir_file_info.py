import os
import sys
import hashlib

// Blog: https://blog.csdn.net/fengbingchun/article/details/86665247

def Usage():
    ''' usage description '''
    num = len(sys.argv)
    if num != 3:
        print("Error: please input two parameters")
        print("for example: {} path_name save_file_name".format(sys.argv[0]))
        sys.exit(1)

def GetFilesList():
    ''' get file list '''
    input_path_name = sys.argv[1]
    result = list()

    for dirpath, dirnames, filenames in os.walk(input_path_name, followlinks=True):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            result.append(file_path)

    result.sort()
    return result

def CalcFileSha256(filname):
    ''' calculate file sha256 '''
    with open(filname, "rb") as f:
        sha256obj = hashlib.sha256()
        sha256obj.update(f.read())
        hash_value = sha256obj.hexdigest()
        return hash_value

def CalcFileSize(filename):
    ''' calculate file size '''
    return os.stat(filename).st_size

def GetFileContent():
    ''' get file contnet '''
    files_list = GetFilesList()
    result = list()

    for f in files_list:
        hash = CalcFileSha256(f)
        size = CalcFileSize(f)
        file_name = os.path.basename(os.path.realpath(f))
        path_name = os.path.dirname(os.path.realpath(f))
        dictionary = {"path": path_name, "filename": file_name, "sha256": hash, "size": size}
        #print("result: {}".format(dictionary))
        result.append(dictionary)
    return result

def WriteToFile(contents):
    ''' write content to the specified file '''
    fp = open(sys.argv[2], "w")

    for content in contents:
        #print("content:", content)
        str0 = str(content)
        str1 = str0.replace("\\\\", "/")
        fp.write(str1)
        fp.write("\n")
    fp.close()

def ReplaceStr(src_str, new_str):
    ''' replace source string with new string '''
    contents = list()
    
    fp = open(sys.argv[2], "r")
    line = fp.readline()
    while line:
        contents.append(line)
        line = fp.readline()
    fp.close()

    fp = open(sys.argv[2], "w")
    for content in contents:
        str0 = content.replace(src_str, new_str)
        fp.write(str0)
    fp.close()

def main():
    Usage()
    WriteToFile(GetFileContent())
    ReplaceStr(" ", "")
    ReplaceStr("'", "\"")

if __name__ == "__main__":
    main()