# coding=utf-8
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        递归：深度优先搜索（先序遍历），战胜88.65%
        时间复杂度：O(N)；空间复杂度：O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def re_level(level, root, result):
            # 如果结果列表长度不大于层深，需要加一层空列表
            if len(result) <= level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                re_level(level+1, root.left, result)
            if root.right:
                re_level(level+1, root.right, result)
            return result

        if not root:
            return []
        result, level = [], 0
        return re_level(level, root, result)


if __name__ == "__main__":
    # n1 = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n4 = TreeNode(4)
    # n5 = TreeNode(5)
    # n1.left, n1.right = n2, n3
    # n3.left, n3.right = n4, n5
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(4)
    n7 = TreeNode(3)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    s = Solution()
    print s.levelOrder(n1)
