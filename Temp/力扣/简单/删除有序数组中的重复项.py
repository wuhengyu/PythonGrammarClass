# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 20:06
# @Author  : Walter
# @File    : 删除有序数组中的重复项.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按升序排列
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


print(Solution().removeDuplicates([1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7]))
