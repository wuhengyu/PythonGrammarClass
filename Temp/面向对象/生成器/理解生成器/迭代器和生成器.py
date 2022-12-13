# power这时已经不再是一个函数了，它是一个生成器
# power在调用过程中并没有执行print，但是在用for进行遍历时它执行了print
# 生成器是用函数中yield语句来创建的。迭代器的创建首先跟函数无关，可以用iter([1,2])来创建
# 生成器里面的过程只有在被next()调用或者for循环调用时，里面的过程才会被执行
# 如同上面的例子只是单纯调用add这个对象时，add里面的过程没有被执行，迭代器同样可以被for和next调用但是由于没有其他过程，
# 在被调用时只会返回值，不会有其他动作
def power(values):
    for value in values:
        print("powing %s" % value)
        yield value


def add(values):
    # for循环调用时，power里面的过程才会被执行
    for value in values:
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


elements = [1, 4, 7, 9, 12, 19]
print(power(elements))  # 输出生成器<generator object power at 0x000001B3DB0FB900>，没有执行print
add(power(elements))
for i in add(power(elements)):
    print(i)
