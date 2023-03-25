# -*- coding: utf-8 -*-
# Time    : 2023/3/19 22:07
# Author  : Walter
# File    : 生成器函数1.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import itertools

# 1. count(): 从 10 开始不停地生成数字，每次增加 2，生成十个数字
counter1 = itertools.count(10, 2)
for i in range(10):
    print(next(counter1))
print()

# 2. groupby(): 按照奇偶性对一个列表进行分组
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
groups = itertools.groupby(lst, lambda x: x % 2 == 0)  # 分组条件为奇偶性
# <class 'itertools.groupby'>
# print(type(groups))
for key, group in groups:
    print(key, list(group))
print()

# 3. chain(): 将三个列表组合成一个迭代器
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst3 = [4.5, 5.6, 6.7]
chained = itertools.chain(lst1, lst2, lst3)
print(list(chained))
print()

# 4. zip_longest(): 将多个迭代器组合起来，用 None 填充缺失元素，直到最长的那个迭代器元素用完
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
numbers = [1, 2, 3, 4]
# 输出同字典推导式
print(dict(zip(letters, numbers)))
together = itertools.zip_longest(letters, numbers)
for letter, number in together:
    print(letter, number)
    # 字典推导式，讲两个列表转换为字典
    print({letters[i]: numbers[i] for i in range(len(numbers))})
print()

# 5. islice(): 切取一个迭代器的一部分元素，生成一个迭代器
squares = (x * x for x in range(10))
# print(squares.__next__())
# print(squares.__next__())
# print(squares.__next__())
sliced = itertools.islice(squares, 2, 3, 2)  # itertools.islice(iterable, start, stop[, step])
print(list(sliced))
# 如果只传递一个参数，如 islice('ABCDEFG', 2)，则默认情况下，该参数被解释为 stop 参数，而 start 参数默认为 0，step 参数默认为 1
print(list(itertools.islice('ABCDEFG', 2)))
print()

# 6. product(): 对两个元素进行笛卡尔积，返回一个迭代器
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
product = itertools.product(lst1, lst2)
print(list(product))


