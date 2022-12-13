# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:16
# @Author  : Walter
# @File    : 回文数2.py
# @License : (C)Copyright Walter
# @Desc    :

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


print(Solution().isPalindrome(2332))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(12))
