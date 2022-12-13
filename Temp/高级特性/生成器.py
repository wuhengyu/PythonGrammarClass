# 在Python中，这种一边循环一边计算的机制，称为生成器
# 列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素
# 不必创建完整的list，从而节省大量的空间

print("a是一个list,可以直接打印出list的每一个元素")
a = [x * x for x in range(10)]
print("b是一个generator生成器,通过next()函数获得generator的下一个返回值")
b = (x * x for x in range(10))
print(a)
print(
    "generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误")
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
for x in b:
    print(x, end=" ")

print("")
print("通过`yield`来创建生成器")


def func():
    for i in range(10):
        yield i


f = func()
print(f)
print(f.__next__())
print(f.__next__())

print("通过列表来创建生成器")
print([i for i in range(10)])
g = (x * x for x in range(10))
print(g)
print(g.__next__())
print(next(g))
