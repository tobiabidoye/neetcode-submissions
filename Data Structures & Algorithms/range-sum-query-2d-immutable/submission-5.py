class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):  
            self.prefix.append([])
            for j in range(len(matrix[0])): 
                summa = matrix[i][j]
                if (i - 1) >= 0:
                    summa += self.prefix[i-1][j]
                if (j - 1) >= 0:
                    print(j-1)
                    summa += self.prefix[i][j-1]
                if (i - 1) >= 0 and (j - 1) >= 0:
                    summa -= self.prefix[i-1][j-1]
                self.prefix[i].append(summa)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #now use the formula, prefix - top - left + topleft
        curSum = self.prefix[row2][col2]
        top = 0 #row1-1 col2
        left = 0
        topleft = 0

        if (row1-1) >= 0:
            top = self.prefix[row1-1][col2]
        if (col1 - 1 >= 0): 
            left = self.prefix[row2][col1-1]
        if (row1-1  >= 0) and (col1-1 >= 0):
            topleft = self.prefix[row1-1][col1-1]
        return curSum -left - top + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)