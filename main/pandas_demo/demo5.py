#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo4.py
   @author:zl
   @time: 2025/7/24 15:57
   @software:PyCharm
   @desc:
"""
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
print(frame)
print(frame.info())
# print(frame.info(memory_usage='deep'))
print(frame.memory_usage(index=False))
print(frame.memory_usage().sum())