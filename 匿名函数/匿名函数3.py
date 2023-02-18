# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 11:56
# @Author  : Walter
# @File    : 匿名函数3.py
# @License : (C)Copyright Walter
# @Desc    :

aa = ['康师傅', '白象', '今麦郎', '统一']

# 列表表达式
new_aa = [name+'_老坛酸菜' for name in aa]
print(new_aa)

# 生成器表达式
new_aa = (name+'_老坛酸菜' for name in aa)
print(new_aa)
# print(new_aa.__next__())

# map(函数，可迭代对象)
res = map(lambda name: name+'_老坛酸菜', aa)
# res是一个生成器
# print(res)
# print(res.__next__())
print(list(res))