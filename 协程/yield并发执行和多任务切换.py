# -*- coding: utf-8 -*-
# Time    : 2023/3/10 12:19
# Author  : Walter
# File    : yield并发执行和多任务切换.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

# 基于yield并发执行，多任务之间来回切换，这就是个简单的协程的体现，但是他能够节省I/O时间吗？不能
import time


def consumer():
    '''任务1:接收数据,处理数据'''
    while True:
        x = yield
        time.sleep(1)  # 发现什么？只是进行了切换，但是并没有节省I/O时间
        print('处理了数据：', x)


def producer():
    '''任务2:生产数据'''
    g = consumer()
    next(g)  # 找到了consumer函数的yield位置
    for i in range(3):
        # for i in range(10000000):
        # 通过这个函数里面的send切换了另外一个任务，consumer循环到下一次yield，再执行producer的下一句print
        g.send(i)  # 给yield传值，然后再循环给下一个yield传值，并且多了切换的程序，比直接串行执行还多了一些步骤，导致执行效率反而更低了。
        print('发送了数据：', i)


start = time.time()
# 基于yield保存状态,实现两个任务直接来回切换,即并发的效果
# PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
producer()  # 我在当前线程中只执行了这个函数，但是通过这个函数里面的send切换了另外一个任务
stop = time.time()

# 串行执行的方式
# res=producer()
# consumer(res)
# stop=time.time()

print(stop - start)
