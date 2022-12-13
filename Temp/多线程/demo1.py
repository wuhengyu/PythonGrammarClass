import threading


def demo1(x, y):
    for i in range(x, y):
        print("%s平方" % threading.currentThread(), i * i)


threading1 = threading.Thread(target=demo1, args=(2, 8))
threading2 = threading.Thread(target=demo1, args=(3, 9))
threading1.start()
threading2.start()
