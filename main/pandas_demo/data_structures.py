#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:pd_structures.py
   @author:zl
   @time: 2025/7/26 10:09
   @software:PyCharm
   @desc:
"""
import pandas as pd

import numpy as np

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.iloc[0])
print(s.iloc[:3])
print(s[s > s.median()])
print(s.iloc[[4, 3, 1]])
print(np.exp(s))
print(s.dtype)
print(s.array)
# series is dict-like
print(s['a'])
s['e'] = 12
print(s)
print(s.get('f', np.nan))
#
print(s + s)
print(s * 2)
print(np.exp(s))
print(s.iloc[1:] + s.iloc[:-1])
# name attributes
s = pd.Series(np.random.randn(5), name='something')
print(s)
print(s.name)
s2 = s.rename('different')
print(s2)
#
d = {
    'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)
print(pd.DataFrame(d, index=['d', 'b', 'a']))
print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))
print(df.index)
print(df.columns)
#
d = {
    'one': [1., 2., 3., 4.],
    'two': [4., 3., 2., 1.]
}
print(pd.DataFrame(d))
print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))

#
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'S10')])
print(data)
data[:] = [(1, 2.0, 'hello'), (2, 3.0, 'world')]
print(pd.DataFrame(data))
print(pd.DataFrame(data, index=['first', 'second']))
print(pd.DataFrame(data, index=['first', 'second'], columns=['C', 'B', 'A']))

df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
print(df)
del df['two']
df.pop('three')
print(df)
df['foo'] = 'bar'
print(df)
df['one_func'] = df['one'][:2]
print(df)
df.insert(1, "bar", df['one'])
print(df)

iris = pd.DataFrame({
    'SepalLength': [5.1, 4.9, 4.7],
    'SepalWidth': [3.5, 3.0, 3.2],
    'PetalLength': [3.5, 3.0, 3.2],
    'PetalWidth': [3.5, 3.0, 3.2],
})
iris = iris.assign(sepal_ratio=lambda x: x['SepalLength'] / x['SepalWidth'])
print(iris)
print(df)
print(df.loc[['a', 'c']])
print(df.iloc[:, 1:3])
df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])
print(df + df2)
print(df - df.iloc[0])
df1 = pd.DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]}, dtype=bool)
df2 = pd.DataFrame({"a": [0, 1, 1], "b": [1, 1, 0]}, dtype=bool)
print(df1 & df2)
print(df1 | df2)
print(df1 ^ df2)
print(-df1)

ser1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser2 = pd.Series([1, 3, 5], index=['b', 'a', 'c'])
print(ser1)
print(ser2)
print(np.remainder(ser1, ser2))
ser3 = pd.Series([2, 4, 6], index=['b', 'c', 'd'])
print(np.mod(ser1, ser3))

#
ser = pd.Series([1, 2, 3])
idx = pd.Index([4, 5, 6])
print(np.maximum(ser, idx))
