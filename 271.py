# https://neetcode.io/problems/string-encode-and-decode/question
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
# strings can contain any ascii characters!!!

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f'{len(s)}#{s}'

        return encoded

    def decode(self, s: str) -> list[str]:
        index = 0
        maximum = len(s)
        decoded = []
        while index < maximum:
            length_prefix = ""
            while s[index].isdigit():
                length_prefix += s[index]
                index += 1

            length = int(length_prefix)
            index += 1
            content = s[index: index + length]
            decoded.append(content)
            index += length

        return decoded


sol = Solution()
en = sol.encode(["##Hello", "####World"])
de = sol.decode(en)
print(de)

