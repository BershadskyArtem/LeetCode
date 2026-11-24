
# https://leetcode.com/problems/daily-temperatures/

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get a warmer temperature. If there is no future day for which this is possible,
# keep answer[i] == 0 instead.
#
# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
#
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
#
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # This structure is called monotonic stack (all values are in ascending or descending order)
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(index)
                continue

            if temperatures[stack[-1]] >= temperature:
                stack.append(index)
                continue

            while len(stack) > 0 and temperatures[stack[-1]] < temperature:
                previous_index = stack.pop()
                result[previous_index] = index - previous_index

            stack.append(index)

        return result


sol = Solution()
res = sol.dailyTemperatures([73,74,75,71,69,72,76,73])
# res = sol.dailyTemperatures([30,40,50,60])
# res = sol.dailyTemperatures([30,60,90])
print(res)