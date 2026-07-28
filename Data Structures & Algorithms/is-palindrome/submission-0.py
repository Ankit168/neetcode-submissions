class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleared_str = ''.join([ch for ch in s if ch.isalnum()])

        i = 0
        j = len(cleared_str)-1

        while i<j:
            if cleared_str[i].lower() == cleared_str[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False
                
        return True
        