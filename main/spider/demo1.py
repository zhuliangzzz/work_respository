#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo1.py
   @author:zl
   @time: 2025/9/2 16:15
   @software:PyCharm
   @desc:
"""

import requests
from bs4 import BeautifulSoup
# 初始化用户代理池
from fake_useragent import UserAgent
ua = UserAgent(browsers=['Chrome'], os=['windows'])

# url = 'https://mp.weixin.qq.com/s/FhgPAPt_6mF3sSxPuGeWCQ'
# url = 'https://mp.weixin.qq.com/s/KbqgsQYPMfQ5pzETvF-fqg'
# url = 'https://mp.weixin.qq.com/s/tiqC28mCAcO6HaS_PnVA9w'
url = 'https://mp.weixin.qq.com/s/v-CyssD8nHyIFF8pGg3dvw'
header = {'User-Agent': ua.random}
html = requests.get(url, headers=header).content
soup = BeautifulSoup(html, 'html.parser')
media_content = soup.find('div', class_='rich_media_content')
imgs = media_content.find_all('img')
for i, img in enumerate(imgs):
    print(img.get('data-src'))
    img_content = requests.get(img.get('data-src'), headers=header, stream=True)
    img_content.raise_for_status()
    total_size = int(img_content.headers.get('content-length', 0))
    # print(img_content)
    print(total_size)
    with open(f'images/20250918/{i+1}.gif', 'wb') as writer:
        downloaded = 0
        for chunk in img_content.iter_content(chunk_size=1024):
            if chunk:
                writer.write(chunk)
                downloaded += len(chunk)
                # 显示下载进度
                if total_size > 0:
                    progress = (downloaded / total_size) * 100
                    print(f"\r下载进度: {progress:.1f}%", end='')
        print(f'{i+1}.gif下载完成')