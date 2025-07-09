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

    image_path = "E:/GitHub/AgNPs/0326/01-03/A1.jpg"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp/A1"
    center_crop_image(image_path, output_folder, 800, 800, 'A1')

    image_path = "E:/GitHub/AgNPs/0326/01-03/A2.jpg"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp/A2"
    center_crop_image(image_path, output_folder, 800, 800, 'A2')

    image_path = "E:/GitHub/AgNPs/0326/01-03/A3.jpg"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp/A3"
    center_crop_image(image_path, output_folder, 800, 800, 'A3')

    image_path = "E:/GitHub/AgNPs/0326/01-03/A4.jpg"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp/A4"
    center_crop_image(image_path, output_folder, 800, 800, 'A4')

    image_path = "E:/GitHub/AgNPs/0326/01-03/A5.jpg"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp/A5"
    center_crop_image(image_path, output_folder, 800, 800, 'A5')

    image_path = "E:/GitHub/AgNPs/0326/01-03/A6.jpg"
    output_folder = "E:/GitHub/AgNPs/0326/01-01/UniExp/A6"
    center_crop_image(image_path, output_folder, 800, 800, 'A6')