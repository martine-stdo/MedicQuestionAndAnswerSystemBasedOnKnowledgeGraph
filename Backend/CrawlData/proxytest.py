import requests
url ="https://www.baidu.com/"
response = requests.get(url=url)
print(response.status_code)
print(response.text)