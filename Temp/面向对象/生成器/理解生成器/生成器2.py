# 列表生成器
# 方法一（简单）：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
# for index,i in enumerate(info):
#     print(i+1)
#     b.append(i+1)
# print(b)
for index, i in enumerate(info):
    info[index] += 1
print(info)

# 方法二（一般）：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
a = map(lambda x: x + 1, info)
print(a)
for i in a:
    print(i, end=" ")

a1 = map(lambda x: x + 1, list(range(1, 100)))
for i in a1:
    print(i, end=" ")

# 方法三（高级）：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i + 1 for i in range(10)]
print(a, end=" ")

# 简单生成器1
# 可以通过next（）函数获得generator的下一个返回值
# generator保存的是算法，每次调用next(generaotr_ex)就计算出他的下一个元素的值，直到计算出最后一个元素，没有更多的元素时，抛出StopIteration的错误，而且上面这样不断调用是一个不好的习惯，正确的方法是使用for循环，因为generator也是可迭代对象
generator_ex = (x * x for x in range(10))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))

print("-----------------------------------------")

# 简单生成器2
generator_ex1 = (x * x for x in range(10))
for i in generator_ex1:
    print(i)
