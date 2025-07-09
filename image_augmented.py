from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np
import random
import os

def adjust_brightness(image, factor):
    """
    调整图像亮度

    :param image: PIL.Image对象，输入图像
    :param factor: float，亮度调整因子，大于1增加亮度，小于1降低亮度
    :return: PIL.Image对象，调整亮度后的图像
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    """
    调整图像对比度

    :param image: PIL.Image对象，输入图像
    :param factor: float，对比度调整因子，大于1增加对比度，小于1降低对比度
    :return: PIL.Image对象，调整对比度后的图像
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def adjust_saturation(image, factor):
    """
    调整图像饱和度

    :param image: PIL.Image对象，输入图像
    :param factor: float，饱和度调整因子，大于1增加饱和度，小于1降低饱和度
    :return: PIL.Image对象，调整饱和度后的图像
    """
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)

def adjust_hue(image, factor):
    """
    调整图像色相

    :param image: PIL.Image对象，输入图像
    :param factor: int，色相调整值，取值范围为-180到180
    :return: PIL.Image对象，调整色相后的图像
    """
    hsv_image = image.convert('HSV')
    hsv = np.array(hsv_image)
    hsv[..., 0] = (hsv[..., 0] + factor) % 360
    hsv_image = Image.fromarray(hsv, 'HSV')
    return hsv_image.convert('RGB')

def add_noise(image, mean=0, std=10):
    """
    给图像添加高斯噪声

    :param image: PIL.Image对象，输入图像
    :param mean: float，噪声均值
    :param std: float，噪声标准差
    :return: PIL.Image对象，添加噪声后的图像
    """
    img_array = np.array(image)
    noise = np.random.normal(mean, std, img_array.shape)
    noisy_image = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)

def apply_blur(image, radius=2):
    """
    对图像应用高斯模糊

    :param image: PIL.Image对象，输入图像
    :param radius: int，模糊半径
    :return: PIL.Image对象，模糊后的图像
    """
    return image.filter(ImageFilter.GaussianBlur(radius))

def apply_sharpen(image, factor=2):
    """
    对图像应用锐化

    :param image: PIL.Image对象，输入图像
    :param factor: float，锐化因子，大于1增加锐化效果，小于1降低锐化效果
    :return: PIL.Image对象，锐化后的图像
    """
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)

def rotate_image(image, angle):
    """
    旋转图像

    :param image: PIL.Image对象，输入图像
    :param angle: int，旋转角度，取值范围为-360到360
    :return: PIL.Image对象，旋转后的图像
    """
    return image.rotate(angle, resample=Image.BICUBIC, expand=True)

def flip_image(image, direction):
    """
    翻转图像

    :param image: PIL.Image对象，输入图像
    :param direction: str，翻转方向，取值为'horizontal'或'vertical'
    :return: PIL.Image对象，翻转后的图像
    """
    if direction == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == 'vertical':
        return image.transpose(Image.FLIP_TOP_BOTTOM)

def translate_image(image, x_offset, y_offset):
    """
    平移图像

    :param image: PIL.Image对象，输入图像
    :param x_offset: int，水平平移量
    :param y_offset: int，垂直平移量
    :return: PIL.Image对象，平移后的图像
    """
    return image.transform(
        image.size,
        Image.AFFINE,
        (1, 0, x_offset, 0, 1, y_offset),
        resample=Image.BICUBIC
    )

def scale_image(image, factor):
    """
    缩放图像

    :param image: PIL.Image对象，输入图像
    :param factor: float，缩放因子，大于1放大图像，小于1缩小图像
    :return: PIL.Image对象，缩放后的图像
    """
    new_size = (int(image.width * factor), int(image.height * factor))
    return image.resize(new_size, resample=Image.BICUBIC)

def data_augmentation(image_path, num_augmented_images=1000):
    """
    对输入图像进行数据增强

    :param image_path: str，输入图像的路径
    :param num_augmented_images: int，生成的增强图像数量
    :return: list，包含增强图像的列表
    """
    original_image = Image.open(image_path)
    augmented_images = []

    for _ in range(num_augmented_images):
        # 随机选择增强操作
        operations = [
            ('brightness', random.uniform(0.5, 1.5)),
            ('contrast', random.uniform(0.5, 1.5)),
            ('saturation', random.uniform(0.5, 1.5)),
            ('hue', random.randint(-30, 30)),
            ('noise', random.randint(5, 20)),
            ('blur', random.randint(1, 3)),
            ('sharpen', random.uniform(0.5, 2)),
            ('rotate', random.randint(-30, 30)),
            ('flip', random.choice(['horizontal', 'vertical'])),
            ('translate', (random.randint(-45, 45), random.randint(-45, 45))),
            ('scale', random.uniform(0.8, 1.2))
        ]
        
        # 随机选择 1 到 5 种操作
        selected_operations = random.sample(operations, random.randint(6, 8))

        # 应用增强操作
        augmented_image = original_image.copy()
        for operation, value in operations:
            if operation == 'brightness':
                augmented_image = adjust_brightness(augmented_image, value)
            elif operation == 'contrast':
                augmented_image = adjust_contrast(augmented_image, value)
            elif operation == 'saturation':
                augmented_image = adjust_saturation(augmented_image, value)
            elif operation == 'hue':
                augmented_image = adjust_hue(augmented_image, value)
            elif operation == 'noise':
                augmented_image = add_noise(augmented_image, std=value)
            elif operation == 'blur':
                augmented_image = apply_blur(augmented_image, radius=value)
            elif operation == 'sharpen':
                augmented_image = apply_sharpen(augmented_image, factor=value)
            elif operation == 'rotate':
                augmented_image = rotate_image(augmented_image, value)
            elif operation == 'flip':
                augmented_image = flip_image(augmented_image, value)
            elif operation == 'translate':
                augmented_image = translate_image(augmented_image, *value)
            elif operation == 'scale':
                augmented_image = scale_image(augmented_image, value)

        augmented_images.append(augmented_image)

    return augmented_images

def center_crop(image, crop_size=(800, 800)):
    """
    中心裁剪图像

    :param image: PIL.Image对象，输入图像
    :param crop_size: tuple，裁剪的目标尺寸 (宽, 高)
    :return: PIL.Image对象，裁剪后的图像
    """
    width, height = image.size
    crop_width, crop_height = crop_size
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return image.crop((left, top, right, bottom))

def process_folder(input_folder, output_folder, num_augmented_images=10, crop_size=(800, 800)):
    """
    批量处理文件夹中的所有图像文件，进行数据增强和中心裁剪。

    :param input_folder: str，输入文件夹路径
    :param output_folder: str，输出文件夹路径
    :param num_augmented_images: int，每张图像生成的增强图像数量
    :param crop_size: tuple，裁剪的目标尺寸 (宽, 高)
    """
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # 检查是否为图像文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            print(f"正在处理图像: {filename}")
            try:
                # 数据增强
                augmented_images = data_augmentation(input_path, num_augmented_images=num_augmented_images)

                # 为每张输入图像创建单独的输出子文件夹
                original_filename = os.path.splitext(filename)[0]
                file_output_folder = os.path.join(output_folder, original_filename)
                os.makedirs(file_output_folder, exist_ok=True)

                # 保存增强后的图像
                for i, image in enumerate(augmented_images):
                    # 中心裁剪为指定大小
                    cropped_image = center_crop(image, crop_size=crop_size)
                    # 生成文件名：原文件名 + 4 位递增数字
                    output_filename = f"{original_filename}_{i:04d}.jpg"
                    # 保存裁剪后的图像到对应的子文件夹
                    cropped_image.save(os.path.join(file_output_folder, output_filename))

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

    print(f"所有图像已处理完成，结果保存在文件夹: {output_folder}")


# 示例用法
input_folder = 'E:/GitHub/AgNPs/0326/00'  # 输入文件夹路径
output_folder = 'E:/GitHub/AgNPs/0326/04'  # 输出文件夹路径
process_folder(input_folder, output_folder, num_augmented_images=100, crop_size=(800, 800))
 