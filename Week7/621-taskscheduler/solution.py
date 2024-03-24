class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskDict={}

        for task in tasks:
            taskDict[task]=taskDict.get(task,0)+1
        
        maxHeap=[-ct for ct in taskDict.values()]

        heapq.heapify(maxHeap)
        taskQ=[]
        time=0

        while taskQ or maxHeap:
            time+=1

            if maxHeap:
                ct=heapq.heappop(maxHeap)+1
                if ct!=0:
                    taskQ.append([ct,time+n])
            
            if taskQ and taskQ[0][1]==time:
                task=taskQ.pop(0)
                heapq.heappush(maxHeap,task[0])
        
        return time