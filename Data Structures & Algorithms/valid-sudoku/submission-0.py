class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       #using hashset to store the columns rows and sets and keeping track of unique elements
       #key value pair is [index][value in board]
        cols = defaultdict(set)
        rows = defaultdict(set) 
        squares = defaultdict(set) #squares are determined by dividing each of the rows and columns by 3

        for r in range(9):
                for c in range(9): 
                    if board[r][c] == ".": 
                        continue
                    if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                        #last condition returns square that we find ourself in at the moment
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
        return True
                
                
                
                



