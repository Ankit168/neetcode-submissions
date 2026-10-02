class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp_stack = []
        result = [0]*len(temperatures)

        for i,temp in enumerate(temperatures):
                
            while temp_stack and temp > temp_stack[-1][1]:
                prev_index,prev_temp = temp_stack.pop()
                result[prev_index] = i-prev_index
            
            temp_stack.append((i,temp))

        return result