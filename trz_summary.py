import requests
from bs4 import BeautifulSoup
import pandas as pd

# 给定的链接列表
# urls = [
#     'https://mp.weixin.qq.com/s/IrAvWSMVnCQOx83smyI7iA',
#     "https://mp.weixin.qq.com/s/SZZj6M0-cubJ4Up0T80R-A",
#     "https://mp.weixin.qq.com/s/Mk77_ip7lcPYInu2HnJuNw",
#     "https://mp.weixin.qq.com/s/t1RTkWNgF19nrPIdl-vJ1g"
# ]
urls = []
while True:
    url = input("Enter URL: ")
    if url == "":
        break
    urls.append(url)

entries_with_cloud = []
keywords = ["AR","VR","元宇宙","AI","大模型","人工智能","云","数据","存储","安全","机器学习","编码","操作系统","芯片"]


# 遍历每个链接
for url in urls:
    # 发送HTTP请求并获取响应
    response = requests.get(url)

    # 如果请求成功（HTTP状态码为200），则处理响应的HTML
    if response.status_code == 200:
        html_content = response.text

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 提取所有的 <strong> 标签
        strong_tags = soup.find_all('strong')

        # 遍历所有的 <strong> 标签
        for tag in strong_tags:
            # 如果标签的文本含有“云”字样，则将其添加到列表中
            next_span = tag.find_next_sibling('span')
            if next_span is not None:
                for key in keywords:
                    if (key in tag.text) or (key in next_span.text):
                        # 如果找到了<span>标签，把它的文本也添加到结果中
                        entries_with_cloud.append((tag.text, tag.text + next_span.text,key))
                        # continue


# 创建一个 pandas DataFrame
df = pd.DataFrame(entries_with_cloud, columns=['Title', 'Content',"Type"])

# 将 DataFrame 保存为 Excel 文件
df.to_excel('entries_with_cloud.xlsx', index=False)
