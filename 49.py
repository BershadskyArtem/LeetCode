from collections import defaultdict

# https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            fingerprint = [0] * 26

            for character in s:
                character_ascii = ord(character) - ord('a')
                fingerprint[character_ascii] += 1

            groups[tuple(fingerprint)].append(s)

        return list(groups.values())


sol = Solution()
result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)



