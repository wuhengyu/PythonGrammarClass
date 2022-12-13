# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
a = [1, 2, 3, 6]
b = [4, 5, 6]
zipped1 = zip(a, b)  # 打包为元组的列表, 元素个数与最短的列表一致
print(zipped1)  # <zip object at 0x000001E4C6773180>
print(list(zipped1))

aa = (1, 4, 5, 7, 8, 3)
bb = (4, 5, 7, 8, 9, 3)
zipped2 = zip(aa, bb)
print(list(zip(*zipped2)))  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
