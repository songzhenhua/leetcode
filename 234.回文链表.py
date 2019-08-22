# coding=utf-8
"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome1(self, head):
        """
        将链表的值放在list里，再对比。空间复杂度不符合O(1)
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l2 = list(reversed(l))
        if l==l2:
            return True
        return False

    def isPalindrome2(self, head):
        """
        大神方法：用快慢指针2分链表，反转前半链表，再对比前、后半链表是否一致
        重点：   慢指针每次移动1位，快指针每次移动2位，可2分链表
        该方法空间复杂度符合O(1)，但速度还没有方法1快
        """
        if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
            return True
        slow = head
        fast = head.next
        pre_node = None
        while fast and fast.next:  # 快指针及快指针后节点不为空
            next_node = slow.next
            slow.next = pre_node
            pre_node = slow
            slow = next_node  # 前4行反转并让慢指针每次移动1位
            fast = fast.next.next  # 快指针每次移动2位
        # 2分后，将慢指针移到前半链表开头，需要根据链表单双位分2种情况
        if fast:
            fast = slow.next  # 2分后，将快指针移到后半链表开头
            slow.next = pre_node
        else:
            fast = slow.next  # 2分后，将快指针移到后半链表开头
            slow = pre_node
        # 遍历前、后半链表每个节点是否一致
        while fast:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next
        return True


if __name__ == "__main__":
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(4)
    n4 = ListNode(2)
    # n5 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    # n4.next = n5
    c = Solution()
    print c.isPalindrome1(n1)
