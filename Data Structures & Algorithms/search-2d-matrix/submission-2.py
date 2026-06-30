class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom: 
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target: 
                bottom = mid - 1
            else: 
                break
        
        if not(top <= bottom): 
            return False

        mid = (top + bottom) // 2

        a = 0 
        b = len(matrix[mid]) - 1

        while a <= b: 
            mid2 = (a+b) // 2
            
            if matrix[mid][mid2] < target: 
                a = mid2 + 1
            elif matrix[mid][mid2] > target: 
                b = mid2 - 1
            elif matrix [mid][mid2] == target: 
                return True
        
        return False