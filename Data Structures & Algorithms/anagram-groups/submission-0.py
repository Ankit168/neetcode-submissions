from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            count = [0]*26
            for ch in str:
                index= ord(ch) - ord('a')
                count[index] += 1
            groups[tuple(count)].append(str)
        
        return list(groups.values())