import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

# 读取Excel文件（修改文件路径和工作表名称）
file_path = 'E:/GitHub/AgNPs/Fig/confusion_matrix_uniaut5_0411.xlsx'
sheet_name = 'sheet1'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 只保留数值型行和列，并确保为135*135
df = df.select_dtypes(include=[np.number])
df = df.iloc[:135, :135]

# 设置x/y轴标签为SE01-SE135
labels = [f'SE{str(i+1).zfill(2)}' for i in range(135)]

# 设置A4纸宽度（A4为210mm≈8.27英寸，建议宽度8.3，高度可适当加大以保证可读性）
plt.figure(figsize=(10, 10))

# 只突出非0部分，使用对数色阶或自定义色阶
# 在已有导入部分新增颜色映射库
from matplotlib.colors import ListedColormap

# 修改热力图绘制部分
# 修改主热力图部分
from matplotlib.colors import LogNorm, LinearSegmentedColormap

# 创建分段颜色映射（1-9红色，10-200蓝色渐变）
# 创建分段颜色映射（修正版）
colors = [
    '#ff4d4d',  # 起始红色
    '#ff4d4d',  # 保持红色到10^0.1≈1.26
    '#e6f3ff',  # 浅蓝过渡
    '#0066cc'   # 结束深蓝
]
custom_cmap = LinearSegmentedColormap.from_list('RedBlue', colors, N=256)

sns.heatmap(
    df,
    annot=False,
    cmap=custom_cmap,
    norm=LogNorm(vmin=1, vmax=200),
    linewidths=0.05,
    square=True,
    cbar_kws={'shrink': 0.8, 'aspect': 30},
    mask=(df == 0)
)

# 删除之前添加的红色、蓝色分层热力图代码

# 添加红色标注（<10的值）
# 修改红色标注的mask条件
sns.heatmap(
    df,
    mask=(df >= 10) | (df == 0),  # 新增排除0值
    cmap=ListedColormap(['#ff4d4d']),
    linewidths=0.05,
    square=True,
    cbar=False,
    annot=False
)

# 添加蓝色标注（>190的值）
sns.heatmap(
    df,
    mask=(df <= 190),
    cmap=ListedColormap(['#0066cc']),  # 深蓝色
    linewidths=0.05,
    square=True,
    cbar=False,
    annot=False
)

# 每隔5个显示一个标签
tick_pos = np.arange(0.5, 135, 5)
tick_labels = [labels[i] for i in range(0, 135, 5)]
plt.xticks(ticks=tick_pos, labels=tick_labels, fontsize=7, rotation=90)
plt.yticks(ticks=tick_pos, labels=tick_labels, fontsize=7, rotation=0)

# 设置colorbar不使用科学计数法
cbar = plt.gca().collections[0].colorbar
cbar.ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))

# 删除以下两行文本标注代码
# cbar.ax.text(-1.2, 0.05, '<10', ... )
# cbar.ax.text(1.3, 0.95, '>190', ... )

plt.title('Confusion Matrix (135x135)', fontsize=18, pad=10)
plt.xlabel('Predicted Labels', fontsize=16)
plt.ylabel('True Labels', fontsize=16)

# 显示混淆矩阵边框
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1)
    spine.set_linestyle('-')

plt.tight_layout()
plt.savefig('confusion_matrix_uniaut5_135x135.png', dpi=300, bbox_inches='tight')
plt.show()