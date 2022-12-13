'''
Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
Queue 模块中的常用方法:
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''

import queue
from threading import Thread

exitflag = 0


# 构建形成类
class MyThread(Thread):

    def __init__(self, threadname, q) -> None:
        super().__init__()
        self.threadname = threadname
        self.q = q

    # 重写线程任务
    def run(self) -> None:
        # super().run()
        while not exitflag:
            # 退出条件
            if self.q.empty():
                break
            # 执行线程任务
            try:
                # 获取数据
                num = self.q.get()
                print("%s--------------------取出%d" % (self.threadname, num))

                # 此处必须添加队列任务结束，否则，程序将一直开启，
                self.q.task_done()
            except Exception as e:
                print(e)


def main():
    print("***********主线程开始***********")
    # 创建队列，并向队列中添加数据
    q = queue.Queue(80)
    for x in range(80):
        q.put(x)

    # 创建线程对象，执行从队列中取数据
    thread1 = MyThread("thread1", q)
    thread2 = MyThread("thread2", q)
    thread3 = MyThread("thread3", q)

    # 开启线程任务
    thread1.start()
    thread2.start()
    thread3.start()

    # 注意:在关闭子线程任务之后才能继续执行主线程任务

    # 结束子线程
    thread1.join()
    thread2.join()
    thread3.join()

    # 结束队列任务
    # q.join()

    print("***********主线程结束************")


if __name__ == '__main__':
    main()
