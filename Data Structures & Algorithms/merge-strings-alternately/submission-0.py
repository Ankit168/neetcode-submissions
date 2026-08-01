class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n = len(word1)
        m = len(word2)

        k = min(n,m)
        result = ""

        for i in range(k):
            result += word1[i] + word2[i]

        if n>m:
            result += word1[m:]
        else:
            result += word2[n:]

        return result
