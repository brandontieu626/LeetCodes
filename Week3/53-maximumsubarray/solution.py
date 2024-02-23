class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=max(nums)
        temp=0
        for n in nums:
            if temp<0:
                temp=0
            temp+=n
            res=max(res,temp)      
        return res 
            