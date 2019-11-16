# coding=utf-8
"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        l = [0 for i in range(max_num+1)]
        for i in nums:
            l[i] = 1
        for j in range(max_num+1):
            if l[j] == 0:
                return j
        return max_num + 1

if __name__ == "__main__":
    s = Solution()
    a1 = [3,0,1]
    a2 = [9,6,4,2,3,5,7,0,1]
    a3 = [0]
    print s.missingNumber(a3)

