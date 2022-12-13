# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 17:34
# @Author  : Walter
# @File    : 有效的括号.py
# @License : (C)Copyright Walter
# @Desc    :给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


print(Solution().isValid('[([])]'))
print(Solution().isValid('[([])'))

# 首先遍历括号字符串，把左括号存入栈中，如果栈顶和下一个待入栈的括号相对比，相等的时候pop出栈栈顶的括号
