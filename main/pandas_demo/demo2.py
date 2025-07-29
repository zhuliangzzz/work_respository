#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo3.py
   @author:zl
   @time: 2025/7/23 9:56
   @software:PyCharm
   @desc:
"""
import numpy as np
import pandas as pd

# pivot table
df = pd.DataFrame({
    "A": ["one", "one", "two", "three"] * 3,
    "B": ["A", "B", "C"] * 4,
    "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
    "D": np.random.randn(12),
    "E": np.random.randn(12)
})
print(df)
print(pd.pivot_table(df, values='D', index=["A", "B"], columns=["C"]))
rng = pd.date_range("1/1/2012", periods=100, freq="s")
print(rng)

rng = pd.date_range("1/1/2025", periods=5)
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print(ts_utc.tz_convert('US/Eastern'))
print(rng + pd.offsets.BusinessDay(5))

df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
})
print(df)
df['grade'] = df["raw_grade"].astype("category")
print(df['grade'])

new_categories = ['very good', 'good', 'very bad']
df['grade'] = df['grade'].cat.rename_categories(new_categories)
print(df['grade'])

df['grade'] = df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])
print(df['grade'])

print(df.sort_values(by='grade'))
print(df.groupby("grade", observed=False).size())