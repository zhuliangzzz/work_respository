#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo3.py
   @author:zl
   @time: 2025/7/23 11:39
   @software:PyCharm
   @desc:
"""
import matplotlib
matplotlib.use('TkAgg')  # 使用Tkinter作为后端
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2022', periods=1000))
ts = ts.cumsum()
# ts.plot()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"])
df.plot()
plt.title('Random Walk Time Series')  # 添加标题
plt.xlabel('Date')  # x轴标签
plt.ylabel('Cumulative Sum')  # y轴标签
plt.grid(True)  # 显示网格线
plt.show()
plt.legend(loc='best')