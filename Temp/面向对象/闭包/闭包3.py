def majia(n):
    if (n == 1):
        print("流浪地球", end="")  # end=""表示不换行
        pingjia(n)
    else:
        print("疯狂的外星人", end="")


def pingjia(m):  # 闭包 函数里嵌套的函数就是闭包
    if (m == 1):
        print(" 好电影111")
    else:
        print(" 一般电影")


print("大年初一看电影：")
majia(1)  # cinema 实际就是pingjia
