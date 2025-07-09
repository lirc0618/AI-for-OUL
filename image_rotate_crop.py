# 输入一张照片，实现每0.72°旋转一次，生成500张变体，中心裁剪；
# 输入2160*2160，输出800*800；
# 实现效果不佳
from PIL import Image
import os

def center_crop_image(image_path, output_folder, target_width, target_height, prefix):
    img = Image.open(image_path)
    width, height = img.size
    angle = 0.72

    # 中心裁剪
    left = (width - target_width) // 2
    top = (height - target_height) // 2
    right = (width + target_width) // 2
    bottom = (height + target_height) // 2

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, int(360 / angle) + 1):
        rotated_img = img.rotate(i * angle, resample=Image.BICUBIC, expand=False)

        cropped_img = rotated_img.crop((left, top, right, bottom))
        cropped_img.save(os.path.join(output_folder, f"{prefix}{'%03d' % i}.jpg"))


if __name__ == "__main__":
    input_folder = "E:/GitHub/AgNPs/0326/01-00"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp1"

    target_width = 800
    target_height = 800
    
    # 获取输入文件夹中所有文件的路径
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # 遍历所有文件
    for file in image_files:
        if file.lower().endswith('.jpg'):  # 确保处理的是图片文件
            image_path = os.path.join(input_folder, file)
            prefix = os.path.splitext(file)[0]  # 使用文件名作为前缀
            # 创建以原始照片名（不带后缀）命名的子文件夹
            output_subfolder = os.path.join(output_folder, prefix)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            # 调用函数处理图片
            center_crop_image(image_path, output_subfolder, target_width, target_height, prefix)