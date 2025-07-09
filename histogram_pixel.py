import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# 读取Excel文件（假设数据格式：Pixel_Value | B | G | R）
df = pd.read_excel('pixel_distribution.xlsx', header=0)

# 提取数据通道
# 修改通道顺序和颜色定义
# 原代码：
channels = ['Blue', 'Red', 'Green', 'Unweighted']
colors = plt.cm.tab10(range(4)) 

# 修改后：
# 在数据提取部分添加
channels = ['Blue', 'Green', 'Red', 'Unweighted']  # 新增Unweighted
colors = ['blue', 'green', 'red', 'gray']  # 新增灰色
channel_cmaps = {
    'Blue': 'Blues',
    'Green': 'Greens',
    'Red': 'Reds',
    'Unweighted': 'Greys'  # 新增灰色映射
}

counts = [df[ch].values for ch in channels]
pixel_values = df['Pixel_Value'].values

# 创建图形布局（改为3行1列）
fig = plt.figure(figsize=(14, 12))  # 增加宽度以容纳颜色条
gs = fig.add_gridspec(4, 1)

# 添加颜色定义
# 修改颜色定义部分
# 原冲突代码：
# colors = plt.cm.tab10(range(4))  # 使用tab10色板

# 修改后保持手动颜色定义：
colors = ['blue', 'green', 'red', 'gray']  # 保持手动颜色定义

# 同时确保颜色映射对应关系：
channel_cmaps = {
    'Blue': 'Blues',
    'Green': 'Greens',  # 确保键名与channels列表完全一致
    'Red': 'Reds',
    'Unweighted': 'Greys'
}

# 分别创建三个子图
axes = [fig.add_subplot(gs[i]) for i in range(4)]

# 新增颜色映射定义
channel_cmaps = {'Red': 'Reds', 'Green': 'Greens', 'Blue': 'Blues', 'Unweighted': 'Greys'}

# 绘制每个通道的直方图
# 移除整体图形创建和布局代码
# 新增保存路径设置
output_dir = "histogram_outputs"
import os
os.makedirs(output_dir, exist_ok=True)

# 在绘图循环中会自动处理新增通道
for ch, color, cnt in zip(channels, colors, counts):
    # 为每个通道创建独立图形
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    
    # 绘制直方图（调整颜色参数）
    ax.bar(pixel_values, cnt, width=1, color=color, edgecolor='black', alpha=0.7)
    
    # 设置坐标轴 (修正缩进)
    ax.set_xlim(0, 255)
    ax.set_ylim(0, df[ch].max()*1.1)
    ax.set_xticks(np.arange(0, 256, 50))  # 主刻度每50单位
    ax.set_xticks(np.arange(0, 256, 25), minor=True)  # 次刻度每25单位
    ax.set_xlabel('Pixel Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # 添加颜色条（保持原有设置）
    norm = plt.Normalize(vmin=0, vmax=255)
    cmap = plt.get_cmap(channel_cmaps[ch])
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    cbar = plt.colorbar(sm, ax=ax, orientation='horizontal', pad=0.15)
    cbar.set_label('Pixel Value', fontsize=10, labelpad=10)
    cbar.set_ticks(np.arange(0, 256, 50))
    
    # 设置独立标题
    plt.title(f'{ch} Channel Pixel Distribution', fontsize=14, pad=20)
    
    # 保存并关闭图形
    plt.tight_layout()
    plt.savefig(f"{output_dir}/{ch}_channel_histogram.png", dpi=300, bbox_inches='tight')
    plt.close()

# 移除原代码中的整体图形显示部分（plt.show等）