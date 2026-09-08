class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mymatrix = []
        for i in range(len(matrix)):
            self.mymatrix.append(matrix[i])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        startRow = row1
        startCol = col1
        endRow = row2
        endCol = col2
        summa = 0 
        for i in range(len(self.mymatrix)):
            for j in range(len(self.mymatrix[0])):
                if i < startRow or i > endRow:
                    continue
                if j < startCol or j > endCol:
                    continue
                summa += self.mymatrix[i][j]

        return summa
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)