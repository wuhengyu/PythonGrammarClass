import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [
    (1963309, 2265973), (1879675, 2493670), (2030677, 3814172),
    (1551645, 2229620), (1988912, 4736670), (2198964, 7876293)]

if __name__ == '__main__':
    # 不使用多线程和多进程
    start = time.time()
    results0 = list(map(gcd, numbers))
    print(results0)
    end = time.time()
    print('未使用--timestamp:{:.3f} second'.format(end - start))

    # 使用多线程
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=3)
    results1 = list(pool.map(gcd, numbers))
    print(results1)
    end = time.time()
    print('使用多线程--timestamp:{:.3f} second'.format(end - start))

    # 使用多进程
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=3)
    results2 = list(pool.map(gcd, numbers))
    print(results2)
    end = time.time()
    print('使用多进程程--timestamp:{:.3f} second'.format(end - start))
