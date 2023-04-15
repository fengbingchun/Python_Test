import os
import json

# Blog: https://blog.csdn.net/fengbingchun/article/details/130175469

def get_dir_list(path):
    dir_list = []
    for x in os.listdir(path):
        if x.endswith(".txt"):
            dir_list.append(path+"/"+x)

    return dir_list

def vec_to_matrix(els):
    matrix = [
        [
            els[0][0],
            els[0][1],
            els[0][2],
            els[0][3]
        ],
        [
            els[1][0],
            els[1][1],
            els[1][2],
            els[1][3]
        ],
        [
            els[2][0],
            els[2][1],
            els[2][2],
            els[2][3],
        ],
        [
            0.0,
            0.0,
            0.0,
            1.0
        ]
    ]

    return matrix

def get_image_name(txt_name, img_suffix_name):
    pos = txt_name.rfind("/")
    name = txt_name[pos+1:]
    name = name.replace("txt", img_suffix_name)
    
    return "images/" + name

def write_to_json(dir_list, out_file, img_suffix_name):
    out = {
        "frames": [],
    }

    for x in dir_list:
        with open(os.path.join(x), "r") as f:
            els = [] # 6*4
            for line in f:
                if line[0] == "#":
                    continue

                tmp = []
                for v in line.split(" "):
                    tmp.append(v.replace("\n", "")) # remove line breaks(\n) at the end of the line
                ret = [float(ele) for ele in tmp] # str to float
                els.append(ret)

            if len(els) != 6:
                print(f"Error: the number of rows that are not supported:{len(els)}")
                raise

            # camera intrinsics
            fl_x = els[0][0]
            fl_y = els[1][1]
            cx = els[0][2]
            cy = els[1][2]

            # camera extrinsics: R t
            transform_matrix = vec_to_matrix(els[3:6])

            image_name = get_image_name(x, img_suffix_name)

            frame = {"file_path":image_name,"fl_x":fl_x,"fl_y":fl_y,"cx":cx,"cy":cy,"transform_matrix":transform_matrix}
            out["frames"].append(frame)

    with open(out_file, "w") as f:
        json.dump(out, f, indent=2)

if __name__ == "__main__":
    dir_list = get_dir_list("test_data/txt")
    #print(f"dir_list:\n\t{dir_list}")

    write_to_json(dir_list, "test_data/txt/transforms.json", "png")
    print("test finish")
