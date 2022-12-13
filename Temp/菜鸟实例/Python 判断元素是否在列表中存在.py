# 实例 1
test_list = [1, 6, 3, 5, 3, 4]

print("查看 4 是否在列表中 ( 使用循环 ) : ")
for x in test_list:
    if x == 4:
        print("存在")
    # else:
    #     print("不存在")

print("查看 4 是否在列表中 ( 使用 in 关键字 ) : ")
if 5 in test_list:
    print("存在")
else:
    print("不存在")
