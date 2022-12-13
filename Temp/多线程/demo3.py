import threading


def demo3(x, y, thre=None):
    if thre:
        thre.join()
    for i in range(x, y):
        print("%s平方%s" % (threading.currentThread().getName(), i * i))


threading0 = threading.Thread(target=demo3, args=(1, 6))
threading1 = threading.Thread(target=demo3, args=(2, 8))
threading2 = threading.Thread(target=demo3, args=(3, 9, threading1))

threading0.setName('threading0')
threading1.setName('threading1')
threading2.setName('threading2')

threading0.start()
threading1.start()
threading2.start()

print(threading.activeCount())
