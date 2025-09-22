#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:analysis_data.py
   @author:zl
   @time: 2025/9/5 8:42
   @software:PyCharm
   @desc:
"""
import pandas as pd

csv = pd.read_csv('Result_3.csv')
print(csv)
info = csv.groupby('jobname').size()

info.to_excel('Result_3.xlsx')