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
import numpy as np

# 创建示例数据
data = np.random.randint(0, 100, 20)
print("原始数据:", data)

# # 等宽分箱 - 指定边界
bins = [0, 25, 50, 75, 100]
result_cut = pd.cut(data, bins)
print("cut() 结果:", result_cut)
print("各区间的数量:")
print(result_cut.value_counts())

# 等频分箱
# result_qcut = pd.qcut(data, 4)  # 分成4个等频区间
# print("qcut() 结果:", result_qcut)
# print("各区间的数量:")
# print(result_qcut.value_counts())