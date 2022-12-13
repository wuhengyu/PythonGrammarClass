import threading

num = 10  # 共享变量


def func():
    global num
    lock.acquire()  # 加锁
    num = num - 1
    lock.release()  # 解锁
    print(num)


threads = []
lock = threading.Lock()  # 生成全局锁
for x in range(10):
    t = threading.Thread(target=func)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
