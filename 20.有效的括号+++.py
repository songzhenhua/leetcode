# coding=utf-8
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '[': ']', '{': '}'}
        if s == '':
            return True
        if len(s)%2 != 0:  # 如果s长度不是偶数，必不匹配
            return False
        stack = [s[0]]  # 存放符号的栈，初始把第1个字符入栈
        # 从第2字符开始对比,如果字符在字典的values中，那就要匹配栈中最后字符，不是一对返回F，是的话出栈；
        # 如果字符在字典的keys中，入栈
        for i in range(1, len(s)):
            if s[i] in d.values():
                if s[i] != d.get(stack[-1]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        # 遍历后，如果栈不为空，说明有不匹配的
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    a1 = "()"
    a2 = "()[]{}"
    a3 = "(]"
    a4 = "([)]"
    a5 = "{[]}"
    print s.isValid(a4)

