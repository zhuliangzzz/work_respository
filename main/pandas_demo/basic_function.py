#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:basic_function.py
   @author:zl
   @time: 2025/7/29 16:42
   @software:PyCharm
   @desc:
"""
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)
print(df)
s = pd.Series(np.arange(10))
print(s)
div, rem = np.divmod(s, 3)
print(div, rem)
idx = pd.Index(np.arange(10))
print(idx)
div, rem = np.divmod(idx, 3)
print(div, rem)
print(divmod(idx, 3))

df2 = df.copy()
df2.loc['a', 'three'] = 1
print(df2)
print(df + df2)
print(df.add(df2, fill_value=0))

print(df.gt(df2))
print(df2.ne(df))
print((df > 0).all())
print((df > 0).any())
print((df > 0).any().any())
print(df.empty)

print(pd.DataFrame(columns=list("ABC")).empty)
print(df + df == df * 2)
print((df + df).equals(df * 2))

df1 = pd.DataFrame({'col': ['foo', 0, np.nan]})
df2 = pd.DataFrame({'col': [np.nan, 0, 'foo']}, index=[2, 1, 0])
print(df1.equals(df2))
print(df1.equals(df2.sort_index()))
print(pd.Series(['foo', 'bar', 'baz']) == 'foo')
print(pd.Index(['foo', 'bar', 'baz']) == 'foo')
print(pd.Series(['foo', 'bar', 'baz']) == (pd.Index(['foo', 'bar', 'qux'])))

df1 = pd.DataFrame(
    {"A": [1.0, np.nan, 3.0, 5.0, np.nan], "B": [np.nan, 2.0, 3.0, np.nan, 6.0]}
)
df2 = pd.DataFrame(
    {
        "A": [5.0, 2.0, 4.0, np.nan, 3.0, 7.0],
        "B": [np.nan, np.nan, 3.0, 4.0, 6.0, 8.0],
    }
)
print(df1.combine_first(df2))


def combiner(x, y):
    return np.where(pd.isna(x), y, x)


print(df1.combine(df2, combiner))

print(df)
print(df.mean(0))
print(df.mean(1))
print(df.sum(0, skipna=False))
print(df.sum(1, skipna=True))

ts_stand = (df - df.mean()) / df.std()
print(ts_stand.std())
print(df.cumsum())
print(np.mean(df['one']))
print(np.mean(df['one'].to_numpy()))

series = pd.Series(np.random.randn(500))
series[20:500] = np.nan
series[10:20] = 5
print(series)
print(series.unique())

series = pd.Series(np.random.randn(1000))
series[::2] = np.nan
print(series.describe())
print(series.describe(percentiles=[0.05, 0.25, 0.75, 0.95]))

s = pd.Series(["a", "a", "b", "b", "a", "a", np.nan, "c", "d", "a"])
print(s.describe())
frame = pd.DataFrame({"a": ["Yes", "Yes", "No", "No"], "b": range(4)})
print(frame.describe())
print(frame.describe(include=['object']))
print(frame.describe(include=['number']))
print(frame.describe(include='all'))

s1 = pd.Series(np.random.randn(5))
print(s1)
print(s1.idxmin(), s1.idxmax())
df1 = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
print(df1)
print(df1.idxmin(axis=0))
print(df1.idxmax(axis=1))

data = np.random.randint(0,7, size=50)
print(data)
print(pd.Series(data).value_counts())

data = {"a": [1, 2, 3, 4], "b": ["x", "x", "y", "y"]}
print(data)
print(pd.DataFrame(data).value_counts())

s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
print(s5.mode())

df5 = pd.DataFrame(
    {
        "A": np.random.randint(0, 7, size=50),
        "B": np.random.randint(-10, 15, size=50),
    }
)
print(df5.mode())


data = {
    'Product': ['Apple', 'Banana', 'Apple', np.nan, 'Apple', 'Banana', 'Orange'],
    'Sales': [100, 150, 100, 200, 100, 150, 300],
    'Region': ['North', 'North', 'South', 'South', 'North', 'East', 'East']
}

df = pd.DataFrame(data)
print(df)
print(df.mode())
# 计算每一行的众数
df_row_mode = df.mode(axis=1)
print(df_row_mode)