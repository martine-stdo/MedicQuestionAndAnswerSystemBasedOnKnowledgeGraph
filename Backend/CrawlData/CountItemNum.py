import os

def count_total_lines_except_total_csv(folder_path):
    total_lines = 0
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, filename)
        # 如果是CSV文件且不是total.csv
        if filename.endswith('.csv') and filename != 'total.csv' and os.path.isfile(file_path):
            # 统计文件的行数
            with open(file_path, 'r', encoding='utf-8') as file:
                total_lines += sum(1 for line in file)
    return total_lines

# 使用示例
folder_path = "SourceData"
total_lines = count_total_lines_except_total_csv(folder_path)
print("除了 total.csv 外，该文件夹下所有 CSV 文件的行数之和为:", total_lines)
