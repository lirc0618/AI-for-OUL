import os
from PIL import Image
import pandas as pd

def analyze_images(folder_path):
    # 初始化数据结构
    red_data = pd.DataFrame(index=range(256))
    green_data = pd.DataFrame(index=range(256))
    blue_data = pd.DataFrame(index=range(256))

    valid_ext = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    processed_files = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith(valid_ext):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    img = img.convert('RGB')
                    pixels = img.getdata()
                    
                    # 初始化临时计数器
                    r_counts = [0] * 256
                    g_counts = [0] * 256
                    b_counts = [0] * 256
                    
                    # 统计单个图片
                    for r, g, b in pixels:
                        r_counts[r] += 1
                        g_counts[g] += 1
                        b_counts[b] += 1
                    
                    # 添加到DataFrame
                    col_name = os.path.splitext(filename)[0]
                    red_data[col_name] = r_counts
                    green_data[col_name] = g_counts
                    blue_data[col_name] = b_counts
                    processed_files.append(col_name)
                    
            except Exception as e:
                print(f"处理文件 {filename} 出错: {str(e)}")
    
    # 添加汇总列
    red_data['Total'] = red_data.sum(axis=1)
    green_data['Total'] = green_data.sum(axis=1)
    blue_data['Total'] = blue_data.sum(axis=1)
    
    return red_data, green_data, blue_data, processed_files

def save_to_excel(red_df, green_df, blue_df, output_file):
    with pd.ExcelWriter(output_file) as writer:
        red_df.to_excel(writer, sheet_name='Red_Channel')
        green_df.to_excel(writer, sheet_name='Green_Channel')
        blue_df.to_excel(writer, sheet_name='Blue_Channel')

if __name__ == "__main__":
    image_folder = "E:/GitHub/AgNPs/0326/00"
    output_file = "Pixel_Distribution_Report1.xlsx"
    
    r_df, g_df, b_df, files = analyze_images(image_folder)
    save_to_excel(r_df, g_df, b_df, output_file)
    
    print(f"成功处理 {len(files)} 张图片")
    print(f"结果已保存至: {output_file}")