class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        if len(s)<len(p):
            return res
        

        sDict={}
        pDict={}
        
        for i in range(len(p)):
            sDict[s[i]]=sDict.get(s[i],0)+1
            pDict[p[i]]=pDict.get(p[i],0)+1
        

        if sDict==pDict:
            res.append(0)
        start=0
        for i in range(len(p),len(s)):
            sDict[s[i]]=sDict.get(s[i],0)+1

            sDict[s[start]]-=1

            if sDict[s[start]]==0:
                sDict.pop(s[start])
            start+=1
            if sDict==pDict:
                res.append(start)
            
        
        return res