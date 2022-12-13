import threading
import time


def func(n):
    while n > 0:
        print("当前线程数:", threading.activeCount())
        time.sleep(2)
        n -= 1


for x in range(5):
    t = threading.Thread(target=func, args=(5,))
    t.start()

print("主线程：", threading.current_thread().name)
