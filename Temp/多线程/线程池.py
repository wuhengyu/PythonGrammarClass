import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print('运行 线程 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(int(random.random() * 3))
    end = time.time()
    print('线程 %s 运行 %0.2f 秒.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
