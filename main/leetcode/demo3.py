#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo3.py
   @author:zl
   @time: 2025/7/29 14:41
   @software:PyCharm
   @desc:
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_ = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i:j] == s[i:j][::-1]:
                    list_.append(s[i:j])
        if list_:
            maxlenth = max([len(s) for s in list_])
            return filter(lambda s: len(s) == maxlenth, list_).__next__()
        else:
            return None

s = 'babad'
print(Solution().longestPalindrome(s))