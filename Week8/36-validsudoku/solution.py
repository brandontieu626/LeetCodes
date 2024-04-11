class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict=collections.defaultdict(set)
        colDict=collections.defaultdict(set)
        gridDict=collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                
                if board[i][j] in rowDict[i] or board[i][j] in colDict[j] or board[i][j] in gridDict[(i//3,j//3)]:
                    return False
                
                rowDict[i].add(board[i][j])
                colDict[j].add(board[i][j])
                gridDict[(i//3,j//3)].add(board[i][j])
        

        return True