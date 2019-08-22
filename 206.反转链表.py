# coding=utf-8
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        当前节点node，当前节点的前1个节点pre_node，当前节点的后1个节点next_node
        每次先把next_node取出来(最后一个节点没有所以不用)，然后把node的next属性指向pre_node
        特殊处理：第1个节点的next属性指定为None

        执行用时 :28 ms, 在所有 Python 提交中击败了75.88%的用户
        内存消耗 :13.6 MB, 在所有 Python 提交中击败了44.44%的用户

        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
            return head
        pre_node = head
        node = head.next
        head.next = None  # 第一个节点反转后其next属性应为None
        while node.next is not None:  # 只要不是最后一个节点，就把其下一个节点取出来
            next_node = node.next  # 把其下一个节点取出来
            node.next = pre_node  # 反转
            pre_node = node  # 往后移
            node = next_node  # 往后移
        node.next = pre_node  # 最后一个节点在循环外反转
        return node


    def reverseList1(self, head):
        """
        官方解法，思路和上一个解法大同小异，重点是在第1个节点前构造一个虚拟节点
        """
        if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
            return head
        pre_node = None
        current_node = head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node
        return pre_node


if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    c = Solution()
    pointer = c.reverseList(n1)
    while pointer.next is not None:
        print pointer.val
        pointer = pointer.next
    print pointer.val
