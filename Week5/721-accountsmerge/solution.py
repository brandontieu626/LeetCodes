class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph=collections.defaultdict(set)
        emailToName={}
        for account in accounts:
            name=account[0]

            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                emailToName[email]=name
        

        visited=set()
        q=deque()
        res=[]

        for node in graph:
            nodeRes=[]
            if node not in visited:
                q.append(node) 
                visited.add(node)

            while q:
                n=q.popleft()
                nodeRes.append(n)
                for neighbor in graph[n]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            
            if nodeRes:
                res.append([emailToName[node]]+sorted(nodeRes))
        
        return res