# coding=utf-8
"""
统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution(object):
    def countPrimes(self, n):
        """
        质数:大于等于2 不能被它本身和1以外的数整除
        :type n: int
        :rtype: int
        """
        def is_prime(n):
            top = int(n ** 0.5)  # 技巧：1个正整数如果能从2到自己的的平方根(取整)整除，则其不是质数
            for i in range(2, top+1):
                if n % i == 0:
                    return False
            return True
        n = n-1
        if n < 2:
            return 0
        counter = 1  # 直接将2算为质数并计数
        for j in range(3, n+1):
            if is_prime(j):
                counter += 1
        return counter

    def countPrimes1(self, n):
        """
        厄拉多塞筛法:2是质数，则2的倍数均不是质数了(4,6,8...)；3是质数，则3的倍数均不是质数了(6,9,12...)。
        确定不是质数的数，直接略过。所以需要n空间的list存放该数是否是质数的标志位。
        :type n: int
        :rtype: int
        """
        n -= 1
        count = 0
        flag = [True]*(n+1)  # 默认标志全是质数-Ture，标志list多1个是因为列表下标从0开始，为了保持和n一致，多余1个下标0
        for i in range(2, n+1):  # 从2到n(包含)
            if flag[i]:
                count += 1
                # i是质数，则i的倍数均不会是质数，标志设False
                for j in range(2*i, n+1, i):  # 从i的双倍开始，步长为i，一直到n(包含)
                    flag[j] = False
        return count


if __name__ == "__main__":
    s = Solution()
    print s.countPrimes(10)

