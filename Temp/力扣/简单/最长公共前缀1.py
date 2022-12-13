# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 19:14
# @Author  : Walter
# @File    : 最长公共前缀.py
# @License : (C)Copyright Walter
# @Desc    : 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
from typing import List


# 横向扫描
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
