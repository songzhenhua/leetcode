# coding=utf-8
"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]

示例 1:
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

说明:
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        从链表里删除一个节点 node 的最常见方法是修改之前节点的 next 指针，使其指向之后的节点。但我们无法访问之前的节点。
        所以我们必须将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点。
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    c = Solution()
    c.deleteNode(n3)
    print n1.next.val
    print n2.next.val

