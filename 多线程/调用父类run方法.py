# -*- coding: utf-8 -*-
# Time    : 2023/3/2 16:04
# Author  : Walter
# File    : 调用父类run方法.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, sleep_time):
        # 调用父类Thread的构造方法，并将参数name传递给父类的构造方法来初始化线程对象的名称。
        # 避免在子类中重复实现父类的构造方法，我们可以使用super()函数来调用父类的构造方法，并传递必要的参数，以便父类的构造方法可以正确地执行
        super().__init__(name=name)
        self.sleep_time = sleep_time

    def run(self):
        print(f"Thread {self.name} started.")
        for i in range(5):
            print(f"Thread {self.name}: {i}")
            time.sleep(self.sleep_time)
            # run方法已经在Thread类中实现了，因此不应该再调用super().run()。
            # super().run()
        print(f"Thread {self.name} finished.")


if __name__ == '__main__':
    t1 = MyThread(name="Thread 1", sleep_time=1)
    t2 = MyThread(name="Thread 2", sleep_time=2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All threads finished.")
