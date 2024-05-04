import os

# 设置源目录
source_data_dir = 'CleanData'

# 存储文件名和行数的字典
file_line_count = {}

# 遍历源目录中的文件
for file in os.listdir(source_data_dir):
    # 构建文件路径
    file_path = os.path.join(source_data_dir, file)
    # 检查文件是否是文件而不是目录
    if os.path.isfile(file_path) and file.endswith('.csv'):
        # 统计文件行数
        with open(file_path, 'r', encoding='utf-8') as f:
            line_count = sum(1 for line in f)
        # 去除文件后缀，并将文件名及行数存储到字典中
        file_names = os.path.splitext(file)[0]
        file_line_count[file_names] = line_count

# 打印每个文件名及对应的行数
for name, count in file_line_count.items():
    print(f"{name}:{count}")
