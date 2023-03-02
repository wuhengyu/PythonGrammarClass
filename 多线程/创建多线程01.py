# -*- coding: utf-8 -*-
# Time    : 2023/3/2 0:19
# Author  : Walter
# File    : 创建多线程01.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading


# 创建多线程方法一：直接使用threading.Thread()
def run(n):
    print("current task：", n)


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("thread 1",))
    t2 = threading.Thread(target=run, args=("thread 2",))
    t1.start()
    t2.start()
