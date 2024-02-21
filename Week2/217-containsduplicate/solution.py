class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist=set()

        for n in nums:
            if n in dist:
                return True
            dist.add(n)
        
        return False