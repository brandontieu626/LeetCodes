class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        
        maxAmount=0

        while l<r:
            length=min(height[l],height[r])
            width=r-l

            maxAmount=max(maxAmount,width*length)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return maxAmount