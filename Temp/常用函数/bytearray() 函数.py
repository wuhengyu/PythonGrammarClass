# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
# 语法class bytearray([source[, encoding[, errors]]])

# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。

# 可选的source参数可用于以几种不同的方式初始化数组：
# 如果它是一个字符串，则还必须提供encoding（或可选的错误）参数；byteArray()函数然后使用str.encode()方法将字符串转换为字节。即按照指定的 encoding 将字符串转换为字节序列。
# 如果是整数，则数组将具有该大小，并将使用空字节初始化。即则返回一个长度为 source 的初始化数组。
# 如果是符合缓冲区接口的对象，则将使用该对象的只读缓冲区来初始化字节数组。即被用于初始化 bytearray。
# 如果是iterable，则它必须是0<=x<256范围内的整数的iterable，这些整数用作数组的初始内容。即元素必须为0<=x<256中的整数
# 如果没有参数，将创建大小为0的数组。即默认初始化数组为0个元素。

print(bytearray())
print(bytearray([1, 2, 3, 4]))
print(bytearray('wuhengyu', 'utf-8'))
print((bytearray("中国", 'gbk')))
print((bytearray("中国", 'utf-8')))
