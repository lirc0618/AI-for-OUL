import os
import numpy as np
import shutil

def split_dataset(src_dir, train_dir, val_dir, test_dir, train_ratio=0.7, val_ratio=0.2):
    """
    将数据集划分为训练集、验证集和测试集。

    :param src_dir: str，源数据集目录
    :param train_dir: str，训练集目录
    :param val_dir: str，验证集目录
    :param test_dir: str，测试集目录
    :param train_ratio: float，训练集比例
    :param val_ratio: float，验证集比例
    """
    # 确保目标文件夹存在
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # 获取源文件夹中的文件列表并打乱
    files = os.listdir(src_dir)
    np.random.shuffle(files)

    # 计算分割点
    train_split = int(len(files) * train_ratio)
    val_split = int(len(files) * (train_ratio + val_ratio))

    # 分割文件列表
    train_files = files[:train_split]
    val_files = files[train_split:val_split+1]
    test_files = files[val_split+1:]

    # 复制文件到训练集、验证集和测试集文件夹
    for file in train_files:
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(train_dir, file)
        shutil.copy(src_file, dst_file)

    for file in val_files:
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(val_dir, file)
        shutil.copy(src_file, dst_file)

    for file in test_files:
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(test_dir, file)
        shutil.copy(src_file, dst_file)


# 源数据集的根目录
root_src_dir = 'E:/GitHub/AgNPs/0326/03-01/UniExp3'

# 训练集、验证集和测试集的根目录
root_train_dir = 'E:/GitHub/AgNPs/0326/03-01/Data/AI/UniAut3/train'
root_val_dir = 'E:/GitHub/AgNPs/0326/03-01/Data/AI/UniAut3/val'
root_test_dir = 'E:/GitHub/AgNPs/0326/03-01/Data/AI/UniAut3/test'

# 遍历源数据集的根目录，处理每个子目录
for subdir in os.listdir(root_src_dir):
    src_dir = os.path.join(root_src_dir, subdir)
    if os.path.isdir(src_dir):  # 确保是目录
        train_dir = os.path.join(root_train_dir, subdir)
        val_dir = os.path.join(root_val_dir, subdir)
        test_dir = os.path.join(root_test_dir, subdir)
        split_dataset(src_dir, train_dir, val_dir, test_dir)