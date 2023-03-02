# -*- coding: utf-8 -*-
# Time    : 2023/3/2 0:20
# Author  : Walter
# File    : 创建多线程02.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

# 创建多线程方法二：继承threading.Thread来自定义线程类，重写run方法

import threading


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.n = n

    def run(self):
        print("current task：", self.n)


if __name__ == "__main__":
    t1 = MyThread("thread 1")
    t2 = MyThread("thread 2")

    t1.start()
    t2.start()
