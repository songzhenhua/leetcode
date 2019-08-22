# coding=utf-8
import time
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""


def move1(nums, k):
    """
    较笨的方法，一次数组所有元素两两交换右移一位，一共K次，时间复杂度O(n^2)
    方法没问题，但在leetcode上运行第34个用例时，因为数组超级大，运行超时，无法提交
    :param nums: 要移动的数组
    :param k:  要向右移动k个位置
    :return: 无需返回值，直接在原list操作
    """
    k %= len(nums)  # 当右移位置大于数组长度时，右移取余位数即可
    for i in range(k):
        for j in range(len(nums) - 1, 0, -1):
            nums[j - 1] += nums[j]
            nums[j] = nums[j - 1] - nums[j]
            nums[j - 1] = nums[j - 1] - nums[j]
            # 其实python有更方便的写法如下
            # li[j-1], li[j] = li[j], li[j-1]
# -------------------------------------------------------------------------------------


def move2(nums, k):
    """
    先整个数组反转，再以k为分界，数组前后分别反转，时间复杂度O(n)
    """
    k %= len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)


def reverse(a, start, end):
    while start < end:
        a[start] += a[end]
        a[end] = a[start]-a[end]
        a[start] = a[start]-a[end]
        start += 1
        end -= 1
# -------------------------------------------------------------------------------------


def move3(nums, k):
    """
    借用一个变量，每次数组右移一位，右移k次，时间复杂度O(kn)
    """
    for i in range(k):
        temp = nums[-1]
        for j in range(len(nums)-1, 0, -1):
            nums[j] = nums[j-1]
        nums[j - 1] = temp


if __name__ == "__main__":
    c = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    move3(c, k)
    print c
