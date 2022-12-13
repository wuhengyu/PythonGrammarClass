import threading
import time

num = 10


def func():
    global num
    lock.acquire()
    time.sleep(2)
    num = num - 1
    lock.release()
    print(num)


threads = []
lock = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
for x in range(10):
    t = threading.Thread(target=func)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("主线程：", threading.current_thread().name)
