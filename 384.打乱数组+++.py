# coding=utf-8
import random
"""
打乱一个没有重复元素的数组。

示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
"""


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        result = []
        result[:] = self.nums
        random.shuffle(result)
        return result

    def shuffle1(self):
        """
        官方解法1：暴力法
        循环每次从原数组随机取一个数出来。
        时间复杂度： O(n^2)，乘方时间复杂度来自于 list.remove（list.pop）。每次操作都是线性时间的，总共发生 n 次。
        """
        temp, result = [], []
        temp[:] = self.nums
        for i in range(len(self.nums)):
            idx = random.randrange(len(temp))
            result.append(temp.pop(idx))
        return result

    def shuffle2(self):
        """
        官方解法2： Fisher-Yates 洗牌算法
        Fisher-Yates 洗牌算法跟暴力算法很像。在每次迭代中，生成一个范围在当前下标到数组末尾元素下标之间的随机整数。
        接下来，将当前元素和随机选出的下标所指的元素互相交换，其中选取下标范围的依据在于每个被摸出的元素都不可能再被摸出来了。
        此外还有一个需要注意的细节，当前元素是可以和它本身互相交换的 - 否则生成最后的排列组合的概率就不对了。
        时间复杂度：O(n)，时间复杂度是线性的，因为算法中生成随机序列，交换两个元素这两种操作都是常数时间复杂度的。
        """
        result = []
        result[:] = self.nums
        for i in range(len(result)):
            idx = random.randrange(i, len(result))
            result[i], result[idx] = result[idx], result[i]
        return result


if __name__ == "__main__":
    s = Solution([1,2,3])
    p1 = s.shuffle2()
    print p1
    p2 = s.reset()
    print p2

