import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from brokenaxes import brokenaxes

def plot_correlation_histogram(file_path, output_path=None):
    """
    读取包含标题的相关性矩阵 .xlsx 文件，并绘制相关系数分布直方图（使用断裂轴缩短x轴长度，并用 // 表示截断）。
    """
    # 读取Excel文件
    df = pd.read_excel(file_path, header=0, index_col=0)
    assert df.shape == (135, 135), "数据矩阵必须是135x135"
    data = df.values.flatten()

    # 定义分段参数
    # 修改segments定义
    segments = [
        {"range": (0.36, 0.5), "bins": list(np.arange(0.36, 0.5, 0.01)), "color": "#15B01A", "label": "intercorrelation"},
        # 删除intracorrelation部分
    ]
    
    # 修改断裂轴范围（移除不需要的区间）
    bax = brokenaxes(
        xlims=((0, 0.02), (0.36, 0.5)),  # 移除(0.95, 1)区间
        hspace=0.05,
        despine=False
    )

    # 创建普通坐标系
    plt.figure(figsize=(12, 6))
    ax = plt.gca()

    # 计算全局权重（百分比）
    weights = np.ones_like(data) / len(data) * 100

    # 绘制单个直方图（聚焦在0.36-0.5区间）
    mask = (data >= 0.36) & (data <= 0.5)
    ax.hist(
        data[mask],
        bins=np.arange(0.36, 0.5, 0.01),
        weights=weights[mask],
        edgecolor="white",
        alpha=0.9,
        color="#15B01A",
        label="intercorrelation"
    )

    # 设置坐标轴范围
    ax.set_xlim(0.36, 0.5)
    ax.set_ylim(0, 30)

    # 分段绘制直方图
    for seg in segments:
        low, high = seg["range"]
        mask = (data >= low) & (data <= high)
        
        # 特殊处理半开区间
        if seg["label"] == "0.36-0.50":
            mask = (data >= low) & (data < high)  # 不包含上限
            
        bax.hist(
            data[mask],
            bins=seg["bins"],
            weights=weights[mask],
            edgecolor="white",
            alpha=0.9,
            color=seg["color"],
            label=seg["label"]
        )

    # 设置标题和标签（保持原有设置）
    ax.set_title("Correlation Matrix Histogram", fontsize=20)
    ax.set_xlabel("Correlation Value", fontsize=18)
    ax.set_ylabel("Percentage (%)", fontsize=18)
    
    # 设置坐标轴范围（保持断裂轴时的显示范围）
    ax.set_xlim(0.36, 0.5)  # 调整为完整显示0-0.5区间
    ax.set_ylim(0, 30)
    
    # 保持边框样式
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(0.8)

    # 添加图例
    bax.legend(loc="upper right", framealpha=0.9)

    # 保存或显示图像
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        print(f"直方图已保存为: {output_path}")
    else:
        plt.show()

# 示例调用
if __name__ == "__main__":
    input_file_path = 'E:/GitHub/AgNPs/Fig/fsim_confusion_matrix_1.xlsx'  # 替换为你的输入文件路径
    output_image_path = 'E:/GitHub/AgNPs/Fig/correlation_histogram_0606.jpg'  # 替换为你的输出图片路径
    plot_correlation_histogram(input_file_path, output_image_path)