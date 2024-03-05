class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums.copy()]
        
        res=[]

        for i in range(len(nums)):
            num=nums.pop(0)
            permutations=self.permute(nums)
            for perm in permutations:
                perm.append(num)
            nums.append(num)
            res.extend(permutations)
        
        return res
