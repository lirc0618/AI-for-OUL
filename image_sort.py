# 数据集随机分类，80%训练，20%验证
import os
import numpy as np
import shutil

# from sklearn.utils import shuffle

img_dir1 = 'E:/GitHub/AgNPs/0326/01-01/UniExp0/A1'  # 源数据集图像的文件夹的路径

a1 = os.listdir(img_dir1)
np.random.shuffle(a1)  # 将数据集打乱顺序

d1 = int(len(a1) * 8 / 10)  # 将数据集分为两部分，在这里可以根据自己的需要修改
b1 = a1[:d1]   # 数据集的前80%部分
c1 = a1[d1:]   # 数据集的80%~100%部分

for i in b1:
    train_dir1 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/A1', i)  # 随机数据集的图像的路径
    img_dir1= os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A1', i)  # 原始数据集的图像的路径
    shutil.copy(img_dir1, train_dir1)

for j in c1:
    val_dir1 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/A1', j)  # 随机数据集的图像的路径
    img_dir1 = os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A1', j)  # 原始数据集的图像的路径
    shutil.copy(img_dir1, val_dir1)


img_dir2 = 'E:/GitHub/AgNPs/0326/01-01/UniExp0/A2'  # 源数据集图像的文件夹的路径

a2 = os.listdir(img_dir2)
np.random.shuffle(a2)  # 将数据集打乱顺序

d2 = int(len(a2) * 8 / 10)  # 将数据集分为两部分，在这里可以根据自己的需要修改
b2 = a2[:d2]   # 数据集的前80%部分
c2 = a2[d2:]   # 数据集的80%~100%部分

for i in b2:
    train_dir2 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/A2', i)  # 随机数据集的图像的路径
    img_dir2= os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A2', i)  # 原始数据集的图像的路径
    shutil.copy(img_dir2, train_dir2)

for j in c2:
    val_dir2 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/A2', j)  # 随机数据集的图像的路径
    img_dir2 = os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A2', j)  # 原始数据集的图像的路径
    shutil.copy(img_dir2, val_dir2)


img_dir3 = 'E:/GitHub/AgNPs/0326/01-01/UniExp0/A3'  # 源数据集图像的文件夹的路径

a3 = os.listdir(img_dir3)
np.random.shuffle(a3)  # 将数据集打乱顺序

d3 = int(len(a3) * 8 / 10)  # 将数据集分为两部分，在这里可以根据自己的需要修改
b3 = a3[:d3]   # 数据集的前80%部分
c3 = a3[d3:]   # 数据集的80%~100%部分

for i in b3:
    train_dir3 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/A3', i)  # 随机数据集的图像的路径
    img_dir3= os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A3', i)  # 原始数据集的图像的路径
    shutil.copy(img_dir3, train_dir3)

for j in c3:
    val_dir3 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/A3', j)  # 随机数据集的图像的路径
    img_dir3 = os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A3', j)  # 原始数据集的图像的路径
    shutil.copy(img_dir3, val_dir3)


img_dir4 = 'E:/GitHub/AgNPs/0326/01-01/UniExp0/A4'  # 源数据集图像的文件夹的路径

a4 = os.listdir(img_dir4)
np.random.shuffle(a4)  # 将数据集打乱顺序

d4 = int(len(a4) * 8 / 10)  # 将数据集分为两部分，在这里可以根据自己的需要修改
b4 = a4[:d4]   # 数据集的前80%部分
c4 = a4[d4:]   # 数据集的80%~100%部分

for i in b4:
    train_dir4 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/A4', i)  # 随机数据集的图像的路径
    img_dir4= os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A4', i)  # 原始数据集的图像的路径
    shutil.copy(img_dir4, train_dir4)

for j in c4:
    val_dir4 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/A4', j)  # 随机数据集的图像的路径
    img_dir4 = os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A4', j)  # 原始数据集的图像的路径
    shutil.copy(img_dir4, val_dir4)


img_dir5 = 'E:/GitHub/AgNPs/0326/01-01/UniExp0/A5'  # 源数据集图像的文件夹的路径

a5 = os.listdir(img_dir5)
np.random.shuffle(a5)  # 将数据集打乱顺序

d5 = int(len(a5) * 8 / 10)  # 将数据集分为两部分，在这里可以根据自己的需要修改
b5 = a5[:d5]   # 数据集的前80%部分
c5 = a5[d5:]   # 数据集的80%~100%部分

for i in b5:
    train_dir5 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/A5', i)  # 随机数据集的图像的路径
    img_dir5= os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A5', i)  # 原始数据集的图像的路径
    shutil.copy(img_dir5, train_dir5)

for j in c5:
    val_dir5 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/A5', j)  # 随机数据集的图像的路径
    img_dir5 = os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A5', j)  # 原始数据集的图像的路径
    shutil.copy(img_dir5, val_dir5)


img_dir6 = 'E:/GitHub/AgNPs/0326/01-01/UniExp0/A6'  # 源数据集图像的文件夹的路径

a6 = os.listdir(img_dir6)
np.random.shuffle(a6)  # 将数据集打乱顺序

d6 = int(len(a6) * 8 / 10)  # 将数据集分为两部分，在这里可以根据自己的需要修改
b6 = a6[:d6]   # 数据集的前80%部分
c6 = a6[d6:]   # 数据集的80%~100%部分

for i in b6:
    train_dir6 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/A6', i)  # 随机数据集的图像的路径
    img_dir6= os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A6', i)  # 原始数据集的图像的路径
    shutil.copy(img_dir6, train_dir6)

for j in c6:
    val_dir6 = os.path.join('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/A6', j)  # 随机数据集的图像的路径
    img_dir6 = os.path.join('E:/GitHub/AgNPs/0326/01-01/UniExp0/A6', j)  # 原始数据集的图像的路径
    shutil.copy(img_dir6, val_dir6)


