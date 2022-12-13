# xrange() 函数用法与 range 完全相同，所不同的是, 生成的不是一个数组，而是一个生成器。
# 因为 python3 中取消了 range 函数，而把 xrange 函数重命名为 range，所以现在直接用 range 函数即可。
# 在 Python 中，可迭代对象就是你可以迭代的任何东西，而迭代器就是实际迭代的东西
# 可以使用 iter 函数从任何可迭代对象中获取迭代器
# 一旦有了迭代器，可以用它做的唯一的事情就是获得它的下一个元素
# 如果没有更多的元素了， 则会抛出一个stop iteration exception
# 所有的迭代器都是可迭代对象，意思是你可以从一个迭代器中得到一个迭代器，因此你可以遍历一个迭代器
# 应该指出的是迭代器是有状态的，在循环遍历一次迭代器后，如果尝试再次循环，它将为空
# 在 Python 3 中，enumerate、zip、reversed和其他一些内置函数会返回迭代器
# 生成器（无论来自生成器函数还是生成器表达式）是一种创建迭代器的简单方法
# 经常说迭代器是惰性的一次性可迭代对象。 「惰性」是因为他们只循环计算项目，「单次使用是因为一旦从一个迭代器中「消费」了一个元素之后，这个元素就永远消失了
# Python 3 中的 range 对象（Python 2 中的 xrange）可以像任何其他可迭代对象一样循环使用
# 因为 range 是可迭代对象，所以可以从中得到一个迭代器<range_iterator object at 0x0000025230182B30>
# 但 range 对象本身不是迭代器，我们不能在 range 对象上调用 next
# range 对象本身不是迭代器,与迭代器不同的是，我们可以遍历一个 range 对象而不「消耗」它
# 可迭代对象， 使用iter内置函数可以获取迭代器的对象,可迭代的对象必须实现__iter__方法，但不能实现__next__方法
# 可迭代的对象和迭代器之间的关系是Python从可迭代对象中获取迭代器

diedaiqi = iter(range(6))
# print(diedaiqi) # <range_iterator object at 0x0000027F77D42B30>
# 使用迭代器完成此操作，则第二次循环时不会得到任何元素
print(tuple(diedaiqi))  # (0, 1, 2, 3, 4, 5)
print(tuple(diedaiqi))  # ()

# 可迭代对象具有__iter__ 方法，用于返回一个迭代器，或者定义了 getitem 方法，可以按 index 索引的对象
index = range(6)
print(index[0])

print(list(range(6)))
