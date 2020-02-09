# coding=utf-8
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        前2行没法算，直接判断返回，从第3行开始算
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        if numRows < 1:
            return []
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        for i in range(3, numRows+1):
            temp = [1]
            for j in range(i-2):
                temp.append(result[-1][j] + result[-1][j+1])
            temp.append(1)
            result.append(temp)
        return result


if __name__ == "__main__":
    s = Solution()
    print s.generate(5)

