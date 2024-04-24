import InitFolder, FetchData

def main():
    print("正在初始化文件夹")
    InitFolder.createFile()
    # print("正在获取数据tag_id")
    # FetchData.fetchSouceData()
    print("正在拉取问答数据")
    FetchData.fetchQandA()
    print("数据获取完成")
    
if __name__ =="__main__":
    main()