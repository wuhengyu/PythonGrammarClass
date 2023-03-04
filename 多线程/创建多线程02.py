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
    # 继承了父类Thread，并重写了它的__init__方法来添加了一个新的参数name
    def __init__(self, name):
        # super(MyThread, self).__init__()
        # self.n = n

        # 或者
        # 调用父类Thread的构造方法，并将参数name传递给父类的构造方法来初始化线程对象的名称。
        super().__init__(name=name)

    def run(self):
        print("current task：", self.name)


if __name__ == "__main__":
    t1 = MyThread("thread 1")
    t2 = MyThread("thread 2")

    t1.start()
    t2.start()
