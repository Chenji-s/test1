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




import math
def manual_linear_regression(x, y):
    # 数据点的数量
    n = len(x)
    
    # 计算所有和
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)
    
    # 计算斜率 m
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    
    # 计算截距 b
    b = (sum_y - m * sum_x) / n
    
    return m, b

def get_angle(coords, image_center=50):
    # 提取列（column）和行（row）的坐标
    cols = coords[:, 1]  # x坐标，保持不变
    rows = coords[:, 0]  # y坐标，但需要反转
    
    # 对行数进行变换，使得Y轴从下到上增加
    transformed_rows = -rows
    
    # 手动进行线性回归计算斜率和截距
    slope, intercept = manual_linear_regression(cols, transformed_rows)
    
    # 计算最佳拟合线的角度（弧度）
    angle = np.arctan2(slope, 1)  # 使用 slope 而不是 -slope，因为我们已经进行了行数的反转
    
    # 将角度转换为 0 到 2π 之间的值
    if angle < 0:
        angle += 2 * math.pi
    
    return slope

