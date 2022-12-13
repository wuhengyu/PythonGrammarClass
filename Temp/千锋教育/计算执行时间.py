import time

time1 = time.time()
x = 1
for i in range(1, 100000):
    x += i
time2 = time.time()
totalTime = time2 - time1
print('代码运行时间: {}'.format(round(totalTime, 2)))
