import os
from PIL import Image

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


def batch_center_crop(input_dir, output_dir, crop_size=(800, 800)):
    """
    批量中心裁剪文件夹中的图片
    
    :param input_dir: 输入目录路径
    :param output_dir: 输出目录路径
    :param crop_size: 裁剪尺寸 (宽, 高)
    """
    os.makedirs(output_dir, exist_ok=True)
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            try:
                with Image.open(input_path) as img:
                    cropped = center_crop(img, crop_size)
                    cropped.save(output_path)
                    print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")


if __name__ == "__main__":
    import argparse
    
    # 示例路径（替换为你实际的路径）
    DEFAULT_INPUT = "E:/GitHub/AgNPs/0326/00-01"   # 默认输入目录
    DEFAULT_OUTPUT = "E:/GitHub/AgNPs/0326/00-02"  # 默认输出目录
    
    parser = argparse.ArgumentParser(description='批量中心裁剪图片')
    parser.add_argument('--input', default=DEFAULT_INPUT, 
                      help=f'输入目录路径（默认：{DEFAULT_INPUT}）')
    parser.add_argument('--output', default=DEFAULT_OUTPUT,
                      help=f'输出目录路径（默认：{DEFAULT_OUTPUT}）')
    parser.add_argument('--size', type=int, nargs=2, default=[800, 800],
                      help='裁剪尺寸（宽 高），默认 800 800')
    
    args = parser.parse_args()
    batch_center_crop(args.input, args.output, tuple(args.size))