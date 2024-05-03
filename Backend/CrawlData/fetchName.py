import os

# 设置源目录
source_data_dir = 'CleanData'

# 存储文件名的列表
file_names = []

# 遍历源目录中的文件
for file in os.listdir(source_data_dir):
    # 检查文件是否是文件而不是目录
    if os.path.isfile(os.path.join(source_data_dir, file)):
        # 去除文件后缀，并将文件名存储到列表中
        file_names.append(os.path.splitext(file)[0])

# 打印文件名列表
print(file_names)
