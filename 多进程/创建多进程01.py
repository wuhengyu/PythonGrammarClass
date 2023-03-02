# -*- coding: utf-8 -*-
# Time    : 2023/3/2 0:25
# Author  : Walter
# File    : 创建多进程01.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

from multiprocessing import Process


# 创建多进程方法1：直接使用Process
def show(name):
    print("Process name is " + name)


if __name__ == "__main__":
    proc = Process(target=show, args=('subprocess',))
    proc.start()
    proc.join()
