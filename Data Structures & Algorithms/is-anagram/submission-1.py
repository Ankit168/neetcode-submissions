class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_freq = [0]*26

        for ch in s:
            index = ord(ch) - ord('a')
            char_freq[index] += 1

        for ch in t:
            index = ord(ch) - ord('a')
            if char_freq[index] != 0:
                char_freq[index] -= 1  
            else:
                char_freq[index] += 1
                
        for i in range(len(char_freq)):
            if char_freq[i] > 0:
                return False
        
        return True