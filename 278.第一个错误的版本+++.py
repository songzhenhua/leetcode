# coding=utf-8
"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少调用 API 的次数。

示例:
给定 n = 5，并且 version = 4 是第一个错误的版本。
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。
"""


def isBadVersion(version):
    if version >= 2:
        return True
    return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        先确定1个好版本，之后找好版本挨着的第1个坏版本。采用递归，战胜76%
        :type n: int
        :rtype: int
        """
        def dichotomy(start, end):
            middle = end - (end - start)/2
            # 如果middle==end说明start和end挨着，之前过程已证实start是好，end是坏，则返回第1个坏版本end
            if middle == end:
                return end
            if isBadVersion(middle):
                return dichotomy(start, middle)
            else:
                return dichotomy(middle, end)
        # 第1个版本如果不是坏版本，则先设定第1个版本为好版本&最后1个版本为坏版本
        if isBadVersion(1):
            return 1
        return dichotomy(1, n)

    def firstBadVersion1(self, n):
        """
        官方答案二：
        在二分查找的每次操作中，我们都用left和right表示搜索空间的左右边界，
        因此在初始化时，需要将 left 的值设置为 1，并将 right 的值设置为 n。
        当某一次操作后，left 和 right 的值相等，此时它们就表示了第一个错误版本的位置。

        在二分查找中，选取 mid 的方法一般为mid=(left+right)/2。
        如果使用的编程语言会有整数溢出的情况（例如 C++，Java），那么可以用mid=left+(right−left)/2代替前者。
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    n = 5
    s = Solution()
    print s.firstBadVersion1(n)
