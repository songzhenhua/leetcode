# coding=utf-8
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12] [1,3,0,0,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


def move_zeroes(nums):
    """
    最后一步用了额外的数组，不符题意
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    count = nums.count(0)
    for i in range(count):
        nums.remove(0)
    nums.extend([0]*count)


def move_zeroes1(nums):
    """
    总体参考选择排序思路，加入flag是为了减少后面全是0的循环次数
    """
    i = 0
    flag = True
    while i < len(nums) - 1:
        if nums[i] == 0 and flag:
            for j in range(i + 1, len(nums)):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    flag = True
                    break
                flag = False
        i += 1



if __name__ == "__main__":
    nums = [0,1,0,3,12]
    move_zeroes1(nums)
    print nums