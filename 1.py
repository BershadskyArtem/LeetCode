
# https://leetcode.com/problems/two-sum/description/
# You are given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remainders = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in remainders:
                return [remainders[difference], index]
            remainders[num] = index

        return []


sol = Solution()
res = sol.twoSum([2, 7, 11, 15], 9)
print(res)
