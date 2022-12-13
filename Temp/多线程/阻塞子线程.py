import threading
import time


def func(n):
    while n > 0:
        print("当前线程数:", threading.activeCount())
        time.sleep(2)
        n -= 1


threads = []  # 运行的线程列表
for x in range(5):
    t = threading.Thread(target=func, args=(2,))
    threads.append(t)  # 将子线程追加到列表
    t.start()

for t in threads:
    # join的原理就是依次检验线程池中的线程是否结束，没有结束就阻塞直到线程结束，如果结束则跳转执行下一个线程的join函数
    # 参数timeout为线程的阻塞时间，如timeout = 1就是罩着这个线程2s以后，就不管他了，继续执行下面的代码
    t.join(timeout=1)

print("主线程：", threading.current_thread().name)
