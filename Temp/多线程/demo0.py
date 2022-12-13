import _thread
import time


def newThread(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print('%s:%s' % (threadName, time.strftime("%Y-%m-%d %H:%M:%S")))
        count += 1


# _thread.start_new_thread(newThread, ("线程1", 2))
# _thread.start_new_thread(newThread, ("线程2", 3))

try:
    _thread.start_new_thread(newThread, ('Thread-1', 2))  # 创建第 1 个线程
    _thread.start_new_thread(newThread, ('Thread-2', 1))  # 创建第 2 个线程
except:
    print('Error: 无法启动线程')  # 抛出异常
while 1:
    pass
