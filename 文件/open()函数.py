# -*- coding: utf-8 -*-
# @Time    : 2022/12/19 21:54
# @Author  : Walter
# @File    : open()函数.py
# @License : (C)Copyright Walter
# @Desc    :

'''
file：表示要创建的文件对象。
file_name：要创建或打开文件的文件名称，该名称要用引号（单引号或双引号都可以）括起来。需要注意的是，如果要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可；否则，此参数需要指定打开文件所在的完整路径。
mode：可选参数，用于指定文件的打开模式。可选的打开模式如表 1 所示。如果不写，则默认以只读（r）模式打开文件。
buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区（本节后续会详细介绍）。
encoding：手动设定打开文件时所使用的编码格式，不同平台的 ecoding 参数值也不同，以 Windows 为例，其默认为 cp936（实际上就是 GBK 编码）。
'''

keys = [11, 22, 33, 4, 5, 6, 7, 8, 9]
for key in keys:
    with open('a.txt', 'a', encoding="utf-8") as f:
        f.write("Python教程{}\n".format(key))
        f.close()
