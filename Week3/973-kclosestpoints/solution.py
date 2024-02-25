class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        totals=[]
        res=[]
        for x,y in points:
            total=x**2+y**2
            totals.append([total,[x,y]])
        
        totals.sort()
        
        for i in range(k):
            res.append(totals[i][1])
        
        return res