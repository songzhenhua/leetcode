# coding=utf-8
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    result = ''
    strs.sort(key=len)  # 将列表按字符串长度从小到大排序
    for i in range(len(strs[0])):
        letter = strs[0][i]
        for n in range(len(strs)):
            if strs[n][i] != letter:
                return result
        result += letter
    return result


def longestCommonPrefix1(strs):
    """
    大神方法1：利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb，aba，abac，最大为abb，最小为aba。
              所以只需要比较最大最小的公共前缀就是整个数组的公共前缀。战胜43%
    """
    if not strs:
        return ''
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


def longestCommonPrefix2(strs):
    """
    大神方法2：利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，
              之后遍历list中找到元素长度大于1之前的就是公共前缀。战胜20%
    """
    if not strs:
        return ''
    result = ''
    s = map(set, zip(*strs))
    print s
    for i, x in enumerate(s):
        x = list(x)
        if len(x) > 1:
            break
        result += x[0]
    return result


if __name__ == "__main__":
    s1 = ["flower", "flow", "flight"]
    s2 = ["dog", "racecar", "car"]
    s3 = ["flower", "flow", "flowight"]
    s4 = ['abc', 'bbbb', 'abcdef']
    print longestCommonPrefix2(s1)
