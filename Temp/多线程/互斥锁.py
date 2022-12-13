from threading import Thread, Lock


def work():
    global n
    lock.acquire()
    n -= 1
    print(n)
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()
    for x in l:
        x.join()
