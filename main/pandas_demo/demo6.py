#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo6.py
   @author:zl
   @time: 2025/7/24 18:01
   @software:PyCharm
   @desc:
"""
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
print(s.iloc[3])
print(s.iloc[:3])
print(s.median())
print(s[s > s.median()])
print(s.iloc[[4,3,1]])
print(np.exp(s))
print(s.dtype)
print(s.array)
print(s.to_numpy())