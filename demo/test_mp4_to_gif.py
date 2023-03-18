import imageio
import cv2
import argparse

# Blog: https://blog.csdn.net/fengbingchun/article/details/129641133

def parse_args():
    parser = argparse.ArgumentParser(description="mp4 video file convert to animated gif")

    parser.add_argument("--mp4", required=True, help="mp4 video file")
    parser.add_argument("--gif", required=True, help="gif file to save")
    parser.add_argument("--fps", default=25, help="frames per second")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    cap = cv2.VideoCapture(args.mp4)
    images = []

    while True:
        ret, frame = cap.read()
        if ret == False or frame is None:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        images.append(rgb)

    if images:
        imageio.mimsave(args.gif, images, fps=args.fps)
        print("finish the test")
    else:
        print("Error: empty images")
