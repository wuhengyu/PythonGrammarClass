# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 16:53
# @Author  : Walter
# @File    : 迭代器02.py
# @License : (C)Copyright Walter
# @Desc    :

# 可迭代对象就是含有__iter__()的对象，调用__iter__()对象方法返回一个迭代器对象。
# 迭代器对象就是含有__iter__()和__next__()方法的对象
# 迭代器对象调用__next__()方法得到下一个值，不用索引取值
# 迭代器对象调用__iter__()方法得到迭代器本身
# 设计的原因是为了for循环取值的统一，转换成__iter__()迭代器对象
# for x in 可迭代对象或者迭代器对象.__iter__():
#     print(x)
# 迭代器也是可迭代对象，因为含有__iter__()


aa = (1, 2, 3, 4, 5, 6, 7)
# aa.__iter__()

bb = {1, 2, 3, 4}
# bb.__iter__()

cc = [1, 2, 3, 4, 5]
# cc.__iter__()

dd = {"key": 1, "value": 2}
# dd.__iter__()

with open("test.txt", "r+", encoding='utf-8') as ee:
    print(ee.read())
    # ee.__iter__()

# 调用__iter__方法获取迭代器
# <dict_keyiterator object at 0x102646200>
res = dd.__iter__()
print(res)

# print(next(res))
# print(res.__next__())

# 不依赖索引迭代取值，重新运行__iter__()会产生新的迭代器，重新取值
while True:
    try:
        print(res.__next__())
    except StopIteration:
        print("StopIteration，程序报错了")
        break

