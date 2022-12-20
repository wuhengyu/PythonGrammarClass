# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 18:11
# @Author  : Walter
# @File    : seek()函数.py
# @License : (C)Copyright Walter
# @Desc    :

# 当 offset 值非 0 时，要求文件必须要以二进制格式打开，否则会抛出 io.UnsupportedOperation 错误
# 0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。
# seek(5, 1) ，表示文件指针向后移动，移动至距离当前位置5个字符处。

f = open('a.txt', 'rb')
# 判断文件指针的位置
print(f.tell())
# 读取一个字节，文件指针自动后移1个数据
print(f.read(1))
print(f.tell())
# 将文件指针从文件开头，向后移动到 5 个字符的位置
f.seek(5)
print(f.tell())
print(f.read(1))
# 将文件指针从当前位置，向后移动到 5 个字符的位置
f.seek(5, 1)
print(f.tell())
print(f.read(1))
# 将文件指针从文件结尾，向前移动到距离 2 个字符的位置
f.seek(-1, 2)
print(f.tell())
print(f.read(1))
