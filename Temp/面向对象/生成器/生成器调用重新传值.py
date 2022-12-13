def shengYield(n):  # 定义方法 shengYield()
    while n > 0:  # 如果 n 大于 0 则开始循环
        rcv = yield n
        # 通过「rcv」来接收调用者传来的值
        n -= 1  # 生成以初始值不断递减的数字序列
        if rcv is not None:
            n = rcv


if __name__ == "__main__":  # 当直接运行模块时，
    # 以下代码块会运行，当导入模块时不运行
    sheng_yield = shengYield(2)
    # 开始遍历时从默认值 2 开始递减并输出
    print(sheng_yield.__next__())
    print(sheng_yield.__next__())
    print("传给生成器一个值，重新初始化生成器。")
    print(sheng_yield.send(11))  # 重新传一个值 11 给生成器
    print(sheng_yield.__next__())  # 得到一个从 11 开始递减的遍历
