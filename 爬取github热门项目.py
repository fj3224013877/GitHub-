import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 从环境变量中获取语言类型和 SCKEY
language = os.getenv('LANGUAGE', 'python')  # 默认语言为 python
sckey = os.getenv('SCKEY')

# 设置时间范围
since = 'daily'  # 你可以根据需要修改时间范围，例如 'daily', 'weekly', 'monthly'

# 构建目标 URL
url = f'https://github.com/trending/{language}?since={since}'

# 发送请求
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 解析 HTML 内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取仓库数据
repos = []
for item in soup.select('article.Box-row'):
    # 提取仓库名称和所有者
    full_name = item.select_one('h2.h3 a').text.strip().replace('\n', '').replace(' ', '')
    owner, repo_name = full_name.split('/')
    
    # 提取描述
    description = item.select_one('p').text.strip() if item.select_one('p') else 'No description'
    
    # 提取星标数
    stars = item.select_one('a.Link--muted').text.strip().replace(',', '')
    
    # 提取 Fork 数
    forks = item.select('a.Link--muted')[1].text.strip().replace(',', '') if len(item.select('a.Link--muted')) > 1 else '0'
    
    # 提取项目 URL
    Rope_url = 'https://github.com' + item.select_one('h2.h3 a')['href']
    
    repos.append([owner.strip(), repo_name.strip(), description, stars, forks, Rope_url])

# 将数据保存到 DataFrame
df = pd.DataFrame(repos, columns=['Owner', 'Name', 'Description', 'Stars', 'Forks', 'Rope_url'])

# 显示前几行数据
print(df.head())

# 保存数据到 CSV 文件
csv_filename = f'github_trending_{language}_{since}.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8')
print(f"数据已保存到 {csv_filename}")

# 构建推送消息
message = "GitHub Trending Repositories:\n"
for index, row in df.iterrows():
    message += f"{index + 1}\n"
    message += f"{row['Owner']}/{row['Name']} - Stars: {row['Stars']}, Forks: {row['Forks']}\n"
    message += f"Description: {row['Description']}\n\n"
    message += f"URL: {row['Rope_url']}\n\n"

print('message:', message)  # 打印消息内容

# 推送消息到微信
payload = {
    "title": "GitHub Trending Repositories",
    "desp": message
}

response = requests.post(f'https://sctapi.ftqq.com/{sckey}.send', data=payload)
if response.status_code == 200:
    print("消息推送成功")
else:
    print("消息推送失败")
