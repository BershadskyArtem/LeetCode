# https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            left_character = s[left]
            if not left_character.isalnum():
                left += 1
                continue

            right_character = s[right]
            if not right_character.isalnum():
                right -= 1
                continue

            if left_character.lower() != right_character.lower():
                return False

            left += 1
            right -= 1

        return True


sol = Solution()
res = sol.isPalindrome("A man, a plan, a canal: Panama")
print(res)
