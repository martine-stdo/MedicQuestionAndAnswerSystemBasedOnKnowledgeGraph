from py2neo import Graph, Node, Relationship  # 导入Py2neo库中的Graph、Node和Relationship类
import os  # 导入os库
import csv

# 连接到 Neo4j 数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))  # 使用bolt协议连接到本地Neo4j数据库，提供用户名和密码进行认证

# 创建唯一性约束
graph.run("CREATE CONSTRAINT FOR (d:Department) REQUIRE (d.title) IS UNIQUE")  
# graph.run("CREATE CONSTRAINT FOR (q:Question) REQUIRE (q.Q) IS UNIQUE")  

# 创建节点和关系
def create_department_node(file_name):
    # 去除文件名的扩展名
    department_title = os.path.splitext(file_name)[0]  # 通过os.path.splitext()函数去除文件名的扩展名
    department_node = Node("Department", title=department_title)  # 创建一个部门节点，文件名作为部门节点的标题属性
    graph.create(department_node)  # 在数据库中创建部门节点
    return department_node  # 返回创建的部门节点

def create_question_node(question_text):
    question_node = Node("Question", Q=question_text)  # 创建一个问题节点，问题作为问题节点的属性
    graph.create(question_node)  # 在数据库中创建问题节点
    return question_node  # 返回创建的问题节点

def create_answer_node(answer_text):
    answer_node = Node("Answer", A=answer_text)  # 创建一个答案节点，答案作为答案节点的属性
    graph.create(answer_node)  # 在数据库中创建答案节点
    return answer_node  # 返回创建的答案节点

def create_relationship(start_node, end_node, rel_type):
    relationship = Relationship(start_node, rel_type, end_node)  # 创建两个节点之间的关系
    graph.create(relationship)  # 在数据库中创建关系

# 遍历每个.csv文件
source_data_dir = 'CleanData'  # 定义存放清洗数据的文件夹路径
csv_files = [file for file in os.listdir(source_data_dir) if file.endswith('.csv')]  # 获取文件夹中所有以.csv结尾的文件名

for csv_file in csv_files:
    with open(os.path.join(source_data_dir, csv_file), 'r', encoding='utf-8') as file:  # 打开每个.csv文件
        department_node = create_department_node(csv_file)  # 创建部门节点

        csv_reader = csv.reader(file)  # 创建CSV读取器
        for row in csv_reader:  # 遍历.csv文件中的每一行
            if len(row) == 2:  # 如果行中有两个元素（问题和答案）
                question_node = create_question_node(row[0])  # 创建问题节点
                answer_node = create_answer_node(row[1])  # 创建答案节点

                create_relationship(department_node, question_node, "contain")  # 建立部门与问题的关系
                create_relationship(question_node, answer_node, "reply")  # 建立问题与答案的关系

print("数据导入完成！")  # 输出提示信息，表示数据导入操作完成
