# coding=utf-8
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        左右子树分别中序遍历，遍历的同时进行对比，如有一处不相同则不镜像；遍历到根节点时则左右子树已经完全对比完毕。
        :type root: TreeNode
        :rtype: int
        """
        stackl, stackr, rootl, rootr = [], [], root, root
        while stackl or stackr or rootl or rootr:
            # 循环将左子树入栈
            while rootl:
                stackl.append(rootl)
                rootl = rootl.left
            while rootr:
                stackr.append(rootr)
                rootr = rootr.right
            '''
            下边的if兼容此种情况
                1
               / \
              2   2
             /   / 
            2   2  
            '''
            if len(stackl) != len(stackr):
                return False
            rootl = stackl.pop()
            rootr = stackr.pop()
            # 整个树只有一个根节点，也算镜像
            if rootl == rootr == root:
                return True
            if rootl.val != rootr.val:
                return False
            rootl = rootl.right
            rootr = rootr.left
        return True  # 未进while循环，空也算镜像

    def isSymmetric1(self, root):
        """
        递归:左右子树镜像对称，互为镜像的条件：1.根节点值相同；2.每个树的右子树都与另一个树的左子树镜像对称
        时间复杂度：因为我们遍历整个输入树一次，所以总的运行时间为O(n)，其中 n 是树中结点的总数。
        空间复杂度：递归调用的次数受树的高度限制。在最糟糕情况下，树是线性的，其高度为O(n)。因此，在最糟糕的情况下，
                   由栈上的递归调用造成的空间复杂度为 O(n)。
        """
        def is_mirror(nodel, noder):
            # 空也算镜像
            if not nodel and not noder:
                return True
            # 经过上面判断则左右子树根节点必不同时为None
            if not nodel or not noder:
                return False
            return nodel.val == noder.val and is_mirror(nodel.right, noder.left) and is_mirror(nodel.left, noder.right)
        return is_mirror(root, root)

    def isSymmetric2(self, root):
        """
        迭代:该算法的工作原理类似于 BFS，但存在一些关键差异。
             每次提取两个结点并比较它们的值。然后，将两个结点的左右子结点按相反的顺序插入队列中。
             当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时，该算法结束。
        时间复杂度：因为我们遍历整个输入树一次，所以总的运行时间为O(n)，其中 n 是树中结点的总数。
        空间复杂度：搜索队列需要额外的空间。在最糟糕情况下，我们不得不向队列中插入O(n) 个结点。因此，空间复杂度为 O(n)。
        """
        # 空也算镜像
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            nodel = stack.pop()
            noder = stack.pop()
            if not nodel and not noder:
                continue
            # 经过上面判断则左右子树根节点必不同时为None
            if not nodel or not noder:
                return False
            if nodel.val != noder.val:
                return False
            stack.append(nodel.left)
            stack.append(noder.right)
            stack.append(nodel.right)
            stack.append(noder.left)
        return True


if __name__ == "__main__":
    """
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
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(5)
    n7 = TreeNode(4)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = None, n7
    s = Solution()
    print s.isSymmetric2(n1)
