class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix)
        while l < r: 
            mid = (l + r) // 2
            #if its smaller than the smallest target in the middle then adjust right 
            if target not in matrix[mid]:
                if target < matrix[mid][0]: 
                    r -= 1
                elif target > matrix[mid][-1]: 
                    l += 1
                else: 
                    return False
            else: 
                return True
        
        return False
                
            



