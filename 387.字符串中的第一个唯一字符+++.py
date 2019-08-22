# coding=utf-8
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
"""


def first_uniq_char1(s):
    """
    字符串硬找，打败3%
    :type s: str
    :rtype: int
    """
    for i in s:
        if s.count(i) == 1:
            return s.find(i)
    return -1


def first_uniq_char2(s):
    """
    通过字典，哈希存取快，打败52%
    :type s: str
    :rtype: int
    """
    m = {}
    for i in s:
        m[i] = m.get(i, 0) + 1
    for i in range(len(s)):
        if m[s[i]] == 1:
            return i
    return -1


if __name__ == "__main__":
    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabbcc"
    print first_uniq_char2(s1)