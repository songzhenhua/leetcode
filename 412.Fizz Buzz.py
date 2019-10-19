# coding=utf-8
"""
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                l.append("FizzBuzz")
            elif i % 3 == 0:
                l.append("Fizz")
            elif i % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l

    def fizzBuzz1(self, n):
        """
        如果规则更复杂(如7对应jazz)，用上面的方法联合判断将更复杂。官方答案二：字符连接法。
        如果能被 3 整除，就把对应的 Fizz 连接到答案字符串，如果能被 5 整除，就把 Buzz 连接到答案字符串。
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n + 1):
            answer = ''
            if i % 3 == 0:
                answer = "Fizz"
            if i % 5 == 0:
                answer += "Buzz"
            if answer == '':
                answer = str(i)
            l.append(answer)
        return l


if __name__ == "__main__":
    s = Solution()
    print s.fizzBuzz1(15)

