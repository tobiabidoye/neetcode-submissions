class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        myarr = []
        for i in matrix: 
            for j in i: 
                myarr.append(j)
        
        if target in myarr: 
            return True
        return False