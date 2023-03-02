# -*- coding: utf-8 -*-
# Time    : 2023/3/2 0:22
# Author  : Walter
# File    : 线程合并.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading


def count(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target=count, args=(100000,))
    t2 = threading.Thread(target=count, args=(100000,))
    t1.start()
    t2.start()
    # 将 t1 和 t2 加入到主线程中
    t1.join()
    t2.join()
