class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = -1
        n = len(matrix[0])
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target<=matrix[i][n-1]:
                row = i
        
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]< target:
                low = mid+1
            else:
                high = mid-1
        return False

