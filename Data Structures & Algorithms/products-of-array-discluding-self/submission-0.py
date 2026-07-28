class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)

        prefix_res = [1]*n
        suffix_res = [1]*n
        result = []

        for i in range(n):
            prefix_res[i] = prefix
            prefix *= nums[i]

        for i in range(n-1,-1,-1):
            suffix_res[i] *= suffix
            suffix *= nums[i]

        for i in range(n):
            result.append(prefix_res[i]*suffix_res[i])

        return result
