# -*- coding: utf-8 -*-
# Time    : 2023/3/3 23:13
# Author  : Walter
# File    : 调用super().run().py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, sleep_time):
        super().__init__(name=name)
        self.sleep_time = sleep_time

    def run(self):
        print(f"Initializing thread {self.name} with sleep time {self.sleep_time} seconds.")
        # super().run()
        print(f"Thread {self.name} finished initialization.")
        for i in range(5):
            print(f"Thread-{self.name}: {i}")
            time.sleep(self.sleep_time)


if __name__ == '__main__':
    t1 = MyThread(name="Thread 1", sleep_time=1)
    t2 = MyThread(name="Thread 2", sleep_time=2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All threads finished.")
