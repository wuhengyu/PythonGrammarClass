# -*- coding: utf-8 -*-
# @Time    : 2022/12/19 12:19
# @Author  : Walter
# @File    : count()方法.py
# @License : (C)Copyright Walter
# @Desc    : 检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。
'''
str：表示原字符串；
sub：表示要检索的字符串；
start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。
'''

str = "www.baidu.com"
print(str.count('.'))
print(str.count('baidu', 1, -3))
