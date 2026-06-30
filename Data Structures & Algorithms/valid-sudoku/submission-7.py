class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)): 
            myMap = defaultdict(int)
            for j in board[i]: 
                if j != ".":
                    myMap[j] += 1
                    if myMap[j] > 1: 
                        
                        return False

        for i in range(len(board[0])): 
            myMap = defaultdict(int)
            #nxn matrix so this works
            for j in range(len(board)):
                if board[j][i] != ".":
                    myMap[board[j][i]] += 1
                    if myMap[board[j][i]] > 1: 
                        
                        return False


        #need to floor divide to get grids and loop through the grids
        #to check for duplicates
        myMap = defaultdict(set)
        for i in range(9):   
            for j in range(9): 
                if board[i][j] == ".": 
                    continue
                if board[i][j] in myMap[(i//3, j // 3)]: 
                    return False
                myMap[(i//3,j//3)].add(board[i][j])
        
                 
                

        return True
