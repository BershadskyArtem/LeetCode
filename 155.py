
# https://leetcode.com/problems/min-stack/description/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self._stack = []
        self._minimums = []

    def push(self, value: int) -> None:
        self._stack.append(value)
        if len(self._minimums) == 0:
            self._minimums.append(value)
            return

        previous_minimum = self._minimums[-1]
        self._minimums.append(min(previous_minimum, value))

    def pop(self) -> None:
        self._stack.pop()
        self._minimums.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minimums[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
