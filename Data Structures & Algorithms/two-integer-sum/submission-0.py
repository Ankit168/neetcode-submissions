class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {}

        for i,num in enumerate(nums):
            difference = target - num
            if difference in diff.keys():
                return [diff[difference],i]
            diff[num] = i