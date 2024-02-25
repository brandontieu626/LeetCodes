class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,v in enumerate(nums):
            if i>0 and v==nums[i-1]:
                continue
            
            start=i+1
            end=len(nums)-1

            while l<r:
                total=v+nums[start]+nums[end]

                if total==0:
                    res.append([nums[i],nums[l],nums[r]])
                    start=start+1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    break
                elif total<0:
                    start=start+1
                else:
                    end=end-1
        
        return res
            