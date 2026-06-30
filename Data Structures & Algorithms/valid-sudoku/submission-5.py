class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows

        for i in range(len(board)): 
            myset = set()
            for j in range(len(board[i])): 
                elem = board[i][j]
                
                if elem in myset:
                    return False
                elif elem != '.': 
                    myset.add(elem)

        #columns

        for i in range(len(board)): 
            myset = set()
            for j in range(len(board[i])): 
                elem = board[j][i]
                
                if elem in myset:
                    return False
                elif elem != '.': 
                    myset.add(elem)


        #squares

        starts = [
                (0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)

        ]

        for i , j in starts: 
            myset = set()
            for row in range(i , i+3): 
                for col in range(j, j+3):
                    elem = board[row][col] 
                    if elem in myset: 
                        return False
                    elif elem != '.': 
                        myset.add(elem)

        return True