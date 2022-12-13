# 生成器函数：也是用def定义的，利用关键字yield一次性返回一个结果，阻塞，重新开始
# 生成器表达式：返回一个对象，这个对象只有在需要的时候才产生结果


# 消费者
def consumer(name):
    print("%s 准备学习啦!" % name)
    while True:
        lesson = yield
        print("开始%s了,%s老师来讲课了!" % (lesson + 1, name))


# 生产者
def producer():
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print("同学们开始上课了!")
    for i in range(10):
        print("到了两个同学!")
        c1.send(i)
        c2.send(i)


producer()
