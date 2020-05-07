# coding=utf-8
"""
统计字符串中所有子串及个数，据说是滴滴的题
"""


def subcount(str):
    """
    双重循环取所有可能的子串，放到字典去重&计数
    :param str:
    :return: 子串及个数dict{string:int}
    """
    result = {}
    str.lower()
    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            substr = str[i:j]
            result[substr] = result.get(substr, 0) + 1
    return result


def subcount1(str):
    """
    双重循环取所有可能的子串(必须按字母顺序，如da不算)，放到字典去重&计数
    :param str:
    :return: 子串及个数dict{string:int}
    """
    result = {}
    str.lower()
    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            flag = False # 如果子串不按顺序，则跳过的标识
            substr = str[i:j]
            for x in range(len(substr)-1):
                if len(substr)<2:
                    break
                if ord(substr[x])>=ord(substr[x+1]):
                    flag = True
            if flag:
                continue
            result[substr] = result.get(substr, 0) + 1
    return result


if __name__ == "__main__":
    str = 'abcdabc'
    a = subcount1(str)
    b = sorted(a.items(), key=lambda i: i[0])
    for j in b:
        print j[0], j[1]
