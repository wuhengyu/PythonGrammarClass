a = [1, 2, 3, 4, 5, 6]
print("列表翻转输出")
print(a[::-1])

print("列表翻转输出，间隔2个位置")
print(a[::-2])

print("从头开始，截止到-1，5的位置")
print(a[:-1])

print("从-1，5的位置开始，截止到全部")
print(a[-1:])

print("取第一个")
print(a[0])

print("所有数，每2个取一个,从1开始")
b = list(range(100))
print(b[1::2])

print("所有数，每5个取一个")
print(b[::5])

print("复制一个list")
print(b[:])

print("取前10个数")
print(b[0:10])
print(b[:10])

print("取后10个数")
print(b[-10:])
print(b[-10::])

print("取后20个数，截止到95位置，间隔2个位置")
print(b[-20:95:2])

print("前取20个数，从5位置开始，间隔2个位置")
print(b[5:20:2])

c = tuple(b)
print(c)
print("C:前取20个数，从5位置开始，间隔2个位置")
print(c[5:20:2])
