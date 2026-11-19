# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == "*":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                evaluation = op1 * op2
                stack.append(evaluation)
            elif token == "/":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                evaluation = int(op2 / op1)
                stack.append(evaluation)
            elif token == "+":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                evaluation = op1 + op2
                stack.append(evaluation)
            elif token == "-":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                evaluation = op2 - op1
                stack.append(evaluation)
            else:
                stack.append(int(token))

        return stack[0]


sol = Solution()
# res = sol.evalRPN(["2","1","+","3","*"])
res = sol.evalRPN(["4","13","5","/","+"])
print(res)

