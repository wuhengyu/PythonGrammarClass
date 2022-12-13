# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:24
# @Author  : Walter
# @File    : 罗马数.py
# @License : (C)Copyright Walter
# @Desc    : 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
# 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。

class Solution:
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans


# 判断后面的数比前面的数大的话，改变符号ans -= value，小的话ans += value
# 如果下标大于或等于n-1的话，跳出false
# 小数在大数前面只有6种情况，大数在小数面前没有限制，i不满足时，最后一个数字一定是相加
# IV和IX
# XL和XC
# CD和CM

# 小数在前，相减，1000-500=500
print(Solution().romanToInt("DM"))
# 大数在前，相加,1000+500=1500
# print(Solution().romanToInt("MD"))
# -100+1000-10+100-1+10=999
# print(Solution().romanToInt("CMXCIX"))
