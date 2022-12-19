# -*- coding: utf-8 -*-
# @Time    : 2022/12/19 12:17
# @Author  : Walter
# @File    : find()方法.py
# @License : (C)Copyright Walter
# @Desc    : 如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。

'''
str：表示原字符串；
sub：表示要检索的目标字符串；
start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。
'''

str = "www.baidu.com"
print(str.find('.'))
print(str.find('baidu'))
# 右边
print(str.rfind('.'))
