class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        count = 0

        while(count < len(matrix)): 
            a = 0
            b = len(matrix[count]) - 1
            while(a <= b): 
                midpoint = (a+b)//2
                
                if(matrix[count][midpoint] < target): 
                    a = midpoint + 1
                elif(matrix[count][midpoint] > target): 
                    b = midpoint - 1
                elif(matrix[count][midpoint] == target): 
                    return True
            
            count += 1
        
        return False