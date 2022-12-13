class Use:  # 定义迭代器类 Use
    def __init__(self, x=2, max=50):  # 定义构造方法
        self.__mul, self.__x = x, x
        # 初始化属性，x 的初始值是 2
        self.__max = max  # 初始化属性

    def __iter__(self):  # 定义迭代器协议方法
        return self  # 返回类的自身

    def __next__(self):  # 定义迭代器协议方法
        if self.__x and self.__x != 1:
            # 如果x的值不是1
            self.__mul *= self.__x  # 设置 mul 的值
            if self.__mul <= self.__max:
                # 如果 mul 的值小于等于预设的最大值 max
                return self.__mul  # 则返回 mul 值
            else:
                raise StopIteration  # 当超过参数 max 的值时会引发 StopIteration 异常
        else:
            raise StopIteration


if __name__ == '__main__':
    my = Use()  # 定义类 Use 的对象实例 my
    for i in my:  # 遍历对象实例 my
        print("迭代的数据元素为：", i)
