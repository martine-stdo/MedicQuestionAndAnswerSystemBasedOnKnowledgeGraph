import json
import os
import re
import requests

# 从 OriginalData.json 中获取 sections 即是科室比如儿科
with open("OriginalData.json", mode="r", encoding="utf-8") as f:
    json_data = json.load(f)
sections = json_data["sections"]

# 将每个 section 存储为字典对象，并添加到列表中
section_objects = []
for section in sections:
    section_object = {
        "id": section["id"],
        "name": section["name"],
        "href": section["href"]
    }
    section_objects.append(section_object)


def createFile():
    # 获取每个科室的名称并创建文件夹
    # 遍历每个科室
    for section in sections:
        section_name = section["name"]
        # 创建文件夹路径
        folder_path = os.path.join("SourceData")
        os.makedirs(folder_path, exist_ok=True)  # 确保目录存在
        file_path = os.path.join(folder_path, f"{section_name}.csv")
        # 创建空的 csv文件
        with open(file_path, "a+") as csv_file:
            pass  # 空文件
        
    
    
