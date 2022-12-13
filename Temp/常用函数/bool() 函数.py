# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
# bool 是 int 的子类。

print(bool())  # False
print(bool(""))  # False
print(bool("0"))  # True
print(bool(0))  # False
print(bool(1))  # True
print(issubclass(bool, int))  # True, bool 是 int 子类
