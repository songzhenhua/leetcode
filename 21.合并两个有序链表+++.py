# coding=utf-8
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        题目给的不完整，应该注明是从小到大的2个有序链接，如果是从大到小，则更复杂一点。
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 先定位新链接的第1个节点，head保留到最后返回，new表示新的整合链表
        if l1.val < l2.val:
            head = l1
            new = l1
            l1 = l1.next
        else:
            head = l2
            new = l2
            l2 = l2.next
        # 循环对比并整合链表
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        # 某个链表走完时，将另一个链表剩余部分接在最后
        if l1 is None:
            new.next = l2
        else:
            new.next = l1
        return head


if __name__ == "__main__":
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = None
    n3.next = n4
    n4.next = None
    c = Solution()
    p = c.mergeTwoLists(n1, n3)
    while p.next is not None:
        print p.val
        p = p.next
    print p.val
