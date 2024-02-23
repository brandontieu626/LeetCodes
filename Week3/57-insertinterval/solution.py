class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left=[]
        right=[]

        for s,e in intervals:
            if e<newInterval[0]:
                left.append([s,e])
            elif s>newInterval[1]:
                right.append([s,e])
            else:
                newInterval[0]=min(s,newInterval[0])
                newInterval[1]=max(e,newInterval[1])
        
        #[[]] + [[]] + [[]]
        return left+[newInterval]+right