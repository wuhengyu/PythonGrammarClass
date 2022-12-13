from itertools import *


def height_class(h):  # 定义方法 height_class()
    if h > 180:
        return "tall"  # 如果 h 大于 180 厘米则返回tall
    elif h < 160:
        return "short"
    # 如果 h 小于 160 厘米则返回short
    else:
        return "middle"


# 如果 h 是其他值则返回middle
# 下面定义一个列表 friends
friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
friends = sorted(friends, key=height_class)
# 使用方法 sorted()进行排序
# 下面开始遍历 groupby,将拥有相同函数结果的元素分到一个
# 新的循环器
for m, n in groupby(friends, key=height_class):
    print(m)
    print(list(n))
