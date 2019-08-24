# coding=utf-8
"""
给定一个链表，判断链表中是否有环。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        哈希表：用Python的字典，将每个node存成key，如果1个node出现2次，即是有环。
        时间复杂度：O(n)；空间复杂度：O(n)
        :type head: ListNode
        :rtype: bool
        """
        dicta = {}
        while True:
            if head is None:
                return False
            dicta[head] = dicta.get(head, 0) + 1
            if dicta[head] > 1:
                return True
            head = head.next

    def hasCycle2(self, head):
        """
        双指针：两名运动员以不同的速度在环形赛道上跑步，终会相遇
        时间复杂度：O(n)；空间复杂度：O(1)
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while True:
            if slow == fast:
                return True
            # 快指针的下一个或下下一个是None则不是环，不用判断slow，其在fast后必不为None
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next


if __name__ == "__main__":
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(4)
    n4 = ListNode(2)
    n5 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3
    c = Solution()
    print c.hasCycle2(n1)
