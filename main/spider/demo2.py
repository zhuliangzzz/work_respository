#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo2.py
   @author:zl
   @time: 2025/9/10 18:44
   @software:PyCharm
   @desc:
"""
# https://mp.weixin.qq.com/s/KBScuWqLXZBW1-BgZfcFzA?scene=1&click_id=5

import requests
from bs4 import BeautifulSoup
# 初始化用户代理池
from fake_useragent import UserAgent
ua = UserAgent(browsers=['Chrome'], os=['windows'])

# url = 'https://mp.weixin.qq.com/s/FhgPAPt_6mF3sSxPuGeWCQ'
# url = 'https://mp.weixin.qq.com/s/KbqgsQYPMfQ5pzETvF-fqg'
url = 'https://mp.weixin.qq.com/s/KBScuWqLXZBW1-BgZfcFzA?scene=1&click_id=5'
header = {'User-Agent': ua.random}
html = requests.get(url, headers=header).content
soup = BeautifulSoup(html, 'html.parser')
media_content = soup.find('div', class_='rich_media_content')
imgs = media_content.find_all('img')
for i, img in enumerate(imgs):
    print(img.get('data-src'))
    img_content = requests.get(img.get('data-src'), headers=header, stream=True).content
    with open(f'linedog/{i+1}.png', 'wb') as writer:
        writer.write(img_content)
