print("生成[1-10]")
print(list(range(1, 11)))

print("传统方法生成x * x")
a = []
for x in range(1, 11):
    a.append(x * x)
print(a)
print("列表生成式方法,筛选出仅偶数的平方")
b = [x * x for x in range(1, 11) if x % 2 == 0]
print(b)

print("两层循环")
c = [m + n for m in 'ABC' for n in 'XYZ']
print(c)

print("列出当前目录下的所有文件和目录名")
import os

print(os.listdir('.'))
print([d for d in os.listdir('.')])

print("多个变量同时迭代key和value")
d = {"a": 1, "b": 2, "c": 3}
for k, v in d.items():
    print(k, '=', v)

print("列表生成式两个变量来生成list")
e = {"a": 1, "b": 2, "c": 3}
f = {"a": "1", "b": "2", "c": "3"}
print([k + '=' + str(v) for k, v in e.items()])
print([k + '=' + v for k, v in f.items()])

print("把一个list中所有的字符串变成小写和大写")
g = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in g])
print([s.upper() for s in g])
