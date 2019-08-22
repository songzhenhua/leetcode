# coding=utf-8
"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；

假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：
假设我们的环境只能存储32位大小的有符号整数，其数值范围[−2^31,  2^31−1]。如果数值超过这个范围，返回INT_MAX(2^31−1) 或INT_MIN(−2^31)

示例 1:
输入: "42"
输出: 42

示例 2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例 3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例 4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。

示例 5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−2^31) 。
"""
import re


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.lstrip()  # 丢弃无用的开头空格字符
    result = ''
    sub_flag = False  # 负数标志
    i = 0  # 取数字的下标

    if str == '':  # 字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换
        return 0
    elif str[0] == '-':
        sub_flag = True
        i += 1
    elif str[0] == '+':
        i += 1
    elif str[0].isdigit():
        i = 0
    else:
        return 0  # 假如该字符串中的第一个非空格字符不是一个有效整数字符，则你的函数不需要进行转换
    # '+'针对此用例判断
    if i > len(str)-1:
        return 0
    # 取连续整数
    for j in range(i, len(str)):
        if str[j].isdigit():
            result += str[j]
        else:
            break
    # '+-2'针对此类用例判断
    if result == '':
        return 0
    result = int(result)

    if sub_flag:
        result = -result
    if result < pow(-2, 31):
        result = pow(-2, 31)
    if result > (pow(2, 31)-1):
        result = pow(2, 31)-1
    return result


def myAtoi2(str):
    """
    大神用正则实现，简单明了，战胜100%

    """
    a = re.match(r'^[-+]?\d+', str.strip())  # 正则为：+或-开头出现0或1次，后面为一位或多位数字
    if not a:
        return 0
    a = int(a.group())
    b = 2**31
    if a > b-1:
        return b-1
    elif a < -b:
        return -b
    else:
        return a


if __name__ == "__main__":
    s1 = "42"
    s2 = "   -42"
    s3 = "4193 with words"
    s4 = "-91283472332"
    s5 = '+'
    s6 = '+-2'
    s7 = '   '
    print myAtoi(s7)