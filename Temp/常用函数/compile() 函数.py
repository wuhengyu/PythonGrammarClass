# compile() 函数将一个字符串编译为字节代码。
# eval - 如果源是单个表达式
# exec - 如果源是语句块
# single - 如果源是单个交互式语句
# exec() 函数接受大量代码块，这与 eval() 函数仅接受单个表达式不同。

str1 = "3 * 4 + 5"
a = compile(str1, '', 'eval')  # 编译为字节代码对象
print(a)
print(eval(a))

str2 = "for i in range(0,10): print(i)"
c = compile(str2, '', 'exec')  # 编译为字节代码对象
print(c)
print(exec(c))  # exec 返回值永远为 None
