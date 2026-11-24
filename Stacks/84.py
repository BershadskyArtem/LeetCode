# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2, 1, 5, 6, 2, 3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Please see the link for more details
# https://www.youtube.com/watch?v=zx5Sw9130L0

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = -1
        for index, height in enumerate(heights):
            if len(stack) == 0:
                stack.append((index, height))
                continue

            shifted_start_index = index
            while len(stack) != 0 and stack[-1][1] > height:
                previous_index, previous_height = stack.pop()
                max_area = max(max_area, (index - previous_index) * previous_height)
                shifted_start_index = previous_index

            stack.append((shifted_start_index, height))

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area


sol = Solution()
# res = sol.largestRectangleArea([2, 1, 5, 6, 2, 3])
res = sol.largestRectangleArea([2, 4])
# res = sol.largestRectangleArea([2, 1, 2])
print(res)
