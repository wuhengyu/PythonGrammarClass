# -*- coding: utf-8 -*-
# Time    : 2023/3/2 0:26
# Author  : Walter
# File    : 创建多进程02.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :


import time
from multiprocessing import Process


# 创建多进程方法2：继承Process来自定义进程类，重写run方法
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print('process name :' + str(self.name))
        time.sleep(1)


if __name__ == '__main__':
    for i in range(3):
        p = MyProcess(str(i))
        p.start()
        p.join()
