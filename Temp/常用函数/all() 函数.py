# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True。
# 如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


if all(range(1, 9)) is True:
    print("return True")
else:
    print("return False")

if all([1, 2, 3, 4, 0]) is True:
    print("return True")
else:
    print("return False")
