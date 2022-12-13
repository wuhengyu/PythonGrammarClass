# 首先将列表「list」构建成迭代器，然后使用 for 循环语句遍历迭代器中的数据
list = [1, 2, 3, 4]  # 创建列表「list」
it = iter(list)  # 创建迭代器对象
for x in it:  # 遍历迭代器中的数据
    print(x, end=" ")
