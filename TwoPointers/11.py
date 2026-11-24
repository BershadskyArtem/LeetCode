# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        area = -1
        while left < right:
            left_height = height[left]
            right_height = height[right]
            new_area = min(left_height, right_height) * (right - left)
            area = max(area, new_area)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return area


sol = Solution()
# res = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
res = sol.maxArea([1, 1])
print(res)

