# 给定一个 元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
def search(nums, target):
    le = len(nums)
    l, r = 0, le - 1
    while l <= r:
        mid = (l + r) // 2  # 取整除 - 返回商的整数部分（向下取整）
        if nums[mid] == target:
            while nums[mid - 1] == nums[mid] and mid != 0:
                mid -= 1
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


nums = [1, 3, 4, 5, 6, 7, 8, 8, 9]
target = 3
print(search(nums, target))
