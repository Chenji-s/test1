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
    # 设定差异阈值，调整为更适合你的图像的值
    color_diff_threshold = 0.1  # 这是颜色通道差异的最小值
    # 定义红色和绿色的颜色阈值范围
    red_threshold = [0.7, 0.2, 0.3]  # 红色像素
    green_threshold = [0.3, 0.7, 0.1]  # 绿色像素

    # 遍历图像中的每个像素
    for i in range(clock_RGB.shape[0]):  # 遍历行
        for j in range(clock_RGB.shape[1]):  # 遍历列
            pixel = clock_RGB[i, j]
            
            red_diff = pixel[0] - max(pixel[1], pixel[2])
            green_diff = pixel[1] - max(pixel[0], pixel[2])
        
        # 如果红色通道差异较大，则认为是红色（时针）
            if red_diff > color_diff_threshold:
              hour_hand_pixels.append([i, j])
        
           # 如果绿色通道差异较大，则认为是绿色（分针）
            if green_diff > color_diff_threshold:
              minute_hand_pixels.append([i, j])

    # 将列表转换为 NumPy 数组并返回
    return np.array(hour_hand_pixels), np.array(minute_hand_pixels)




import math
import numpy as np
import math
import matplotlib.pyplot as plt

def manual_linear_regression(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - m * sum_x) / n
    return m, b


def get_angle(coords):
    # 提取坐标中的行和列，并将行坐标进行转换
    rows = 101 - coords[:, 0]  # 将行坐标转换为符合 xy 坐标系的格式
    cols = coords[:, 1]
# 如果列坐标几乎相等，表示垂直情况（针在12点或6点位置）
    if np.std(cols) < 1e-3:  # 标准差非常小，说明列坐标几乎不变
        if np.mean(rows) > 50:  # 针指向12点
            return 0  # 角度为0弧度（12点）
        else:  # 针指向6点
            return np.pi  # 角度为π弧度（6点）

    # 使用线性回归拟合行列关系 (cols, rows)，返回直线的斜率和截距
    slope, intercept = np.polyfit(cols, rows, 1)

    # 计算斜率的角度（反正切）
    angle = np.arctan(slope)

    angle_radians = np.arctan(slope)
    angle_degrees = np.degrees(angle_radians)
    angle=90-angle_degrees

# 判断大部分cols是否大于50
    if np.mean(cols) <= 50:  # 如果大部分数据在50以下
        angle += 180  # 加上180度（相当于加上π）

    # 确保最终的角度在 [0, 2π) 之间
    return angle* np.pi /180





def analog_to_digital(angle_hour, angle_minute):
    # 将时针角度转换为小时
    hour = (angle_hour / (2 * np.pi)) * 12
    hour = int(hour)  # 转换为整数小时
    if hour == 0:
        hour = 12  # 如果小时数是 0，设为 12

    # 将分针角度转换为分钟
    minute = (angle_minute / (2 * np.pi)) * 60
    minute = int(round(minute))  # 将分钟数四舍五入，并转换为整数

    # 格式化小时和分钟，确保小于 10 时添加前导零
    time_str = f"{hour:02d}:{minute:02d}"
    
    return time_str




def check_alignment(angle_hour, angle_minute):
    # 计算时针显示的分钟数（将时针的角度转换为分钟数）
    hour_in_minutes = (angle_hour / (2 * np.pi)) * 12
    hour_in_minutes=(hour_in_minutes*60) % 60
    
    # 计算分针显示的分钟数
    minute = (angle_minute / (2 * np.pi)) * 60
    
    # 计算对齐误差：分针与时针应显示的分钟数之间的差异
    misalignment = minute - hour_in_minutes
    
    # 确保误差在 [-30, 30] 的范围内
    if misalignment > 30:
        misalignment -= 60
    elif misalignment < -30:
        misalignment += 60
    
    return int(misalignment)

import os
from datetime import datetime

def validate_batch(folder_path, tolerance):
    # 获取当前时间并格式化
    current_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    
    # 获取所有时钟文件（假设文件名格式为 clock_X.png）
    clock_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    # 初始化计数
    total_clocks = len(clock_files)
    passing_clocks = 0
    clocks_to_adjust = []
    
    for clock_file in clock_files:
        # 读取每个时钟图片的路径
        clock_path = os.path.join(folder_path, clock_file)
        
        # 读取图片并提取时针和分针像素坐标
        clock_RGB = qc.read_image(clock_path)
        hour_pixels, minute_pixels = qc.get_clock_hands(clock_RGB)
        
        # 计算时针和分针的角度
        angle_hour = qc.get_angle(hour_pixels)
        angle_minute = qc.get_angle(minute_pixels)
        
        # 计算对齐误差
        misalignment = qc.check_alignment(angle_hour, angle_minute)
        
        # 检查误差是否在容差范围内
        if abs(misalignment) <= tolerance:
            passing_clocks += 1
        else:
            clocks_to_adjust.append((clock_file, misalignment))
    
    # 计算批次质量百分比
    batch_quality = (passing_clocks / total_clocks) * 100
    
    # 对需要调整的时钟按误差从大到小排序
    clocks_to_adjust.sort(key=lambda x: abs(x[1]), reverse=True)
    print(batch_quality)
    print(clocks_to_adjust)


import os
import numpy as np

def check_coupling(path_1, path_2):
    # 读取两张图片
    clock_RGB_1 = read_image(path_1)
    clock_RGB_2 = read_image(path_2)
    
    # 提取时针和分针像素数据
    hour_pixels_1, minute_pixels_1 = get_clock_hands(clock_RGB_1)
    hour_pixels_2, minute_pixels_2 = get_clock_hands(clock_RGB_2)
    
    # 计算每张图片的时针和分针角度
    angle_hour_1 = get_angle(hour_pixels_1)
    angle_minute_1 = get_angle(minute_pixels_1)
    angle_hour_2 = get_angle(hour_pixels_2)
    angle_minute_2 = get_angle(minute_pixels_2)
    
    # 计算两张图片之间的时针和分针的错位变化
    hour_change = (angle_hour_2 - angle_hour_1) / (2 * np.pi) * 12  # 计算小时数
    minute_change = (angle_minute_2 - angle_minute_1) / (2 * np.pi) * 60  # 计算分钟数
    
    # 理论上分针应该随着时针变化，计算理论的分针变化
    expected_minute_change = hour_change * 60
    
    # 检查分针的实际变化与理论变化的差异
    minute_misalignment = minute_change - expected_minute_change
    
    if abs(minute_misalignment) < 1e-3:
        return 'The hour and minute hand are coupled properly.'
    
    # 将差异转换为每小时增减的分钟和秒
    minute_per_hour = minute_misalignment / hour_change
    minutes = int(minute_per_hour)
    seconds = int((minute_per_hour - minutes) * 60)
    
    # 返回不同的耦合状态
    if minute_per_hour > 0:
        return f'The minute hand gains {abs(minutes)} minutes, {abs(seconds)} seconds per hour.'
    else:
        return f'The minute hand loses {abs(minutes)} minutes, {abs(seconds)} seconds per hour.'
