import time


def cal_time(fn):
    print("我是外部函数1")
    print("fn = {}".format(fn))

    def inner(x, *args, **kwargs):
        print("我是内部函数")
        start = time.time()
        fn(x, *args, **kwargs)
        end = time.time()
        print("代码耗时:{:.3f}".format(end - start))
        return fn, end - start

    print("我是外部函数2")
    return inner


@cal_time
def demo(x, *args, **kwargs):
    y = 1
    for x in range(1, x):
        y += x
    print("累计总和:", y)
    print("多个参数：", args, kwargs)


print("装饰后的demo = {}".format(demo))
m = demo(10000, "aaaa", "bbbb", "cccc", "dddd", "eeee", aa="1111", bb="2222", cc="3333")
print(m)
