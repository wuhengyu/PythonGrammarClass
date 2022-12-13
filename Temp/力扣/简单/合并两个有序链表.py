# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 22:40
# @Author  : Walter
# @File    : 合并两个有序链表.py
# @License : (C)Copyright Walter
# @Desc    :将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例：
# 123
# 134
# 112344
'''
要求：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
'''


class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# 方法一：递归
'''
我们直接将以上递归过程建模，同时需要考虑边界情况。
如果 l1 或者 l2 一开始就是空链表 ，那么没有任何操作需要合并，所以我们只需要返回非空链表。
否则，我们要判断 l1 和 l2 哪一个链表的头节点的值更小，然后递归地决定下一个添加到结果里的节点。如果两个链表有一个为空，递归结束。
'''


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head


# 方法二：迭代
'''
我们可以用迭代的方法来实现上述算法。当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，
当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

首先，我们设定一个哨兵节点 prehead ，这可以在最后让我们比较容易地返回合并后的链表。我们维护一个 prev 指针，我们需要做的是调整它的 next 指针。
然后，我们重复以下过程，直到 l1 或者 l2 指向了 null ：如果 l1 当前节点的值小于等于 l2 ，
我们就把 l1 当前的节点接在 prev 节点的后面同时将 l1 指针往后移一位。
否则，我们对 l2 做同样的操作。不管我们将哪一个元素接在了后面，我们都需要把 prev 向后移一位。
在循环终止的时候， l1 和 l2 至多有一个是非空的。由于输入的两个链表都是有序的，所以不管哪个链表是非空的，
它包含的所有元素都比前面已经合并链表中的所有元素都要大。这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表即可。
'''


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next


# 创建链表
def build_link(nums):
    li = cur = ListNode()
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    return li.next


nums1 = [1, 2, 4, 5, 8]
nums2 = [1, 3, 6]
l1 = build_link(nums1)
l2 = build_link(nums2)
# res = Solution1().mergeTwoLists(l1, l2)
res = Solution2().mergeTwoLists(l1, l2)
# 打印
while res:
    print(res.val, end=' ')
    res = res.next
print()

# 思路
# 1.先特殊后一般（先考虑为空的情况直接返回）
# 2.始终找两个链表中最小的那个（考虑到这个采用递归的思想解决问题，每次找最小的过程是一样的）
# 【1.如果l1的值比l2小，把l1的下一个和l2重给这个方法递归，把返回值给l1的next】
# 【1.如果l1的值比l2大，把l1和l2的下一个值重给这个方法递归，把返回值给l2的next】
