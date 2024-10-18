# Define all functions in this module.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def read_image(path, show=False):
    # 读取 PNG 图像并将其转换为 NumPy 数组
    img = mpimg.imread(path)
    
    if show:
        # 显示彩色图像
        plt.imshow(img)
        plt.title('RGB Image')
        plt.axis('off')
        plt.show()

        # 分别显示三个颜色通道：红色、绿色和蓝色
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        axs[0].imshow(img[:, :, 0], cmap='Reds')
        axs[0].set_title('Red Channel')
        axs[0].axis('off')

        axs[1].imshow(img[:, :, 1], cmap='Greens')
        axs[1].set_title('Green Channel')
        axs[1].axis('off')

        axs[2].imshow(img[:, :, 2], cmap='Blues')
        axs[2].set_title('Blue Channel')
        axs[2].axis('off')

        plt.show()

    return img





def get_clock_hands(clock_RGB):
    # 初始化两个列表分别保存时针和分针的坐标
    hour_hand_pixels = []
    minute_hand_pixels = []
    
    # 定义红色和绿色的颜色阈值范围
    red_threshold = [0.7, 0.2, 0.3]  # 红色像素
    green_threshold = [0.3, 0.7, 0.1]  # 绿色像素

    # 遍历图像中的每个像素
    for i in range(clock_RGB.shape[0]):  # 遍历行
        for j in range(clock_RGB.shape[1]):  # 遍历列
            pixel = clock_RGB[i, j]
            
            # 如果是红色像素（时针）
            if pixel[0] > red_threshold[0] and pixel[1] < red_threshold[1] and pixel[2] < red_threshold[2]:
                hour_hand_pixels.append([i, j])
            
            # 如果是绿色像素（分针）
            if pixel[1] > green_threshold[1] and pixel[0] < green_threshold[0] and pixel[2] < green_threshold[2]:
                minute_hand_pixels.append([i, j])

    # 将列表转换为 NumPy 数组并返回
    return np.array(hour_hand_pixels), np.array(minute_hand_pixels)



from scipy import stats
import math
def get_angle(coords):
    # 提取行（row）和列（column）的坐标
    rows = coords[:, 0]
    cols = coords[:, 1]
    
    # 进行线性回归，找出最佳拟合线的斜率和截距
    slope, intercept, _, _, _ = stats.linregress(cols, rows)
    
    # 计算最佳拟合线的角度（弧度）
    angle = np.arctan2(-slope, 1)  # 使用 -slope 因为 y 是行数，x 是列数，方向相反
    
    # 将角度转换为 0 到 2π 之间的值
    if angle < 0:
        angle += 2 * math.pi
    
    return angle


