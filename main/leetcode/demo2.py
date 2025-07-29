#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo2.py
   @author:zl
   @time: 2025/7/29 14:37
   @software:PyCharm
   @desc:寻找两个正序数组的中位数
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine_list = nums1 + nums2
        combine_list.sort()
        if len(combine_list)%2:
            return combine_list[(len(combine_list))//2]
        else:
            return (combine_list[(len(combine_list) + 1)//2 -1] + combine_list[(len(combine_list) + 1)//2])/2


nums1 = [1,3]
nums2 = [2,4]
print(Solution().findMedianSortedArrays(nums1, nums2))