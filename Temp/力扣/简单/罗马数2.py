# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 17:30
# @Author  : Walter
# @File    : 罗马数2.py
# @License : (C)Copyright Walter
# @Desc    :

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        i, res = 0, 0
        while i < len(s) - 1:
            if dct[s[i]] < dct[s[i + 1]]:
                res -= dct[s[i]]
            else:
                res += dct[s[i]]
            i += 1
        return res + dct[s[-1]]


# 小数在大数前面只有6种情况，大数在小数面前没有限制，i不满足时，最后一个数字一定是相加
# IV和IX
# XL和XC
# CD和CM

print(Solution().romanToInt("CDCM"))
# -100+1000-10+100-1+10=999
# print(Solution().romanToInt("CMXCIX"))
