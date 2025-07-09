import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# 读取Excel文件
file_path = 'E:/GitHub/AgNPs/Fig/uniaut5_training_history_0411.xlsx'  # 请替换为你的文件路径
df = pd.read_excel(file_path, engine='openpyxl')

# 提取数据列
epochs = df['Epoch']
train_loss = df['Train Loss']
train_acc = df['Train Accuracy']
val_loss = df['Validation Loss']
val_acc = df['Validation Accuracy']
lr = df['Learning Rate']

# 新增：检测学习率变化点（前三个）
change_points = []
for i in range(1, len(lr)):
    if lr[i] != lr[i-1]:
        change_points.append(epochs[i])
        if len(change_points) >= 3:
            break

plt.style.use('seaborn-v0_8')
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 300

# 绘制loss和learning rate双轴曲线
fig, ax1 = plt.subplots(figsize=(8, 6))
l1, = ax1.plot(epochs, train_loss, 'b-', label='Train Loss')
l2, = ax1.plot(epochs, val_loss, 'r-', label='Validation Loss')

# 删除以下3行 axvline 代码
# for cp in change_points:
#     ax1.axvline(x=cp, color='yellow', linestyle='--', alpha=0.7, linewidth=1.5)

ax1.set_xlabel('Epoch', fontsize=16)
ax1.set_ylabel('Loss', fontsize=16)
ax1.set_title('Training and Validation Loss with Learning Rate', fontsize=18)
ax1.grid(True, which='both', linestyle='--', alpha=0.8, color='black')
for spine in ax1.spines.values():
    spine.set_linestyle('-')
    spine.set_linewidth(1.2)
    spine.set_color('black')
ax1.set_facecolor('white')
fig.patch.set_facecolor('white')

ax2 = ax1.twinx()
l3, = ax2.plot(epochs, lr, 'g-', label='Learning Rate')
ax2.set_ylabel('Learning Rate', fontsize=16, color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.set_yscale('log')  # 设置右侧y轴为对数坐标轴
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1e'))  # 指数表示法


# 合并图例
lines = [l1, l2, l3]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper right', bbox_to_anchor=(1, 0.92))

plt.tight_layout()
plt.savefig('uniaut5_loss_lr_curve1.jpg')
plt.close()

# 绘制accuracy和learning rate双轴曲线
fig, ax1 = plt.subplots(figsize=(8, 6))
l1, = ax1.plot(epochs, train_acc, 'b-', label='Train Accuracy')
l2, = ax1.plot(epochs, val_acc, 'r-', label='Validation Accuracy')

# 删除以下3行 axvline 代码
# for cp in change_points:
#     ax1.axvline(x=cp, color='yellow', linestyle='--', alpha=0.7, linewidth=1.5)

ax1.set_xlabel('Epoch', fontsize=16)
ax1.set_ylabel('Accuracy', fontsize=16)
ax1.set_title('Training and Validation Accuracy with Learning Rate', fontsize=18)
ax1.grid(True, which='both', linestyle='--', alpha=0.8, color='black')
for spine in ax1.spines.values():
    spine.set_linestyle('-')
    spine.set_linewidth(1.2)
    spine.set_color('black')
ax1.set_facecolor('white')
fig.patch.set_facecolor('white')

ax2 = ax1.twinx()
l3, = ax2.plot(epochs, lr, 'g-', label='Learning Rate')
ax2.set_ylabel('Learning Rate', fontsize=14, color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.set_yscale('log')  # 设置右侧y轴为对数坐标轴
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1e'))  # 指数表示法

# 合并图例时新增（修改代码）
#proxy_line = plt.Line2D([0], [0], color='yellow', linestyle='--', linewidth=1.5, alpha=0.7, label='LR Change Point')
lines = [l1, l2, l3]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper right', bbox_to_anchor=(1, 0.92))

plt.tight_layout()
plt.savefig('uniaut5_accuracy_lr_curve1.jpg')
plt.close()

print("图表已保存为 uniaut5_loss_lr_curve1.jpg 和 uniaut5_accuracy_lr_curve1.jpg")