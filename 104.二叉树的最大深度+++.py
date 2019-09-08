# coding=utf-8
"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度 3 。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        自己写的递归，DFS（深度优先搜索）策略
        时间复杂度为 O(N)；最好情况下（树是完全平衡的），树的高度是log(N)。因此空间复杂度是O(log(N))。
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = self.redepth(root, 1)
        return depth

    def redepth(self, node, deep):
        deepl, deepr = deep, deep
        if node.left:
            deepl = self.redepth(node.left, deep+1)
        if node.right:
            deepr = self.redepth(node.right, deep+1)
        deep = max(deepl, deepr)
        return deep

    def maxDepth1(self, root):
        """官方的递归，思路一样，代码更简洁"""
        if root:
            deepl = self.maxDepth1(root.left)
            deepr = self.maxDepth1(root.right)
            return max(deepl, deepr) + 1
        else:
            return 0

    def maxDepth2(self, root):
        """利用栈的概念，时间复杂度：O(N),空间复杂度：O(N)"""
        if root is None:
            return 0
        stack = [(root, 1)]
        deep = 0
        while stack:
            node, depth = stack.pop()
            deep = max(deep, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return deep


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = None, None
    n3.left, n3.right = n4, n5
    n4.left, n4.right = None, None
    n5.left, n5.right = None, None
    s = Solution()
    print s.maxDepth2(n1)
