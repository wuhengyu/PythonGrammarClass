# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:18
# @Author  : Walter
# @File    : 回文数3.py
# @License : (C)Copyright Walter
# @Desc    :

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if y == str(x):
                return True
            else:
                return False


print(Solution().isPalindrome(2332))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(12))
