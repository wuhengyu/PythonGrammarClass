# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 16:33
# @Author  : Walter
# @File    : 整数反转2.py
# @License : (C)Copyright Walter
# @Desc    :
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        minus = False
        if x < 0:
            minus = True
            x = -x

        temp = 0
        while x > 0:
            temp = temp * 10 + x % 10
            x = x // 10
        if minus:
            temp = -temp

        if temp <= -pow(2, 31) or temp >= pow(2, 31) - 1:
            return 0
        return temp


print(Solution().reverse(6463847412))
print(Solution().reverse(7463847412))
