#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo1.py
   @author:zl
   @time: 2025/7/29 14:38
   @software:PyCharm
   @desc:
   无重复字符的最长子串
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_ = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if len(set(s[i:j])) == len(s[i:j]):
                    list_.append(s[i:j])
        maxlenth = max([len(s) for s in list_])
        # return filter(lambda s: len(s) == maxlenth, list_).__next__()
        return maxlenth

s = 'pwwkew'
print(Solution().lengthOfLongestSubstring(s))