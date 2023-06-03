import os
import json
import cv2
import sys
import math
import numpy as np
from inspect import currentframe, getframeinfo
from pyquaternion import Quaternion

def get_txt_list(path, suffix_name):
    txt_list = []
    for x in os.listdir(path):
        if x.endswith(suffix_name):
            txt_list.append(path+"/"+x)

    return txt_list

def get_image_size(txt_list, image_suffix_name, txt_suffix_name):
    name = txt_list[0].replace(txt_suffix_name, image_suffix_name)
    #print(f"name: {name}, txt_list[0]: {txt_list[0]}")
    img = cv2.imread(name)
    h, w, _ = img.shape
    
    return w, h

def parse_camera_parameter_txt(name):
    with open(os.path.join(name), "r") as f:
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

def generate_cameras_txt(txt_list, width, height, colmap_text_path):
    f = open(colmap_text_path+"cameras.txt", "w")
    #f.write("# Camera list with one line of data per camera:\r")
    #f.write("#   CAMERA_ID, MODEL, WIDTH, HEIGHT, PARAMS[]\r")
    #f.write("# Number of cameras: %d\r" % len(txt_list))

    camera_id = 1
    camera_model = "PINHOLE"

    for x in txt_list:
        elements = parse_camera_parameter_txt(x)
        #print(f"{x} elements:\n{elements}")

        string = str(camera_id) + " " + camera_model + " " + str(width) + " " + str(height) # CAMERA_ID, MODEL, WIDTH, HEIGHT
        string = string + " " + str(elements[0][0]) + " " + str(elements[1][1]) + " " + str(elements[0][2]) + " " + str(elements[1][2]) + "\r" # PARAMS[] 
        f.write(string)

        camera_id = camera_id + 1

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

def get_image_name(txt_name, txt_suffix_name, image_suffix_name):
    pos = txt_name.rfind("/")
    name = txt_name[pos+1:]
    image_name = name.replace(txt_suffix_name, image_suffix_name)
    #print(f"image name: {image_name}, txt_name: {txt_name}")
    
    return image_name

def generate_images_txt(txt_list, txt_suffix_name, image_suffix_name, colmap_text_path):
    f = open(colmap_text_path+"images.txt", "w")
    #f.write("# Image list with two lines of data per image:\r")
    #f.write("#   IMAGE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID, NAME\r")
    #f.write("#   POINTS2D[] as (X, Y, POINT3D_ID)\r")
    #f.write("# Number of images: %d, mean observations per image:\r" % len(txt_list))

    image_id = 1
    camera_id = image_id

    for x in txt_list:
        elements = parse_camera_parameter_txt(x)
        quaternion, m = calculate_quaternion(elements)
        #print(f"quaternion:{quaternion}")
        
        T = np.array([[elements[3][3]], [elements[4][3]], [elements[5][3]]])
        T = np.matmul((-m), T) # 3*1

        image_name = get_image_name(x, txt_suffix_name, image_suffix_name)

        string = str(image_id) + " " + str(quaternion[0]) + " " + str(quaternion[1]) + " " + str(quaternion[2]) + " " + str(quaternion[3]) + " " # IMAGE_ID, QW, QX, QY, QZ
        string = string + str(T[0][0]) + " " + str(T[1][0]) + " " + str(T[2][0]) + " " + str(image_id) + " " + str(image_name) + "\r\n" # TX, TY, TZ, CAMERA_ID, NAME
        f.write(string)

        image_id = image_id + 1
        camera_id = image_id

    f.close()

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def sharpness(imagePath):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    return fm

def qvec2rotmat(qvec):
    return np.array([
        [
            1 - 2 * qvec[2]**2 - 2 * qvec[3]**2,
            2 * qvec[1] * qvec[2] - 2 * qvec[0] * qvec[3],
            2 * qvec[3] * qvec[1] + 2 * qvec[0] * qvec[2]
        ], [
            2 * qvec[1] * qvec[2] + 2 * qvec[0] * qvec[3],
            1 - 2 * qvec[1]**2 - 2 * qvec[3]**2,
            2 * qvec[2] * qvec[3] - 2 * qvec[0] * qvec[1]
        ], [
            2 * qvec[3] * qvec[1] - 2 * qvec[0] * qvec[2],
            2 * qvec[2] * qvec[3] + 2 * qvec[0] * qvec[1],
            1 - 2 * qvec[1]**2 - 2 * qvec[2]**2
        ]
    ])

def rotmat(a, b):
    a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
    v = np.cross(a, b)
    c = np.dot(a, b)
    # handle exception for the opposite direction input
    if c < -1 + 1e-10:
        return rotmat(a + np.random.uniform(-1e-2, 1e-2, 3), b)
    s = np.linalg.norm(v)
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2 + 1e-10))

def closest_point_2_lines(oa, da, ob, db): # returns point closest to both rays of form o+t*d, and a weight factor that goes to 0 if the lines are parallel
    da = da / np.linalg.norm(da)
    db = db / np.linalg.norm(db)
    c = np.cross(da, db)
    denom = np.linalg.norm(c)**2
    t = ob - oa
    ta = np.linalg.det([t, db, c]) / (denom + 1e-10)
    tb = np.linalg.det([t, da, c]) / (denom + 1e-10)
    if ta > 0:
        ta = 0
    if tb > 0:
        tb = 0
    return (oa+ta*da+ob+tb*db) * 0.5, denom

def write_to_json(txt_path, txt_list, image_suffix_name, txt_suffix_name, colmap_text_path, json_name):
    width, height = get_image_size(txt_list, image_suffix_name, txt_suffix_name)
    #print(f"width: {width}, height: {height}")

    os.makedirs(colmap_text_path, exist_ok=True)
    generate_cameras_txt(txt_list, width, height, colmap_text_path)
    generate_images_txt(txt_list, txt_suffix_name, image_suffix_name, colmap_text_path)
    
    AABB_SCALE = 2
    camera_intrinsics = {}

    with open(os.path.join(colmap_text_path,"cameras.txt"), "r") as f:
        angle_x = math.pi / 2
        for line in f:
            # 1 SIMPLE_RADIAL 2048 1536 1580.46 1024 768 0.0045691
            # 1 OPENCV 3840 2160 3178.27 3182.09 1920 1080 0.159668 -0.231286 -0.00123982 0.00272224
            # 1 RADIAL 1920 1080 1665.1 960 540 0.0672856 -0.0761443
            # if line[0] == "#":
            #     continue
            els = line.split(" ")
            w = float(els[2])
            h = float(els[3])
            fl_x = float(els[4])
            fl_y = float(els[4])
            k1 = 0
            k2 = 0
            k3 = 0
            k4 = 0
            p1 = 0
            p2 = 0
            cx = w / 2
            cy = h / 2
            is_fisheye = False
            if els[1] == "SIMPLE_PINHOLE":
                cx = float(els[5])
                cy = float(els[6])
            elif els[1] == "PINHOLE":
                fl_y = float(els[5])
                cx = float(els[6])
                cy = float(els[7])
            elif els[1] == "SIMPLE_RADIAL":
                cx = float(els[5])
                cy = float(els[6])
                k1 = float(els[7])
            elif els[1] == "RADIAL":
                cx = float(els[5])
                cy = float(els[6])
                k1 = float(els[7])
                k2 = float(els[8])
            elif els[1] == "OPENCV":
                fl_y = float(els[5])
                cx = float(els[6])
                cy = float(els[7])
                k1 = float(els[8])
                k2 = float(els[9])
                p1 = float(els[10])
                p2 = float(els[11])
            elif els[1] == "SIMPLE_RADIAL_FISHEYE":
                is_fisheye = True
                cx = float(els[5])
                cy = float(els[6])
                k1 = float(els[7])
            elif els[1] == "RADIAL_FISHEYE":
                is_fisheye = True
                cx = float(els[5])
                cy = float(els[6])
                k1 = float(els[7])
                k2 = float(els[8])
            elif els[1] == "OPENCV_FISHEYE":
                is_fisheye = True
                fl_y = float(els[5])
                cx = float(els[6])
                cy = float(els[7])
                k1 = float(els[8])
                k2 = float(els[9])
                k3 = float(els[10])
                k4 = float(els[11])
            else:
                print("Unknown camera model ", els[1])
            # fl = 0.5 * w / tan(0.5 * angle_x);
            angle_x = math.atan(w / (fl_x * 2)) * 2
            angle_y = math.atan(h / (fl_y * 2)) * 2
            fovx = angle_x * 180 / math.pi
            fovy = angle_y * 180 / math.pi

            camera_intrinsics[els[0]] = [w, h, cx, cy, fl_x, fl_y] 

    print(f"camera:\n\tres={w,h}\n\tcenter={cx,cy}\n\tfocal={fl_x,fl_y}\n\tfov={fovx,fovy}\n\tk={k1,k2} p={p1,p2} ")
    #print(f"camera_intrinsics:\n{camera_intrinsics}")

    with open(os.path.join(colmap_text_path,"images.txt"), "r") as f:
        i = 0
        bottom = np.array([0.0, 0.0, 0.0, 1.0]).reshape([1, 4])
        out = {
            "camera_angle_x": angle_x,
            "camera_angle_y": angle_y,
            "fl_x": fl_x,
            "fl_y": fl_y,
            "k1": k1,
            "k2": k2,
            "k3": k3,
            "k4": k4,
            "p1": p1,
            "p2": p2,
            "is_fisheye": is_fisheye,
            "cx": cx,
            "cy": cy,
            "w": w,
            "h": h,
            "aabb_scale": AABB_SCALE,
            "frames": [],
        }

        up = np.zeros(3)
        for line in f:
            line = line.strip()
            # if line[0] == "#":
            #     continue
            i = i + 1
            # if i < SKIP_EARLY*2:
            #     continue
            if  i % 2 == 1:
                elems=line.split(" ") # 1-4 is quat, 5-7 is trans, 9ff is filename (9, if filename contains no spaces)
                #name = str(PurePosixPath(Path(IMAGE_FOLDER, elems[9])))
                # why is this requireing a relitive path while using ^
                image_rel = os.path.relpath(txt_path)
                name = str(f"./{image_rel}/{'_'.join(elems[9:])}")
                #print(f"name: {name}")
                b = sharpness(name)
                print(name, "sharpness=",b)
                image_id = int(elems[0])
                qvec = np.array(tuple(map(float, elems[1:5])))
                tvec = np.array(tuple(map(float, elems[5:8])))
                R = qvec2rotmat(-qvec)
                t = tvec.reshape([3,1])
                m = np.concatenate([np.concatenate([R, t], 1), bottom], 0)
                c2w = np.linalg.inv(m)
                if True: #not args.keep_colmap_coords:
                    #print(f"LINE: {getframeinfo(currentframe()).lineno}")
                    c2w[0:3,2] *= -1 # flip the y and z axis
                    c2w[0:3,1] *= -1
                    c2w = c2w[[1,0,2,3],:]
                    c2w[2,:] *= -1 # flip whole world upside down

                    up += c2w[0:3,1]

                #print(f"camera id: {elems[8]}")
                #frame = {"file_path":name,"sharpness":b,"transform_matrix": c2w}
                params = camera_intrinsics[elems[8]] # w, h, cx, cy, fl_x, fl_y
                frame = {"file_path":name,"sharpness":b,"w":params[0],"h":params[1],"cx":params[2],"cy":params[3],"fl_x":params[4],"fl_y":params[5],"transform_matrix": c2w}
                out["frames"].append(frame)
    nframes = len(out["frames"])

    if False: #args.keep_colmap_coords:
        print(f"LINE: {getframeinfo(currentframe()).lineno}")
        flip_mat = np.array([
            [1, 0, 0, 0],
            [0, -1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ])

        for f in out["frames"]:
            f["transform_matrix"] = np.matmul(f["transform_matrix"], flip_mat) # flip cameras (it just works)
    else:
        # don't keep colmap coords - reorient the scene to be easier to work with
        #print(f"LINE: {getframeinfo(currentframe()).lineno}")

        up = up / np.linalg.norm(up)
        print("up vector was", up)
        R = rotmat(up,[0,0,1]) # rotate up vector to [0,0,1]
        R = np.pad(R,[0,1])
        R[-1, -1] = 1

        for f in out["frames"]:
            f["transform_matrix"] = np.matmul(R, f["transform_matrix"]) # rotate up to be the z axis

        # find a central point they are all looking at
        print("computing center of attention...")
        totw = 0.0
        totp = np.array([0.0, 0.0, 0.0])
        for f in out["frames"]:
            mf = f["transform_matrix"][0:3,:]
            for g in out["frames"]:
                mg = g["transform_matrix"][0:3,:]
                p, w = closest_point_2_lines(mf[:,3], mf[:,2], mg[:,3], mg[:,2])
                if w > 0.00001:
                    totp += p*w
                    totw += w
        if totw > 0.0:
            totp /= totw
        print(totp) # the cameras are looking at totp
        for f in out["frames"]:
            f["transform_matrix"][0:3,3] -= totp

        avglen = 0.
        for f in out["frames"]:
            avglen += np.linalg.norm(f["transform_matrix"][0:3,3])
        avglen /= nframes
        print("avg camera distance from origin", avglen)
        for f in out["frames"]:
            f["transform_matrix"][0:3,3] *= 4.0 / avglen # scale to "nerf sized"

    for f in out["frames"]:
        f["transform_matrix"] = f["transform_matrix"].tolist()
    print(nframes,"frames")
    print(f"writing transforms.json")
    with open(txt_path+"/transforms.json", "w") as outfile:
        json.dump(out, outfile, indent=2)

if __name__ == "__main__":
    txt_path = "test_data/lego" # = image path
    txt_suffix_name = ".txt"
    txt_list = get_txt_list(txt_path, txt_suffix_name)
    #print(f"txt_list:\n{txt_list}")

    image_suffix_name = ".png"
    json_name = "test_data/lego/transforms.json"
    colmap_text_path = "test_data/lego/colmap_text/"
    write_to_json(txt_path, txt_list, image_suffix_name, txt_suffix_name, colmap_text_path, json_name)

    print("test finish")
