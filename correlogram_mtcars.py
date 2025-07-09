import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# 读取Excel文件（修改文件路径和工作表名称）
file_path = 'E:/GitHub/AgNPs/Fig/fsim_confusion_matrix_1.xlsx'  # 替换为你的Excel文件路径
sheet_name = 'sheet1'        # 替换为你的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 处理数据（根据需要调整）
# 删除包含缺失值的行
df = df.dropna(how='any')

# 选择数值型列（可选）
numeric_df = df.select_dtypes(include=[np.number])

# 计算相关矩阵
corr_matrix = numeric_df.corr()

# 翻转行顺序，使数据从下到上
corr_matrix = corr_matrix.iloc[::-1]

# 设置图像尺寸
plt.figure(figsize=(12, 10))

# 绘制热力图
# 创建自定义颜色映射（添加在热力图绘制之前）
# 修改颜色映射定义
colors = [
    (0, "#ffffff"),     # 纯白 (最小值)
    (0.5, "#00FF00"),   # 纯绿 (中间点)
    (0.5, "#87CEEB"),   # 浅蓝起始 (中间点)
    (1, "#00008B")      # 深蓝结束 (最大值)
]
custom_cmap = LinearSegmentedColormap.from_list("GreenBlue", colors)

# 修改热力图绘制部分
sns.heatmap(
    corr_matrix,
    annot=False,
    cmap=custom_cmap,  # 使用自定义颜色映射
    vmin=0, vmax=1,
    linewidths=0,
    square=True,
    cbar_kws={'aspect': 30}
)

# 设置最外边框可见
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)  # 显示边框
    spine.set_color('black') # 设置边框颜色
    spine.set_linewidth(0.8) # 设置边框宽度

plt.gca().set_yticks(range(0, len(corr_matrix.index), 5))  # 每隔 5 个显示一次
plt.gca().set_yticklabels(corr_matrix.index[::-1][::-5])  # 确保最后一个标签显示
plt.gca().set_xticks(range(5, len(corr_matrix.columns)+1, 5))  # 每隔 5 个显示一次
plt.gca().set_xticklabels(reversed(corr_matrix.index[0:135:5]))  # 确保最后一个标签显示
# 设置标题和标签
plt.title('Correlogram of Labels', fontsize=22, pad=20)
plt.xlabel('First Scan of Labels', fontsize=18)
plt.ylabel('Second Scan of Labels', fontsize=18)

# 调整布局
plt.tight_layout()

# 保存图像（修改保存路径）
plt.savefig('E:/GitHub/AgNPs/correlation_matrix_1.png', dpi=300, bbox_inches='tight')

# 显示图像（可选）
plt.show()