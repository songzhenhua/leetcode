# coding=utf-8
"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


def strstr(haystack, needle):
    """
    python自带方法，这算作弊吗
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)


def strstr1(haystack, needle):
    """
    自己实现的，时间超时了
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    i, j, index = 0, 0, -1
    if needle == '':
        return 0
    # 防止出现"mississippi", "issip"类似case，第一次查找不完全匹配，就从第一次匹配的+1位置重新开始
    while index < len(haystack):
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                if j == 0:  # needle第一次匹配上，haystack相应的下标
                    index = i
                j += 1  # needle匹配上，下标往后走
            elif j != 0:  # j!=0说明没有完全匹配，跳出此次循环
                break
            i += 1
        # needle的下标全部走完，才是完全匹配
        if j == len(needle):
            return index
        # 如果index一直是-1说明一个字符也没匹配上;否则就是匹配不完全
        if index == -1:
            return -1
        else:
            i, j, index = index + 1, 0, -1
    return -1


def strstr2(haystack, needle):
    """
    这是大神的
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == '':
        return 0
    elif needle not in haystack:
        return -1
    else:
        lens = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i + lens] == needle:
                return i


if __name__ == "__main__":
    # haystack, needle = "hello", "ll"
    # haystack, needle = "aaaaa", "bba"
    haystack, needle = "mississippi", "issip"
    # haystack, needle = "mississippi", ""
    print strstr2(haystack, needle)
