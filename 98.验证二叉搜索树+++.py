# coding=utf-8
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

二叉搜索树：它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
           若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
示例 1:

输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST1(self, root):
        """官方答案1
            2
           / \
          1   6
             / \
            4   7
           / \
          3  5
        利用递归，每次判断当前节点要>最小值，<最大值。时间复杂度 : O(N)，每个结点访问一次。空间复杂度 : O(N)，我们跟进了整棵树。
        节点2：>无穷小，<无穷大
        节点1：>无穷小，<2；        节点6：>2，<无穷大
        节点4：>2，<6；            节点7：>6(也必大于2)，<无穷大
        节点3：>2，<4(也必小于6)；  节点5：>4(也必大于2)，<6
        :type root: TreeNode
        :rtype: bool
        """
        # Python中可以用如下方式表示正负无穷：float("inf"), float("-inf")
        def reValid(node, miner=float("-inf"), maxer=float("inf")):
            if not node:
                return True
            value = node.val
            if value <= miner or value >= maxer:
                return False
            if not reValid(node.left, miner, value):
                return False
            if not reValid(node.right, value, maxer):
                return False
            return True

        return reValid(root)


    def isValidBST2(self, root):
        """官方答案2:利用栈的概念，时间复杂度：O(N),空间复杂度：O(N)"""
        if not root:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, miner, maxer = stack.pop()
            if not node:
                continue
            if node.val <= miner or node.val >= maxer:
                return False
            stack.append((node.left, miner, node.val))
            stack.append((node.right, node.val, maxer))
        return True

    def isValidBST3(self, root):
        """官方答案3
            4
           / \
          2   5
         / \
        1   3
        利用中序遍历，即左子树->结点->右子树，每个元素都应该比下一个元素小
        正常思维是依次对比1-2-3-4-5，但我们需要从根结点依次遍历入栈，在这个过程中就可以对比结点是否符合要求
        时间复杂度：O(N),空间复杂度：O(N)
        """
        stack, miner = [], float("-inf")
        while stack or root:
            # 循环将左子树入栈
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= miner:
                return False
            miner = root.val
            root = root.right
        return True


if __name__ == "__main__":
    n1 = TreeNode(5)
    n2 = TreeNode(1)
    n3 = TreeNode(7)
    n4 = TreeNode(6)
    n5 = TreeNode(8)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = None, None
    n3.left, n3.right = n4, n5
    n4.left, n4.right = None, None
    n5.left, n5.right = None, None
    s = Solution()
    print s.isValidBST3(n1)
