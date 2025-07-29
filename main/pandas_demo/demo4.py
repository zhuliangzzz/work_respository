#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo4.py
   @author:zl
   @time: 2025/7/23 11:57
   @software:PyCharm
   @desc:
"""
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
# print(frame)
# frame.to_csv('foo.csv')
# print(pd.read_csv('foo.csv'))

# frame.to_parquet('foo.parquet')
# frame.to_excel('foo.xlsx', sheet_name='Sheet1')
print(pd.read_excel('foo.xlsx', sheet_name='Sheet1', index_col=None, names=list('abcdef'),na_values=['NA']))
print(pd.read_excel('foo.xlsx', sheet_name='Sheet1', index_col=False, names=list('abcdef'),na_values=['NA']))