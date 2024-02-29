class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows=len(grid)
        cols=len(grid[0])
        islandCt=0

        def findIsland(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=='0':
                return
            
            grid[r][c]='0'

            findIsland(r+1,c)
            findIsland(r-1,c)
            findIsland(r,c+1)
            findIsland(r,c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    findIsland(i,j)
                    islandCt+=1
        
        return islandCt
