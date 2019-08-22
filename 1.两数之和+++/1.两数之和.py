# coding=utf-8
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def two_sum(nums, target):
    """
    题目实际要求是只返回一对下标，我的解法是返回多对下标
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    temp = []  # 记录大于target的下标
    # 下标不在筛选出来的列表中，且能找到2个数的和为target，记入结果列表
    i = 0
    while i < len(nums):
        if (i in temp) or (i in result):
            i += 1
            continue
        else:
            second_num = target - nums[i]
            try:
                idx = nums.index(second_num)
                # 如果idx==i，说明是同一个数，不是2个数
                if idx == i:
                    i += 1
                    continue
                result.append(i)
                result.append(idx)
            except ValueError:
                temp.append(i)
            i += 1
    return result


if __name__ == "__main__":
    nums = [-3,4,3,90]#[2, 7, 11, 15, 3, 6, 0]
    target = 10
    print two_sum(nums, target)
