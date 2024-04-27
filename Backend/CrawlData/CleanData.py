import os
import csv
from tqdm import tqdm  # 导入tqdm库

# 创建CleanData文件夹
clean_data_dir = 'CleanData'
if not os.path.exists(clean_data_dir):
    os.makedirs(clean_data_dir)

# 获取SourceData文件夹下所有.csv文件，排除total.csv
source_data_dir = 'SourceData'
csv_files = [file for file in os.listdir(source_data_dir) if file.endswith('.csv') and file != 'total.csv']

# 计算文件总数
total_files = len(csv_files)

# 使用tqdm创建总的进度条
with tqdm(total=total_files, desc="Cleaning files") as pbar:
    # 清洗每个.csv文件
    for csv_file in csv_files:
        input_file_path = os.path.join(source_data_dir, csv_file)  # 输入文件路径
        output_file_path = os.path.join(clean_data_dir, csv_file)  # 输出文件路径

        with open(input_file_path, 'r', encoding='utf-8') as input_file, \
                open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:

            reader = csv.reader(input_file)  # 创建CSV读取器
            writer = csv.writer(output_file)  # 创建CSV写入器

            for row in reader:
                if len(row) > 0 and len(row[0]) > 12:  # 只保留每行字数大于12个字的行
                    writer.writerow(row)

        pbar.update(1)  # 更新进度条

print("清洗完成！")
