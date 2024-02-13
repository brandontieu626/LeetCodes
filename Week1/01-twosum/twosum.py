class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i,n in enumerate(nums):
            if target-n in seen:
                return [i,seen[target-n]]
            else:
                seen[n]=i
        
        return []