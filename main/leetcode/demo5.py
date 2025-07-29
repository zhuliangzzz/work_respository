#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo5.py
   @author:zl
   @time: 2025/7/29 15:13
   @software:PyCharm
   @desc:
   整数反转
"""
class Solution:
    def reverse(self, x: int) -> int:
        is_subtractive = True if x < 0 else False
        s = str(abs(x))
        if is_subtractive:
            return -1 * int(s[::-1])
        else:
            return int(s[::-1])


print(Solution().reverse(-234))