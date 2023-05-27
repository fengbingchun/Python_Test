import os
from inspect import currentframe, getframeinfo
import numpy as np
from pyquaternion import Quaternion

# Blog: https://blog.csdn.net/fengbingchun/article/details/130900119

def get_dir_list(path):
    dir_list = []
    txt_list = []

    for x in os.listdir(path):
        if x.startswith("N") and x.endswith(".txt"): # it starts with N and ends with .txt
            dir_list.append(path+"/"+x)
            txt_list.append(x)

    return dir_list, txt_list

def parse_txt(txt_name):
    with open(os.path.join(txt_name), "r") as f:
        elements = [] # 6*4

        for line in f:
            if line[0] == "#":
                continue

            tmp = []
            for v in line.split(" "):
                tmp.append(v.replace("\n", "")) # remove line breaks(\n) at the end of the line
            ret = [float(ele) for ele in tmp] # str to float
            if len(ret) != 4:
                print(f"Error: the number of cols that are not supported:{len(ret)}, LINE: {getframeinfo(currentframe()).lineno}")
                raise
    
            elements.append(ret)

        if len(elements) != 6:
            print(f"Error: the number of rows that are not supported:{len(elements)}, LINE: {getframeinfo(currentframe()).lineno}")
            raise

    return elements

def get_number(name):
    pos = 0
    for index in name:
        if index.isnumeric():
            break
        pos = pos + 1

    number = int(name[pos:])
    #print(f"number:{number}")

    return number

def get_image_id_and_name(txt_name, image_suffix):
    pos = txt_name.rfind("/")
    name = txt_name[pos+1:]
    image_name = name.replace("txt", image_suffix)
    #print(f"image name: {image_name}; name: {name}")

    image_id = str(name[0:-4]) # remove: .txt
    #image_id = str(name[0:-8]) # remove: _KRT.txt
    #print(f"image id: {image_id}")
    image_id = get_number(image_id)

    return image_id, image_name

def generate_cameras_txt(dir_list, cameras_txt_name, images_number, image_size, image_suffix, camera_model):
    f = open(cameras_txt_name, "w")
    f.write("# Camera list with one line of data per camera:\r")
    f.write("#   CAMERA_ID, MODEL, WIDTH, HEIGHT, PARAMS[]\r")
    f.write("# Number of cameras: %d\r" % images_number)

    for x in dir_list:
        elements = parse_txt(x)
        #print(f"{x} elements:\n\t{elements}")

        image_id, image_name = get_image_id_and_name(x, image_suffix)
        #print(f"id:{image_id},name:{image_name}")

        string = str(image_id) + " " + camera_model + " " + str(image_size[0]) + " " + str(image_size[1])
        string = string + " " + str(elements[0][0]) + " " + str(elements[1][1]) + " " + str(elements[0][2]) + " " + str(elements[1][2]) + "\r"
        f.write(string)

    f.close()

def get_rotate_matrix(elements):
    R = [[elements[3][0], elements[3][1], elements[3][2]],
         [elements[4][0], elements[4][1], elements[4][2]],
         [elements[5][0], elements[5][1], elements[5][2]]]
    #print(f"R:\r{R}")

    return np.array(R)

def calculate_quaternion(elements):
    m = get_rotate_matrix(elements)
    m = m.transpose()

    return Quaternion(matrix=m), m

def generate_images_txt(dir_list, images_txt_name, images_number, image_suffix):
    f = open(images_txt_name, "w")
    f.write("# Image list with two lines of data per image:\r")
    f.write("#   IMAGE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID, NAME\r")
    f.write("#   POINTS2D[] as (X, Y, POINT3D_ID)\r")
    f.write("# Number of images: %d, mean observations per image:\r" % images_number)

    for x in dir_list:
        elements = parse_txt(x)
        quaternion, m = calculate_quaternion(elements)
        #print(f"quaternion:\r\t{quaternion}")
        
        T = np.array([[elements[3][3]], [elements[4][3]], [elements[5][3]]])
        T = np.matmul((-m), T) # 3*1

        image_id, image_name = get_image_id_and_name(x, image_suffix)

        string = str(image_id) + " " + str(quaternion[0]) + " " + str(quaternion[1]) + " " + str(quaternion[2]) + " " + str(quaternion[3]) + " "
        string = string + str(T[0][0]) + " " + str(T[1][0]) + " " + str(T[2][0]) + " " + str(image_id) + " " + str(image_name) + "\r\n"
        f.write(string)

    f.close()

if __name__ == "__main__":
    dir_list, txt_list = get_dir_list("test_data/txt")
    #print(f"dir_list:\n\t{dir_list}\ntxt_list:\n\t{txt_list}")

    cameras_txt_name = "test_data/txt/cameras.txt"
    images_number = 118
    image_size = [5184, 3456] # width, height
    image_suffix = "PNG"
    camera_model = "PINHOLE"
    generate_cameras_txt(dir_list, cameras_txt_name, images_number, image_size, image_suffix, camera_model)
    
    images_txt_name = "test_data/txt/images.txt"
    generate_images_txt(dir_list, images_txt_name, images_number, image_suffix)

    print("test finish")
