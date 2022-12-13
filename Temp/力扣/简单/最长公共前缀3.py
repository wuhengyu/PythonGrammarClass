# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 19:14
# @Author  : Walter
# @File    : 最长公共前缀.py
# @License : (C)Copyright Walter
# @Desc    : 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
from typing import List


# 分治
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
