# coding=utf-8
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""


def single_number1(nums):
    """使用count方法，时间较慢。但若不是其余每个元素均出现偶数次，则用这个"""
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]


def single_number2(nums):
    """异或：相同为0，不同为1. 异或同一个数两次，原数不变"""
    num = 0
    for i in nums:
        num = num ^ i
    return num


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print single_number2(nums)