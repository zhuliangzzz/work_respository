#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:basic_function2.py
   @author:zl
   @time: 2025/8/21 17:52
   @software:PyCharm
   @desc:
"""
import pandas as pd
import numpy as np

arr = np.random.randn(20)
print(arr)
print(sorted(arr))
print(pd.cut(arr, 4))
factor = pd.cut(arr, [-5, -1, 0, 1, 5])
print(factor)