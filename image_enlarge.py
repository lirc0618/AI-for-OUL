import os
from PIL import Image
from collections import Counter

def detect_background_color(image, border_ratio=0.1):
    """
    智能检测背景颜色算法
    :param image: 输入图像对象
    :param border_ratio: 边缘检测比例（默认检测10%的边缘区域）
    :return: 背景颜色元组 (R, G, B)
    """
    width, height = image.size
    border_width = int(min(width, height) * border_ratio)
    
    # 采集边缘像素样本
    samples = []
    for x in range(border_width):
        samples.append(image.getpixel((x, border_width)))          # 左边缘
        samples.append(image.getpixel((x, height-border_width-1))) # 右边缘
    for y in range(border_width, height-border_width):
        samples.append(image.getpixel((border_width, y)))          # 上边缘
        samples.append(image.getpixel((width-border_width-1, y)))  # 下边缘
    
    # 统计最常见的颜色
    color_counter = Counter(samples)
    return color_counter.most_common(1)[0][0]

def expand_background(image_path, output_path, target_size=(2160, 2160)):
    """
    图像背景扩展主函数
    :param image_path: 输入图像路径
    :param output_path: 输出图像路径
    :param target_size: 目标尺寸
    """
    # 打开原始图像
    img = Image.open(image_path)
    original_size = img.size
    
    # 检测背景颜色
    bg_color = detect_background_color(img)
    
    # 创建新画布
    expanded_img = Image.new("RGB", target_size, bg_color)
    
    # 计算居中位置
    paste_position = (
        (target_size[0] - original_size[0]) // 2,
        (target_size[1] - original_size[1]) // 2
    )
    
    # 粘贴原始图像
    expanded_img.paste(img, paste_position)
    
    # 保存结果
    expanded_img.save(output_path)
    print(f"图像已成功扩展至 {target_size[0]}x{target_size[1]}: {output_path}")

def batch_process_images(input_folder, output_folder, target_size=(2160, 2160)):
    """
    批量处理文件夹中的所有图像
    :param input_folder: 输入文件夹路径
    :param output_folder: 输出文件夹路径
    :param target_size: 目标尺寸
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # 检查是否为图像文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                expand_background(input_path, output_path, target_size)
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

if __name__ == "__main__":
    # 输入和输出文件夹路径
    input_folder = "E:/GitHub/AgNPs/0326/03-02"  # 替换为你的输入文件夹路径
    output_folder = "E:/GitHub/AgNPs/0326/03-00"  # 替换为你的输出文件夹路径
    
    # 批量处理图像
    batch_process_images(input_folder, output_folder, target_size=(2160, 2160))