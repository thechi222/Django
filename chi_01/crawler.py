import requests
from bs4 import BeautifulSoup

# 目標：抓取 Dcard 熱門看板的前10篇文章標題與連結
url = "https://www.dcard.tw/f"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.select('h2 a')  # Dcard 的每篇文章通常是用 h2 包住 <a> 標籤

    for i, post in enumerate(posts[:10]):
        title = post.get_text(strip=True)
        link = "https://www.dcard.tw" + post['href']
        print(f"{i+1}. {title}\n👉 {link}\n")
else:
    print("無法連接到網站，狀態碼：", response.status_code)
