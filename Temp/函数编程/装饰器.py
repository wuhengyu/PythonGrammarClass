# 这是装饰函数
def logger(func):
    def wrapper(*args, **kw):
        print('我准备开始计算：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('啊哈，我计算完啦。给自己加个鸡腿！！')

    return wrapper


@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))


add(200, 50)
