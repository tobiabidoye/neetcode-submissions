class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        count = 0

        while(count < len(matrix)):
            a = 0
            b = len(matrix[count]) - 1            

            while(a <= b): 
                m = (a+b) // 2

                if(matrix[count][m] < target): 
                    a = m + 1
                elif(matrix[count][m] > target): 
                    b = m - 1
                elif(matrix[count][m] == target): 
                    return True
            count += 1
        
        return False