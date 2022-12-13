# for循环中操作的对象是生成器中的yield生成的值
# 生成器是迭代器，会生成传给yield关键字的表达式的值。
# 不管有没有return语句，生成器函数都不会抛出StopIteration异常，而是在生成全部值之后直接退出。
def gen():
    print("start")
    yield "Jack"
    print("continue")
    yield "Dennis"
    print("end")


for i in gen():
    print("Hello ", i)
