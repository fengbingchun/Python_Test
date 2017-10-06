import cv2

image_bgr = cv2.imread("E:/GitCode/Python_Test/test_data/lena.png")
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow("bgr image", image_bgr)
cv2.imshow("gray image", image_gray)
cv2.waitKey(0);
cv2.destroyAllWindows()
cv2.imwrite("E:/GitCode/Python_Test/test_data/gray_image.png", image_gray)