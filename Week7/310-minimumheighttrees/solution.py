class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        adjList=collections.defaultdict(set)

        for i,j in edges:
            adjList[i].add(j)
            adjList[j].add(i)
        
        leafQ=deque()
        for i in range(n):
            if len(adjList[i])==1:
                leafQ.append(i)
        

        while n>2:
            levelLen=len(leafQ)
            n-=levelLen

            for i in range(levelLen):
                leaf=leafQ.popleft()
                neigh=adjList[leaf].pop()
                adjList.pop(leaf)
                adjList[neigh].remove(leaf)

                if len(adjList[neigh])==1:
                    leafQ.append(neigh)
            
        
        return leafQ