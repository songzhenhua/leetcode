# coding=utf-8
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        自己写的，战胜1%
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        listn = []
        while True:
            if head.next != None:
                listn.append(head)
                head = head.next
            else:
                listn.append(head)
                break
        if n == len(listn):
            if len(listn) == 1:
                temp = None
            else:
                temp = listn[-n].next
            listn.pop(0)
        elif n == 1:
            listn[-(n + 1)].next = None
        else:
            listn[-(n+1)].next = listn[-(n-1)]
        return temp

    def removeNthFromEnd1(self, head, n):
        """
        标准答案，一次遍历双指针法，过程详见question.png。战胜1%
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first_p = dummy
        second_p = dummy
        for i in range(n+1):
            first_p = first_p.next
        while first_p:
            first_p = first_p.next
            second_p = second_p.next
        second_p.next = second_p.next.next
        return dummy.next


if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(5)
    # n3 = ListNode(1)
    # n4 = ListNode(9)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4
    c = Solution()
    p = c.removeNthFromEnd1(n1, 1)
    print p.val