#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:test.py
   @author:zl
   @time: 2025/7/17 14:25
   @software:PyCharm
   @desc:
"""
import os.path

# import base64
#
# # 加密
# def base64_encode(str):
#     encoded_bytes = base64.b64encode(str.encode('utf-8'))
#     encoded_str = encoded_bytes.decode('utf-8')
#     return encoded_str
#
# # 解密
# def base64_decode(encoded_str):
#     decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
#     decoded_str = decoded_bytes.decode('utf-8')
#     return decoded_str
#
# # 测试
# str = 'Hello World!'
#
# encoded_str = base64_encode(str)
# print(f'Encoded string: {encoded_str}')
#
# decoded_str = base64_decode('MTIzNDU=')
# print(f'Decoded string: {decoded_str}')
path = 'E:\project\main\zip\main.py.py'
print(os.path.splitext(path)[0])