# coding=utf-8
"""
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。
不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:
输入: [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
输入: [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。

注意:
给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。
"""


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 没有火柴返回False
        if not nums:
            return False
        # 火柴总数L
        L = len(nums)
        # 火柴长度总和
        perimeter = sum(nums)
        # 边长
        possible_side = perimeter // 4
        # 边长*4 ！= 总长返回False
        if possible_side * 4 != perimeter:
            return False
        # 排序
        nums.sort(reverse=True)
        # 4边及各边长度
        sums = [0 for _ in range(4)]

        def dfs(index):
            # 遍历到最后1根火柴，检查是否是正方形
            if index == L:
                # 如果4边相等则是正方形返回True
                return sums[0] == sums[1] == sums[2] == sums[3]
            # 当前火柴可以依次放入4边
            for i in range(4):
                # 如果当前的火柴长度+当前边长<=应该的边长
                if sums[i] + nums[index] <= possible_side:
                    # 把当前火柴长度加到边长总和中，递归
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    # 前面的遍历不符合条件，恢复递归结果
                    sums[i] -= nums[index]
            return False
        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    t = [1,1,2,2,2]
    print s.makesquare(t)

