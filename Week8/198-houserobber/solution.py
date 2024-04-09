class Solution:
    def rob(self, nums: List[int]) -> int:
        one=0
        two=0
    
        #0,0[1,2,3,1]
        for n in nums:
            total=n+one
            one=two
            two=max(total,two)
        
        return two
            