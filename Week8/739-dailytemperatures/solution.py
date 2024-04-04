class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        tempStack=[]

        for i,t in enumerate(temperatures):
            while tempStack and t>tempStack[-1][1]:
                temp=tempStack.pop()
                res[temp[0]]=i-temp[0]
            
            tempStack.append([i,t])
        
        return res