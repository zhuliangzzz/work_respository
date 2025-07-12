#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo1.py
   @author:zl
   @time: 2025/7/2 16:14
   @software:PyCharm
   @desc:
"""
import numpy as np
import pandas as pd

print(pd.__version__)
series = pd.Series([1, 3, 5, np.nan, 6, 8])
print(series)
dates = pd.date_range('20250101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)
df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp('20200101'),
    "C": pd.Series(1, index=list(range(4)), dtype='float32'),
    "D": np.array([3] * 4, dtype='int32'),
    "E": pd.Categorical(['test', 'train', 'test', 'train']),
    "F": 'foo',

})
print(df2)
print(df2.dtypes)
print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.to_numpy())
print(df2.to_numpy())
print(df.describe())
print(df.T)
print(df.sort_index(axis=0, ascending=False))
print(df.sort_values(by='B'))
# getitem
# 按标签选择
print(df)
print(df['A'])
print(df[0:3])
print(df['2025-01-02':'2025-01-05'])
print(df.loc[dates[0]])
print(df.loc[:, ['A', 'B']])
print(df.loc['2025-01-02':'2025-01-04', ['A', 'B']])
print(df.loc[dates[0], 'A'])
print(df.at[dates[0], 'A'])
# 按位置选择
print(df)
print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iloc[:, 1:3])
# 访问标量
print(df.iloc[1, 1])
# 布尔索引
print(df[df['A'] > 0])
print(df[df > 0])
df2 = df.copy()
df2['E'] = ["one", "one", "two", "three", "four", "three"]
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20250102', periods=6))
print(s1)
df['F'] = s1
print(df)
df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 0
print(df)
df.loc[:, 'D'] = np.array([5] * len(df))
print('df', df)
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print(df1.dropna(how="any"))
print(df1.fillna(5))
print(pd.isna(df1))
print(df.mean())
print(df.mean(axis=1))
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
print(df.sub(s, axis=0))