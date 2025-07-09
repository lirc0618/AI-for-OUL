import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件（修改文件路径和工作表名称）
file_path = 'E:/GitHub/AgNPs/Fig/fsim_confusion_matrix_1.xlsx'
sheet_name = 'sheet4'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 只保留数值型行和列
df = df.select_dtypes(include=[np.number])


# 设置y轴标签
y_labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']

plt.figure(figsize=(6, 6))

sns.heatmap(
    df,
    annot=True,
    #fmt='d',  # 以整数正常显示，不用科学计数法
    cmap='Blues',
    vmin=0, vmax=1,
    linewidths=0.1,
    square=True,            # 确保单元格为正方形
    cbar_kws={'shrink': 0.75, 'aspect': 20 * len(y_labels) / df.shape[1]}  # 调整尺度条长度  

)

plt.xticks(fontsize=8, rotation=0)
plt.yticks(ticks=np.arange(0.5, len(y_labels)), labels=y_labels, fontsize=8, rotation=0)
plt.title('Similarity of Labels', fontsize=14, pad=10)
plt.xlabel('First Scan of Labels', fontsize=12)
plt.ylabel('Second Scan of Labels', fontsize=12)
plt.tight_layout()
plt.savefig('fsim_confusion_matrix_uniaut0.png', dpi=300, bbox_inches='tight')
plt.show()