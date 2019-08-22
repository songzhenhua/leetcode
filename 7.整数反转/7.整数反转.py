# coding=utf-8
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


def reverse1(x):
    """
    将整数转成字符列表，再反转，再乘回去。战胜40.75%
    :type x: int
    :rtype: int
    """
    flag = 1  # 正负号
    if x < 0:
        flag = -1
        x = abs(x)
    x = list(str(x))
    x.reverse()
    reverse_x = 0
    for i in range(len(x)):
        reverse_x += int(x[i]) * pow(10, len(x)-1-i)
    # 超出[−2^31,  2^31 − 1]，返回0
    if reverse_x < pow(-2, 31) or reverse_x > (pow(2, 31)-1):
        return 0
    return reverse_x*flag


def reverse2(x):
    """
    官方答案，有修改，详见question.png。因为python取整/取余向负无穷取整，所以先去掉负号，最后再加回来。
    :type x: int
    :rtype: int
    """
    rev = 0
    minus = False
    if x < 0:
        minus = True
        x = abs(x)
    while x != 0:
        pop = x % 10
        x /= 10
        if (rev > pow(2, 31)/10) or (rev == pow(2, 31)/10 and pop > 7):
            return 0
        if (rev < pow(-2, 31)/10) or (rev == pow(-2, 31)/10 and pop < -8):
            return 0
        rev = rev*10+pop
    if minus:
        rev = -rev
    return rev


if __name__ == "__main__":
    x = 7463847412#2147483647
    print reverse1(x)