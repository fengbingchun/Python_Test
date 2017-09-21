# 导入matplotlib的所有内容
from pylab import *

# 创建一个8*6点的图，并设置分辨率为80
figure(figsize=(8, 6), dpi=80)

# 创建一个新的2*2的子图,接下来的图样绘制在其中的第1块
subplot(2, 2, 1)

# numpy可以用np这个名字来使用
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为1(像素)的线条
plot(X, C, color="blue", linewidth=2.0, linestyle="-", label="cosine")
# 绘制正弦曲线，使用绿色的、连续的、宽度为2的线条
plot(X, S, color="red", linewidth=2.0, linestyle="-", label="sine")

# 设置横轴的上下限
xlim(-4.0, 4.0)

# 设置横轴记号
xticks(np.linspace(-4, 4, 11, endpoint=True))

# 设置纵轴的上下限
ylim(-2.0, 2.0)

# 设置纵轴记号
yticks(np.linspace(-2.0, 2.0, 9, endpoint=True))

# 等高线图
subplot(2, 2, 2)
def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)

# 饼状图
subplot(2, 2, 3)
n = 20
Z = np.random.uniform(0, 1, n)
pie(Z)

# 条形图
subplot(2, 2, 4)
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

ylim(-1.25,+1.25)

# 以分辨率72来保存图像
savefig("./../../test_matplotlib_1.png", dpi=72)

# 在屏幕上显示
show()