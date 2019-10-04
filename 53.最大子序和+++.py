# coding=utf-8
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        从前往后每数相加，如果和大于>0则保留，继续往下加；如果和不大于0则抛弃前面的数重新开始加。
        每次相加完都跟最大和对比一下，并把大数赋给最大和，这样遍历一遍即可。时间复杂度O(n),空间复杂度O(1)。
        :type nums: List[int]
        :rtype: int
        """
        max_num_sum, temp_sum = nums[0], 0
        for i in range(len(nums)):
            if temp_sum > 0:
                temp_sum += nums[i]
            else:
                temp_sum = nums[i]
            max_num_sum = max(max_num_sum, temp_sum)
        return max_num_sum


if __name__ == "__main__":
    s = Solution()
    # l = [-2,1,-3,4,-1,2,1,-5,4]
    l = [-2,-3,-1,-5,-4]
    print s.maxSubArray(l)
