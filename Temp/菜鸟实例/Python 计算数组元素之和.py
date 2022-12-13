arr1 = [1, 2, 3, 4, 5]
# 实例1
arr_sum1 = 0
for x in arr1:
    arr_sum1 += x
print(arr_sum1)
print(sum(arr1))

# 实例2
from functools import reduce

arr2 = [1, 2, 3, 4, 5]
arr_sum2 = 0
print(reduce(lambda x, y: x + y, arr2))
