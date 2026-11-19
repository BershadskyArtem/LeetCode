# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        deduplicated = set(nums)
        result = 0
        for num in deduplicated:
            if num - 1 in deduplicated:
                continue

            consecutive_counter = 1
            while num + 1 in deduplicated:
                consecutive_counter += 1
                num += 1
            result = max(result, consecutive_counter)

        return result


sol = Solution()
res = sol.longestConsecutive([100, 4, 200, 1, 3, 2])
print(res)
