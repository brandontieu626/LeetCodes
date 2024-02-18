class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        
        mDict={}
        for c in magazine:
            mDict[c]=mDict.get(c,0)+1
        
        for c in ransomNote:
            if c not in mDict or mDict[c]==0:
                return False
            else:
                mDict[c]-=1
        
        return True