import cv2
import os

os_name = os.name
if os_name == "posix": # linux
	print("python running on linux")
else: # nt: windows
	print("python running on windows")

if os_name == "posix":
	image_bgr = cv2.imread("../../test_data/lena.png")
else:
	image_bgr = cv2.imread("E:/GitCode/Python_Test/test_data/lena.png")

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow("bgr image", image_bgr)
cv2.imshow("gray image", image_gray)
cv2.waitKey(0);
cv2.destroyAllWindows()

if os_name == "posix":
	cv2.imwrite("../../test_data/gray_image.png", image_gray)
else:
	cv2.imwrite("E:/GitCode/Python_Test/test_data/gray_image.png", image_gray)
