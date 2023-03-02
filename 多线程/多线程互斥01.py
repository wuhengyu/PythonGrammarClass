# -*- coding: utf-8 -*-
# Time    : 2023/3/2 13:34
# Author  : Walter
# File    : 多线程互斥01.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    : 互斥在多线程编程中的常见实现方式是锁（Lock），它可以让线程独占某个共享资源，避免多个线程同时访问该资源导致的竞态条件和数据不一致等问题。

import threading


# Counter 类表示一个计数器，它有一个 increment 方法用于将计数器加一，另外还有一个 decrement 方法用于将计数器减一。
# 在这两个方法中，首先使用 with 语句获取锁，然后对计数器进行加一或减一的操作，最后自动释放锁。
# 由于只有一个线程可以获取锁，因此可以保证在多个线程之间进行互斥访问。
# worker 函数表示一个工作线程，它会分别调用 Counter 的 increment 和 decrement 方法对计数器进行加一和减一。
# 在主线程中，首先创建两个工作线程 t1 和 t2，然后分别调用它们的 start 方法启动线程，最后调用它们的 join 方法等待线程结束。
# 由于 Counter 中的锁实现了多线程之间的互斥访问，因此可以保证在多个线程之间对计数器进行安全的加减操作，最后输出的结果应该为 0。

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

    def decrement(self):
        with self.lock:
            self.count -= 1


def worker(counter):
    for i in range(100000):
        counter.increment()
    for i in range(100000):
        counter.decrement()


counter = Counter()
t1 = threading.Thread(target=worker, args=(counter,))
t2 = threading.Thread(target=worker, args=(counter,))
t1.start()
t2.start()
t1.join()
t2.join()
print(counter.count)
