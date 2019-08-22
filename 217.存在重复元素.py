# coding=utf-8
"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""


def has_duplicate1(li):
    """使用set集合"""
    return len(set(li)) != len(li)

def has_duplicate2(li):
    """使用字典key的唯一性"""
    if len(dict.fromkeys(li).keys()) != len(li):  # 也可以写成len(list(dict.fromkeys(li)))
        return True
    else:
        return False


def has_duplicate3(li):
    """使用count计数"""
    for i in range(len(li)):
        if li.count(li[i]) > 1:
            return True
    return False


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print has_duplicate1(a)