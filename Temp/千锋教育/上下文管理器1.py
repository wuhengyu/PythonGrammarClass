'''
with语句实际是个上下文管理器，with语句后的对象都会有_enter_()和_exit_()方法，
在进入到上下文时，会自动调用_enter_()方法，程序正常执行完成，或者出现异常中断的时候，都会调用
_exit_()方法

with语句后面的结果对象，需要重写_enter_()和_exit_()方法
'''


class Demo(object):
    def __enter__(self):
        print("调用了__enter__方法")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("调用了__exit__方法")


def create_obj():
    # return Demo()
    x = Demo()
    return x


# 变量d不是create_obj的返回结果
# 它是创建对象x调用__enter__之后的返回结果
# d = create_obj().__enter__()
with create_obj() as d:
    print(d)
