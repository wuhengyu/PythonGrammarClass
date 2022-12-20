# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 19:47
# @Author  : Walter
# @File    : PurePath模块.py
# @License : (C)Copyright Walter
# @Desc    :
from pathlib import *

# 创建PurePath，实际上使用PureWindowsPath
path = PurePath('http:', 'www.baidu.com', 'python')
print(path)

# 不传入任何参数，则等同于传入点‘.’（表示当前路径）作为参数
path = PurePath()
print(path)
path = PurePath('.')
print(path)

# 包含多个根路径，则只会有最后一个根路径及后面的子路径生效
path = PurePath('C://', 'D://', 'my_file.txt')
print(path)

# 重载各种比较运算符，多余同种风格的路径字符串来说，可以判断是否相等，也可以比较大小（实际上就是比较字符串的大小）
# Unix风格的路径区分大小写
print(PurePosixPath('C://my_file.txt') == PurePosixPath('c://my_file.txt'))
# Windows风格的路径不区分大小写
print(PureWindowsPath('C://my_file.txt') == PureWindowsPath('c://my_file.txt'))

# 使用斜杠（/）作为多个字符串之间的连接符
path = PurePosixPath('C://')
print(path / 'my_file.txt')

# 使用 str() 将 PurePath 对象转换成字符串
# Unix风格的路径区分大小写
path = PurePosixPath('C://', 'my_file.txt')
print(path)
print(str(path))
