# coding=utf-8
"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Python作弊玩法
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2  # 这里要用到[:]浅拷贝，因为nums1[:m] + nums2导致nums1指向新的地址了，不会修改原地址的值
        nums1.sort()

    def merge1(self, nums1, m, nums2, n):
        """
        官方解法3，利用nums1后半部分，依次挑两数组最大数从后往前填
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # p1指向nums1有效数的末尾,p2指向nums2末尾,p3指向nums1末尾
        p1, p2, p3 = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]


if __name__ == "__main__":
    nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    m, n = 3, 3
    s = Solution()
    s.merge1(nums1, m, nums2, n)
    print nums1
