# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。元素除了是 0、空、FALSE 外都算 TRUE。
# 如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


if any(range(0, 9)) is True:
    print("return True")
else:
    print("return False")

if any([1, 2, 3, 4, 0]) is True:
    print("return True")
else:
    print("return False")
