# coding=utf-8
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


def intersect(nums1, nums2):
    """
    遍历nums1，如果有相同元素就存入结果列表，同时将nums2中该元素删除（防止出现1个数nums1有2个，nums2有1个）
    默认nums1长度较小，否则先对比下大小，让nums1保持较小
    """
    result = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            result.append(nums1[i])
            nums2.remove(nums1[i])
    return result


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]  # [4, 9, 5]
    nums2 = [2, 2]  # [9, 4, 9, 8, 4]
    print intersect(nums1, nums2)