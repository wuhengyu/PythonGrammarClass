'''
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。
'''

import time
from threading import Thread, Lock


# 通过Thread类来重写父类方法创建多线程
class MyThread(Thread):

    def __init__(self, threadname, delay) -> None:
        super().__init__()
        self.threadname = threadname
        self.delay = delay

    # 重写run函数，在次函数中执行多线程任务
    def run(self) -> None:
        # super().run()
        print("%s开始" % self.threadname)
        # 添加线程锁
        threadlock.acquire()
        cont_thread(self.threadname)
        time.sleep(self.delay)
        # 释放线程锁
        threadlock.release()


# 一个线程循环5次
def cont_thread(threadname):
    print("_________%s" % threadname)
    for x in range(5):
        print("%d-----------%s" % (x, threadname))


if __name__ == '__main__':
    print("主线程开始了")
    starttime = time.time()

    # 创建线程锁
    threadlock = Lock()

    # 创建两个线程
    thread1 = MyThread("thread——1", 2)
    thread2 = MyThread("thread——2", 4)

    # 线程启动
    thread1.start()
    thread2.start()

    # 运行至程序结束所有线程任务
    thread1.join()
    thread2.join()
    endtime = time.time()

    # 记录主线程运行的时间
    print(endtime - starttime)
    print("主线程结束了")
