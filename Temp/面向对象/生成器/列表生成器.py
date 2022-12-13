# 一
info1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, index in enumerate(info1):
    info1[i] += 1
print(info1)
# 二
info2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = []
for index, i in enumerate(info2):
    a.append(i + 1)
print(a)
# 三
d = []
info3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = map(lambda x: x + 1, info3)
for i in b:
    d.append(i)
print(d)
# 四
c = [i + 2 for i in range(10)]
print(c)

# 列表生成式
lis = [x * x for x in range(10)]
print(lis)
# 生成器
generator_ex = (x * x for x in range(10))
print(generator_ex)
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
# print(next(generator_ex))
# 每次调用next(generaotr_ex)就计算出他的下一个元素的值，直到计算出最后一个元素，没有更多的元素时，抛出StopIteration的错误，
# 而且上面这样不断调用是一个不好的习惯，正确的方法是使用for循环，因为generator也是可迭代对象

print("------------------------------------------------------------")
# 生成器迭代
generator_ex = (x * x for x in range(10))
for i in generator_ex:
    print(i)
