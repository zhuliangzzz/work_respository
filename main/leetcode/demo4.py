#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo4.py
   @author:zl
   @time: 2025/7/29 15:11
   @software:PyCharm
   @desc:
   Z 字形变换
   将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

    P   A   H   N
    A P L S I I G
    Y   I   R
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

    请你实现这个将字符串进行指定行数变换的函数：

    string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # 创建行列表，每行初始化为空字符串
        rows = [''] * numRows
        current_row = 0
        going_down = False  # 方向标志，初始设为False，因为第一步要向下走

        for char in s:
            # 将当前字符添加到对应行
            rows[current_row] += char

            # 当到达顶部或底部时，改变方向
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # 根据方向更新行号
            current_row += 1 if going_down else -1

        # 连接所有行
        return ''.join(rows)