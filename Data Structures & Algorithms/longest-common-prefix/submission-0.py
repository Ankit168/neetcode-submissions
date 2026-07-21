class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]

        for i in range(len(first)):
            ch = first[i]

            for str in strs[1:]:
                if i >= len(str) or str[i] != ch:
                    return first[:i]

        return first
            

        