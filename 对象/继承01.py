# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 22:42
# @Author  : Walter
# @File    : 继承01.py
# @License : (C)Copyright Walter
# @Desc    :

# 继承：创建新类的方式，通过继承创建的类称之为子类，被继承的类称之为父类或者基类

# 默认继承object，写上去为了兼容python2
class Parent1(object):
    aa = 10
    pass

class Parent2(object):
    pass


class Child1(Parent1): # 单继承
    pass

class Child2(Parent1, Parent2): # 多继承
    pass

# 查看父类
print(Child1.__bases__)
print(Child2.__bases__)

# 在python2中，有新式类和经典类的区分
# 新式类：继承了object类的子类，以及继承了这个类的子子孙孙类
# 经典类：没有继承了object类的子类，以及继承了这个类的子子孙孙类

print(Parent1.__bases__)
print(Parent2.__bases__)

# 继承就是遗传,子类会遗传父类的属性
print(Child1.aa)