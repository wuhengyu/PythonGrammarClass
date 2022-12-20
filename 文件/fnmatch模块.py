# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 21:28
# @Author  : Walter
# @File    : fnmatch模块.py
# @License : (C)Copyright Walter
# @Desc    :
'''
*：可匹配任意个任意字符。
？：可匹配一个任意字符。
[字符序列]：可匹配中括号里字符序列中的任意字符。该字符序列也支持中画线表示法。比如 [a-c] 可代表 a、b 和 c 字符中任意一个。
[!字符序列]：可匹配不在中括号里字符序列中的任意字符。
'''

import fnmatch

# filter()
# 对 names 列表进行过滤，返回 names 列表中匹配 pattern 的文件名组成的子集合。
print(fnmatch.filter(['dlsf', 'ewro.txt', 'te.py', 'youe.py'], '*.txt'))

# fnmatch()
# 判断 filename 文件名，是否和指定 pattern 字符串匹配
for file in ['word.doc', 'index.py', 'my_file.txt']:
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)

# fnmatchcase()
# 和 fnmatch() 函数功能大致相同，只是该函数区分大小写。
print([addr for addr in ['word.doc', 'index.py', 'my_file.txt', 'a.TXT'] if fnmatch.fnmatchcase(addr, '*.txt')])

# translate()
# 将一个 UNIX shell 风格的 pattern 字符串，转换为正则表达式
print(fnmatch.translate('a*b.txt'))
