# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
#
# Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            left_number = numbers[left]
            right_number = numbers[right]
            two_sum = left_number + right_number
            if two_sum == target:
                return [left + 1, right + 1]
            elif two_sum > target:
                right -= 1
            else:
                left += 1

        return []


sol = Solution()
# res = sol.twoSum([2, 7, 11, 15], 9)
# res = sol.twoSum([2, 3, 4], 6)
res = sol.twoSum([-1, 0], -1)
print(res)


