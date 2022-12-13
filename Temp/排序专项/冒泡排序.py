# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 19:24
# @Author  : Walter
# @File    : 冒泡排序.py
# @License : (C)Copyright Walter
# @Desc    :

def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),
