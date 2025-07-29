#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo2.py
   @author:zl
   @time: 2025/7/11 15:05
   @software:PyCharm
   @desc:
"""
import pandas as pd
filename = r'E:\sh_script\test\tmp\incam密码编辑\\user_info.xlsx'
data = pd.read_excel(filename, dtype={'工号': 'Int64'})
print(data)
print(data.iloc[:10, [0,1]])
# print(data[data])