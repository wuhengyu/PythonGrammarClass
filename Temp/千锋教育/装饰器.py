"""
第一步：调用cal_time
第二步：把被装饰的函数demo传递给fn
第三步：再次调用demo函数时，demo函数已经不是上面的demo
"""

import time


def cal_time(fn):
    print("我是外部函数")
    print("fn = {}".format(fn))

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("代码耗时:{:.3f}".format(end - start))

    return inner


@cal_time
def demo():
    y = 1
    for x in range(1, 100000):
        y += x
    print("累计总和:", y)


demo()
print("装饰后的demo = {}".format(demo))
