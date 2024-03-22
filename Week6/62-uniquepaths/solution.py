class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows=m
        cols=n

        resRow=[1]*cols
        for i in range(rows-2,-1,-1):
            curRow=[1]*cols
            for j in range(cols-2,-1,-1):
                curRow[j]=curRow[j+1]+resRow[j]
            
            resRow=curRow
        
        return resRow[0]