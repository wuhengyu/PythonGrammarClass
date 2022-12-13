import threading  # 导入模块 threading
import time  # 导入模块 time


class mt(threading.Thread):  # 定义继承于线程类的子类 mt
    def run(self):  # 定义重载函数 run
        global x  # 定义全局变量 x
        lock.acquire()  # 在操作变量 x 之前锁定资源
        for i in range(5):  # 遍历操作
            x += 10  # 设置变量 x 的值加 10
        time.sleep(1)  # 休眠 1s
        print(x)  # 输出 x 的值
        lock.release()  # 释放锁资源


x = 1  # 设置 x 的值为 0
lock = threading.RLock()  # 实例化可重入锁类


def main():
    thrs = []  # 初始化一个空列表
    for item in range(8):
        thrs.append(mt())  # 实例化线程类
    for item in thrs:
        item.start()  # 启动线程


if __name__ == '__main__':
    main()
