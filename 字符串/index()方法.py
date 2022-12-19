# -*- coding: utf-8 -*-
# @Time    : 2022/12/19 12:14
# @Author  : Walter
# @File    : index()方法.py
# @License : (C)Copyright Walter
# @Desc    : 当指定的字符串不存在时，index() 方法会抛出异常。

'''
str：表示原字符串；
sub：表示要检索的子字符串；
start：表示检索开始的起始位置，如果不指定，默认从头开始检索；
end：表示检索的结束位置，如果不指定，默认一直检索到结尾。
'''

str = "www.baidu.com"
print(str.index('.'))
print(str.index('baidu'))
# 右边
print(str.rindex('.'))
