from multiprocessing import Process


def loop():
    while True:
        pass


if __name__ == '__main__':

    for i in range(8):
        t = Process(target=loop)
        t.start()

    while True:
        pass
