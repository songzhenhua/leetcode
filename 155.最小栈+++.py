# coding=utf-8
"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack(object):
    """
    # 未能达到在常数时间内检索到最小元素的栈
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)

    # TOP1答案方法一：以空间换时间，使用辅助栈，每层与数据栈平行存放当前所有数中最小值。
    # 数值栈 辅助栈
    # -4      -4
    # -2      -3
    #  0      -3
    # -3      -3
    def __init__(self):
        self.stack, self.helper = [], []

    def push(self, x):
        self.stack.append(x)
        # 如果辅助栈为空或是新加的数小于最小值(辅助栈顶)，则将新加的数加到辅助栈顶，否则把之前最小值加到辅助栈顶
        if not self.helper or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.helper.pop()
        else:
            print 'stack is empty!'

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print 'stack is empty!'

    def getMin(self):
        if self.helper:
            return self.helper[-1]
        else:
            print 'stack is empty!'
"""
    # TOP1答案方法二：方法一辅助栈与数据栈同步，当数多时消耗空间，使用非同步的方法可以节省空间。
    # 数值栈 辅助栈
    # -4      -4
    # -2
    # -3      -3
    # -3      -3
    def __init__(self):
        self.stack, self.helper = [], []

    def push(self, x):
        self.stack.append(x)
        # 如果辅助栈为空或是新加的数<=最小值(辅助栈顶)，则将新加的数加到辅助栈顶
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        if self.stack:
            num = self.stack.pop()
            if num == self.helper[-1]:  # 如果数据栈弹出的数==辅助栈顶的数(即当前最小值)，则将辅助栈顶的数也弹出
                self.helper.pop()
        else:
            print 'stack is empty!'

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print 'stack is empty!'

    def getMin(self):
        if self.helper:
            return self.helper[-1]
        else:
            print 'stack is empty!'


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print obj.getMin()  # -3
    obj.pop()
    param_3 = obj.top()  # 0
    print param_3
    param_4 = obj.getMin()  # -2
    print param_4
