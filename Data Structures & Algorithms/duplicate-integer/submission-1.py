class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        last_seen = {}

        for num in nums:
            if num in last_seen:
                return True
            last_seen[num] = True
        return False
        