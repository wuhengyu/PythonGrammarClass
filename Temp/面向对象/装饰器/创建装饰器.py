# 在 Python 程序中，可以使用装饰器装饰函数。在使用装饰器装饰函数时，首先要定义一个装饰器，然后使用定义的装饰器来装饰这个函数

def zz(fun):  # 定义一个装饰器函数 zz()
    def wrapper(*args, **bian):
        # 定义一个包装器函数 wrapper()
        print("开始运行...")
        fun(*args, **bian)  # 使用被装饰函数
        print("运行结束！")

    return wrapper  # 返回包装器函数 wrapper()


@zz  # 装饰函数语句
def demo_decoration(x):  # 定义普通函数，它被装饰器装饰
    a = []  # 定义空列表 a
    for i in range(x):  # 遍历 x 的值
        a.append(i)  # 将 i 添加到列表末尾
    print(a)


@zz
def hello(name, age):  # 定义普通函数 hello()，它被装饰器装饰
    print("name:", name, "age:", age)
    print()


if __name__ == "__main__":
    demo_decoration(5)  # 调用被装饰器装饰的函数 demo_decoration()
    print()
    hello("hengyu", {"a": 5, "b": 6})  # 调用被装饰器装饰的函数 hello()
