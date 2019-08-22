# coding=utf-8
"""
假设1元、2元、5元、10元、20元、50元、100元的纸币分别有c0, c1, c2, c3, c4, c5, c6张。
现在要用这些钱来支付K元，至少要用多少张纸币
解题原用贪心算法，前提是各面额纸币足够；后面兼容了钱不够时的情况
"""


def change(price, values, counts):
    """
    用贪心算法的思想，每一步尽可能用面值大的纸币即可
    :param price: 金额int
    :param values: 面值list[int]
    :param counts: 现有张数list[int]
    :return: 实际所需张数list[int]，钱是否足够Boolean
    """
    sum_price = price
    nums = [0]*len(values)  # 先定义所有面额所需张数为0
    for i in range(len(values)-1, -1, -1):
        nums[i] = min(counts[i], price/values[i])  # 现有张数和需要张数，取最小值
        price -= values[i] * nums[i]
    if price != 0:  # 当price不为0时，表示前面付出的钱不够，需要回溯
        nums, index = not_zero(price, values, counts, nums)
        if index == -999:
            return nums, False
        nums = new_count(sum_price, index, values, nums)
    return nums, True


def not_zero(lack_price, values, counts, nums):
    """
    贪心算法的找钱不够，需要回溯一下
    :param lack_price: 不足的金额int
    :param values: 面值list[int]
    :param counts: 现有张数list[int]
    :param nums: 之前不够的各面额数量list[int]
    :return: 半成品实际所需张数list[int]，回溯时补齐金额的面额下标int
    """
    for j in range(1, len(values)):
        if counts[j] > nums[j]:
            left_count = counts[j] - nums[j]
            for k in range(1, left_count + 1):
                if lack_price - k * values[j] <= 0:
                    nums[j] += k
                    return nums, j
    return nums, -999  # 金额不够时，返回特殊下标定义-999


def new_count(sum_price, index, values, nums):
    """
    回溯后，根据补齐金额的面额下标，重新计算各面额所需数量
    :param sum_price:金额int
    :param index:回溯时补齐金额的面额下标int
    :param values:面值list[int]
    :param nums:半成品实际所需张数list[int]
    :return:实际所需张数list[int]
    """
    for k in range(index,len(nums)):
        sum_price -= values[k]*nums[k]
    if sum_price <= 0:
        for k in range(index):
            nums[k] = 0
    return nums


if __name__ == "__main__":
    values = [1, 2, 5, 10, 20, 50, 100]  # 人民币面额
    counts = [3, 1, 2, 1, 1, 3, 5]  # 现有人民币张数
    price = 446  # 444钱正好，446钱要的零，4444钱不够
    # values = [1, 2, 5, 10, 20, 50, 100]  # 人民币面额
    # counts = [0, 4, 2, 1, 1, 3, 5]  # 现有人民币张数
    # price = 447
    result, money_enough = change(price, values, counts)
    if not money_enough:
        print "钱不够，逗逼"
    else:
        sum = 0
        for i in range(len(result)):
            sum += values[i] * result[i]
            print "需要%3d元人民币 %s张" % (values[i], result[i]), sum
        if sum > price:
            print "需要找零%s元"%(sum-price)
