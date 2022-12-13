# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 1:19
# @Author  : Walter
# @File    : 搜索插入位置.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
思路：不断用二分法逼近查找第一个大于等于 \textit{target}target 的下标
'''
from typing import List


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left = 0
#         right = n - 1
#         ans = n
#         while left <= right:
##             mid = ((right - left) >> 1) + left
#             mid = (left + right) // 2
#             if target <= nums[mid]:
#                 ans = mid
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return ans

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


nums1 = [1, 3, 5, 6, 8, 11, 23]
target1 = 23
print(Solution().searchInsert(nums1, target1))

nums2 = [1, 3, 5, 6, 8]
target2 = 9
print(Solution().searchInsert(nums2, target2))
