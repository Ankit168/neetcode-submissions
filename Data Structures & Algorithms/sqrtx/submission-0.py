class Solution:
    def mySqrt(self, x: int) -> int:

        if x<2:
            return x

        low = 1 
        high = x//2
        ans = 0

        while low<=high:
            mid = low+(high-low)//2
            sqr = mid*mid

            if sqr == x:
                return mid
            elif sqr<x:
                ans = mid
                #print(". . .",mid)
                low = mid+1
            else:
                high = mid-1
            

        return ans
        

        