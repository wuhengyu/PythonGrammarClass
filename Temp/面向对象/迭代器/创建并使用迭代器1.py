tuple = (1, 2, 3, 4)  # 创建元组「list」
tp = iter(tuple)  # 创建迭代器对象
for x in tp:  # 遍历迭代器中的数据
    print(x, end=" ")
