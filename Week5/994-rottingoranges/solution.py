class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        fresh=0
        time=0

        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1


        while q and fresh>0:
            levelLen=len(q)

            for i in range(levelLen):
                r,c=q.popleft()

                for x,y in (1,0),(-1,0),(0,1),(0,-1):
                    nr=r+x
                    nc=c+y

                    if nr>=0 and nc>=0 and nr<rows and nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        
        return -1 if fresh>0 else time