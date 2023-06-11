import json
import sys
import os
import cv2

def get_json_list(path):
    json_list = []
    for x in os.listdir(path):
        if x.endswith(".json"):
            json_list.append(path+"/"+x)

    return json_list

def parse_json(names):
    jsons_image_names = []
    for name in names:
        images = []
        with open(name, "r") as read_file:
            data = json.load(read_file)
            frames = data["frames"]
            for frame in frames:
                images.append(frame["file_path"])

        jsons_image_names.append(images)

    return jsons_image_names

def get_images_size(json_list, jsons_image_names, width, height):
    index = 0
    for i in json_list:
        print(f"json file:{i}, image number:{len(jsons_image_names[index])}")
        for name in jsons_image_names[index]:
            #print(f"name:{name}")
            img = cv2.imread(name)
            h, w, _ = img.shape
            #print(f"w: {w}, h:{h}")
            if h != height or w != width:
                print(f"#### Warning: name:{name}, w:{w}, h:{h}")

        index = index + 1

def get_image_names(image_names):
    names = []
    for name in image_names:
        pos = name.rfind("/")
        name = name[pos+1:]
        names.append(name)

    return names

def get_unique_image_list(jsons_image_names):
    image_names = []
    for names in jsons_image_names:
        for name in names:
            image_names.append(name)
    #print(f"len:{len(image_names)}")

    image_names = list(set(image_names))
    #print(f"len:{len(image_names)}")
    image_names = get_image_names(image_names)

    return image_names

def list_sort(image_list):
    image_list.sort()

    print(f"image number:{len(image_list)}")
    for name in image_list:
        print(name)

if __name__ == "__main__":
    path = "./test_data/liu/2_rotate_270"
    json_list = get_json_list(path)
    #print(f"json_list:\n{json_list}")

    #names = ["./test_data/liu/2/transforms.json"]
    jsons_image_names = parse_json(json_list)
    #print(jsons_image_names)

    width = 4000
    height = 6000
    #get_images_size(json_list, jsons_image_names, width, height)

    unique_image_list = get_unique_image_list(jsons_image_names)
    #print(f"image list:{unique_image_list}")

    list_sort(unique_image_list)

    print("test finish")
