import json
import re
import requests
import random
import time
import os
from bs4 import BeautifulSoup
import InitFolder
proxy = {
    
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Cookie": "csrfToken=UU9rKXRdR1Y3CPX7OZE_DA4b; dxy_da_cookie-id=cd8eb9163a73fdf3c8a78a385317c8851713875061882; ASK_TRACE=1713875088708629595"
}

#获取tag_id的函数，需要根据tag_id跳转到问答页

def fetchSouceData():
    section_objects = InitFolder.section_objects
    
    for section in section_objects:
        try:
            response = requests.get(url=section["href"], headers=headers)
            response.raise_for_status()  # 检查请求是否成功
            text = response.text
            tag_ids = re.findall(r'"tag_id":(\d+)', text)
            
            # 将 tag_ids 写入总文件中，每个 tag_id 占据一行，确保不重复
            file_path = os.path.join("SourceData", "total.csv")
            existing_tag_ids = set()  # 存储已经存在的 tag_id
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    for line in file:
                        existing_tag_ids.add(line.strip())
            else:
                # 如果文件不存在，则创建一个空文件
                open(file_path, 'w').close()
                
            with open(file_path, "a") as file:
                for tag_id in tag_ids:
                    if tag_id not in existing_tag_ids:
                        file.write(tag_id + "\n")  # 每个 tag_id 占据一行
                        existing_tag_ids.add(tag_id)  # 更新已经存在的 tag_id 集合
        except requests.exceptions.RequestException as e:
            print("请求异常:", e)


# 拉取问答页的问答数据
def fetchQandA():
    # 读取total.text文件
    with open('SourceData/total.csv', 'r') as f:
        # 逐行读取文件内容
        for line in f:
            # 移除行尾的换行符并转换为数字
            number = int(line.strip())
            # 构建URL
            base_url = 'https://dxy.com/disease/'
            url = base_url + str(number) + '/detail'
            print("正在请求:", url)
            
            # 发送请求
            response = requests.get(url, headers=headers)
            
            # 检查请求是否成功
            if response.status_code == 200:
                # 处理响应内容，这里可以添加你的逻辑
                soup = BeautifulSoup(response.text, 'html.parser')
                department = extract_department(soup)
                questions_and_answers = extract_q_and_a(soup)
                save_q_and_a(department, questions_and_answers)
                print("请求成功！")
            else:
                print("请求失败:", response.status_code)
                
            # 添加延迟，随机时间
            delay = random.uniform(1, 2)  # 设置一个随机延迟时间，例如1到3秒之间
            print("延迟 %.2f 秒" % delay)
            time.sleep(delay)  # 暂停一段时间

def extract_department(soup):
    # 找到包含所需值的<div>元素
    tag_content_section = soup.find('div', class_='tag-content-section')
    # 如果找到了匹配的元素
    if tag_content_section:
        # 获取该元素的文本内容
        department = tag_content_section.text.strip()
        # 去掉 "就诊科室：" 部分
        department = department[len("就诊科室："):].strip()
        print(department)
        return department
    else:
        print("未找到匹配的元素")
        return None

def extract_q_and_a(soup):
    # 提取所有问题和答案
    questions_and_answers = {}

    # 查找所有问题（以<h2>标签表示）
    questions = soup.find_all('h2')

    # 遍历每个问题
    for question in questions:
        # 获取问题文本
        question_text = question.get_text().strip() 
        # 找到相邻的下一个兄弟节点，通常是答案的段落或列表
        answer = question.find_next_sibling()
        # 初始化答案文本
        answer_text = ""
        # 如果相邻节点是 <p> 标签或者后面跟着多个连续的 <p> 标签，则拼接成一个答案
        if answer.name == 'p':
            answer_text += answer.get_text().strip() + "\n"
            # 检查后续兄弟节点是否也是 <p> 标签，若是，则继续拼接
            next_sibling = answer.find_next_sibling()
            while next_sibling and next_sibling.name == 'p':
                answer_text += next_sibling.get_text().strip() + "\n"
                next_sibling = next_sibling.find_next_sibling()  
        # 如果答案是一个列表，则提取列表项文本并拼接
        elif answer.name == 'ul':
            for li in answer.find_all('li'):
                # 查找每个 <li> 下的 <p> 标签，并将其文本添加到答案中
                for p in li.find_all('p'):
                    answer_text += p.get_text().strip() + "\n"  
        # 否则，答案就是相邻的段落
        else:
            answer_text = answer.get_text().strip() 

        # 将问题和答案添加到字典中
        questions_and_answers[question_text] = answer_text
    
    return questions_and_answers

def save_q_and_a(department, questions_and_answers):
    if department:
        # 文件夹路径
        data_folder = "SourceData"
        # 如果部门是产科或者是妇科，则将其归为妇产科
        if department == "产科" or department == "妇科":
            department = "妇产科"
        
        # 遍历 SourceData 文件夹下的所有文件夹名称
        for file_name_with_extension in os.listdir(data_folder):
            # Split the filename and extension
            file_name, extension = os.path.splitext(file_name_with_extension)
            # 如果匹配到的科室和文件名称相同就将获取到的问题数据存储到该文件
            if department == file_name:
                # 创建或追加文件并写入数据
                file_path = os.path.join(data_folder, file_name_with_extension)
                with open(file_path, 'a', encoding='utf-8') as file:
                    # 将提取到的问题和答案写入文件
                    for question, answer in questions_and_answers.items():
                        # 去除答案中的多余空格和换行
                        cleaned_answer = re.sub(r'\s+', ' ', answer.strip())
                        if cleaned_answer:  # 如果答案不为空
                            # 将问题和答案组合成一行，并用逗号分隔
                            line = f"{question}, {cleaned_answer}"
                            file.write(line + "\n")
    else:
        print("部门名称为空，无法保存问题和答案")


fetchSouceData()