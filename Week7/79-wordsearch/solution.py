class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=set()
        def dfs(r,c,i):
            if i>=len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or board[r][c]!=word[i]:
                return False
                   
            visited.add((r,c))
            
            value=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            visited.remove((r,c))
            
            return value
            

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        

        return False
                    