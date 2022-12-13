# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 19:13
# @Author  : Walter
# @File    : 罗马数3.py
# @License : (C)Copyright Walter
# @Desc    :
class Solution:
    def romanToInt(self, s: str) -> int:
        arr = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans, prev = 0, 1000
        for c in s:
            num = arr[c]
            ans += num
            if prev < num:
                ans -= 2 * prev
            prev = num

        return ans


print(Solution().romanToInt("CMXCIX"))
