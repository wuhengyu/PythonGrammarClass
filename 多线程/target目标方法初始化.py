# -*- coding: utf-8 -*-
# Time    : 2023/3/4 0:01
# Author  : Walter
# File    : target目标方法初始化.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, sleep_time):
        # name是线程的名称，target是线程要执行的目标方法，这里将目标方法设为子类的run方法。
        # 这样，在调用start方法启动线程时，父类会调用子类的run方法作为线程的执行逻辑。

        # 如果不使用target参数初始化，run()方法仍然会成为线程的执行目标方法。
        # 在这种情况下，线程会在start()方法被调用时自动执行run()方法。
        super().__init__(name=name, target=self.run)
        self.sleep_time = sleep_time

    def run(self):
        print(f"Initializing thread {self.name} with sleep time {self.sleep_time} seconds.")
        super().run()
        print(f"Thread {self.name} finished initialization.")
        for i in range(5):
            print(f"Thread {self.name}: {i}")
            time.sleep(self.sleep_time)


if __name__ == '__main__':
    t1 = MyThread(name="Thread 1", sleep_time=1)
    t2 = MyThread(name="Thread 2", sleep_time=2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All threads finished.")
