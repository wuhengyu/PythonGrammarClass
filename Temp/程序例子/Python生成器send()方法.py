# 通过调用 next() 或者 __next__() 方法，可以实现从外界控制生成器的执行。除此之外，通过 send() 方法，还可以向生成器中传值
def foo():
    bar_a = yield "111111"
    bar_b = yield bar_a
    bar_c = yield bar_b
    yield bar_c


# 首先，构建生成器函数，并利用器创建生成器(对象)f
f = foo()
# 使用生成器 f 调用无参的 send() 函数，其功能和 next() 函数完全相同，因此开始执行生成器函数，
# 即执行到第一个 yield "111111" 语句，该语句会返回 "111111" 字符串，然后程序停止到此处(注意，此时还未执行对 bar_a 的赋值操作)。
# 下面开始使用生成器 f 调用有参的 send() 函数，首先它会将暂停的程序开启，同时还会将其参数“222222”赋值给当前 yield 语句的接收者，
# 也就是 bar_a 变量。程序一直执行完 yield bar_a 再次暂停，因此会输出“222222”。
print(f.send(None))
print(f.send(None))
# print(f.send("222222"))
# print(f.send("333333"))
# print(f.send("444444"))
