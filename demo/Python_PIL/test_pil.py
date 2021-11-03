from PIL import Image, ImageFilter

# Blog: https://blog.csdn.net/fengbingchun/article/details/121116940

img = Image.open("../../test_data/lena.png") # 加载图像
width, height = img.size # 获得图像宽、高
print("src image size: %dx%d" % (width, height))

img2 = img.resize((128, 64))
print("dst image size: %dx%d" % (img2.size[0], img2.size[1]))
img2.save("../../test_data/resize.jpg", "jpeg") # 将缩放后的图像保存成jpeg格式

img3 = img.filter(ImageFilter.BLUR) # 图像模糊
img3.save("../../test_data/blur.png", "png") # 将模糊后的图像保存成png格式

gray = img.convert("L") # 图像转换: 转为灰度图
gray.save("../../test_data/gray.bmp", "bmp") # 将灰度图保存成bmp格式

quantize = gray.quantize(colors=16, kmeans=5) # 图像量化
quantize.save("../../test_data/quantize.png", "png")

crop = img.crop((64, 64, 248, 248)) # 图像剪切
crop.save("../../test_data/crop.png", "png")

pixel = img.getpixel((128, 64)) # 获取像素值
print("pixel value:", pixel)

rotate = img.rotate(90) # 图像旋转
rotate.save("../../test_data/rotate.png", "png")
rotate.show() # 显示图像
print("color mode:", rotate.mode) # get color mode: RGB
print("image format:", img.format) # get image format: PNG

print("test finish")
