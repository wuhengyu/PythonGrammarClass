def processs(string):
    print('Processing:', string)


# with open('diedai.txt') as f:
#     char = f.read(1)
#     while char:
#         processs(char)
#         char = f.read(1)


# with open('diedai.txt') as f:
#     while True:
#         char = f.read(1)
#         if not char:
#             break
#         processs(char)

# 使用read迭代字符
# with open('diedai.txt') as f:
#     for char in f.read():
#         processs(char)

# 使用readline迭代行
with open('diedai.txt') as f:
    for line in f.readline():
        processs(line)

# 使用readlines迭代全部行
# with open('diedai.txt') as f:
#     for line in f.readlines():
#         processs(line)
