# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 19:14
# @Author  : Walter
# @File    : 最长公共前缀.py
# @License : (C)Copyright Walter
# @Desc    : 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
from typing import List


# 纵向扫描
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
