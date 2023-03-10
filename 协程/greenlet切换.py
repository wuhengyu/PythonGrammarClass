# -*- coding: utf-8 -*-
# Time    : 2023/3/10 18:30
# Author  : Walter
# File    : greenlet切换.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

# 真正的协程模块就是使用greenlet完成的切换
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)  # 2
    g2.switch('taibai')  # 3
    print('%s eat 2' % name)  # 6
    g2.switch()  # 7


def play(name):
    print('%s play 1' % name)  # 4
    g1.switch()  # 5
    print('%s play 2' % name)  # 8


g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('taibai')  # 可以在第一次switch时传入参数，以后都不需要  #1
