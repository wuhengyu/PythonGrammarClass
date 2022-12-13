class Counter:  # 定义类 Counter
    def __init__(self, x=0):  # 定义构造方法
        self.x = x  # 初始化属性 x


counter = Counter()  # 实例化类 Counter


def used_iter():  # 定义方法 used_iter()
    counter.x += 2  # 修改实例属性的值，加 2
    return counter.x  # 返回实例属性 x 的值


for i in iter(used_iter, 2000):  # 迭代遍历方法 iter()产生的迭代器
    print("当前遍历的数值：", i)
