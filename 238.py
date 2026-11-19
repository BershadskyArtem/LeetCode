# https://leetcode.com/problems/product-of-array-except-self/description/

# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        prefix = 1
        for index in range(len(nums) - 1):
            num = nums[index]
            prefix *= num
            result[index + 1] *= prefix

        postfix = 1
        for index in range(len(nums) - 1, 0, -1):
            num = nums[index]
            postfix *= num
            result[index - 1] *= postfix

        return result


sol = Solution()
# res = sol.productExceptSelf([1, 2, 3, 4])
res = sol.productExceptSelf([-1, 1, 0, -3, 3])
print(res)
