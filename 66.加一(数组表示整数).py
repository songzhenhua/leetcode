# coding=utf-8
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

示例 3:
输入: [9]
输出: [1,0]
解释: 输入数组表示数字 10。

示例 4:
输入: [9,9]
输出: [1,0,0]
解释: 输入数组表示数字 100。

"""


def plus_one1(digits):
    """
    方法比较笨，只战胜了5%
    :type digits: List[int]
    :rtype: List[int]
    """
    # 列表->字符串->整数-> +1
    num = ''
    for j in range(len(digits)):
        num += str(digits[j])
    num = int(num) + 1
    # 依次从整数第1位开始取数
    li = []
    for i in range(len(str(num))-1, 0, -1):
        a = num/pow(10, i)
        li.append(a)
        num -= a*pow(10, i)
    li.append(num)
    return li


def plus_one2(digits):
    """
    与方法1思路一样，只是取数时从字符串依次取，好理解但耗时比1略高
    :type digits: List[int]
    :rtype: List[int]
    """
    # 列表->字符串->整数->+1->字符串
    num = ''
    for j in range(len(digits)):
        num += str(digits[j])
    num = int(num) + 1
    num = str(num)
    li = []
    for i in range(len(num)):
        li.append(int(num[i]))
    return li


def plus_one3(digits):
    """
    参考别人，战胜81%
    :type digits: List[int]
    :rtype: List[int]
    """
    for i in range(1, len(digits)+1):
        if digits[-i] == 9:
            digits[-i] = 0
        else:
            digits[-i] += 1
            return digits
    return [1] + digits


if __name__ == "__main__":
    digits = [1,2]
    print plus_one3(digits)
