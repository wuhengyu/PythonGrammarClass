# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 18:22
# @Author  : Walter
# @File    : 二分查找2.py
# @License : (C)Copyright Walter
# @Desc    :

def BinarySearch(nums: list, x: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [2, 3, 4, 10, 40, 20, 25]
x = 25
result = BinarySearch(arr, x)

if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")
