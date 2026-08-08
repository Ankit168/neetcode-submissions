class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        n = len(nums)
        j = n-1
        k = k%n
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0,k-1)
        reverse(k,n-1)
        