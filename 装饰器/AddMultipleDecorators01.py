# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 19:54
# @Author  : Walter
# @File    : AddMultipleDecorators01.py
# @License : (C)Copyright Walter
# @Desc    : 给一个函数添加两个装饰器

# 为函数添加一个统计运行时长的功能以及日志记录功能
import time

'''
执行顺序是:
1，第一步先执行how_much time函数的外部代码，
2，第二步执行mylog函数的外部代码;
3，第三步执行mylog的内部函数代码;
4，第四步执行how much time函数的内部函数代码
运行结果为:
how much time函数开始了mylog函数开始了
start
5秒结束了一共花费了5.012601613998413秒时间
end
'''


def how_much_time(func):
    print("how_much_time函数开始了")

    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start, ))

    return inner


def mylog(func):
    print("mylog函数开始了")

    def inner_1():
        print("start")
        func()
        print("end")

    return inner_1


@mylog
@how_much_time
# 等价于mylog(how_much_time(sleep_5s))
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5,))


if __name__ == '__main__':
    sleep_5s()
# how_much_time函数开始了
# mylog函数开始了
# start
# 5秒结束了
# 一共花费了5.012601613998413秒时间
# end
