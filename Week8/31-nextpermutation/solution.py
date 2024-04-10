class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Find first decreasing number
        #Swap with the closest number thats bigger
        #Reverse the area
        def swap(nums,i,j):
            nums[i],nums[j]=nums[j],nums[i]

        
        def reverse(nums,start):
            end=len(nums)-1

            while start<end:
                swap(nums,start,end)
                start+=1
                end-=1
        

        i=len(nums)-1

        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        

        if i==0:
            reverse(nums,0)
            return
        pivot=i-1
        for i in range(len(nums)-1,pivot,-1):
            if nums[i]>nums[pivot]:
                swap(nums,i,pivot)
                break
        
        reverse(nums,pivot+1)