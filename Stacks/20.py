# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for character in s:
            if character not in lookup:
                stack.append(character)
                continue

            opening_bracket = lookup[character]

            if len(stack) == 0:
                return False

            if opening_bracket != stack[-1]:
                return False

            stack.pop()

        return len(stack) == 0


sol = Solution()
# res = sol.isValid("()")
# res = sol.isValid("(")
# res = sol.isValid(")")
res = sol.isValid("(]")
print(res)





