#生成数据集标签，train.txt, val.txt, 模型训练使用
import os
def generate(dir, label):
    files = os.listdir(dir) #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    files.sort()  #对文件或文件夹进行排序
    print('****************')
    print('input :', dir)
    print('start...')
    listText = open('E:/GitHub/AgNPs/0326/01-01/Data/AI/train/train.txt', 'a+')  #创建并打开一个txt文件，a+表示打开一个文件并追加内容
    #listText = open('E:/GitHub/AgNPs/0326/01-01/Data/AI/val/val.txt', 'a+')  #创建并打开一个txt文件，a+表示打开一个文件并追加内容
    for file in files:  #遍历文件夹中的文件
        fileType = os.path.split(file) #os.path.split（）返回文件的路径和文件名，【0】为路径，【1】为文件名
        if fileType[1] == '.txt':  #若文件名的后缀为txt,则继续遍历循环，否则退出循环
            continue
        name = folder+ '/' +file + ' ' + str(int(label)) + '\n'  #name 为文件路径和文件名+空格+label+换行
        listText.write(name)  #在创建的txt文件中写入name
    listText.close() #关闭txt文件
    print('down!')
    print('****************')


train_path = 'E:/GitHub/AgNPs/0326/01-01/Data/AI/train'  # 这里是你的图片路径
#val_path = 'E:/GitHub/AgNPs/0326/01-01/Data/AI/val'  # 这里是你的图片路径

if __name__ == '__main__':  #主函数
    i = 1
    train_list = os.listdir(train_path)# 列举文件夹
    for folder in train_list:  #遍历文件夹中的文件夹(若engagement文件夹中存在txt或py文件，则后面会报错）
        generate(os.path.join(train_path, folder), i)#调用generate函数，函数中的参数为：（图片路径+文件夹名，标签号）
        i += 1

    # i = 1
    # val_list = os.listdir(val_path)# 列举文件夹
    # for folder in val_list:  #遍历文件夹中的文件夹(若engagement文件夹中存在txt或py文件，则后面会报错）
    #     generate(os.path.join(val_path, folder), i)#调用generate函数，函数中的参数为：（图片路径+文件夹名，标签号）
    #     i += 1