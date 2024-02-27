class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq={}

        for i in range(numCourses):
            courseToPrereq[i]=[]
        

        for c,p in prerequisites:
            courseToPrereq[c].append(p)
        
        visited=set()

        def dfs(course):
            if courseToPrereq[course]==[]:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for p in courseToPrereq[course]:
                if not dfs(p):
                    return False
            
            courseToPrereq[course]=[]
            visited.remove(course)

            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True