class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = (len(matrix)) - 1

        while top <= bottom: 
            mid = (top + bottom) // 2

            if(matrix[mid][-1] < target): 
                top = mid + 1
            elif(matrix[mid][0] > target): 
                bottom = mid - 1
            else: 
                break
        
        if not(top <= bottom): 
            return False

        mid = (top + bottom) // 2 

        l = 0
        r = len(matrix[mid]) - 1

        while l <= r : 
            mid2 = (l+r) // 2

            if matrix[mid][mid2] < target: 
                l = mid2 + 1
            elif matrix[mid][mid2] > target: 
                r = mid2 - 1
            elif matrix[mid][mid2] == target: 
                return True 

        return False 