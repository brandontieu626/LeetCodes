class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        chars=set()
        l=0
        
        for c in s:
            while c in chars:
                chars.remove(s[l])
                l+=1
            chars.add(c)
            res=max(res,len(chars))
        
        return res
