# 实例 1
list1 = [10, 11, 12, 13, 14, 15]
print([ele for ele in reversed(list1)])
print("列表生成式:", [ele + 1 for ele in list1])
# 实例 2
list2 = [10, 11, 12, 13, 14, 15]
list2.reverse()
print(list2)
# 实例 3
list3 = [10, 11, 12, 13, 14, 15]
new_list3 = list3[::-1]
print(new_list3)
