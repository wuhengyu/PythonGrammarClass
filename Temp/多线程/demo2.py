import threading


class Demo2(threading.Thread):
    def __init__(self, aa):
        super().__init__()
        self.aa = aa

    def run(self) -> None:
        for i in range(self.aa, self.aa + 5):
            print("%s平方%d" % (threading.currentThread(), i * i))


threading1 = Demo2(3)
threading2 = Demo2(2)
threading1.start()
threading2.start()
