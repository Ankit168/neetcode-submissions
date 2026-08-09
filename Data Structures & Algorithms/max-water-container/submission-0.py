class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        max_water = 0

        while i<j:
            water = (j-i)*min(heights[j],heights[i])
            if heights[i]<heights[j]:
                i += 1
            elif heights[j]<heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
            max_water = max(water,max_water)
        
        return max_water
