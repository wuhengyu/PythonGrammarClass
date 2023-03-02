# -*- coding: utf-8 -*-
# Time    : 2023/3/2 13:27
# Author  : Walter
# File    : 生产者-消费者模型.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import random
import threading
import time


# 生产者-消费者模型使用了一个缓冲区 Buffer 来存储生产者生成的数据，消费者从中取出数据进行消费。
# 缓冲区的大小为 5，当缓冲区满时，生产者将等待缓冲区有空闲位置；当缓冲区为空时，消费者将等待缓冲区有数据可供消费。
# 在实现过程中，使用了 Lock 和 Condition 类来保证线程同步和互斥。
# 其中 Lock 用于对共享资源进行互斥访问，Condition 则用于线程之间的同步。
# 具体来说，not_full 条件变量用于等待缓冲区不满，not_empty 条件变量用于等待缓冲区不空。
# 生产者和消费者在对缓冲区进行操作时，需要先获取锁，然后使用对应的条件变量进行等待或通知。
# 这样可以确保生产者和消费者之间的互斥和同步，避免竞态条件和死锁等问题。


class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = []
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def put(self, value):
        with self.not_full:
            while len(self.buffer) == self.size:
                self.not_full.wait()
            self.buffer.append(value)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while len(self.buffer) == 0:
                self.not_empty.wait()
            value = self.buffer.pop(0)
            self.not_full.notify()
            return value


class ProducerThread(threading.Thread):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer

    def run(self):
        for i in range(10):
            value = random.randint(1, 100)
            self.buffer.put(value)
            print(f"Produced {value}")
            time.sleep(random.randint(1, 3))


class ConsumerThread(threading.Thread):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer

    def run(self):
        for i in range(10):
            value = self.buffer.get()
            print(f"Consumed {value}")
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    buffer = Buffer(5)
    producer_thread = ProducerThread(buffer)
    consumer_thread = ConsumerThread(buffer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()
