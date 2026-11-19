
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1
        m = max(counts.values())
        buckets = [[] for i in range(m + 1)]

        for (num, count) in counts.items():
            buckets[count].append(num)

        result = []

        for index in range(len(buckets) - 1, 0, -1):
            bucket = buckets[index]
            for num in bucket:
                if k == 0:
                    return result
                k -= 1
                result.append(num)

        return result


sol = Solution()
# res = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
res = sol.topKFrequent([1, 1, 1, 1, 1, 1, 1, 1], 2)
print(res)
