class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)

        if total%2!=0:
            return False
        
        half=total//2
        sumSet=set()
        sumSet.add(0)

        for n in nums:
            newSet=set()
            for s in sumSet:
                if s+n==half:
                    return True
                newSet.add(s)
                newSet.add(s+n)
            sumSet=newSet
        
        return False