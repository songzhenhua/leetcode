# coding=utf-8
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。
"""


def is_anagram1(s, t):
    """
    转换成列表对比，战胜6%
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    ls = list(s)
    ts = list(t)
    ls.sort()
    ts.sort()
    if ls != ts:
        return False
    return True


def is_anagram2(s, t):
    """
    转换成字典对比，战胜9%
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    ds, dt = {}, {}
    for i in s:
        ds[i] = ds.get(i, 0) + 1
    for i in t:
        dt[i] = dt.get(i, 0) + 1
    """
    上边4行可以合并成3行，减少一次循环
    for i in range(len(s)):
        ds[s[i]] = ds.get(s[i], 0) + 1
        dt[t[i]] = dt.get(t[i], 0) + 1
    """
    if ds != dt:
        return False
    return True


def is_anagram3(s, t):
    """
    参考大神写法战胜63%
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    ls, lt = [0 for i in range(26)], [0 for i in range(26)]
    for i in range(len(s)):
        ls[ord(s[i]) - ord('a')] += 1  # 建立s的字母表映射，列表0-25依次表示字母出现次数
        lt[ord(t[i]) - ord('a')] += 1
    if ls != lt:
        return False
    return True


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    # s, t = "rat", "car"
    print is_anagram2(s, t)