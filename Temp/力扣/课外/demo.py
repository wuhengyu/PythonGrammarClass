# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 21:07
# @Author  : Walter
# @File    : asyncCounter.py
# @License : (C)Copyright Walter
# @Desc    :
class Node(object):
    """创建单个结点类"""

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    """创建一个单链表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """获取链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add_fist(self, data):
        """在链表的头部添加元素"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_last(self, data):
        """在链表的尾部添加元素"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node


if __name__ == '__main__':
    lists = SingleLinkedList()
    lists.add_fist(2)
    lists.add_last(3)
    lists.add_last(4)
    print(lists.is_empty())
    print(lists.length())
