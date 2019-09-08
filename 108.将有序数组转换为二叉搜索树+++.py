# coding=utf-8
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        每次取数组len/2为根节点，之后剩余左右数组分别递归。击败了95.81%的用户。
        每次如果数组长度为1，只取根节点，左右节点为None；
        每次如果数组长度为2，只取根节点和左节点，右节点为None；
        :type nums: List[int]
        :rtype: TreeNode
        """
        def temp(l):
            index = len(l)/2
            node = TreeNode(l[index])
            if len(l) == 1:
                node.left = None
                node.right = None
            elif len(l) == 2:
                node.left = temp(l[:index])
                node.right = None
            else:
                node.left = temp(l[:index])
                node.right = temp(l[index+1:])
            return node
        if nums:
            return temp(nums)
        else:
            return None

    def levelOrder(self, root):
        """
        打印二叉树，验证数组转二叉树结果是否正确
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
    # nums = [-10,-3,0,5,9]
    # nums = [1,2,3,4,5,6,7,8]
    nums = []
    s = Solution()
    node = s.sortedArrayToBST(nums)
    print s.levelOrder(node)