# -*- coding: utf-8 -*-
# Time    : 2023/3/2 13:32
# Author  : Walter
# File    : 多线程同步01.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading


class Counter:
    def __init__(self):
        self.count = 0
        self.condition = threading.Condition()

    def increment(self):
        with self.condition:
            self.count += 1
            self.condition.notify()

    def wait_until(self, target):
        with self.condition:
            while self.count < target:
                self.condition.wait()


def worker(counter):
    print("Worker 1")
    counter.increment()
    print("Worker 2")
    counter.increment()
    print("Worker 3")
    counter.increment()


counter = Counter()
t1 = threading.Thread(target=worker, args=(counter,))
t2 = threading.Thread(target=worker, args=(counter,))
t1.start()
t2.start()
counter.wait_until(6)
print("Done")
