class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high = max(piles)
        ans = 0
        while(low<=high):
            total_time = 0
            mid = low + (high-low)//2

            for pile in piles:
                total_time += (pile+mid-1)//mid

            if total_time <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1 
                
        return ans

        


