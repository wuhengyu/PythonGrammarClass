# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 1:08
# @Author  : Walter
# @File    : 实现 strStr().py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。
0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack, needle))
