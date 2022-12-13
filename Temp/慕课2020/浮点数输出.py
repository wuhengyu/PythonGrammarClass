str1 = r"tdtgdg\n"
str2 = "tdtgdg\n"
print(str1)
print(str2)

import time

timenum = time.time()
name = "wuhengyu"
for x in range(10000):
    print(x)
print(f'{name} in {time.time() - timenum:.2f}s')

# 格式化输出浮点数
print('{:.2f}'.format(0.2345356))
print('%.2f' % 0.3646)
# 四舍五入取整
print(round(0.345345, 2))
