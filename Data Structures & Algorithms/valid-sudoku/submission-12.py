class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1 = set()
        #check rows
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if board[i][j] in set1:
                    return False
                if board[i][j] != ".":
                    set1.add(board[i][j])
            set1.clear()
        #check columns
        set2 = set()
        for i in range(len(board[0])):
            for j in range(len(board)): 
                if board[j][i] in set2: 
                    print("aaa")
                    return False 
                if board[j][i] != ".":
                    set2.add(board[j][i]) 
            set2.clear()
        #check boxes how?
        mymap = {}
        for i in range(len(board)): 
            for j in range(len(board[0])):
                val = board[i][j]
                cur1,cur2 = i//3, j//3
                if (cur1,cur2) not in mymap:
                    mymap[(cur1,cur2)] = set()
                elif val in mymap[(cur1,cur2)]:
                    print("false 1")
                    return False
                if board[i][j] != ".":
                    mymap[(cur1,cur2)].add(val)

        return True 