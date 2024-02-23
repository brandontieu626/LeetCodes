class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        romanToInt={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        for i,c in enumerate(s):
            if i+1<len(s) and romanToInt[s[i+1]]>romanToInt[c]:
                res-=romanToInt[c]
            else:
                res+=romanToInt[c]
        
        return res
