#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo.py
   @author:zl
   @time: 2025/4/28 17:01
   @software:PyCharm
   @desc:
"""
# import io

import requests
import bs4
from fake_useragent import UserAgent
session = requests.session()
data = {
    'word': '朱亮',
    'fonts': 'zql.ttf',
    'size': 60,
    'fontcolor': '#000000',
}
url = 'https://www.uustv.com/'
useragent = UserAgent().chrome
post = session.post(url, data, headers={
    'User-Agent': useragent,
    'Referer':url
})
print(post.text)
soup = bs4.BeautifulSoup(post.text, 'html.parser')
img_ = soup.find('div', class_='tu').img.attrs.get('src')
print(img_)
# response = session.get(url + img_, stream=True,headers={"Cache-Control": "no-cache"})
print(url + img_)
gif_response = session.get(url + img_, headers={
    'User-Agent': useragent,
    'Referer': url
})
# 检查响应状态和内容类型
print("GET状态码:", gif_response.status_code)
print("Content-Type:", gif_response.headers.get('Content-Type'))  # 应为 image/gif
with open('res.gif', 'wb') as w:
    w.write(gif_response.content)
