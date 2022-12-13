import threading


def func(n):  # 定义每个线程要运行的函数
    while n > 0:
        print("当前线程数:", threading.activeCount())
        n -= 1


for x in range(5):
    t = threading.Thread(target=func, args=(2,))  # 生成一个线程实例,生成实例后 并不会启动,需要使用start命令
    t.start()  # 启动线程
