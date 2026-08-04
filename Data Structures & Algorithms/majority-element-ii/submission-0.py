from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        target_freq = int(len(nums)/3)
        
        for num in nums:
            count[num] += 1

        result = []

        for key,value in count.items():
            if value > target_freq:
                result.append(key)

        return result