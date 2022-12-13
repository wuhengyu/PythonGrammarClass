# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# map(function, iterable, ...),可迭代对象
# Python 2.x 返回列表,Python 3.x 返回迭代器。

def square(x):
    return x * x


print(list(map(square, range(9))))

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
