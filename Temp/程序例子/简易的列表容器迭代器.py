# 自定义实现一个迭代器，则类中必须实现如下 2 个方法：
# __next__(self)：返回容器的下一个元素。
# __iter__(self)：该方法返回一个迭代器（iterator）。

class listDemo:
    def __init__(self):
        self.__date = []
        self.__step = 0

    def __next__(self):
        if self.__step <= 0:
            raise StopIteration
        self.__step -= 1
        # 返回下一个元素
        return self.__date[self.__step]

    def __iter__(self):
        # 实例对象本身就是迭代器对象，因此直接返回 self 即可
        return self

    # 添加元素
    def __setitem__(self, key, value):
        self.__date.insert(key, value)
        self.__step += 1


mylist = listDemo()
mylist[0] = 1
mylist[1] = 2
for i in mylist:
    print(i)
