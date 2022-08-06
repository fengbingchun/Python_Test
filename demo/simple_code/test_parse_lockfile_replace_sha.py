import sys
import shutil
import os

def usage():
    if len(sys.argv) -1 != 2:
        print("Error: input parameter length must be 2, for example: utils/build.lock face/build.lock")
        sys.exit(1)

    return sys.argv[1], sys.argv[2]

def extract_sha(filename):
    names = []
    shas = []
    substr = "dependencies."

    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            if line.find(substr) != -1:
                names.append(line)
                shas.append(f.readline())

    return names, shas
 
def replace_sha(filename, names, shas, tmpfile):
    contents = []
    flag = False
    count = 0

    with open(filename, "r") as f:
        for line in f:
            if flag:
                flag = False
                continue

            contents.append(line)
            for name in names:
                if line == name:
                    contents.append(shas[count])
                    count += 1
                    flag = True
    
    with open(tmpfile, "w") as f:
        for content in contents:
            f.write(content)

def replace_file(srcfile, dstfile):
    shutil.move(srcfile, dstfile)

def main():
    filename1, filename2 = usage()

    names, shas = extract_sha(filename1)

    tmpfile = "tmp.txt"
    replace_sha(filename2, names, shas, tmpfile)

    replace_file(tmpfile, filename2)
    print("test finish")

if __name__ == "__main__":
    main()
