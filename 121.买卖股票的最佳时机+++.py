# coding=utf-8
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        暴力遍历，提交leetcode提示超时。时间复杂度O(n^2),空间复杂度O(1)。
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    if prices[j] - prices[i] > profit:
                        profit = prices[j] - prices[i]
        return profit

    def maxProfit1(self, prices):
        """
        最大利润必定出现在某个低点L1（可能不是整个序列的最低点）和其后的高点H1（可能不是整个序列的最高点）之间。
        时间复杂度O(n),空间复杂度O(1)。
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


if __name__ == "__main__":
    s = Solution()
    l = [7,1,5,3,6,4]
    # l = [7,6,4,3,1]
    # l = []
    l = [i for i in range(10000,0,-1)]
    print s.maxProfit(l)