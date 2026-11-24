
# https://leetcode.com/problems/valid-anagram/description/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for character in s:
            if character not in s_dict:
                s_dict[character] = 0

            s_dict[character] += 1

        t_dict = {}
        for character in t:
            if character not in t_dict:
                t_dict[character] = 0

            t_dict[character] += 1

        if len(t_dict) != len(s_dict):
            return False

        for (character, count) in s_dict.items():
            if character not in t_dict:
                return False

            if count != t_dict[character]:
                return False

        return True


sol = Solution()
# res = sol.isAnagram('a', 'ab')
# res = sol.isAnagram('aa', 'a')
res = sol.isAnagram('ba', 'ab')
print(res)



