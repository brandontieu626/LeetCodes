class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterCt=set()

        for c in s:
            if c in letterCt:
                letterCt.remove(c)
            else:
                letterCt.add(c)
        

        if len(letterCt)!=0:
            return len(s)-len(letterCt)+1
        
        return len(s)