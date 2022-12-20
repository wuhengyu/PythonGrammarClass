# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 19:02
# @Author  : Walter
# @File    : fileinput模块.py
# @License : (C)Copyright Walter
# @Desc    :

'''
fileinput.input（files="filename1, filename2, ...", inplace=False, backup='', bufsize=0, mode='r', openhook=None）
files：多个文件的路径列表；
inplace：用于指定是否将标准输出的结果写回到文件，此参数默认值为 False；
backup：用于指定备份文件的扩展名；
bufsize：指定缓冲区的大小，默认为 0；
mode：打开文件的格式，默认为 r（只读格式）；
openhook：控制文件的打开方式，例如编码格式等。
'''

import fileinput

# 使用for循环遍历 fileinput 对象
for line in fileinput.input(files=('my_file.txt', 'file.txt'), encoding='utf-8'):
    # 输出读取到的内容
    print(line)
# 关闭文件流
fileinput.close()
