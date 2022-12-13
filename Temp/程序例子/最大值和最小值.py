# 列表遍历值打印
a = [3, 2, 8]
for it in a:
    print(it, end=" ")

print("")

# 列表遍历索引打印
for i in range(len(a)):
    print(i + 1, end=" ")

print("")

# 字典遍历key，value 方法一
b = {"a": "1", "b": "2", "c": "3"}
for x in b.items():
    print(x, end=" ")

print("")

# 字典遍历key
for x in b:
    print(x, end=" ")

print("")

# 字典遍历key，value 方法二
b = {"a": "1", "b": "2", "c": "3"}
for x, y in b.items():
    print(x, y, end=" ")

print("")

# 最大值和最小值
c = [3, 5, 7, 9, 2, 6]
max = c[0]
min = c[0]
for x in c:
    if max < x:
        max = x
    elif min > x:
        min = x

print("最大值：", max)
print("最小值：", min)
