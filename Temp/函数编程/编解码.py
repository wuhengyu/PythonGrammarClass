"""
s1 = "哈哈哈哈"
# s1.encode("utf-8")
print(s1.encode("utf-8").decode("utf-8"))
"""

# f = open("byte.txt", encoding="gbk")
# s = f.read()
# print(s)
# f.close()

# f = open("byte.txt")
# s = f.read()
# print(s)
# f.close()

f = open("byte.txt", "rb")
s = f.read()
print(s)
f.close()

s_unicode = s.decode("gbk")
s_utf8 = s_unicode.encode("utf-8")
f = open("byte.txt", "wb")
f.write(s_utf8)
f.close()
