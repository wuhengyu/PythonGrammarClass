# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 14:09
# @Author  : Walter
# @File    : 转换生成器.py
# @License : (C)Copyright Walter
# @Desc    :
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
        print('Done!')


# Create the generator, notice no output appears
c = countdown(3)
print(c)
# <generator object countdown at 0x1006a0af0>

# Run to first yield and emit a value
next(c)
# Starting to count from 3

# Run to the next yield 2
next(c)

# Run to next yield 1
next(c)

# Run to next yield (iteration stops) 0
next(c)
# Done!
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# StopIteration
