# 区分大小写
a = "aAAAAAAAAAsmr3IIIIIIidd4bgs7Dlsf9eAF"
# a = a.lower()
b = {}
for i in a:
    b[i] = a.count(i)
print(b)

# 区分大小写
# 1.目标字符串转为列表
ss = 'abcacaFdS212dafaCCCCC'
ll = list(ss)
# 2.用一个列表记录总共多少种字符
new_ll = []
for i in ss:
    if i not in new_ll:
        new_ll.append(i)
# 3.用一个字典记录结果 ,  遍历列表 , 求count()
d = {}
for i in new_ll:
    d[i] = ll.count(i)
print(d)


# 区分大小写
def strcount(a):
    # 定义一个空字典
    b = {}
    # 求出字符串的长度
    c = len(a)
    i = 0
    while i < c:
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
        i += 1
    # 遍历字典
    for item in b.items():
        print(item)


# 区分大小写
def strcount1(a1):
    # 定义一个空字典
    b1 = {}
    # 求出字符串的长度
    a1 = list(a1)
    for i in a1:
        if i in b1:
            b1[i] += 1
        else:
            b1[i] = 1
    # 遍历字典
    for item1 in b1.items():
        print(item1)


if __name__ == '__main__':
    a = 'abcacaFdS212dafa'
    strcount(a)
    print("-------------------------------")
    a1 = '1122324235dfgdfhfghdfgdfhdfghgd'
    strcount1(a1)
