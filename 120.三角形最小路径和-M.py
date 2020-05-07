# coding=utf-8
"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        自底向上的动态规划，思路实例：
        最底层的4和1取最小的，然后和上一层的6相加，和为7，把7赋值到6的位置……依次类推，最后顶部就是存的最小路径和。
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        for i in range(len(triangle)-1, -1, -1):
            for j in range(i):
                triangle[i-1][j] = triangle[i-1][j] + min(triangle[i][j], triangle[i][j+1])
        return triangle[0][0]



if __name__ == "__main__":
    s = Solution()
    t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print s.minimumTotal(t)

