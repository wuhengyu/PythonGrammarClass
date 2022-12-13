import queue  # 导入模块 queue
import random  # 导入模块 random

q = queue.PriorityQueue()  # 级别越低越先出队列


class Node:  # 定义类 Node
    def __init__(self, x):  # 构造函数
        self.x = x  # 属性初始化

    def __lt__(self, other):  # 内置函数
        return other.x > self.x

    def __str__(self):  # 内置函数
        return '{}'.format(self.x)


a = [Node(int(random.uniform(0, 10))) for i in range(10)]  # 生成 10 个随机数字
print(a)
for i in a:  # 遍历列表
    print(i, end='')  # 转出遍历数字
    q.put(i)  # 调用队列对象的 put()方法在队尾插入一项
print('')
while q.qsize():  # 返回队列的大小
    print(q.get(), end='')  # 按序转出列表中数字
