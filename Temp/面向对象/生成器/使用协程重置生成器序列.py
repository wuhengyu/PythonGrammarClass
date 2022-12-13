# 简单的生产者与消费者编程模型的实现过程
# 消费者模型实际是一个生成器
# 生产者模型实际是xie()方法
# 生产者模型函数中每个循环模拟发送一个任务给消费者模型（生成器），而生成器可以调用相关函数来处理任务
# 通过 yield 语句的「停止」特性来完成这一任务的
# 程序在运行时，每次的发送任务都是通过调用生成器函数 send()实现的，收到任务的生成器会执行相关的函数调用并完成子任务
def xie():
    print("等待接收处理任务")
    while True:
        # 每个循环模拟发送一个任务给消费者模型(生成器)
        data = (yield)
        print("收到任务:", data)


def producer():  # 方法 producer()代表消费者模型
    c = xie()  # 调用函数 xie()来处理任务
    c.__next__()  # yield停止运行，下一次调用执行后面
    for i in range(3):  # 遍历 3 个任务
        print("发送一个任务, 任务%d" % i)
        c.send("任务:%d" % i)  # 发送任务


if __name__ == "__main__":
    producer()
