# -*- coding: utf-8 -*-
# Time    : 2023/3/3 21:01
# Author  : Walter
# File    : asyncCounter.py
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
        print(f"Thread {self.name} started.")
        time.sleep(self.sleep_time)
        super().run()
        print(f"Thread {self.name} finished.")


if __name__ == '__main__':
    t1 = MyThread(name="Thread 1", sleep_time=2)
    t2 = MyThread(name="Thread 2", sleep_time=4)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All threads finished.")
