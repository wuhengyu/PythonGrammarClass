# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 17:52
# @Author  : Walter
# @File    : 线程使用.py
# @License : (C)Copyright Walter
# @Desc    :

# threading模块
# -*- coding:utf-8 -*-
# 线程使用的方式一
import threading
import time


# 需要多线程运行的函数
def fun(args):
    print("我是线程%s" % args)
    time.sleep(2)
    print("线程%s运行结束" % args)


# 创建线程
t1 = threading.Thread(target=fun, args=(1,))
t2 = threading.Thread(target=fun, args=(2,))
start_time = time.time()
t1.start()
t2.start()
end_time = time.time()
print("两个线程一共的运行时间为：", end_time - start_time)
print("主线程结束")

"""
运行结果：
我是线程1
我是线程2两个线程一共的运行时间为： 0.0010077953338623047
主线程结束

线程1运行结束
线程2运行结束
"""
