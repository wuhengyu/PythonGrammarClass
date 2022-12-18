# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:56
# @Author  : Walter
# @File    : 自定义序列.py
# @License : (C)Copyright Walter
# @Desc    :

class IntDic:
    def __init__(self):
        # 用于存储数据的字典
        self.__date = {}

    def __len__(self):
        return len(list(self.__date.values()))

    def __getitem__(self, key):
        # 如果在self.__changed中找到已经修改后的数据
        if key in self.__date:
            return self.__date[key]
        return None

    def __setitem__(self, key, value):
        # 判断value是否为整数
        if not isinstance(value, int):
            raise TypeError('必须是整数')
        # 修改现有 key 对应的 value 值，或者直接添加
        self.__date[key] = value

    def __delitem__(self, key):
        if key in self.__date: del self.__date[key]


dic = IntDic()
# 输出序列中元素的个数，调用 __len__() 方法
print(len(dic))
# 向序列中添加元素，调用 __setitem__() 方法
dic['a'] = 1
dic['b'] = 2

print(len(dic))
dic['a'] = 3
dic['c'] = 4
print(dic['a'])
# 删除指定元素，调用 __delitem__() 方法
del dic['a']
print(dic['a'])
print(len(dic))
