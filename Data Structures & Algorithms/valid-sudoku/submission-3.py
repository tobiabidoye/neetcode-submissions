class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #rows

        for i in range(len(board)): 
            myset = set()
            for j in range(len(board[i])): 
                newelem = board[i][j]

                if newelem in myset: 
                    return False
                elif newelem != '.': 
                    myset.add(newelem)
        #columns

        for i in range(len(board)): 
            myset = set()
            for j in range(len(board[i])): 
                newelem = board[j][i]

                if newelem in myset: 
                    return False
                elif newelem != '.': 
                    myset.add(newelem)


        #as for rows
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                   (6,0), (6,3), (6,6)]

        for i,j in starts: 
            myset = set()
            for row in range(i, i+3): 
                for col in range(j , j+3): 
                    newelem = board[row][col]
                
                    if newelem in myset:
                        return False
                    elif newelem != '.':
                        myset.add(newelem)

        return True            
        
          

