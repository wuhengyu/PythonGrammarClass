# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 22:45
# @Author  : Walter
# @File    : 移除元素.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != val:
                # nums[left] = nums[right]
                left += 1
            right += 1
        return left


nums = [3, 2, 2, 3, 3, 4, 5]
val = 3
print(Solution().removeElement(nums, val))
