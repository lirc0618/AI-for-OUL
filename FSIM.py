import os
import cv2
import numpy as np
import pandas as pd
from scipy.fftpack import fft2, fftshift
from scipy.ndimage import gaussian_filter

def calculate_fsim(img1_path, img2_path):
    """
    计算两幅图像的FSIM值
    :param img1_path: 图像1路径
    :param img2_path: 图像2路径
    :return: FSIM值（范围[0,1]，越接近1越相似）
    """
    # 读取图像并转换为灰度图
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    
    if img1 is None or img2 is None:
        raise ValueError("图像路径无效或无法读取")
    
    # 确保两幅图像尺寸一致
    if img1.shape != img2.shape:
        raise ValueError("图像尺寸不一致")

    # 计算相位一致性（Phase Congruency）
    def phase_congruency(img):
        # 高斯滤波平滑
        img_smooth = gaussian_filter(img, sigma=1)
        # 计算梯度
        gx = cv2.Scharr(img_smooth, cv2.CV_64F, 1, 0)
        gy = cv2.Scharr(img_smooth, cv2.CV_64F, 0, 1)
        magnitude = np.sqrt(gx**2 + gy**2)
        orientation = np.arctan2(gy, gx)
        
        # 傅里叶变换计算相位信息
        fft_img = fft2(img_smooth)
        fft_shift_img = fftshift(fft_img)
        phase = np.angle(fft_shift_img)
        
        # 相位一致性计算（简化版）
        pc = np.abs(np.cos(phase) + np.sin(phase))  # 实际需结合频带能量，此处为简化
        return pc, magnitude

    # 计算两幅图像的相位一致性和梯度幅度
    pc1, mag1 = phase_congruency(img1)
    pc2, mag2 = phase_congruency(img2)

    # 计算梯度幅度相似性（SIM_G）
    sim_g = (2 * mag1 * mag2 + 1e-6) / (mag1**2 + mag2**2 + 1e-6)

    # 计算相位一致性权重（phi）
    phi = (2 * pc1 * pc2 + 1e-6) / (pc1**2 + pc2**2 + 1e-6)

    # 合并特征相似性
    numerator = phi * sim_g
    denominator = phi + 1e-6  # 避免除零
    fsim = np.sum(numerator) / np.sum(denominator)

    return fsim

def calculate_fsim_for_folder_as_matrix(folder_path, output_csv):
    """
    计算文件夹中任意两张图像的FSIM相似度，并保存为混淆矩阵形式的CSV文件
    :param folder_path: str，图像文件夹路径
    :param output_csv: str，输出CSV文件路径
    """
    # 获取文件夹中的所有图像文件
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    image_paths = [os.path.join(folder_path, f) for f in image_files]

    # 初始化混淆矩阵
    fsim_matrix = pd.DataFrame(index=image_files, columns=image_files)

    # 计算任意两张图像的FSIM
    for i in range(len(image_paths)):
        for j in range(len(image_paths)):
            img1_path = image_paths[i]
            img2_path = image_paths[j]
            try:
                fsim_value = calculate_fsim(img1_path, img2_path)
                fsim_matrix.iloc[i, j] = fsim_value
                #print(f"计算完成: {os.path.basename(img1_path)} vs {os.path.basename(img2_path)} -> FSIM: {fsim_value:.4f}")
            except Exception as e:
                #print(f"计算失败: {os.path.basename(img1_path)} vs {os.path.basename(img2_path)} -> 错误: {e}")
                fsim_matrix.iloc[i, j] = None

    # 保存混淆矩阵为CSV文件
    fsim_matrix.to_csv(output_csv, index=True)
    print(f"FSIM混淆矩阵已保存为: {output_csv}")

# 示例用法
if __name__ == "__main__":
    folder_path = "E:/GitHub/AgNPs/0326/00"  # 输入图像文件夹路径
    output_csv = "E:/GitHub/AgNPs/0326/00/fsim_confusion_matrix.csv"  # 输出CSV文件路径
    calculate_fsim_for_folder_as_matrix(folder_path, output_csv)