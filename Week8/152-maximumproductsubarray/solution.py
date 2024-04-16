class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) #What if array with single item

        currMax=1
        currMin=1
        #Use 1 to be neutral and collect total


        #[2,3,-2,4]

        for n in nums:
            if n==0:
                currMin=0
                currMax=0
            
            temp=currMax
            currMax=max(n*currMax,n*currMin,n)
            currMin=min(n*temp,n*currMin,n)

            res=max(res,currMax)
        
        return res