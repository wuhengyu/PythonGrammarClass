# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 19:14
# @Author  : Walter
# @File    : 最长公共前缀.py
# @License : (C)Copyright Walter
# @Desc    : 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
from typing import List


# 二分查找
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
