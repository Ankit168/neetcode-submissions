class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = {0:1}
        count = 0

        prefix = 0

        for num in nums:
            prefix += num
            target = prefix - k

            if target in prefix_sum:
                count += prefix_sum[target]

            prefix_sum[prefix] = prefix_sum.get(prefix,0) + 1 

        return count
        