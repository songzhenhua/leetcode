# coding=utf-8
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


def is_palindrome(s):
    """
    利用快排的思想：左右两个指针向中间移动，如果指针所指不是数字和字母，则再次移动1位；然后对比2个指针的字符是否相等，以此循环
    击败27.23%
    :type s: str
    :rtype: bool
    """
    if s == '':
        return True
    i, j = 0, len(s)-1
    while i<j:
        while i < j and (not s[i].isalnum()):
            i += 1
        while i < j and (not s[j].isalnum()):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def is_palindrome1(s):
    """
    此方法简单明了，击败56.89%
    :type s: str
    :rtype: bool
    """
    ls=[]
    for a in s:
        if a.isalnum():
            ls.append(a.lower())
    if ls==list(reversed(ls)):
        return True
    return False


def is_palindrome2(s):
    """
    参考大神写法，使用filter函数，更加简洁
    filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列
    :type s: str
    :rtype: bool
    """
    s = ''.join(filter(str.isalnum, s)).lower()
    if s == s[::-1]:
        return True
    return False


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s1 = "race a car"
    s2 = '.,'
    print is_palindrome2(s2)